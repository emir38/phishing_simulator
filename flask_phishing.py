#!/usr/bin/env python3

from flask import Flask, request, render_template, jsonify, redirect, url_for
from termcolor import colored

app = Flask(__name__)

@app.route('/')
def index():
    
    user_info ={
            'ip':request.remote_addr,
            'user_agent':request.headers.get('User-Agent'),
            'headers':dict(request.headers),
    }

    print(colored(f"Get request info: {user_info}", "red"))

    with open('click_log.txt', 'a') as f:
        f.write(f"{user_info}")

    return render_template("form.html", user_info=user_info)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    user_info = {
            'form_data': form_data
    }

    print(colored(f"Submit request info: {user_info}", "red"))

    with open('submit_form.txt', 'a') as f:
        f.write(f"{user_info}")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
