#Latihan Mandiri

def validasi_nilai(nilai):
    return 0 <= nilai <=100
def input_nilai():
    while True:
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nailai UAS: "))

        if validasi_nilai(tugas) and validasi_nilai(uts) and validasi_nilai(uas):
            return tugas, uts, uas
        else:
            print("Nilai harus antara 0 - 100, ulangi!")

def hitung_nilai(tugas, uts, uas):
    return (0.3 * tugas) + (0.3 * uts) + (0.4 * uas)

def tentukan_grade(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai <= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"
    
def tampilkan_hasil(nilai, grade):
    print("Nilai akhir:", nilai)
    print("Grade:", grade)
    
#program utama
tugas, uts, uas = input_nilai()
nilai_akhir = hitung_nilai(tugas, uts, uas)
grade = tentukan_grade(nilai_akhir)
tampilkan_hasil(nilai_akhir, grade)