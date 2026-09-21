Name : Yohana Louisa Saragih    
NPM : 2506584205    
Class : PBP E  

### Assignment 1  
  
1. I use a combination of HTML5 elements, such as `<section>` to separate the profile and skills sections, `<p>` for my bio text, and `<article>` for the content of each skill, to make the structure easier to understand. I haven't used `<aside>` yet because I don't have any content that serves as a sidebar or supplement to the main content.  
  
2. My biggest challenge is keeping my skill cards from getting jumbled on mobile. That’s why I use media queries to display them in a single column on small screens.  
  
3. The drawback of my static website is that whenever I want to change the information, I have to manually edit the code. Moving forward, I want my skill data to be stored and updated in a database, not in HTML.  
  
### AI Disclosure  
  
I use AI as a tool to help me understand the concepts of semantic HTML and CSS Grid
and to debug when the results aren't as expected  

```Assignment 2```  
  
1. Ketika pertama kali pengguna membuka halaman portofolio melalui browser, itu menggunaka url.py dari project, kemudian Django mengarahkan ke urls.py aplikasi yang relevan. Lalu, memetakan URL tersebut kepada fungsi view tertentu. Kemudian mengambil data dari Model dan meneruskannya ke Template. Template ini lah dapat dilihat oleh pengguna dan kemudian mengirim respons kembali ke browser pengguna.  

2. Penyimpanan data pada Model, bukan di Template, menjadikan web lebih modular dan mudah dikelola sehingga apabila ingin dilakukan pengembangan pada data atau sebaliknya, tidak akan mengganggu fungsi lain.  
  
3. makemigration membuat file migrasi beisi sekumpulan peubahan yang telah kita tambahkan pada Model, sedangkan migrate menerapkan file migrasi yang telah kita ciptakan ke database. Contoh kasus menjalankan kedua perintah tersebut adalah jika ingin menambahkan field baru, misalnya bio, di model portofolio, kita perlu menjalankan makemigration dan migrate agar perubahan terintegrasi dengan database.  
  
```AI Disclosure```  
  
Saya menggunakan ChatGPT sebagai alat untuk membantu saya dalam melakukan debugging saat terjadi ketidak sesuaian pada hasil yang saya ekspektasikan. Kemudian saya juga meminta cheat sheet command reference CSS untuk mempermudah saya dalam menyelesaikan tugas 2 ini.  
  
```Assignment 2```  
  
1. Form beroperasi secara independen dalam membuat formulir, mendefenisikan serta memvalidasi input yang dibuat secara manual sehingga dapat di custom dan hasilnya tidak langsung terkail dengan model. Karena itu, dalam pengembangannya dibutuhkan kontrol penuh. Di sisi lain, dengan ModelForm, kita dapat membuat formulir secara otomatis berdasarkan model database sehingga memudahkan kita dalam membuat, memvalidasi, serta memperbarui data pada database. Fleksibilitas dan efisiensi yang ditawarkan ModelForm sangat membantu kita dalam maintenance web nantinya.
Dalam pembuatan formulir, {% csrf_token %} wajib kita tambahkan karena token yang unik per sesi inilah yang akan memverifikasi request http yang tidak aman dengan menggunakan autentikasi berbasis cookie sehingga dapat mencegah penyerang melakukan perubahan yang tidak diinginkan.  
  
2. JSON lebih disukai dalam pengembangan aplikasi web karena lebih fleksibel, ringkas karena tidak menggunakan tag sehingga lebih padat, dan readable. Selain itu, JSON  bersifat independent dari bahasa pemrograman tertentu dan menjadi format output umum bagi bebrapa API umum modern. Sebaliknya, XML masih menggunakan tag sehingga strukturnya lebih berat dan strukturnya sangat rentan terhadap risiko keamanan. XML juga menyediakan aturan untuk mendefenisikan data apapun dan menggunakan tanda untuk membedakan atribut data dan data aktual sehingga membuatnya lebih kompleks.  
  
3. Alur pengembalian data portofolio saya dimulai dari  view yang mengambil data dari model menggunakan query, kemudian dilakukan proses serialization, di mana data pada model diubah menjadi seperti dictionary dengan struktur python, kemudian dikonversi menjadi JSON. Serialization sangat penting agar dapat mengubah objek model mentah menjadi format yang mudah disimpan dan ditransmisikan sehingga user dapat memahami data dengan benar.  
  
```AI Disclosure```  
  
001 / 1 - Update Experience Feature: https://share.gemini.google/QMYuFsERSASa  
Membantu permasalahan penambahan fitur update serta menemukan error pada Experience  
 
