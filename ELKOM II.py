mahasiswa=[]
def input_data():
    print("[1. Input data]")
    nama=input("Masukkan nama mahasiswa : ")
    nilai1=int(input("Masukkan nilai praktikum 1 : "))
    nilai2=int(input("Masukkan nilai praktikum 2 : "))
    nilai3=int(input("Masukkan nilai praktikum 3 : "))
    list=[nama,nilai1,nilai2,nilai3]
    mahasiswa.insert(len(mahasiswa),list)
    main()

def view_data():
    print("[2. View data]")
    print("NAMA |","PRAK 1 |","PRAK 2 |","PRAK 3")
    print("-------------------------------")
    for i in mahasiswa:
        print(i[0],"\t",i[1],"\t ",i[2],"\t  ",i[3])
    main()

def nilai_rerata1():
    print("[3. Hitung rata-rata praktikum tiap mahasiswa]")
    for i in range(len(mahasiswa)):
        total=mahasiswa[i][1]+mahasiswa[i][2]+mahasiswa[i][3]
        print(mahasiswa[i][0],"\t=","%0.1f"%(total/3))
    main()

def nilai_rerata2():
    print("[4. Hitung nilai rata-rata tiap praktikum]")
    nilai1=0
    nilai2=0
    nilai3=0
    for i in range(len(mahasiswa)):
        nilai1+=mahasiswa[i][1]
        nilai2+=mahasiswa[i][2]
        nilai3+=mahasiswa[i][3]
    nilai1=nilai1/len(mahasiswa)
    nilai2=nilai2/len(mahasiswa)
    nilai3=nilai3/len(mahasiswa)
    print("Rerata praktikum 1 = ",nilai1)
    print("Rerata praktikum 2 = ",nilai2)
    print("Rerata praktikum 3 = ",nilai3)
    main()

def nilai_rerata3():
    print("[5. Mencari nilai rata-rata dari setiap mahasiswa]")
    nama=input("Masukkan nama mahasiswa : ")
    for i in range(len(mahasiswa)):
        total=mahasiswa[i][1]+mahasiswa[i][2]+mahasiswa[i][3]
        print(mahasiswa[i][0],"\t=","%0.1f"%(total/3))
    main()

def update_nilai():
    print("[6. Update nilai praktikum mahasiswa]")
    update=input("Masukan nama mahasiswa : ")
    nilai=int(input("Ingin update nilai praktikum ke- : "))
    nilai_baru=int(input("Nilai baru : "))
    for i in mahasiswa:
        if i [0]==update:
            i[nilai]=nilai_baru
    main()

def main():
    print("\nPROGRAM LIST")
    print("1. Input data")
    print("2. View data")
    print("3. Hitung nilai rata-rata praktikum tiap mahasiswa")
    print("4. Hitung nilai rata-rata tiap praktikum")
    print("5. Mencari nilai rata-rata dari setiap mahasiswa")
    print("6. Update nilai praktikum mahasiswa")
    print("7. Exit")
    menu=int(input("Pilih menu yang tersedia : "))
    if menu==1:
        input_data()
    elif menu==2:
        view_data()
    elif menu==3:
        nilai_rerata1()
    elif menu==4:
        nilai_rerata2()
    elif menu==5:
        nilai_rerata3()
    elif menu==6:
        update_nilai()
    elif menu==7:
        print("Terima kasih!")
        exit()
    else:
        print("Menu tidak tersedia!")
        menu=int(input("Pilih menu yang tersedia : "))
main()