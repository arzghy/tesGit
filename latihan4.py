'''
Nama  : Faza Izzaturrafi
Kelas : TPL A/P1
NIM   : J0403241102
'''

setPertama = {1, 2, 3, 4, 5, 6, 7, 8} # Membuat set bernama setPertama yang berisi angka 1 sampai 8
setKedua = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15} # Membuat set bernama setKedua yang berisi angka 6 sampai 15

# Mencetak hasil operasi union setPertama dan setKedua
print('Union:',	setPertama.union(setKedua))

# Mencetak hasil operasi intersection setPertama dan setKedua
print('Intersection:', setPertama.intersection(setKedua))

# Mencetak hasil operasi difference setPertama
print('Difference:', setPertama.difference(setKedua))

# Mencetak hasil operasi difference setKedua
print('Difference:', setKedua.difference(setPertama))
