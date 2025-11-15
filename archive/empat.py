# percabangan

kumpulan_angka = [1,2,3,4,6,7,8]
# IF

# if 9 not in  kumpulan_angka and 5 in kumpulan_angka:
#     # print("ini sama")

# IF - ELSE
# if 10 in kumpulan_angka:
#     print("ini ngak muncul")
# else:
#     print("ini jalan karena tidak true")

# IF - ELIF - ELSE
if 10 in kumpulan_angka:
    print("ada 10 woy")
elif 5 in kumpulan_angka:
    print("ada 5 woy")
elif 2 in  kumpulan_angka:
    print("ada 2 woy")
else:
    print("gak ada tuh")

# SWITCH

angka = 3

# if angka == 1:
#     print("angka 1")
# elif angka == 2:
#     print("angka 2")
# elif angka == 3:
#     print("angka 3")
# elif angka == 4:
#     print("angka 4")

match angka:
    case 1:
        print("angka 1")
    case 2:
        print("angka 2")
    case 3:
        print("angka 3")
    case 3:
        pass
# try Except
try:
    print(5 / 0)
except:
    print("ini jalan karena ada error")

print("ini jalan")
# For pake Range

# for dengan in

# while loop