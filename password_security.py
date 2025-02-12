from bcrypt import hashpw, gensalt, checkpw

# Fungsi untuk menyulitkan kata laluan
def encrypt_password(password):
    return hashpw(password.encode(), gensalt())

# Fungsi untuk mengesahkan kata laluan
def verify_password(password, hashed_password):
    return checkpw(password.encode(), hashed_password)

# Contoh penggunaan
if __name__ == "__main__":
    plain_password = "mysecurepassword"
    hashed_password = encrypt_password(plain_password)

    print("Kata laluan asal:", plain_password)
    print("Kata laluan yang disulitkan:", hashed_password)

    is_correct = verify_password("mysecurepassword", hashed_password)
    print("Kata laluan sah:", is_correct)
