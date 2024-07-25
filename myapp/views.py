from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
# Create your views here.

def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        
        # Save the blog post
        Blog.objects.create(title=title, image=image, description=description)
        return redirect('blog_item')  # Redirect to a success page or the blog list

    return render(request, 'addblog.html')

def blog_list(request):
    blogs=Blog.objects.all()
    return render(request,'blogitems.html',{'blogs':blogs})

def edit_blog(request,pk):
    blog=get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.title = request.POST.get('title')
        new_image = request.FILES.get('image')
        if new_image:
            blog.image = new_image
        
        blog.description = request.POST.get('description')
        blog.save()
        return redirect('blog_item')
    
    return render(request, 'editblog.html', {'blog': blog})

def blog_item(request):
    blogs=Blog.objects.all()
    return render(request,'bloglist.html',{'blogs':blogs})

def delete_blog(request,pk):
    blog=get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('blog_item')


