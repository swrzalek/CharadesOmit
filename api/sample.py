import json
from flask import Flask, Response, abort
from .utils import fetch_word,scrap_page
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route('/api/<keyword>')
def homepage(keyword):
    soup = scrap_page(keyword)
    response = fetch_word(soup)
    
    return {keyword : response}

@app.errorhandler(404)
def not_found(e):
    return '', 404