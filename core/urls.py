# core/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    # decors
    path('', include('apps.decors.urls', namespace='decors')),

    # projects
    path('', include('apps.projects.urls', namespace='projects')),

    # CKEditor
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:

    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns     

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
