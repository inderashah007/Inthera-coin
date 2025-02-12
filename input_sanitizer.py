import html

# Fungsi untuk membersihkan input
def sanitize_input(user_input):
    sanitized = html.escape(user_input)
    return sanitized

# Contoh penggunaan
if __name__ == "__main__":
    user_input = '<script>alert("XSS Attack!")</script>'
    print("Input asal:", user_input)
    print("Input yang telah dibersihkan:", sanitize_input(user_input))
