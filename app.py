import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def send_page():
    page = render_template('info_page.html')
    return page


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')


@app.route('/male_female.html')
def send_mf():
    vis = render_template('male_female.html')
    return vis


@app.route('/anxiety_hist.html')
def send_anx():
    vis = render_template('anxiety_hist.html')
    return vis


@app.route('/user_map.html')
def send_usermap():
    vis = render_template('user_map.html')
    return vis


@app.route('/anx_map.html')
def send_anxmap():
    vis = render_template('anx_map.html')
    return vis


if __name__ == '__main__':
    app.run()
