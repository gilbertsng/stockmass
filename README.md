# Kevin Gilbert Sinaga - 2206826053
# PBP F
https://github.com/gilbertsng/stockmass

## README Tugas 2
### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
<img src="/Foto//foto.bagan.png">

### 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment merupakan tools untuk membuat lingkungan python virtual yang terisolasi atau tidak bisa diakses dari dunia luar dan kita menggunakan virtual environment untuk membantu dalam mengisolasi dependensi proyek, menghindari konflik antara paket, dan menjaga instalasi yang bersih. Membuat aplikasi web berbasis Django tanpa menggunakan virtual environment bisa saja tetapi, hal ini tidak disarankan supaya terhindar terjadinya project tidak terisolasi. 

### 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC atau yang biasa disebut Model View Controller merupakan model yang sering digunakan untuk mengembangkan sebuah software. 

MVT atau yang biasa disebut Model-View-Template, digunakan dalam Django, serupa dengan MVC, Model mengelola data, View menampilkan data, dan Template merender tampilan.

MVVM atau Model-View-ViewModel merupakan pengembangan software yang memisahkan Model (data), View (tampilan), dan ViewModel (perantara antara data dan tampilan), dan biasanya fokus ke pemisahan antara tampilan, logika, dan data.
---
---

## README Tugas 3
### 1. Apa perbedaan antara form POST dan form GET dalam Django?
Form POST menggunakan metode di mana data dikirim sebagai bagian dari permintaan HTTP POST, form POST digunakan ketika perlu mengirim data yang sifatnya rahasia (data pribadi atau kata sandi). Data ini tidak muncul di URL, dan metode ini dapat mengirim data yang lebih besar. Biasanya, dalam Django, penggunaan metode POST berhubungan dengan mengirimkan data yang nantinya akan diproses atau disimpan di server.

sedangkan untuk Form GET merupakan cara di mana data dikirim sebagai bagian dari URL yang bentuknya string query. form GET digunakan ketika ingin berbagi data dengan mudah atau ketika pengguna dapat melihat data yang dikirim atau menyimpannya sebagai bookmark. 
Ini berguna saat Anda ingin berbagi data dengan mudah atau ingin pengguna dapat melihat data yang dikirim atau menyimpannya sebagai bookmark. Penggunaan metode GET seringkali terkait dengan tindakan pencarian atau penyaringan, tetapi perlu diingat bahwa data yang dikirimkan melalui GET memiliki batasan panjang URL dan kurang cocok untuk data yang berukuran besar atau bersifat rahasia.

### 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
XML atau eXtensible Markup Language merupakan format yang fleksibel yang memungkinkan penggunaan tag dan atribut yang dapat disesuaikan, biasanya digunakan untuk pertukaran data antara aplikasi yang berbeda atau untuk keperluan konfigurasi. XML tidak memiliki format bawaan untuk representasi data yang lebih sederhana.

JSON atau JavaScript Object Notation merupakan format ringkas yang lebih mudah dibaca dan sangat efisien dalam pertukaran data antar aplikasi web dan API karena kemampuannya yang baik dalam merepresentasikan data struktur beranak dan berulang.Biasanya digunakan dalam pengembangan web modern dan API karena ringan dan mudah diuraikan oleh JavaScript.

HTML atau HyperText Markup Language merupakan bahasa markup yang digunakan untuk membuat tampilan halaman web dan tidak digunakan untuk pertukaran data secara langsung. HTML memiliki struktur khusus untuk mengatur tampilan halaman web, sementara XML dan JSON lebih tentang representasi data.

### 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
Alasan JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena :

Ringkas dan Mudah Dibaca: 
--> JSON memiliki struktur yang padat dan mudah dimengerti, sehingga menjadi pilihan yang sempurna untuk pertukaran data antara aplikasi web.

Kompatibel dengan JavaScript: 
--> JSON adalah bagian yang terintegrasi dengan JavaScript, sehingga dengan mudah dapat diurai dan dimanfaatkan oleh aplikasi web yang dikembangkan dengan menggunakan JavaScript.

