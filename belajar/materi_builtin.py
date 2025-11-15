# =====================================================================
#                  MATERI BUILT-IN FUNCTIONS & LIBRARY
# =====================================================================
# File ini berisi penjelasan lengkap mengenai:
# ✔ Built-in Function Python
# ✔ Library Standar Python
# ✔ Library Eksternal: PrettyTable, Colorama, dll.
# =====================================================================


# =====================================================================
# BAB 1 — BUILT-IN FUNCTIONS PYTHON
# =====================================================================
# Built-in Function = fungsi bawaan Python yang bisa dipakai langsung
# tanpa perlu mengimport library apa pun.
#
# Berikut daftar fungsi penting dan kegunaannya:


# --- Fungsi Tipe Data ---
# int()        → ubah ke integer
# float()      → ubah ke desimal
# str()        → ubah ke string
# bool()       → ubah ke boolean
# list()       → ubah ke list
# tuple()      → ubah ke tuple
# set()        → ubah ke set
# dict()       → ubah ke dictionary


# --- Fungsi Aritmatika / Numerik ---
# abs(x)       → nilai absolut
# pow(a, b)    → pangkat (sama dengan a**b)
# round(x, n)  → pembulatan
# max(list)    → nilai terbesar
# min(list)    → nilai terkecil
# sum(list)    → total penjumlahan list


# --- Fungsi String ---
# len()        → panjang data
# chr(kode)    → kode ASCII ke huruf
# ord(huruf)   → huruf ke kode ASCII


# --- Fungsi Input / Output ---
# input()      → ambil input user
# print()      → tampilkan output


# --- Fungsi Keamanan / Pemeriksaan ---
# type()       → melihat tipe data
# id()         → melihat alamat memori
# isinstance(x, tipe) → cek apakah x adalah tipe tertentu


# --- Fungsi Struktur Data ---
# sorted(list) → mengurutkan tanpa mengubah data asli
# reversed()   → membalik urutan data


# --- Fungsi File ---
# open(nama_file, mode)
# mode: r=read, w=write, a=append


# --- Fungsi Utility ---
# help()       → melihat dokumentasi fungsi
# dir()        → melihat isi sebuah modul atau objek


# =====================================================================
# BAB 2 — LIBRARY STANDARD PYTHON (SUDAH ADA DI PYTHON)
# =====================================================================


# ---------------------------------------------------------
# 1. MATH — Operasi Matematika Tingkat Lanjut
# ---------------------------------------------------------
# Fungsi dari module math membantu dalam:
# - akar
# - logaritma
# - trigonometri
# - konstanta matematika
#
# Fungsi populer:
# math.sqrt(x)     → akar kuadrat
# math.factorial() → faktorial
# math.sin(), cos(), tan()
# math.pi, math.e


# ---------------------------------------------------------
# 2. RANDOM — Membuat Angka Acak
# ---------------------------------------------------------
# random.random()     → angka acak 0.0 – 1.0
# random.randint(a,b) → angka bulat acak
# random.choice(list) → memilih item acak dari list
# random.shuffle(list)→ mengacak urutan list


# ---------------------------------------------------------
# 3. DATETIME — Waktu & Tanggal
# ---------------------------------------------------------
# datetime.datetime.now() → waktu sekarang
# datetime.date()         → tanggal
# timedelta()             → selisih waktu


# ---------------------------------------------------------
# 4. OS — Berhubungan dengan Sistem Operasi
# ---------------------------------------------------------
# os.getcwd()    → mendapatkan lokasi folder sekarang
# os.listdir()   → menampilkan isi directory
# os.mkdir()     → membuat folder
# os.remove()    → menghapus file


# ---------------------------------------------------------
# 5. SYS — Informasi Sistem Python
# ---------------------------------------------------------
# sys.exit()     → keluar dari program
# sys.version    → cek versi Python


# ---------------------------------------------------------
# 6. JSON — File Penyimpanan Format JSON
# ---------------------------------------------------------
# json.dumps()   → dict → string JSON
# json.loads()   → string JSON → dict
# json.dump()    → simpan ke file JSON
# json.load()    → baca file JSON


# ---------------------------------------------------------
# 7. CSV — Membaca & Menulis File CSV
# ---------------------------------------------------------
# Digunakan untuk tabel data
# writer.writerow()  → menulis baris
# reader             → membaca baris


# ---------------------------------------------------------
# 8. RE — Regular Expression (Regex)
# ---------------------------------------------------------
# re.match()     → cocokkan dari awal teks
# re.search()    → cari pola di teks
# re.findall()   → ambil semua hasil
# re.sub()       → ganti pola
#
# Regex dipakai untuk:
# - validasi email
# - validasi nomor hp
# - filtering teks


