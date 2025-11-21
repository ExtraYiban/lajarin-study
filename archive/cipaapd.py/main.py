from auth import login
role = login()
if role == "admin":
    print("kamu admin")
elif role == "staff":
    print("kamu staff")
else:
    print("bukan siapa siapa")
