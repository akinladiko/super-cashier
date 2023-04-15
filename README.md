# Python Project: super-cashier

## Background
Perkembangan teknologi informasi pada dasarnya membuat pekerjaan yang biasa dilakukan oleh manusia jadi lebih mudah. Termasuk dengan susunan kode yang dibangun untuk mempermudah manusia dalam mengurusi kasir. Dengan adanya prototipe yang dibuat menggunakan bahasa Python ini, pekerjaan manusia akan lebih mudah ke depannya dan prototipe bisa dikembangkan lebih baik lagi.

## Goals
1. Membuat prototipe kasir menggunakan bahasa pemrograman Python, fitur yang dimiliki sebagai berikut:
- Keranjang Belanja
- Penambahan Barang
- Fitur Ubah Barang
- Fitur Hapus Barang
- Penghitung Total Belanja
- Main Menu
2. Membantu pekerjaan manusia dalam melakukan pekerjaannya di supermarket melalui otomasi kasir
3. Melatih penulis dalam penggunaan bahasa pemrograman Python

## Requirements
1. Saat customer akan membuat ID Transaction, dibutuhkan suatu class yang berisikan instance variable ID. Lalu dibuatlah method agar bisa memulai alur yang ada di toko
2. Ketika customer ingin menambahkan barang, dibutuhkan suatu method yang bisa memasukkan barang tersedia ke dalam keranjang belanja
3. Ketika customer ingin mengubah barang yang dibeli, dibutuhkan suatu method yang bisa mengubah langsung barang yang sudah dimasukkan ke dalam keranjang belanja
4. Ketika customer tidak jadi membeli, dibutuhkan suatu method yang bisa mengurangi barang yang dimaksud atau mengosongkan keranjang belanja sama sekali
5. Ketika customer ingin cek keranjang belanjanya, dibutuhkan suatu method yang bisa melihat isi keranjang belanja
6. Ketika customer ingin membayar, dibutuhkan suatu method yang langsung menghitung total belanja berikut dengan diskon yang ditetapkan.

## Flowchart
![flowchart](https://github.com/akinladiko/super-cashier/blob/main/flowchart_python.png?raw=true)

## Function
Berikut adalah penjelasan function yang ada di script:
- start_belanja = Untuk memulai alur belanja di toko, mendeteksi ID dari pelanggan.
- main_menu = Untuk mengakses main menu toko, sebagai center dari segala fitur pada kasir.
- tambah_barang = Untuk menambahkan barang ke dalam keranjang belanja.
- update_barang = Untuk mengubah jenis barang yang sudah ada di dalam keranjang belanja.
- update_jumlah = Untuk mengubah jumlah barang yang sudah ada di dalam keranjang belanja.
- hapus_barang = Untuk menghapus sebagian barang yang ada di dalam keranjang belanja.
- reset_barang = Untuk menghapus seluruh barang yang ada di dalam keranjang belanja.
- cek_keranjang = Untuk mengecek ulang barang yang ada di dalam keranjang belanja.
- pembayaran = Untuk membayar seluruh barang yang ada di dalam keranjang belanja.

## Test Case

### Test 1
![test1_1](https://github.com/akinladiko/super-cashier/blob/main/test%20case/test1_1.png?raw=true)
![test1_2](https://github.com/akinladiko/super-cashier/blob/main/test%20case/test1_2.png?raw=true)
![test1_3](https://github.com/akinladiko/super-cashier/blob/main/test%20case/test1_3.png?raw=true)

### Test 2
![test2](https://github.com/akinladiko/super-cashier/blob/main/test%20case/test2.png?raw=true)

### Test 3
![test3](https://github.com/akinladiko/super-cashier/blob/main/test%20case/test3.png?raw=true)

### Test 4
![test4_1](https://github.com/akinladiko/super-cashier/blob/main/test%20case/test4_1.png?raw=true)
![test4_2](https://github.com/akinladiko/super-cashier/blob/main/test%20case/test4_2.png?raw=true)

## Conclusion and Suggestion
Kesimpulan yang bisa diambil dari dibangunya prototipe ini adalah bahwa saat ini mesin bisa membantu manusia dalam mengerjakan pekerjaannya. Saran yang bisa diambil adalah debugging yang lebih baik lagi, karena script yang dibuat cukup kompleks.

