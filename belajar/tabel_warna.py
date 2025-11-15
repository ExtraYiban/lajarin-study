from colorama import Fore, Back, Style, init
from prettytable import PrettyTable
init(autoreset=True)
# =====================================================================
#  COLORAMA (Membuat Warna di Terminal)
# =====================================================================
# Colorama adalah library eksternal yang digunakan untuk memberikan
# warna dan gaya pada teks yang ditampilkan di terminal.
#
# Untuk menggunakan Colorama:
#   1. Install dulu:
#          pip install colorama
#
#   2. Import komponen penting:
#          from colorama import Fore, Back, Style, init
#
#   3. Jalankan inisialisasi:
#          init(autoreset=True)
#
# Dengan autoreset=True warna otomatis kembali normal setelah print.
#
# ---------------------------------------------------------------------
# KOMPONEN COLORAMA
# ---------------------------------------------------------------------
#
# 1. Fore (warna teks)
#    Fore.RED
#    Fore.GREEN
#    Fore.YELLOW
#    Fore.BLUE
#    Fore.CYAN
#    Fore.MAGENTA
#    Fore.WHITE
#
# 2. Back (warna background)
#    Back.RED
#    Back.GREEN
#    Back.YELLOW
#
# 3. Style (gaya font)
#    Style.BRIGHT   → Teks tebal/terang
#    Style.DIM      → Teks redup
#    Style.NORMAL   → Normal
#    Style.RESET_ALL→ Reset manual warna dan gaya
#
# ---------------------------------------------------------------------
# CONTOH PENGGUNAAN (Hanya sebagai catatan, bukan eksekusi):

#
merahTerang = Fore.RED + Style.BRIGHT
print(merahTerang + "Ini teks merah")
print(Fore.GREEN + Style.BRIGHT + "Hijau terang")
print(Back.YELLOW + Fore.BLACK + "Teks hitam latar kuning")
print(Back.RED+Fore.YELLOW + "Peringatan!")
#
# Dengan Colorama kamu bisa:
# - Membuat banner program berwarna
# - Memberi indikator error (merah)
# - Memberi indikator sukses (hijau)
# - Menampilkan menu CLI yang lebih keren
#
# =====================================================================



# =====================================================================
#  PRETTYTABLE (Membuat Tabel Cantik di Terminal)
# =====================================================================
# PrettyTable adalah library eksternal yang digunakan untuk membuat
# tabel dengan tampilan rapi dan profesional di terminal.
#
# Install dulu:
#       pip install prettytable
#
# Import:
#       from prettytable import PrettyTable
#
# ---------------------------------------------------------------------
# FITUR PENTING PRETTYTABLE
# ---------------------------------------------------------------------
#
# 1. Membuat objek tabel:
#       table = PrettyTable()
tabel = PrettyTable()
tabel.field_names = [f"{merahTerang}nama", "umur", f"hobi {Style.RESET_ALL}"]
tabel.add_row(["Cipa", 20, "ngoding"])
tabel.add_row(["alia", 18, "makan"])
print(tabel)
#
# 2. Menambahkan header kolom:
#       table.field_names = ["Nama", "Umur", "Alamat"]
#
# 3. Menambahkan baris data:
#       table.add_row(["Budi", 20, "Samarinda"])
#       table.add_row(["Aldi", 21, "Balikpapan"])
#
# 4. Menampilkan tabel:
#       print(table)
#
# ---------------------------------------------------------------------
# FITUR LANJUTAN:
#
# 1. Mengatur alignment (rata kiri/kanan)
#       table.align["Nama"] = "l"
#       table.align["Umur"] = "r"
#
# 2. Mengatur border / garis
#       table.hrules = True
#
# 3. Menghapus garis vertikal:
#       table.vertical_char = " "
#
# 4. Mengatur format angka (float → 2 desimal)
#       table.float_format = ".2"
#
# ---------------------------------------------------------------------
# KEGUNAAN PRETTYTABLE:
# - Menampilkan tabel mahasiswa
# - Menampilkan daftar barang
# - Membuat menu CRUD agar rapi
# - Menampilkan laporan keuangan
# - Menampilkan hasil pencarian
#
# PrettyTable sangat cocok jika kamu ingin program CLI terlihat profesional.
#
# =====================================================================