# =====================================================================
# BAB 3 — LIBRARY EKSTERNAL (INSTAL MANUAL)
# =====================================================================
# Untuk menggunakan library eksternal, kamu harus install dulu:
# pip install nama-library
#
# Di bawah ini adalah library populer untuk pemula.


# ---------------------------------------------------------
# 1. COLORAMA — Warna pada Terminal
# ---------------------------------------------------------
# Colorama digunakan untuk memberi warna pada teks terminal.
#
# Contoh warna:
# Fore.RED        → warna teks merah
# Fore.GREEN      → warna hijau
# Fore.YELLOW     → warna kuning
# Fore.CYAN       → cyan
# Style.BRIGHT    → gaya tebal/terang
# Style.RESET_ALL → reset warna
#
# Fungsi penting:
# init(autoreset=True)
#
# Autoreset memastikan warna kembali normal setelah print.


# ---------------------------------------------------------
# 2. PRETTYTABLE — Tabel Cantik di Terminal
# ---------------------------------------------------------
# Library ini digunakan untuk membuat tabel rapi.
#
# Contoh fungsi penting:
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.field_names = ["Nama", "Umur"]
# table.add_row(["Aldi", 20])
# table.add_row(["Bintang", 21])
# print(table)
#
# Kegunaan:
# - membuat menu CLI
# - menampilkan database
# - laporan keuangan
# - daftar barang


# ---------------------------------------------------------
# 3. TERM COLOR LIBRARY LAIN (opsional)
# ---------------------------------------------------------
# Selain Colorama ada:
# - Rich         (tampilan terminal modern)
# - Blessings    (kontrol terminal)
# - Crayons      (warna simple)
#
# Rich sangat populer karena mendukung:
# - tabel
# - panel
# - progress bar
# - syntax highlighting


# ---------------------------------------------------------
# 4. REQUESTS — HTTP Client
# ---------------------------------------------------------
# Digunakan untuk akses data internet/API.
#
# requests.get(url)
# requests.post(url)
#
# Contoh penggunaan:
# Mengambil data JSON dari API.


# ---------------------------------------------------------
# 5. PYFIGLET — Teks ASCII Keren
# ---------------------------------------------------------
# Digunakan untuk membuat header CLI keren.
#
# example:
# from pyfiglet import Figlet
# f = Figlet(font='slant')
# print(f.renderText("My App"))


# ---------------------------------------------------------
# 6. TABULATE — Alternatif PrettyTable
# ---------------------------------------------------------
# tabulate(data, headers="firstrow", tablefmt="grid")
#
# Cocok untuk laporan tabel cepat.


# ---------------------------------------------------------
# 7. PANDAS — Data Analysis (lanjutan)
# ---------------------------------------------------------
# Tidak wajib untuk pemula, tapi sangat powerful.
#
# digunakan untuk:
# - membaca CSV
# - memproses tabel data
# - analisis statistik


# =====================================================================
# BAB 4 — PERBEDAAN LIBRARY STANDARD vs EKSTERNAL
# =====================================================================
# 1. Standard Library:
#    - Sudah ada di Python
#    - Tidak perlu install
#    - Contoh: os, sys, random, datetime, csv, json, re
#
# 2. External Library:
#    - Harus di-install manual
#    - Lebih powerful
#    - Contoh: colorama, prettytable, requests, pandas, rich


# =====================================================================
# BAB 5 — CARA MEMILIH LIBRARY YANG TEPAT
# =====================================================================
# Gunakan library berdasarkan kebutuhan:
#
# • Ingin terminal berwarna?       → Colorama / Rich
# • Ingin tabel rapi?              → PrettyTable / Tabulate
# • Ingin akses internet?          → Requests
# • Ingin data besar?              → Pandas
# • Ingin tampilan mewah di CLI?   → Rich
# • Ingin acak angka?              → Random
# • Ingin hitung matematika?       → Math
# • Ingin waktu dan tanggal?       → Datetime
# • Ingin file JSON?               → json
# • Ingin file CSV?                → csv


# =====================================================================
# AKHIR FILE
# =====================================================================
# File ini adalah dokumentasi komplit untuk memperkenalkan:
# - Built-in Functions
# - Library Standard Python
# - Library Eksternal Umum
#
# Kamu bisa belajar satu per satu sambil melakukan praktik kecil.
# Jika ingin saya buatkan versi yang berisi CONTOH KODE, tinggal bilang!
# =====================================================================
