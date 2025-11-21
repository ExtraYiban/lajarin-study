
def login():
    print("silahkan cek kembali")
    username = input("masukkan username: ")
    password = input("masukkan password: ")
    if username == "admin" and password == "admin123":
        role = "admin"
    elif username == "staff" and password == "staff123":
        role = "staff"
    else:
        role = "None"
        print("silahkan cek kembali")
    return role 