nilai_minimum = float(input("Nilai minimum: "))
if nilai_minimum:
    print('Selamat anda lulus!')
nilai_teori = float(input("Nilai teori: "))
if nilai_teori<70:
    print('Anda harus mengulang ujian teori')
nilai_praktek = float(input("Nilai prakrek: "))
if nilai_praktek<70:
    print('Anda harus mengulang ujian praktek')

