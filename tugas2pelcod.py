# 2. kamu ingin membeli cupang dengan harga 10rb dan koi dengan harga 20rb
# uang yang kamu bawa sebesar Rp.182.000 (3 angka terakhir nim saya adalah 082 jadi jika di + 100 adalah 182 jadi Rp. 182 000)
# kamu hanya beli 5 cupang dan 2 koi
# berapa sisa uangmu

ikan_cupang=10000
ikan_koi=20000
banyaknya_uang=182000
banyaknya_uang=(print("banyaknya uang yang saya miliki adalah : Rp. 182.000"))
banyaknya_beli_ikan_cupang=int(input("berapa banyak membeli ikan cupang : "))
jumlah_harga_ikan_cupang_seluruhnya=banyaknya_beli_ikan_cupang*ikan_cupang
print("jumlah harga ikan cupang seluruhnya adalah : ", jumlah_harga_ikan_cupang_seluruhnya)
benyaknya_beli_ikan_koi=int(input("berapa banyak membeli ikan koi : "))
jumlah_harga_ikan_koi_seluruhnya=benyaknya_beli_ikan_koi*ikan_koi
print("jumlah harga ikan koi seluruhnya adalah : ", jumlah_harga_ikan_koi_seluruhnya)
berapa_uang_yang_saya_miliki=int(input("berapa uang yang saya miliki : "))
jadi=jumlah_harga_ikan_cupang_seluruhnya+jumlah_harga_ikan_koi_seluruhnya
print("jumlah harga keseluruhannya adalah : ", jadi)
kembalian_yang_saya_dapatkan_adalah=berapa_uang_yang_saya_miliki-jadi
print("sisa uang saya adalah : ", kembalian_yang_saya_dapatkan_adalah)

print("-"*50)