Mudah Diproses: 
--> JSON memiliki format yang dapat dengan mudah diolah oleh berbagai bahasa pemrograman, sehingga dapat digunakan secara efektif dalam berbagai teknologi dan platform.

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. Pertama saya membuat file dengan nama forms.py, lalu file tersebut diisi dengan variabel sesuai dengan model yang didefinisikan di file models.py
2. Kedua saya memodifikasi beberapa pada file view.py, dengan cara membuat fungsi baru "create_product" tujuannya untuk membuat produk sesuai input user. setelah itu, saya mengubah bagian fungsi show_main yang ada di file views.py agar produk yang diinput bisa disimpan.
3. Ketiga saya membuat file create_product.html. Lalu, membuat file create_product.html untuk tampilan pada input produk. Didalam file ini ada tombol add new product yang mengarahkan user ke page input produk. Setelah diinput, user akan kembali ke main page untuk melihat input produk.
4. Terakhir adalah routing, dalam langkah ini saya melakukan routing pada semua fungsi. Dalam langkah ini saya menambahkan beberapa import yang diperlukan pada file views.py, lalu saya tambahkan juga beberapa path baru untuk manggil fungsi melalui URL. Dibawah ini adalah isi dari urls.py saya:
<img src="/Foto//urls.png">

### 5. Screenshot hasil akses URL pada Postman.
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
---
---

## README Tugas 4
### 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
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

### 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi merupakan proses verifikasi identitas pengguna yang mencoba akses ke suatu aplikasi dengan username dan password. Autentikasi digunakan untuk memastikan bahwa user yang mengakses aplikasi merupakan user yang sah dan memiliki izin untuk masuk ke suatu aplikasi. Django menyediakan sistem autentikasi yang kuat yang mencakup model pengguna (User model) yang dapat digunakan untuk mengelola data pengguna seperti nama pengguna dan kata sandi, serta berbagai alat untuk mengatur autentikasi, termasuk form bawaan seperti UserCreationForm dan AuthenticationForm.

Otorisasi merupakan proses yang terjadi setelah autentikasi berhasil. Hal ini menentukan apa yang diizinkan pengguna lakukan dalam aplikasi, seperti mengakses halaman tertentu, menggunakan fitur khusus, atau mengubah data. Otorisasi digunakan untuk memastikan user hanya memiliki akses ke bagian-bagian dari aplikasi sesuai peran mereka. Ini membatasi aksi apa yang dapat mereka lakukan dalam aplikasi tersebut.
Django menyediakan mekanisme otorisasi melalui sistem izin (permissions) dan grup pengguna (user groups). Anda dapat mengatur izin untuk model dan tindakan tertentu, dan kemudian menetapkan izin-izin ini kepada pengguna atau grup pengguna. Django juga memiliki dekorator seperti @login_required yang memungkinkan Anda mengontrol akses pengguna ke tampilan tertentu.

Pentingnya autentikasi dan otorisasi dalam aplikasi web adalah sebagai berikut:
1. Keamanan, autentikasi memastikan bahwa user yang memiliki izin dapat mengakses aplikasi dan otorisasi memastikan bahwa user dapat melakukan aksi sesuai dengan peran user yang dapat melindungi data dan fungsi sensitif.
2. Menggunakan kedua hal tersebut dapat meningkatkan pengalaman user dengan memastikan bahwa user dapat memiliki akses yang tepat ke fitur" yang sesuai dengan peran mereka dalam suatu aplikasi.

### 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies dalam konteks aplikasi web merupakan potongan" kecil dari data yang disimpan pada sisi klien (web browser) saat user berinteraksi dengan aplikasi web. Cookies digunakan untuk menyimpan informasi yang diperlukan agar dapat mengenali user, melacak sesi, atau menyimpan preferensi pengguna dan cookies berguna untuk mengingat informasi tertentu dari user seperti kunjungan sebelumnya sehingga user tidak perlu memasukkan data yang sama berulang-ulang.

