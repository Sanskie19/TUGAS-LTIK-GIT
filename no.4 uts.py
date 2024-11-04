#NAMA : MUHAMMAD IHSAN ANSORI
#NIM : 2400409
#KELAS : RPL 1C

def kelompokkelas(nim):
  
  tiga_digit_terakhir = int(str(nim)[-3:])

  if tiga_digit_terakhir >= 1 and tiga_digit_terakhir <= 50:
    if tiga_digit_terakhir % 2 == 0:
      return "K2"
    else:
      return "K1"
  elif tiga_digit_terakhir >= 51 and tiga_digit_terakhir <= 100:
    if tiga_digit_terakhir % 2 == 0:
      return "K4"
    else:
      return "K3"
  elif tiga_digit_terakhir >= 101 and tiga_digit_terakhir <= 150:
    if tiga_digit_terakhir % 2 == 0:
      return "K6"
    else:
      return "K5"
  else:
    if tiga_digit_terakhir % 2 == 0:
      return "K8"
    else:
      return "K7"

nim = int(input("Masukan NIM anda: "))
kelas = kelompokkelas(nim)
print(f"NIM: {nim}, Kelas: {kelas}")