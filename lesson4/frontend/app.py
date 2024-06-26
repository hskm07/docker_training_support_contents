from flask import Flask, jsonify, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get("http://backend:8080/hello")
    if response.status_code == 200:
        data = response.json()
    else:
        data = {"error": "Failed to connect to backend"}

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sample Flask Frontend</title>
    </head>
    <body>
        <h1>Sample Flask Frontend</h1>
        <pre>{{ data }}</pre>
    </body>
    </html>
    """
    return render_template_string(html, data=data)

if __name__ == '__main__':
    app.run(debug=True)
