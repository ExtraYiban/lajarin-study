# =====================================================================
#  DICTIONARY (Struktur Data Berpasangan Key–Value)
# =====================================================================
# Dictionary adalah struktur data yang menyimpan data dalam bentuk:
#
#        key : value
#
# Contoh sederhana:
#        {"nama": "Alif", "umur": 20}
#         { 1   : "Alif", 2    : 20   }
#
# Key harus unik, dan biasanya berupa string. Value bebas apa saja:
# - string
# - integer
# - float
# - boolean
# - list
# - tuple
# - dictionary (nested dictionary)
#
# Dictionary sangat penting karena bentuknya mirip "database kecil"
# sehingga sering dipakai untuk:
# - menyimpan data user
# - data mahasiswa
# - data produk
# - data login
# - JSON API
#
# ---------------------------------------------------------------------
# CARA MEMBUAT DICTIONARY
# ---------------------------------------------------------------------
#
# 1. Literal (paling sering)
#    data = {"nama": "Budi", "umur": 18}
#
# 2. Menggunakan dict()
#    data = dict(nama="Budi", umur=18)
#
# 3. Kosong dulu, isi nanti
# data = {}
# data["nama"] = "Budi"
# data["umur"] = 18
# print(data)
#
# ---------------------------------------------------------------------
# CARA MENGAKSES DATA DICTIONARY
# ---------------------------------------------------------------------
#
#    data["nama"]    → mendapat nilai dari key 'nama'
#    data.get("nama")→ aman digunakan, tidak error jika key tidak ada
data = {
    "nama": "Andi",
    "umur": 19,
    "alamat": {
        "kota": "Jakarta",
        "jalan": "Jalan Merdeka No. 10"
    },
}

#
# Akses nested dictionary:
#    data["alamat"]["kota"]
#
# ---------------------------------------------------------------------
# CARA MENAMBAH DATA KE DICTIONARY
# ---------------------------------------------------------------------
#
#    data["hobi"] = "mancing"
#
# Jika key sudah ada → nilainya akan menimpa data sebelumnya.
#
# ---------------------------------------------------------------------
# CARA MENGUPDATE DATA DICTIONARY
# ---------------------------------------------------------------------
#
#    data["umur"] = 20
#
#    data.update({"nama": "Andi"})
#
#
# ---------------------------------------------------------------------
# CARA MENGHAPUS DATA DICTIONARY
# ---------------------------------------------------------------------
#
# 1. Menghapus key tertentu:
#       del data["umur"]
# del data["nama"]
# print(data)
#
# 2. Pop (mengambil + menghapus):
# nilai = data.pop("umur")
# print(nilai)
#
# 3. Hapus semua:
# data.clear()
# print(data)
#
# ---------------------------------------------------------------------
# LOOPING DICTIONARY
# ---------------------------------------------------------------------
#
# Loop key saja:
# for k in data:
#     print(k)
#
# Loop key dan value:
# for k, v in data.items():
#     print(k, v)
#
# Loop hanya value:
# for v in data.values():
#     print(v)
#
# Loop hanya key:
#       for k in data.keys():
#           print(k)
#
# ---------------------------------------------------------------------
# DICTIONARY DI DALAM LIST (PENTING UNTUK CRUD)
# ---------------------------------------------------------------------
#
# Banyak aplikasi Python memakai struktur seperti ini:
#
mahasiswa = [
    {"nama": "Budi", "umur": 20},
    {"nama": "Aldi", "umur": 21}
]
#
# Mengakses:
#    mahasiswa[0]["nama"]  → "Budi"
#
# Ini bentuk data yang mirip database tabel.
#
# ---------------------------------------------------------------------
# NESTED DICTIONARY (DICTIONARY DI DALAM DICTIONARY)
# ---------------------------------------------------------------------
#
#    user = {
#       "nama": "Budi",
#       "alamat": {
#           "kota": "Samarinda",
#           "jalan": "Mawar"
#       }
#    }
#
# Akses:
#    user["alamat"]["jalan"]
#
# ---------------------------------------------------------------------
# KONVERSI DICTIONARY KE JSON
# ---------------------------------------------------------------------
#
#    import json
#    json.dumps(data)
#
# Ini digunakan untuk:
# - API
# - penyimpanan file
# - data aplikasi modern
#
# ---------------------------------------------------------------------
# KEGUNAAN PENTING DICTIONARY DALAM PROGRAM:
# ✔ CRUD (Create Read Update Delete)
# ✔ Simpan data user
# ✔ Simpan data barang/produk
# ✔ Struktur tabel sederhana
# ✔ Pemrosesan JSON
# ✔ Data konfigurasi program
# ✔ Menu switch-case menggunakan dictionary mapping
#
# Dictionary adalah struktur data paling fleksibel dan paling sering
# digunakan dalam aplikasi Python tingkat pemula sampai profesional.
#
# =====================================================================
