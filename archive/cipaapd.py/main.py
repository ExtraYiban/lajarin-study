from auth import login
while True:
    role = login()
    if role == "admin":
        print("kamu admin")
        break
    elif role == "staff":
        print("kamu staff")
        break
    else:
        print("bukan siapa siapa")
