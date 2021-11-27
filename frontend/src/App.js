import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import Login from './Login.js';

function App() {

  async function post_code(code){

    const response = await fetch('/token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      
      body: JSON.stringify({"code" : code}) // body data type must match "Content-Type" header
    });

  }

  useEffect(() => {
    const queryParams = new URLSearchParams(window.location.search);
    const code = queryParams.get('code');
    if (code){
      post_code(code);
    }
  },[])
  

  return (
    <div className="App">
      <header className="App-header">
        <h1> SpotifyCluster </h1>
       
       <Login/>

        
      </header>
    </div>
  );
}

export default App;
