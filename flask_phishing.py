#!/usr/bin/env python3

from flask import Flask, request
from termcolor import colored

app = Flask(__name__)

@app.route('/')
def index():
    
    user_info ={
            'ip':request.remote_addr,
            'user_agent':request.headers.get('User-Agent'),
            'headers':dict(request.headers),
    }

    print(colored(f"Get request info: {user_info}"))

    with open('click_log.txt', 'a') as f:
        f.write(f"{user_info}")

    return "This was a phishing simulation. Your click has been logged."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
