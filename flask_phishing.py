#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    ip=request.remote_addr
    user_agent=request.headers.get('User-Agent')

    with open('click_log.txt', 'a') as f:
        f.write(f"IP: {ip}, User-Agent: {user_agent}\n")

    return "This was a phishing simulation. Your click has been logged."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
