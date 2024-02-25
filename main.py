from flask import Flask
from playground.search_and_replace import search_and_replace_func

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/search_and_replace')
def search_and_replace():
    search_and_replace_func('abc', '123')
    return 'success！！！'


app.run(host='0.0.0.0', port=81)
