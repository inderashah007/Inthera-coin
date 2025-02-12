import jwt
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = 'inthera_super_secret_key'

# Fungsi untuk menghasilkan token
def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token sah selama 1 jam
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

# Middleware untuk mengesahkan token
def token_required(f):
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token tidak diberikan!'}), 403
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token telah tamat tempoh!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token tidak sah!'}), 403
        return f(*args, **kwargs)
    return decorator

# Contoh API dengan pengesahan token
@app.route('/secure-data', methods=['GET'])
@token_required
def secure_data():
    return jsonify({'message': 'Data selamat diakses!'})

if __name__ == '__main__':
    app.run(debug=True)
