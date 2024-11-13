from flask import Flask, request, jsonify
from encryption import encrypt_text, decrypt_text
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.get_json()
    plain_text = data.get("text", "")
    encrypted_text = encrypt_text(plain_text)
    return jsonify({"output": encrypted_text})

@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.get_json()
    cipher_text = data.get("text", "")
    decrypted_text = decrypt_text(cipher_text)
    return jsonify({"output": decrypted_text})

if __name__ == "__main__":
    app.run(debug=True)