Cara Django mengelola data sesi user:
1. Mengidentifikasi User
2. Penyimpanan Data Sesi
3. Pengiriman Cookie ke Browser
4. Penggunaan Cookie pada Setiap Permintaan
5. Penghapusan Otomatis

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies aman secara default dalam pengembangan web jika diimplementasikan dengan benar, tetapi ada beberapa risiko potensial yang harus diwaspadai seperti,
1. Data yang disadap, cookies biasanya tersimpan pada sisi klien, dan meskipun mereka sering dienkripsi, mereka masih dapat rentan terhadap penyadapan data jika SSL/TLS (HTTPS) tidak diaktifkan. Dalam skenario tanpa HTTPS, data yang disimpan dalam cookies dapat dengan mudah dibaca oleh pihak yang tidak berwenang jika ada serangan man-in-the-middle.
2. Jika aplikasi rentan terhadap serangan XSS, penyerang dapat menyisipkan skrip berbahaya ke dalam halaman web yang akan dieksekusi oleh browser user. Ini dapat memungkinkan penyerang untuk mengambil cookies user, yang dapat digunakan untuk mengakses sesi user atau informasi pribadi.
3. Serangan CSRF (Cross-Site Request Forgery) dapat menyebabkan user yang sudah diautentikasi melakukan tindakan tanpa sepengetahuan mereka. Penyerang dapat memaksa user untuk mengirim permintaan yang tidak disengaja ke aplikasi dengan cookies sesi yang sah, yang dapat menyebabkan aksi yang tidak diinginkan.
4. Jika menyimpan data sensitif seperti informasi login atau informasi pribadi dalam cookies, risiko kebocoran data meningkat. Meskipun data dienkripsi, ada kemungkinan risiko jika cookie dicuri atau disusupi.
5. Jika sesi user tidak memiliki waktu kadaluarsa yang sesuai, cookies sesi dapat tetap aktif terlalu lama, yang dapat membahayakan keamanan jika user lupa untuk logout atau meninggalkan komputer mereka terbuka.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
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
---
---

## README Tugas 5
### 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
- Selector Universal ("*")
Digunakan untuk memilih semua elemen yang ada pada halaman web, dalam menggunakan selector ini harus teliti karena bisa mempengaruhi seluruh halaman. Jadi, selector ini biasa digunakan untuk reset atau mengatur nilai default.
- Selector ID
Digunakan untuk memilih elemen dengan atribut id yang unik dan dapat mengatur style pada elemen tertentu. 
- Selector Class <"div class = "profile""> (syntax)
Digunakan untuk memilih elemen dengan atribut class tertentu. Contoh dari syntax diatas adalah untuk membantu menerapkan gaya pada class profile. Selector ini digunakan ketika ingin mengganti tampilan elemen yang tergabung dalam kelas tertentu.
- Element Style
Elemen ini berisi style untuk dokumen atau bagian dari dokumen. Dalam elemen ini biasa dibuat dalam file yang berbeda yaitu file css, dalam menerapkan elemen dalam HTML file css tersebut akan dipanggil seperti dengan menggunakan tag <"link"> di dalam dokumen HTML.

### 2. Jelaskan HTML5 Tag yang kamu ketahui.
<"html">, membuat sebuah dokumen HTML
<"head">, membuat bagian head
<"body">, untuk membuat bagian body
<"h1"> to <"h6">, untuk membuat heading
<"p">, membuat paragraf
<"table">, membuat sebuah tabel
<"tr">, membuat baris dalam sebuah tabel
<"td">, membuat sel dalam sebuah tabel

### 3. Jelaskan perbedaan antara margin dan padding.
a. Margin merupakan sisi luar dari sebuah elemen HTML dan digunakan untuk mengatur jarak antar elemen, seperti elemen dalam kontainer yang sama.
- margin: properti ini digunakan untuk mengatur margin secara keseluruhan (atas, bawah, kiri, kanan) dari suatu elemen.
- margin-top, margin-bottom, margin-left, margin-right: properti-properti ini digunakan untuk mengatur margin secara terpisah untuk sisi-sisi tertentu dari elemen.
b. Padding merupakan sisi dalam dari sebuah elemen HTML dan digunakan untuk mengatur jarak antara konten elemen dan batas elemen.
- padding: properti ini digunakan untuk mengatur padding secara keseluruhan dari suatu elemen.
- padding-top, padding-bottom, padding-left, padding-right: properti-properti ini digunakan untuk mengatur padding secara terpisah untuk sisi-sisi tertentu dari elemen.

