from django.shortcuts import render


# Create your views here.
def get_devops_blog(request):
    return render(request, 'blog/devops_blog.html')
