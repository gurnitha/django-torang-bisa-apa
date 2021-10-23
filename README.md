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


#### 10.2 Daftarkan model pada admin.py

        modified:   README.md
        modified:   apps/profiles/admin.py


### 11. DJANGO ADMIN 
### ---------------------------------------


#### 11.1 Membuat superuser

        Langkah:

        1. Jalankan perintah: python manage.py createsuperuser
        dan ikuti perintah selanjutnya

        modified:   README.md


#### 11.2 Mengupdate model

        modified:   README.md
        new file:   apps/profiles/migrations/0002_auto_20211023_1222.py
        modified:   apps/profiles/models.py


### 12. DJANGO CKEditor
### ---------------------------------------


#### 12.1 Install Django CKEditor

        modified:   README.md
        modified:   apps/profiles/admin.py
        modified:   core/settings.py
        modified:   core/urls.py


### 13. DJANGO DEBUG TOOLBAR
### ---------------------------------------


#### 13.1 Install django-debug-toolbar

        modified:   README.md
        modified:   core/settings.py
        modified:   core/urls.py


### 14. CRUD
### ---------------------------------------


#### 14.1 Create data dan Modifiksi profile_list page

        modified:   README.md
        modified:   apps/profiles/templates/profiles/profile_list.html
        new file:   static/images/profiles/bisma.PNG


#### 14.2 READ data profile di db dan display data pada profile_list page

        modified:   README.md
        modified:   apps/profiles/templates/profiles/profile_list.html
        modified:   apps/profiles/views.py


#### 14.3 READ data skill di db dan display data pada profile_list page

        modified:   README.md
        modified:   apps/profiles/templates/profiles/profile_list.html
        modified:   apps/profiles/views.py


#### 14.4 PROFILE_SINGLE - READ data profil dan display profile_detail page

        modified:   README.md
        new file:   apps/profiles/migrations/0003_auto_20211023_1531.py
        new file:   apps/profiles/migrations/0004_profile_github.py
        modified:   apps/profiles/models.py
        modified:   apps/profiles/templates/profiles/profile_detail.html
        modified:   apps/profiles/templates/profiles/profile_list.html
        modified:   apps/profiles/urls.py
        modified:   apps/profiles/views.py


#### 14.5 PROFILE_SINGLE - Display data skill yg memiliki deskripsi

        modifie:   README.md
        new file:   apps/profiles/migrations/0005_skill_description.py
        modified:   apps/profiles/models.py
        modified:   apps/profiles/templates/profiles/profile_detail.html
        modified:   apps/profiles/views.py


#### 14.6 PROFILE_SINGLE - Display data skill yg tidak memiliki deskripsi

        modified:   README.md
        modified:   apps/profiles/templates/profiles/profile_detail.html
        modified:   apps/profiles/views.py


#### 14.7 DJANGO CKEditor - Add CKEditor to Skill model dan modifikasi README file

        modified:   README.md
        modified:   apps/profiles/admin.py


### 15. MENGUBAH NAMA DJANGO APP
### ---------------------------------------


#### 15.1 Mengubah nama django app dari 'apps/profiles' menjadi 'apps/decors'

        modified:   README.md
        renamed:    apps/profiles/__init__.py -> apps/decors/__init__.py
        renamed:    apps/profiles/admin.py -> apps/decors/admin.py
        renamed:    apps/profiles/apps.py -> apps/decors/apps.py
        renamed:    apps/profiles/migrations/__init__.py -> apps/decors/migrations/__init__.py
        renamed:    apps/profiles/models.py -> apps/decors/models.py
        renamed:    apps/profiles/templates/profiles/profile_detail.html -> apps/decors/templates/profiles/profile_detail.html
        renamed:    apps/profiles/templates/profiles/profile_list.html -> apps/decors/templates/profiles/profile_list.html
        renamed:    apps/profiles/tests.py -> apps/decors/tests.py
        renamed:    apps/profiles/urls.py -> apps/decors/urls.py
        renamed:    apps/profiles/views.py -> apps/decors/views.py
        deleted:    apps/profiles/migrations/0001_initial.py
        deleted:    apps/profiles/migrations/0002_auto_20211023_1222.py
        deleted:    apps/profiles/migrations/0003_auto_20211023_1531.py
        deleted:    apps/profiles/migrations/0004_profile_github.py
        deleted:    apps/profiles/migrations/0005_skill_description.py
        modified:   core/settings.py
        modified:   core/urls.py


