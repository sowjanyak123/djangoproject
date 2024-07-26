# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Event,Blog


# def create_event(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         image = request.FILES.get('image')
        
#         Event.objects.create(title=title, description=description,image=image)
#         return redirect('event_list')
#     return render(request, 'addevent.html')

# def event_list(request):
#     events = Event.objects.all()
#     return render(request, 'eventlist.html', {'events': events})

# def edit_event(request,pk):
#     event=get_object_or_404(Event, pk=pk)
#     if request.method == 'POST':
#         event.title = request.POST.get('title')
#         new_image = request.FILES.get('image')
#         if new_image:
#             event.image = new_image
        
#         event.description = request.POST.get('description')
#         event.save()
#         return redirect('event_list')
    
#     return render(request, 'editblog.html', {'event': event})


# def delete_event(request,pk):
#     event=get_object_or_404(Event, pk=pk)
#     event.delete()
#     return redirect('event_list')

# def dashboard(request):
#     blogs =Blog.objects.all()
#     events =Event.objects.all()
#     context={
#         'blogs':blogs,
#         'events':events
#     }
#     return render(request, 'dashboard.html', {'context': context})


