from flask import Flask, render_template, request, jsonify
from text_parser.parser import Parser
from goog_api.goog_api import GoogleApi
from wiki_api.wiki_api import WikiApi

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/user_text', methods=['POST'])
def user_text():
    user_input_text = request.json['question']

    p = Parser(user_input_text)
    google_args = p.call_all_methods()

    g = GoogleApi()
    g.goog_fetch_infos(google_args)
    wiki_args = g.google_coords
    g_lat = g.google_lat
    g_long = g.google_long
    g_form_adress = g.google_adress

    w = WikiApi()
    wiki_results = w.wiki_fetch_infos(wiki_args)

    return jsonify(
        google_args=google_args,
        wiki_args=wiki_args,
        g_lat=g_lat,
        g_long=g_long,
        g_form_adress=g_form_adress,
        wiki_results=wiki_results
    )


if __name__ == '__main__':
    app.run(debug=True)