### 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Tailwind lebih fleksibel dalam custom style karena tidak memiliki design bawaan, sedangkan bootstrap lebih cepat dan mudah dalam membuat tampilan karena sudah memiliki design bawaan. Dalam ukuran file, tailwind lebih kecil dibanding bootstrap.
Kesimpulannya gunakan tailwind jika lebih suka fleksibilitas dan memiliki pengetahuan yang lebih dalam tentang CSS dan jika lebih suka membuat tampilan dengan cepat dan tidak ingin membuat banyak kustomisasi maka gunakan bootstrap

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Dalam kustomisasi saya memanfaatkan css <"style">, lalu file html nya saya memanggil class seperti:
<"div class="container mt-5">
    <"h1 class="text-center">STOCKMASS</h1>
    <"hr class="mb-4">
    
    <div class="row">
        <div class="col-md-6 offset-md-3">
            <h5>Name:</h5>
            <p>{{ name }}</p>
    
            <h5>Class:</h5>
            <p>{{ class }}</p>
        </div>
    </div>

    <div class="table-responsive">
        <table class="table table-bordered table-striped">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Price</th>
                    <th>Description</th>
                    <th>Date Added</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                {% for product in products %}
                    <tr>
                        <td>{{ product.name }}</td>
                        <td>{{ product.price }}</td>
                        <td>{{ product.description }}</td>
                        <td>{{ product.date_added }}</td>
                        <td>
                            <a href="{% url 'main:edit_product' product.pk %}" class="btn btn-sm btn-primary">Edit</a>
                            <a href="{% url 'main:delete_product' product.pk %}" class="btn btn-sm btn-danger">Delete</a>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>

saya melakukan beberapa modifikasi pada CSS. CSS saya disatuka di file html yang sama, berikut kode saya:
<"style">
    body {
    display: grid;
    place-items: center;
    height: 100vh; /* Mengisi tinggi viewport untuk memastikan elemen berada di tengah vertikal */
    }

    * {
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif; 
    }

    .container {
        width: 350px;
        padding: 20px;
        background-color: #f5f5f5;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); 
        margin: 0 auto;
        text-align: center;
    }

    h1 {
        text-align: center;
        color: #007bff; 
        font-size: 25px;
        margin-bottom: 20px;
    }

    form {
        margin-bottom: 15px;
    }

    table {
        margin: 0 auto;
    }


    input[type="text"],
    input[type="number"] {
        width: 100%;
        padding: 10px;
        margin-bottom: 15px;
        border: 1px solid #ccc;
        border-radius: 10px;
    }


    .btn-edit {
        background-color: #1870d4; 
        color: #fff;
        font-size: 16px;
        padding: 10px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }

    /* Tombol Edit Product hover effect */
    .btn-edit:hover {
        background-color: #1262b8;
    }
<"/style">
---
---

## README Tugas 6
### 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous programming mengharuskan eksekusi berurutan di mana function 1 harus diselesaikan terlebih dahulu sebelum function 2 dan function berikutnya dapat dimulai. Synchronous programming memudahkan penulisan dan pemahaman program, tetapi bisa terasa lambat jika tindakan memerlukan waktu lama atau terjadi kesalahan. Sebaliknya, asynchronous programming mengizinkan penundaan eksekusi, yang berarti function 2 dan seterusnya dapat dimulai tanpa harus menunggu function 1 hingga selesai, sehingga memungkinkan function 2 dan yang lainnya untuk berjalan secara bersamaan dalam waktu yang sama. Asynchronous programming dapat membuat penulisan dan pemahaman program lebih kompleks karena alur eksekusi tidak mengikuti urutan kode.

