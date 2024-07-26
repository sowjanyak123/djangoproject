from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog,Event
# Create your views here.

def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        
        # Save the blog post
        Blog.objects.create(title=title, image=image, description=description)
        return redirect('dashboard')  # Redirect to a success page or the blog list

    return render(request, 'addblog.html')

def blog_list(request):
    blogs=Blog.objects.all()
    return render(request,'bloglist.html',{'blogs':blogs})

def edit_blog(request,pk):
    blog=get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.title = request.POST.get('title')
        new_image = request.FILES.get('image')
        if new_image:
            blog.image = new_image
        
        blog.description = request.POST.get('description')
        blog.save()
        return redirect('dashboard')
    
    return render(request, 'editblog.html', {'blog': blog})

def delete_blog(request,pk):
    blog=get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('blog_item')


def create_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        
        Event.objects.create(title=title, description=description,image=image)
        return redirect('dashboard')
    return render(request, 'addevent.html')

def event_list(request):
    events = Event.objects.all()
    return render(request, 'eventlist.html', {'events': events})

def edit_event(request,id):
    event=get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.title = request.POST.get('title')
        new_image = request.FILES.get('image')
        if new_image:
            event.image = new_image
        
        event.description = request.POST.get('description')
        event.save()
        return redirect('dashboard')
    
    return render(request, 'editevent.html', {'event': event})


def delete_event(request,id):
    event=get_object_or_404(Event, id=id)
    event.delete()
    return redirect('dashboard')

def dashboard(request):  
    events =Event.objects.all()
    blogs=Blog.objects.all()
    context={
        'events':events,
        'blogs':blogs
    }
    return render(request, 'dashboard.html', context)


