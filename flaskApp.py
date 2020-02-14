from flask import Flask, render_template
from webui import WebUI
import pandas as pd


app = Flask(__name__)
ui = WebUI(app, debug=True)


@app.route("/")
def index():
    table = pd.read_csv('clean_inv.csv')
    return(table.to_html())

    
if __name__ == "__main__":
    ui.run()