### 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Paradigma event-driven programming adalah pendekatan pemrograman di mana program merespons peristiwa (event) yang terjadi, seperti interaksi pengguna, input, atau perubahan keadaan sistem, dan menjalankan tindakan atau fungsi yang sesuai dengan peristiwa tersebut. Ini berarti program tidak menjalankan operasi secara berurutan, melainkan menunggu dan merespons peristiwa yang terjadi asinkronus.

Dalam tugas ini yang melibatkan JavaScript dan AJAX, salah satu contoh penerapan paradigma event-driven programming adalah ketika mengambil dan menampilkan data produk pada halaman web. Ketika pengguna mengakses halaman, JavaScript dapat merespons peristiwa seperti klik tombol "Add Product by AJAX" pada produk tertentu. Ketika pengguna melakukan klik pada button tersebut, event-driven programming memungkinkan JavaScript untuk mengirim permintaan AJAX ke server dan menangani hasilnya tanpa harus memuat ulang seluruh halaman.

### 3. Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada ajax merujuk pada pendekatan di mana permintaan data ke server atau operasi lainnya dapat dilakukan secara asinkron, tanpa harus menghentikan eksekusi kode JavaScript.Hal ini menghasilkan responsifitas yang lebih baik dalam halaman web, memungkinkan pengguna untuk tetap berinteraksi dengan halaman tanpa harus menunggu permintaan data selesai. Callback functions sering digunakan dalam asynchronous programming untuk menangani respons dari server atau operasi lainnya dengan lebih terstruktur dan responsif, serta memungkinkan perubahan tampilan halaman secara dinamis sesuai dengan data yang tiba, meningkatkan pengalaman pengguna secara keseluruhan.

### 4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
a. Kompatibilitas Peramban:
    - Fetch API cocok untuk peramban modern.
    - jQuery lebih sesuai untuk peramban lama.
b. Pengelolaan Respons Asinkron:
    - Fetch API menggunakan Promise, menghindari masalah "callback hell."
    - jQuery menggunakan callback yang lebih fleksibel.
c. Kemudahan Penggunaan:
    - jQuery menyediakan antarmuka lebih sederhana, terutama untuk tugas seperti pengiriman data JSON.
    - Fetch API memberikan lebih banyak kontrol pada permintaan dan respons.
d. Konversi Respons:
    - Fetch API memiliki metode bawaan untuk mengubah respons menjadi berbagai tipe data.
    - jQuery memerlukan penentuan jenis data di awal dengan opsi dataType.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
a. Membuat fungsi get_item_json pada views.py, digunakan untuk menampilkan data produk pada HTML dalam bentuk JSON. Setelah itu, membuat fungsi "add_product_ajax" menambahkan produk baru ke basis data dengan AJAX dengan cara import csrf_exempt.
b. Pada file main.html, saya akan menggunakan Fetch API untuk mengambil item. Ini dilakukan dengan menambahkan blok kode script di akhir dokumen HTML dan membuat fungsi asinkron bernama getItems.
c. Lalu saya menambahkan fungsi pada blok kode script, yaitu async function refreshProducts() untuk memunculkan cards yang menggunakan AJAX.Fungsi ini akan mengambil data item terbaru, memperbarui informasi yang ada, seperti jumlah item yang tersimpan, dan melakukannya secara asinkron.
d. Pada blok kode script saya menambahkan function untuk menambahkan product.
e. Membuat fungsi "delete_item_ajax" dalam views.py yang akan digunakan untuk menghapus item dengan parameter ID dari item yang akan dihapus dan membuat fungsi "deleteProduct(id)" dalam blok kode script pada file main.html yang digunakan untuk menghapus item menggunakan AJAX.
f. Lalu saya membuat btn pada cards (AJAX) untuk menghapus dan edit item dalam file main.html.
g. Menjalankan perintah collectstatic untuk mengumpulkan atau menggabungkan berkas statis seperti file JavaScript, CSS, gambar, dan lainnya ke dalam satu direktori yang akan digunakan oleh server web.
---
---