
def login():
    username = input("masukkan username: ")
    password = input("masukkan password: ")
    if username == "admin" and password == "admin123":
        role = "admin"
        print("login berhasil")
    elif username == "staff" and password == "staff123":
        role = "staff"
        print("login berhasil")
    return role
