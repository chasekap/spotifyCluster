from datetime import time
import pandas as pd
from pandas.core.arrays import sparse
from pandas.core.frame import DataFrame 


def gen_artist_string(artists: object) -> str: 
    
    artlist = [artist['name'] for artist in artists]
    return ", ".join(artlist)

def add_audio_features(df: DataFrame, features: object) -> DataFrame: 
    
    acousticness = []
    danceability = []
    energy = []
    loudness = []
    key = []
    instrumentalness = []
    mode = []
    speechiness = []
    tempo = []
    time_signature = []
    valence = []

    for song in features: 

        acousticness.append(song['acousticness'])
        danceability.append(song['danceability'])
        energy.append(song['energy'])
        loudness.append(song['loudness'])
        key.append(song['key'])
        instrumentalness.append(song['instrumentalness'])
        mode.append(song['mode'])
        speechiness.append(song['speechiness'])
        tempo.append(song['tempo'])
        time_signature.append(song['time_signature'])
        valence.append(song['valence'])

    df['acousticness'] = acousticness
    df['danceability'] = danceability
    df['energy'] = energy
    df['loudness'] = loudness
    df['key'] = key
    df['instrumentalness'] = instrumentalness
    df['mode'] = mode
    df['speechiness'] = speechiness
    df['tempo'] = tempo
    df['time_signature'] = time_signature
    df['valence'] = valence 
    df.to_csv('afff.csv')
    return df 

def get_id_str(df: DataFrame) -> str: 
    
    ids = df['id'].to_list()
    return ",".join(ids)

def json_to_df(data: object) -> DataFrame: 
    
    df = pd.DataFrame(columns=['id','name','artists'])
    for entry in data['items']: 
        row = {'id': entry['id'],'name': entry['name'], 
                     'artists': gen_artist_string(entry['artists'])}
        df = df.append(row,ignore_index=True)
    df.to_csv('aff.csv')
    return df

    