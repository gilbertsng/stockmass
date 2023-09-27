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
<img src="/Foto//urls.png">

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

### Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Django UserCreationForm adalah salah satu bentuk formulir bawaan (built-in form) yang disediakan oleh Django, sebuah framework pengembangan web Python yang populer. Form ini digunakan untuk membuat dan mendaftarkan pengguna baru dalam aplikasi web kita. UserCreationForm telah dirancang khusus untuk memudahkan proses pembuatan akun pengguna dengan informasi seperti username, password1, dan password2 (yang digunakan untuk konfirmasi password).

Berikut adalah beberapa kelebihan dan kekurangan dari Django UserCreationForm:

(+)
1. Penggunaannya sangat mudah karena UserCreationForm merupakan salah satu form yang sudah disediakan Django sehingga dapat digunakan dengan mudah karena membuatnya tidak perlu menulis kode form dari awal.
2. Validasi yang otomatis, ini digunakan untuk menyocokan antara password yang dimasukkan dengan konfirmas password dan form ini dapat mecegah kesalahan dalam proses pendaftaran.
3. Form ini berintegrasi dengan baik dengan Django Authentication (Setelah user mendaftarkan akun, user dapat login ke aplikasi tanpa penyesuaian tambahan).
4. Form ini menjaga keamanan password user.

(-)
1. Form ini hanya memiliki username, password, dan konfirmasi password. Hal ini tidak mencukupi jika kita membutuhkan informasi tambahan dari user seperti alamat email, nama lengkap dan lain-lain sehingga kita harus menambahkan beberapa bidang secara manual jika diperlukan.
2. Tampilan dari form ini sangat sederhana
3. Form ini hanya dapat digunakan dalam aplikasi Django sehingga ketika ingin mengembangkan aplikasi di luar Django, kita harus mencari solusi autentikasi user yang berbeda
4. Validasi yang dimiliki form ini terbatas karena hanya memeriksa antara kesamaan password yang diinput dengan konfirmasi password. Kita harus menambahkan validasi lagi, seperti validasi alamat email yang unik.
5. Meskipun UserCreationForm mencakup validasi otomatis untuk password, masih penting untuk mengimplementasikan praktik keamanan tambahan seperti hashing password untuk melindungi password pengguna dengan lebih baik.

### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi merupakan proses verifikasi identitas pengguna yang mencoba akses ke suatu aplikasi dengan username dan password. Autentikasi digunakan untuk memastikan bahwa user yang mengakses aplikasi merupakan user yang sah dan memiliki izin untuk masuk ke suatu aplikasi. Django menyediakan sistem autentikasi yang kuat yang mencakup model pengguna (User model) yang dapat digunakan untuk mengelola data pengguna seperti nama pengguna dan kata sandi, serta berbagai alat untuk mengatur autentikasi, termasuk form bawaan seperti UserCreationForm dan AuthenticationForm.

Otorisasi merupakan proses yang terjadi setelah autentikasi berhasil. Hal ini menentukan apa yang diizinkan pengguna lakukan dalam aplikasi, seperti mengakses halaman tertentu, menggunakan fitur khusus, atau mengubah data. Otorisasi digunakan untuk memastikan user hanya memiliki akses ke bagian-bagian dari aplikasi sesuai peran mereka. Ini membatasi aksi apa yang dapat mereka lakukan dalam aplikasi tersebut.
Django menyediakan mekanisme otorisasi melalui sistem izin (permissions) dan grup pengguna (user groups). Anda dapat mengatur izin untuk model dan tindakan tertentu, dan kemudian menetapkan izin-izin ini kepada pengguna atau grup pengguna. Django juga memiliki dekorator seperti @login_required yang memungkinkan Anda mengontrol akses pengguna ke tampilan tertentu.

Pentingnya autentikasi dan otorisasi dalam aplikasi web adalah sebagai berikut:
1. Keamanan, autentikasi memastikan bahwa user yang memiliki izin dapat mengakses aplikasi dan otorisasi memastikan bahwa user dapat melakukan aksi sesuai dengan peran user yang dapat melindungi data dan fungsi sensitif.
2. Menggunakan kedua hal tersebut dapat meningkatkan pengalaman user dengan memastikan bahwa user dapat memiliki akses yang tepat ke fitur" yang sesuai dengan peran mereka dalam suatu aplikasi.

### Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies dalam konteks aplikasi web merupakan potongan" kecil dari data yang disimpan pada sisi klien (web browser) saat user berinteraksi dengan aplikasi web. Cookies digunakan untuk menyimpan informasi yang diperlukan agar dapat mengenali user, melacak sesi, atau menyimpan preferensi pengguna dan cookies berguna untuk mengingat informasi tertentu dari user seperti kunjungan sebelumnya sehingga user tidak perlu memasukkan data yang sama berulang-ulang.

Cara Django mengelola data sesi user:
1. Mengidentifikasi User
2. Penyimpanan Data Sesi
3. Pengiriman Cookie ke Browser
4. Penggunaan Cookie pada Setiap Permintaan
5. Penghapusan Otomatis

### Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies aman secara default dalam pengembangan web jika diimplementasikan dengan benar, tetapi ada beberapa risiko potensial yang harus diwaspadai seperti,
1. Data yang disadap, cookies biasanya tersimpan pada sisi klien, dan meskipun mereka sering dienkripsi, mereka masih dapat rentan terhadap penyadapan data jika SSL/TLS (HTTPS) tidak diaktifkan. Dalam skenario tanpa HTTPS, data yang disimpan dalam cookies dapat dengan mudah dibaca oleh pihak yang tidak berwenang jika ada serangan man-in-the-middle.
2. Jika aplikasi rentan terhadap serangan XSS, penyerang dapat menyisipkan skrip berbahaya ke dalam halaman web yang akan dieksekusi oleh browser user. Ini dapat memungkinkan penyerang untuk mengambil cookies user, yang dapat digunakan untuk mengakses sesi user atau informasi pribadi.
3. Serangan CSRF (Cross-Site Request Forgery) dapat menyebabkan user yang sudah diautentikasi melakukan tindakan tanpa sepengetahuan mereka. Penyerang dapat memaksa user untuk mengirim permintaan yang tidak disengaja ke aplikasi dengan cookies sesi yang sah, yang dapat menyebabkan aksi yang tidak diinginkan.
4. Jika menyimpan data sensitif seperti informasi login atau informasi pribadi dalam cookies, risiko kebocoran data meningkat. Meskipun data dienkripsi, ada kemungkinan risiko jika cookie dicuri atau disusupi.
5. Jika sesi user tidak memiliki waktu kadaluarsa yang sesuai, cookies sesi dapat tetap aktif terlalu lama, yang dapat membahayakan keamanan jika user lupa untuk logout atau meninggalkan komputer mereka terbuka.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Pertama saya mengaktifkan virtual environment
2. Lalu saya melakuka import beberapa modul yang diperlukan, seperti UserCreationForm
3. Untuk menghasilkan form regis secara otomatis, saya membuat fungsi register
4. Membuat berkas HTML yang digunakan untuk tampilan dari hasil form pendaftaran akun user ketika data disubmit
5. Dalam berkas urls.py saya import fungsi register dan menambahkan path URL ke urlpatterns
6. Lalu saya import lagi fungsi login dengan nama login_user dan authenticate dengan cara yang sama
7. Import logout dan membuat fungsi logout
8. Saya menambahkan sebuah tag hyperlink yang dimiliki fungsi logout pada berkas main.html
9. views.py yang ada pada subdirektori main saya buka dan menambahkan import login_required pada bagian paling atas untuk melakukan proses otorisasi (membatasi akses pengguna)
10. Lalu saya menambahkan kode @login_required(login_url='/login') di atas fungsi show_main agar halaman main hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).
11. Setelah itu, saya membuat akun untuk menghubungkan Item dan Product, dengan cara Import User ke models.py
12. Pada fungsi create_product di views.py saya mengubah kode untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database
13. Terakhir, saya melakukan migrasi untuk menyimpan semua perubahan di sistem.


