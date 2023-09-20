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


