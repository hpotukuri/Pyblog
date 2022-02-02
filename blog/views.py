from django.shortcuts import render
from . models import Post


def main_page(request):
    return render(request, 'blog\\main_page.html')


def post(request):
    context = {'post': Post.objects.all()}
    return render(request, 'blog\\home.html', context)


def about(request):
    return render(request, 'blog\\about.html')


    
def Test(request):
    pass