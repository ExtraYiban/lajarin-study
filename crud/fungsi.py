import csv
from prettytable import PrettyTable

def read_data():
    table = PrettyTable()
    with open("crud/data.csv", "r") as file:
            content = csv.DictReader(file)
            table.field_names  = content.fieldnames
            for row in content:
                table.add_row(row.values())
            print(table)

def create_data():
    namaDepan = input("Nama depan: ")
    namaBelakang = input("Nama belakang: ")
    usia = int(input("Usia : "))
    with open("crud/data.csv","r") as file:
        data = []
        content = csv.DictReader(file)
        for row in content:
            data.append(row)
        newOrang = {
            "id": len(data) + 1, 
            "nama_depan": namaDepan,
            "nama_belakang": namaBelakang,
            "usia": usia
        }
        data.append(newOrang)
        with open("crud/data.csv","w") as writer:
            fieldNames = ["id","nama_depan","nama_belakang","usia"]
            alat = csv.DictWriter(writer,fieldnames=fieldNames)
            alat.writeheader()
            alat.writerows(data)
    print("data berhasil ditambahkan")

def delete_data():
    read_data()
    id = input("Masukkan ID yang ingin dihapus: ")
    with open("crud/data.csv","r") as file:
        data = []
        content = csv.DictReader(file)
        for row in content:
            if id == row["id"]:
                print(f'Menghapus data: {row["nama_depan"]} {row["nama_belakang"]}')
                continue
            data.append(row)
        with open("crud/data.csv","w") as writer:
            fieldNames = ["id","nama_depan","nama_belakang","usia"]
            alat = csv.DictWriter(writer,fieldnames=fieldNames)
            alat.writeheader()
            alat.writerows(data)
    print("data berhasil dihapus") 

def update_data():
    read_data()
    id = input("Masukkan ID yang ingin diupdate: ")
    with open("crud/data.csv","r") as file:
        data = []
        content = csv.DictReader(file)
        for row in content:
            if id == row["id"]:
                namaD = input("Nama depan yang baru : ")
                namaB = input("Nama belakang yang baru : ")
                usia = input("usia yang baru : ")
                row["nama_depan"] = namaD 
                row["nama_belakang"] = namaB
                row["usia"] = usia             
            data.append(row)
        with open("crud/data.csv","w") as writer:
            fieldNames = ["id","nama_depan","nama_belakang","usia"]
            alat = csv.DictWriter(writer,fieldnames=fieldNames)
            alat.writeheader()
            alat.writerows(data)
    print("data berhasil di update") 
