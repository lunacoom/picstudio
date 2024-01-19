
from django.contrib import admin
from django.urls import path
from .views import index_page
from .views import about_page
from .views import blog_page
from .views import gallery_page
from .views import testimonial_page



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index_page, name='home'),
    path("about/", about_page, name='about'),
    path("blog/", blog_page, name='blog'),
    path("gallery/", gallery_page, name='gallery'),
    path("testimonial/", testimonial_page, name='testimonial')
    
]
