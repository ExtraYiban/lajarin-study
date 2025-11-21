from auth import login
role = login()
if role == "admin":
    print ("anda admin")
elif role == "staff":
    print ("anda staff")