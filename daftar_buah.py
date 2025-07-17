def daftar_buah(*buah):
  """Menampilkan daftar buah yang dibeli."""
  print("Buah yang anda beli adalah:")
  for i, b in enumerate(buah, 1):
    print(f"{i}. {b}")
  print("Terimakasih...")


jumlah_buah = int(input("Masukan banyaknya buah yang dibeli: "))
nama_buah = []
for i in range(jumlah_buah):
  nama = input(f"Buah {i+1}: ")
  nama_buah.append(nama)

daftar_buah(*nama_buah)