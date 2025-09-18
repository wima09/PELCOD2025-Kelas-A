# 3. kamu ingin pergi liburan dengan sepeda motor 
# total jarak perjalanan 82km (82km karena 3 angka terakhir nim saya adalah 082)
# konsumsi BBM sepeda motor 2.7 KM per liter 
# kapasitas tangki sepeda motor 8 liter (8 liter karena angka paling belakang dari nim saya adalah 8)
# harga bensin per liter Rp. 10820 (10820 karena 3 angka belakang nim saya adalah 082)
# jika total bensin yang di butuhkan > 3 liter, maka dapat diskon Rp. 500 per liter 
# berapa total bensin yang di butuhkan. harga bensin perliter setelah diskon (jika ada)
# total biaya bensin, dan perkiraan berapa kali kamu harus mengisi bensin (dengan asumsi tangki penuh setiap kali isi ) ? 

BBM=2.7

jarak=int(input("masukan jarak perjalanan yang di tempuh : "))
kapasitas_tangki=int(input("masukan kapasitas tangki motor : "))
harga_bensin_per_liter=int(input("masukan harga bensin perliternya : "))

total_bensin_yang_di_butuhkan=jarak//BBM
print("total bensin yang di butuhkan adalah", (int(total_bensin_yang_di_butuhkan)) ) 
diskon=(total_bensin_yang_di_butuhkan > 3) *500
harga_setelah_mendapatkan_diskon=harga_bensin_per_liter - diskon
total_biaya_selama_perjalanan=total_bensin_yang_di_butuhkan * harga_setelah_mendapatkan_diskon
print("total biaya bensin : Rp.", harga_setelah_mendapatkan_diskon)
isi_ulang=-(-total_bensin_yang_di_butuhkan // kapasitas_tangki)
print("jumlah isi ulang bensin selama perjalanan :", (int(isi_ulang)) )