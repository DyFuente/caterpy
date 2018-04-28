#!/usr/bin/env python3
# -*- codinf: utf-8 -*-
"""A Flask app to provide page for caterpy."""


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
