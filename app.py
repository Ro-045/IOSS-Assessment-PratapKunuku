# from flask import Flask, render_template, request, redirect
# import string
# import random

# app = Flask(__name__)

# # In-memory storage: short_code -> original_url
# url_mapping = {}

# def generate_short_code(length=6):
#     characters = string.ascii_letters + string.digits
#     return ''.join(random.choice(characters) for _ in range(length))

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     short_url = None
#     if request.method == 'POST':
#         original_url = request.form['url']
#         short_code = generate_short_code()
#         url_mapping[short_code] = original_url
#         short_url = request.host_url + short_code
#     return render_template('index.html', short_url=short_url)

# @app.route('/<short_code>')
# def redirect_to_original(short_code):
#     if short_code in url_mapping:
#         return redirect(url_mapping[short_code])
#     return "Invalid URL", 404

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)


from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Railway + Docker!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
