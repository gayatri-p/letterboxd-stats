from flask import Flask, render_template, url_for
from stats_page import alltime 
from yearly_stats_page import yearly

app = Flask(__name__)
app.register_blueprint(alltime, url_prefix='')
app.register_blueprint(yearly, url_prefix='')

@app.route('/')
def index():
    return 'render error'

if __name__ == '__main__':
    app.run(debug=True)