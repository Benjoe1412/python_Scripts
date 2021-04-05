# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:26:54 2020

@author: Benjoe
"""

from bottle import Bottle, HTTPResponse, run, request, response

app = Bottle()

@app.get("/")
def index():
    return "OK"

if __name__ == '__main__':
    run(app=app, host='localhost', port=8081)