### 16. MEMBUAT DJANGO APP
### ---------------------------------------


#### 16.1 Membuat app dengan nama 'apps/projects'

        Langkah:

        1. Membuat folder baru 'apps/projects'
        2. Membuat app baru 'apps/projects'
        3. Mengubah nama configurasi app:
           1. Buka file projects/apps.py
           2. Ubah nama
              dari -> name = 'projects'
              menjadi -> name = 'apps.projects'
        4. Meregistrasi app projects pada core/settings.py
        5. Menjalan server untuk menguji

        modified:   README.md
        new file:   apps/projects/__init__.py
        new file:   apps/projects/admin.py
        new file:   apps/projects/apps.py
        new file:   apps/projects/migrations/__init__.py
        new file:   apps/projects/models.py
        new file:   apps/projects/tests.py
        new file:   apps/projects/views.py
        modified:   core/settings.py


#### 16.2 House keeping - modifikasi links pada decors app, migrasi

        modified:   README.md
        new file:   apps/decors/migrations/0001_initial.py
        renamed:    apps/decors/templates/profiles/profile_detail.html -> apps/decors/templates/decors/profile_detail.html
        renamed:    apps/decors/templates/profiles/profile_list.html -> apps/decors/templates/decors/profile_list.html
        modified:   templates/shared/header.html


### 17. MEMBUAT HALAMAN PROJECTS
### ---------------------------------------


#### 17.1 Membuat halaman project_list dan project_detail

        modified:   README.md
        new file:   apps/projects/templates/projects/project_detail.html
        new file:   apps/projects/templates/projects/project_list.html


#### 17.2 Membuat view method untuk project_list dan project_detail

        modified:   README.md
        modified:   apps/projects/views.py


#### 17.3 Membuat urls untuk project_list dan project_detail

        modified:   README.md
        modified:   apps/projects/templates/projects/project_list.html
        new file:   apps/projects/urls.py
        modified:   core/urls.py
        modified:   templates/shared/header.html


#### 17.4 Menambahkan template untuk project_list dan project_detail

        modified:   README.md
        modified:   apps/projects/templates/projects/project_detail.html
        modified:   apps/projects/templates/projects/project_list.html


### 18. MEMBUAT MODELS
### ---------------------------------------


#### 18.1 Membuat model Project, Review dan Tag

        modified:   README.md
        modified:   apps/projects/models.py
        new file:   static/images/projects/default.jpg


#### 18.2 Menjalankan migrasi untuk membuat tabel

        modified:   README.md
        new file:   apps/projects/migrations/0001_initial.py


#### 18.3 Mencatatkan model pada admin.py

        modified:   README.md
        modified:   apps/projects/admin.py


### 19. ADMIN DASHBOARD
### ---------------------------------------


#### 19.1 Menambahkan CKEditor pada Project dan Review model

        modified:   README.md
        modified:   apps/projects/admin.py


#### 19.2 Adding data to test CKEditor and render the data

        modified:   README.md
        modified:   apps/decors/admin.py
        modified:   apps/decors/templates/decors/profile_detail.html
        modified:   apps/projects/admin.py
        new file:   static/images/profiles/bisma_G2ZxTo2.PNG
        new file:   static/images/projects/Devsearch_Profile.jpg


### 20. LOADING DATA TO PROJECT PAGES
### ---------------------------------------


#### 20.1 Retrieve dan load data projects pada project_list

        modified:   README.md
        modified:   apps/projects/templates/projects/project_list.html
        modified:   apps/projects/views.py
        new file:   static/images/profiles/drona.PNG


#### 20.2 Retrieve dan load data tags pada project_list

        modified:   README.md
        modified:   apps/projects/templates/projects/project_list.html
        modified:   apps/projects/views.py




































































































































































































































































