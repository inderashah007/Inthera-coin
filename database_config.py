import sqlite3

# Sambungan ke pangkalan data
def connect_db():
    conn = sqlite3.connect('transactions.db')
    return conn

# Contoh masukan data selamat
def insert_transaction(user_id, itc_amount):
    conn = connect_db()
    c = conn.cursor()

    # Gunakan parameterized query
    c.execute('INSERT INTO transactions (user_id, itc_amount) VALUES (?, ?)', (user_id, itc_amount))
    conn.commit()
    conn.close()

# Contoh penggunaan fungsi
if __name__ == "__main__":
    user_id = "user123"
    itc_amount = 50
    insert_transaction(user_id, itc_amount)
    print("Transaksi berjaya disimpan dengan selamat!")
