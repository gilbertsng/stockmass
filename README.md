# Kevin Gilbert Sinaga - 2206826053
# PBP F
https://github.com/gilbertsng/stockmass

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Pertama saya membuat project django baru dengan nama stockmass
2. Lalu saya menjalankan command "python3 -m venv env" dan "source env/bin/activate"
3. Setelah menjalankan command, saya membuat file nama "requirements.txt" yang isinya beberapa dependencies
4. Untuk mendownload isi requirements, saya menjalankan "pip3 install -r requirements.txt"
5. Kemudian buka file settings.py dalam direktori stockmass, lalu tambahkan * pada ALLOWED_HOSTS di settings.py untuk keperluan deployment
6. Lalu, tambahkan berkas .gitignore untuk mengabaikan file" yang tidak diperlukan
7. Setelah itu saya akan membuat aplikasi baru bernama main dalam proyek stockmass dengan command "python manage.py startapp main"
8. Kemudian didalam main folder, saya buat folder dengan nama templates yang akan diisi file main.html untuk menampilkan aplikasi
9. Lalu, saya membuat file baru dengan nama urls.py di dalam folder main dan menambahkan path baru "path('', show_main, name='show_main')" untuk url file bisa saling terhubung
10. Setelah itu, saya menambahkan path baru yaitu "main" pada url patterns ke file urls.py yang ada di folder stockmass
11. Lalu, saya membuat atribut pada models.py dan klik views.py
12. Kemudian membuat function yang mewakilkan atribut pada models.py agar dapat di return pada main.html untuk ditampilkan secara statis
13. Setelah selesai, saya melakukan add, push, dan commit ke repo github saya
14. Ketika github sudah terupdate, saya bisa melakukan deploy di adaptable dengan cara menghubungkan ke repo saya.

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
<img src="/Foto//foto.bagan.png">

### Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment merupakan tools untuk membuat lingkungan python virtual yang terisolasi atau tidak bisa diakses dari dunia luar dan kita menggunakan virtual environment untuk membantu dalam mengisolasi dependensi proyek, menghindari konflik antara paket, dan menjaga instalasi yang bersih. Membuat aplikasi web berbasis Django tanpa menggunakan virtual environment bisa saja tetapi, hal ini tidak disarankan supaya terhindar terjadinya project tidak terisolasi. 

### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC atau yang biasa disebut Model View Controller merupakan model yang sering digunakan untuk mengembangkan sebuah software. 

MVT atau yang biasa disebut Model-View-Template, digunakan dalam Django, serupa dengan MVC, Model mengelola data, View menampilkan data, dan Template merender tampilan.

MVVM atau Model-View-ViewModel merupakan pengembangan software yang memisahkan Model (data), View (tampilan), dan ViewModel (perantara antara data dan tampilan), dan biasanya fokus ke pemisahan antara tampilan, logika, dan data.

### Apa perbedaan antara form POST dan form GET dalam Django?

Form POST menggunakan metode di mana data dikirim sebagai bagian dari permintaan HTTP POST, form POST digunakan ketika perlu mengirim data yang sifatnya rahasia (data pribadi atau kata sandi). Data ini tidak muncul di URL, dan metode ini dapat mengirim data yang lebih besar. Biasanya, dalam Django, penggunaan metode POST berhubungan dengan mengirimkan data yang nantinya akan diproses atau disimpan di server.

sedangkan untuk Form GET merupakan cara di mana data dikirim sebagai bagian dari URL yang bentuknya string query. form GET digunakan ketika ingin berbagi data dengan mudah atau ketika pengguna dapat melihat data yang dikirim atau menyimpannya sebagai bookmark. 
Ini berguna saat Anda ingin berbagi data dengan mudah atau ingin pengguna dapat melihat data yang dikirim atau menyimpannya sebagai bookmark. Penggunaan metode GET seringkali terkait dengan tindakan pencarian atau penyaringan, tetapi perlu diingat bahwa data yang dikirimkan melalui GET memiliki batasan panjang URL dan kurang cocok untuk data yang berukuran besar atau bersifat rahasia.

### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML atau eXtensible Markup Language merupakan format yang fleksibel yang memungkinkan penggunaan tag dan atribut yang dapat disesuaikan, biasanya digunakan untuk pertukaran data antara aplikasi yang berbeda atau untuk keperluan konfigurasi. XML tidak memiliki format bawaan untuk representasi data yang lebih sederhana.

JSON atau JavaScript Object Notation merupakan format ringkas yang lebih mudah dibaca dan sangat efisien dalam pertukaran data antar aplikasi web dan API karena kemampuannya yang baik dalam merepresentasikan data struktur beranak dan berulang.Biasanya digunakan dalam pengembangan web modern dan API karena ringan dan mudah diuraikan oleh JavaScript.

HTML atau HyperText Markup Language merupakan bahasa markup yang digunakan untuk membuat tampilan halaman web dan tidak digunakan untuk pertukaran data secara langsung. HTML memiliki struktur khusus untuk mengatur tampilan halaman web, sementara XML dan JSON lebih tentang representasi data.

### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena :

Ringkas dan Mudah Dibaca: 
--> JSON memiliki struktur yang padat dan mudah dimengerti, sehingga menjadi pilihan yang sempurna untuk pertukaran data antara aplikasi web.

Kompatibel dengan JavaScript: 
--> JSON adalah bagian yang terintegrasi dengan JavaScript, sehingga dengan mudah dapat diurai dan dimanfaatkan oleh aplikasi web yang dikembangkan dengan menggunakan JavaScript.

Mudah Diproses: 
--> JSON memiliki format yang dapat dengan mudah diolah oleh berbagai bahasa pemrograman, sehingga dapat digunakan secara efektif dalam berbagai teknologi dan platform.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Pertama saya membuat file dengan nama forms.py, lalu file tersebut diisi dengan variabel sesuai dengan model yang didefinisikan di file models.py
2. Kedua saya memodifikasi beberapa pada file view.py, dengan cara membuat fungsi baru "create_product" tujuannya untuk membuat produk sesuai input user. setelah itu, saya mengubah bagian fungsi show_main yang ada di file views.py agar produk yang diinput bisa disimpan.
3. Ketiga saya membuat file create_product.html. Lalu, membuat file create_product.html untuk tampilan pada input produk. Didalam file ini ada tombol add new product yang mengarahkan user ke page input produk. Setelah diinput, user akan kembali ke main page untuk melihat input produk.
4. Terakhir adalah routing, dalam langkah ini saya melakukan routing pada semua fungsi. Dalam langkah ini saya menambahkan beberapa import yang diperlukan pada file views.py, lalu saya tambahkan juga beberapa path baru untuk manggil fungsi melalui URL. Dibawah ini adalah isi dari urls.py saya:
<img src="/Foto//urls">

5. Screenshot hasil akses URL pada Postman.
a. HTML
<img src="/Foto//foto.html.png">
b. XML
<img src="/Foto//foto.xml.png">
c. JSON
<img src="/Foto//foto.json.png">
d. XML by ID
<img src="/Foto//foto.xmlid.png">
e. JSON by ID
<img src="/Foto//foto.jsonid.png">
