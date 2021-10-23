# django-torang-bisa-apa
Aplikasi untuk orang Indonesia yang kreatif.


### 1. INISIAL KOMIT
### ---------------------------------------


#### 1.1 Membuat remote repositori di Github

        modified:   README.md


### 2. DJANGO PROYEK
### ---------------------------------------


#### 2.1 Membuat django proyek dengan nama 'core'

        modified:   README.md
        new file:   core/__init__.py
        new file:   core/asgi.py
        new file:   core/settings.py
        new file:   core/urls.py
        new file:   core/wsgi.py
        new file:   manage.py


### 3. DJANGO APP
### ---------------------------------------


#### 3.1 Membuat folder untuk django app dengan nama 'apps'

        modified:   README.md


#### 3.2 Membuat django app dengan nama 'profiles'

        modified:   README.md
        new file:   apps/profiles/__init__.py
        new file:   apps/profiles/admin.py
        new file:   apps/profiles/apps.py
        new file:   apps/profiles/migrations/__init__.py
        new file:   apps/profiles/models.py
        new file:   apps/profiles/tests.py
        new file:   apps/profiles/views.py


#### 3.3 Install django app 'profiles' pada django proyek 'core'

        modified:   README.md
        modified:   apps/profiles/apps.py
        modified:   core/settings.py


### 4. DATABASE: MYSQL
### ---------------------------------------


#### 4.1 Membuat database dan menghubungkannya dengan aplikasi

        Langkah:

        1. Membuat database menggunakan mysql
        2. Menginstall mysqlclient
        3. Menginstall django-environ
        4. Membuat .env file di dalam 'core'
        5. Mensetup parameter pada .env file
        6. Mengsetup parameter environment pada core/settings.py
        7. Mensetup parameter database pada core/setting.py

        modified:   README.md
        modified:   core/settings.py


### 5. TEMPLATES, STATIC FILES DAN MEDIA FILES
### ---------------------------------------


#### 5.1 Membuat BASE_DIR templates

        modified:   README.md
        modified:   core/settings.py


#### 5.2 Mengonfigurasi berkas statis dan media

        modified:   README.md
        modified:   core/settings.py


#### 5.3 Melayani file statis selama pengembangan

        modified:   README.md
        modified:   core/settings.py
        modified:   core/urls.py


### 6. PAGES
### ---------------------------------------


#### 6.1 Membuat halaman profile_list dan profile_detail

        modified:   README.md
        new file:   apps/profiles/templates/profiles/profile_detail.html
        new file:   apps/profiles/templates/profiles/profile_list.html


#### 6.2 Membuat view untuk profile_list dan profile_detail

        modified:   README.md
        modified:   apps/profiles/views.py


#### 6.3 Membuat route

        modified:   README.md
        new file:   apps/profiles/urls.py


#### 6.4 Meregistrasi route pada route proyek 'core/urls.py'

        modified:   README.md
        modified:   core/urls.py


#### 6.5 Mentautkan halaman profile_list dan profile_detail

        modified:   README.md
        modified:   apps/profiles/templates/profiles/profile_detail.html
        modified:   apps/profiles/templates/profiles/profile_list.html


### 7. THEMES DAN STATIC ASSETS
### ---------------------------------------


#### 7.1 Menambahkan theme pada halaman profile_list dan profile_detail

        modified:   README.md
        modified:   apps/profiles/templates/profiles/profile_detail.html
        modified:   apps/profiles/templates/profiles/profile_list.html


#### 7.2 Menambahkan static assets

        new file:   static/assets/uikit/styles/modules/_tag.css
        new file:   static/assets/uikit/styles/modules/_typography.css
        ...
        new file:   static/assets/uikit/styles/modules/_utilities.css
        new file:   static/assets/uikit/styles/modules/_variables.css


#### 7.3 Mengunggah static files

        modified:   README.md
        modified:   apps/profiles/templates/profiles/profile_detail.html
        modified:   apps/profiles/templates/profiles/profile_list.html


### 8. TEMPLATES INHERITANCE
### ---------------------------------------


#### 8.1 Membuat base (layout) file

        modified:   README.md
        new file:   templates/base.html


#### 8.2 Menggunakan base file pada profile_list

        modified:   README.md
        modified:   apps/profiles/templates/profiles/profile_list.html


#### 8.3 Menggunakan base file pada profile_detail

        modified:   README.md
        modified:   apps/profiles/templates/profiles/profile_detail.html


#### 8.4 Menggunakan include

        modified:   README.md
        modified:   templates/base.html
        new file:   templates/shared/head.html
        new file:   templates/shared/header.html


#### 8.5 Menghubungkan halaman profile_list dan profile_detail dan mengganti logo dan favicon

        modified:   README.md
        modified:   apps/profiles/templates/profiles/profile_list.html
        new file:   static/assets/images/favicon-tbs.jpg
        new file:   static/assets/images/favicon-tbs.png
        new file:   static/assets/images/favicon-tbs1.png
        new file:   static/assets/images/favicon-tbs3.jpg
        new file:   static/assets/images/tbs.png
        new file:   static/assets/images/tbs2.png
        new file:   static/assets/images/tbs3.png
        new file:   static/assets/images/torang-bisa-apa.png
        modified:   templates/shared/head.html
        modified:   templates/shared/header.html


### 9. PAGE TITLE
### ---------------------------------------


#### 9.1 Membuat page title dinamis

        modified:   README.md
        modified:   apps/profiles/templates/profiles/profile_detail.html
        modified:   apps/profiles/templates/profiles/profile_list.html
        modified:   apps/profiles/views.py
        modified:   templates/base.html


### 10. MODEL: PROFILE DAN SKILL
### ---------------------------------------


#### 10.1 Membuat model Profile dan Skill serta jalan migrasi

        Langkah:

        1. Buat model Profile
        2. Buat model Skill
        3. Jalankan perintah: makemigrations
        4. Jalankan perintah: migrate
        
        modified:   README.md
        new file:   apps/profiles/migrations/0001_initial.py
        modified:   apps/profiles/models.py
        new file:   static/assets/images/favicon-tbs-new.jpg
























































































































































































































































































































