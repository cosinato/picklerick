#!/usr/bin/env python3
from flask import render_template
import connexion

# app = Flask(__name__, template_folder="templates")
app = connexion.App(__name__, specification_dir="./")
app.add_api("openapi.yml")


@app.route("/")
def root_index():
    return render_template("app.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1080, debug=True)

#
