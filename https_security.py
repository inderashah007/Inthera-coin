from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app)  # Aktifkan HTTPS

@app.route('/')
def home():
    return "Semua sambungan disulitkan dengan HTTPS!"

if __name__ == '__main__':
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))  # Tambahkan SSL sertifikat
