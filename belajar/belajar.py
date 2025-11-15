# =====================================================================
#                 PEMBELAJARAN PYTHON DASAR – FULL COMMENT
# =====================================================================


# =====================================================================
#  VARIABEL
# =====================================================================
# Pada bagian ini kamu belajar:
# - Apa itu variabel
# - Cara membuat variabel
# - Aturan penamaan variabel
# - Multiple assignment (mengisi banyak variabel dalam satu baris)
# - Cara mengubah nilai variabel
# - Cara menghapus variabel menggunakan 'del'

# Variabel adalah tempat menyimpan data.
# Contoh:
# usia = 20
# nama = "Andi"
# a, b, c = 10, 20, 30
# del a


# =====================================================================
#  INPUT & OUTPUT
# =====================================================================
# Pada bagian ini kamu belajar:
# - Mengambil input dari user dengan input()
# - Mengubah input menjadi tipe tertentu (int, float, bool)
#
# Kamu juga belajar:
# - Menangani error input menggunakan try/except

# Contoh:
# try:
#     angka_pertama = int(input("Angka pertama : "))
#     angka_kedua = int(input("Angka kedua : "))

#     if angka_kedua == 1:
#         raise ValueError("Angka keduanya 1")

#     print(angka_pertama / angka_kedua)
# except ValueError as e:
#     print("input harus angka!")
# except ZeroDivisionError:
#     print("Tidak bisa dibagi 0")
# except:
#     print("asdasd")


# print("Berhasil di print")

# =====================================================================
#  TIPE DATA
# =====================================================================
# Pada bagian ini kamu belajar:
# - Integer (angka bulat)
# - Float (angka desimal)
# - Boolean (True/False)
# - List (data berubah)
# - Tuple (data tetap)
# - Dictionary (data berpasangan key:value)
# - Set (data unik)
#
# Semua tipe ini penting untuk struktur data dalam program.


# =====================================================================
#  OPERASI DASAR
# =====================================================================
# Kamu belajar:
# ➤ Operasi Aritmatika
#    + - * / % ** //
#
# ➤ Operasi Perbandingan
#    == != > < >= <=
#
# ➤ Assignment Operator
#    += -= *= /= dll
#
# ➤ Membership
#    x in list
#
# ➤ Identity
#    obj1 is obj2
#
# ➤ Operasi Bitwise
#    & | ^ >> <<
#
# ➤ Logika
#    and, or, not


# =====================================================================
#  PERCABANGAN (IF)
# =====================================================================
# Kamu belajar:
# - if
# - if else
# - if elif else
# - match-case (switch di Python)
#
# Percabangan menentukan alur program berdasarkan kondisi.


# =====================================================================
#  PERULANGAN (LOOP)
# =====================================================================
# Kamu belajar:
# - for loop
# - while loop
# - nested loop (loop di dalam loop)
# - break, continue, pass
#
# Loop digunakan untuk mengulang instruksi.

# sudah = ""
# while sudah != "iya":
#     sudah = input("Apakah sudah? (iya/no) :")

# for angka in range(10):
#     pass



# =====================================================================
#  STRING
# =====================================================================
# Kamu belajar:
# - Multi-line string (""" ... """)
# - Escape character (\n, \t, \b)
# - Menggabungkan string
# - 10+ method string:
#   replace(), split(), join(), upper(), lower(), title(), dll
# - Menampilkan data dengan berbagai format:
#   * formatting %s
#   * .format()
#   * f-string (cara modern)
#
# String sangat penting dalam pengolahan teks.




# =====================================================================
#  LIST
# =====================================================================
# Kamu belajar:
# - Membuat list
# - append(), extend(), remove(), pop()
# - sort(), reverse()
# - slicing list [start:end]
# - looping isi list
#
# List adalah struktur data yang sering digunakan.


# =====================================================================
#  TUPLE
# =====================================================================
# Kamu belajar:
# - Tuple tidak bisa diubah
# - Menambah elemen dengan menggabungkan tuple
# - Menghapus elemen dengan mengubah ke list dulu
# - Gabungkan tuple
# - Fungsi max(), min(), len()
#
# Tuple digunakan untuk data yang tidak boleh berubah.


# =====================================================================
#  SET
# =====================================================================
# Kamu belajar:
# - Set otomatis menghapus data duplikat
# - add(), remove()
# - union()
# - intersection()
# - difference()
# - symmetric_difference()
# - subset dan superset
#
# Set sangat berguna untuk operasi matematika himpunan.


# =====================================================================
#  DICTIONARY
# =====================================================================
# Kamu belajar:
# - key : value
# - mengakses nilai
# - menambah data
# - menghapus data
# - nested dictionary (dictionary di dalam dictionary)
# - list berisi dictionary
#
# Dictionary adalah struktur data paling penting di Python.


# =====================================================================
#  FUNCTION
# =====================================================================
# Kamu belajar:
# - Fungsi dengan parameter
# - Fungsi dengan default parameter
# - Keyword argument
# - Return value
# - Fungsi yang memanggil fungsi lain
# - Validasi dalam fungsi
# - Loop dalam fungsi
#
# Function membantu program lebih rapi dan terstruktur.