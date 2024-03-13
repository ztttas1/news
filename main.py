from flask import Flask, render_template
import requests

app = Flask(__name__)
NEWS_API_KEY = '8d3db2a0f076426482dfc5b8787bad32'

@app.route('/')
def index():
    url = f'https://newsapi.org/v2/top-headlines?country=jp&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
