'''
Nama  : Faza Izzaturrafi
Kelas : TPL A/P1
NIM   : J0403241102
'''

karakterWebtoon	= {
				'Nama': 'Gamin Yoon', # key 'Nama' dengan value 'Gamin Yoon'
				'Genre': 'Aksi', # key 'Genre' dengan value 'Aksi'
				'Gender': 'Laki-laki', # key 'Gender' dengan value 'Laki-laki'
				'Keterangan Tambahan': (180, 80, 18), # Value bertipe data tuple yang berisi tinggi badan, berat badan, dan usia
				'Hobi':	{'Belajar',	'Berantem',	'Memecahkan kasus'} # Value bertipe data set dengan key 'Hobi'
                }

print('Nama:', karakterWebtoon['Nama']) # Mencetak key 'Nama' beserta valuenya
print('Genre:', karakterWebtoon['Genre']) # Mencetak key 'Genre' beserta valuenya
print('Gender:', karakterWebtoon['Gender']) # Mencetak key 'Gender' beserta valuenya
print('Keterangan Tambahan:',	karakterWebtoon['Keterangan Tambahan']) # Mencetak key 'Keterangan Tambahan' beserta valuenya
print('Hobi:',	karakterWebtoon['Hobi']) # Mencetak key 'Hobi' beserta valuenya

# Operasi dictionary
karakterWebtoon['Judul'] = 'Study Group' # Menambahkan key 'Judul' dengan value 'Study Group' ke dictionary karakterWebtoon
karakterWebtoon['Gender'] = 'Pria' # Mengubah value pada key 'Gender' menjadi 'Pria'
genre = karakterWebtoon.pop('Genre') # Menghapus key 'Genre' beserta valuenya dan menyimpannya ke dalam variable genre

# Operasi set
karakterWebtoon['Hobi'].add('Mengungkap kasus') # Menambahkan satu elemen, yaitu 'Mengungkap kasus' ke dalam value set pada key 'Hobi'
# Menambahkan banyak elemen sekaligus ke dalam value set pada key 'Hobi'
karakterWebtoon['Hobi'].update(['Bermain', 'Menuntut ilmu', 'Berkelahi', 'Memukul lawan'])
karakterWebtoon['Hobi'].remove('Memukul lawan') # Menghapus satu elemen, yaitu 'Memukul lawan' dari value set pada key 'Hobi'
karakterWebtoon['Hobi'].pop() # Menghapus satu elemen secara acak dari value set pada key 'Hobi'
karakterWebtoon['Hobi'].clear() # Menghapus semua elemen dari value set pada key 'Hobi'
# Menambahkan banyak elemen sekaligus ke dalam value set pada key 'Hobi'
karakterWebtoon['Hobi'].update(['Belajar',	'Berantem',	'Memecahkan kasus']) 

# Operasi tuple tidak bisa karena tuple bersifat immutable

print(karakterWebtoon) # Mencetak dictionary karakterWebtoon yang telah dimodifikasi
print('key yang telah dihapus adalah', genre) # Mencetak value dari key yang telah dihapus
