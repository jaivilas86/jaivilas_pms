from flask import Flask, render_template, request, jsonify
import re
from functions import *
app = Flask(__name__)

@app.route('/get_area', methods = ["POST"])
def get_area_api():
    data = request.json
    text = data.get("text",'')
    result = extract_all_areas(text)
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)