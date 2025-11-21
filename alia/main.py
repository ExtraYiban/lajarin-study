from auth import login

while True:
    role = login()

    if role == "admin":
        print('kamu admnin')
        break
    elif role == "staff":
        print('kamu staff')
        break
    else:
        print('tidak ada')
        break