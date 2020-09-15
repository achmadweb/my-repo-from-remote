#class MyClass:
#   nama = "Achmad Hidayat"

#name = MyClass()
#print(name.nama)

class person:
    def __init__(obj, name, age):
        obj.name = name
        obj.age = age

#tambahan fungsi def disini
    def myfunc(abc):
        print("Hallo nama saya adalah" + abc.name)
        print("Umur saya adalah " + str(abc.age))

#konversi string abc.age dulu
#tambahan selesai

run = person ("john", 30)

#run disini dicomment dulu
#print(run.name)
#print(run.age)

#tambahkan run.myfunc()
run.myfunc()