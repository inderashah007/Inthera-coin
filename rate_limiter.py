from flask import Flask, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Konfigurasi Flask-Limiter
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per hour", "10 per minute"]
)

@app.route('/api/data', methods=['GET'])
@limiter.limit("5 per minute")  # Hadkan kepada 5 permintaan seminit
def get_data():
    return jsonify({"message": "Data berjaya diakses!"})

if __name__ == '__main__':
    app.run(debug=True)
