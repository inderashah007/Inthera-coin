from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/get_itc', methods=['GET'])
def get_itc():
    user_id = request.args.get('user_id')
    # Logik untuk mendapatkan jumlah ITC untuk pengguna berdasarkan data buangan mereka
    itc_amount = 100  # Contoh nilai
    return jsonify({"user_id": user_id, "itc": itc_amount})

if __name__ == "__main__":
    app.run(debug=True)
