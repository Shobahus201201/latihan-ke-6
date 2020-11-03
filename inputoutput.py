# input output file

"""

w = write mode / mode menulis dan menghapus file lama, jika file tidak ada maka akan dibuat file baru 
r = read mode only / hanya bisa baca
a = appending mode / menambahkan data diakhir baris
r+ = write and read mode

"""

# membuat file dalam bentuk text 

file = open("data.txt",'w')

file.write("ini adalah data text yang dibuat dengan menggunakan data python")
file.write("\nHallo perkenalkan nama saya Shobahus")
file.write("\nsaya sering di panggil shoba")
file.write("\nSaya kuliah di UNIVERSITAS PELITA BANGSA")
file.write("\nSaya masih belajar")

file.close()










