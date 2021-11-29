import time
import os
import random
import string 
import json

from flask import Flask, request
import requests
import html

import data


app = Flask(__name__)

def gen_rand_string(n: int, chars: list) -> str: 
    return ''.join(random.choice(chars) for i in range(10))

def stringify_fields(fields) -> str: 
    out = ""
    for field in fields.keys():  
       out += field + "=" + fields[field] + "&"
    return out[:len(out) - 1]

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/creds')
def get_creds(): 
    randstr = gen_rand_string(16, string.ascii_letters + string.digits)
    scope = 'user-read-private user-read-email'
    
    fields = {
        'response_type': 'code', 
        'client_id': os.environ['SPOTID'], 
        'scope': 'user-read-private+user-read-email+user-top-read', 
        'redirect_uri': 'http://localhost:3000/', 
        'state': randstr

    }
    url = "https://accounts.spotify.com/authorize?" + stringify_fields(fields)
    
    return {"id": url}

@app.route('/token',methods=['POST'])
def get_token(): 
    code = request.json['code']
    fields = {
        'client_id': os.environ['SPOTID'], 
        'client_secret': os.environ['SPOTSEC'], 
        "grant_type": "authorization_code", 
        "code": code, 
        'redirect_uri': 'http://localhost:3000/'
    }
    url = "https://accounts.spotify.com/api/token"
    r = requests.post(url, data=fields)
    
    access_token = r.json()['access_token']
   
    
    header = {
        'Authorization': 'Bearer ' + access_token, 
        'Content-Type': "application/json", 
        "Accept" : "application/json"
    }
    opts = {
        "time_range": "long_term", 
        "limit" : "50"
    }

    r = requests.get('https://api.spotify.com/v1/me/top/tracks?' + stringify_fields(opts), headers=header, 
                     )
   
    
    df = data.json_to_df(r.json())
    id_str = data.get_id_str(df)
    opts = {"ids": id_str}
    r = requests.get('https://api.spotify.com/v1/audio-features?' + stringify_fields(opts), headers=header, 
                     )
    f = open("feats.txt","w")
    f.write(json.dumps(r.json()))
    data.add_audio_features(df,r.json()['audio_features'])
    

    return {"hi":  1}