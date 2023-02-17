# kripto-tugas-2
repository ini ada untuk sebagai submisi tugas 2 dari matakuliah II4031 Kripto dan Koding STI.  
dibuat oleh:
1. Muhammad Raihan Aulia (18220031)
2. Muhammad Rizki Pratama (18220110)  

## Overview
sistem cipher ini menggunakan RC4 sebagai dasar dan dimodifikasi sedemikian rupa. Bagian yang dimodifikasi adalah pada ksa, key yang dihasilkan di encrypt lagi dengan extended vigenere cipher. Setelah itu pada prga kami menerapkan konsep vigenere cipher pada saat pemilihan key yang akan di xor dengan plaintext. Untuk menambah ke-'randoman' lagi, kami mengeser juga mengubah key register pada prga dengan konsep mirip pada lsfr tetapi kami aplikasikan pada satu register secara keseluruhan.

## How to use
1. buka terminal dan pindah direktori ke folder ini
2. gunakan env python pada folder ini
3. install tkinter dengan melakukan command dibawah ini jika belum diinstall
> pip install tk  
4. jalankan aplikasi dengan me-run command "python main_gui.py"
5. gui sudah bisa digunakan untuk encrypt ataupun decrypt

### Enkripsi Text Entry
1. Masukkan input pada entry box plaintext
2. Masukkan input pada entry box key
3. tekan tombol "encrypt text"
4. jika ingin menyimpan ciphertext, dapat dilakukan dengan menekan tombol save text dibawah entry ciphertext

### Dekripsi Text Entry
1. Masukkan input pada entry box ciphertext dalam base64 (hanya boleh menggunakan text yang berupa hasil encrypt menggunakan cipher ini)
2. Masukkan input pada entry box key
3. tekan tombol "decrypt text"
4. jika ingin menyimpan plaintext, dapat dilakukan dengan menekan tombol save text dibawah entry plaintext

### Enkripsi File Entry
1. tekan tombol upload file
2. pilih file yang ingin di-encrypt
4. masukkan input key pada entry box key
5. tekan tombol "encrypt file"
6. tunggu sampai file selesai dienkripsi, sampai muncul dialogue box simpan file
7. pilih nama file dan lokasi simpan kemudian tekan tombol save

### Dekripsi File Entry
1. tekan tombol upload file
2. pilih file yang ingin di-decrypt
4. masukkan input key pada entry box key
5. tekan tombol "decrypt file"
6. tunggu sampai file selesai di-dekripsi, sampai muncul dialogue box simpan file
7. pilih nama file dan lokasi simpan kemudian tekan tombol save