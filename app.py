# import os

# # Generate a random 32-byte (256-bit) key
# secret_key = os.urandom(32)

# # Convert the binary key to a hexadecimal string
# secret_key_hex = secret_key.hex()

# print("Generated Secret Key:", secret_key_hex)

from flask import Flask, request, render_template, url_for


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, port= 8070)