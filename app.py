from flask import Flask, render_template_string
import os

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Aplikasi Web Sederhana</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
        }
        .container {
            background-color: #f0f0f0;
            padding: 20px;
            border-radius: 8px;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Selamat Datang di Web App Saya!</h1>
        <p>Ini adalah contoh aplikasi web sederhana.</p>
        <p>Waktu server: {{ current_time }}</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    from datetime import datetime
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(TEMPLATE, current_time=current_time)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)