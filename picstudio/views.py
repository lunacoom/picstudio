from django.shortcuts import render






def about_page(request):
    return render (request, template_name='about.html')


def blog_page(request):
    return render (request, template_name='blog.html')

def gallery_page(request):
    return render (request, template_name='gallery.html')

def index_page(request):
    return render (request, template_name='index.html')

def testimonial_page(request):
    return render (request, template_name='testimonial.html')
