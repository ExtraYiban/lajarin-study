from fungsi import *
import os
# create
# read
# update
# delete

def menu():
    print("=== Menu CRUD Sederhana ===")
    print("1. Create Data")
    print("2. Read Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Exit")

while True:
    os.system("clear || cls")
    menu()
    choice = input("Pilih menu (1-5): ")
    match choice:
        case "1":
            print("Anda memilih Create Data")
            create_data()
            input("tekan enter untuk melanjutkan")
        case "2":
            print("Anda memilih Read Data")
            read_data()
            input("tekan enter untuk melanjutkan")
        case "3":
            print("anda memilih update data")
            update_data()
            input("tekan enter untuk melanjutkan")
        case "4":
            print("anda memilih delete data")
            delete_data()
            input("tekan enter untuk melanjutkan")
        case "5":
            print("Terima kasih telah menggunakan program ini.")
            break