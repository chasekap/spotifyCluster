import React, { useState, useEffect } from 'react';
import {Button} from 'rebass'; 
import './App.css';
export default function Login(){
    
    const login = () => {
        
        
            fetch('/creds').then(res => res.json()).then(data => {
                window.location.href = data.id
              });
        
    }

    const queryParams = new URLSearchParams(window.location.search);
    const code = queryParams.get('code');
    const LoginButton = code ? <div/> : 
                               <Button className="Clear-Button" onClick={login}> Log in with Spotify </Button> 
    return (
        <>
        {LoginButton}
        </>
    )
}