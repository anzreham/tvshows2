from django.shortcuts import render, HttpResponse, redirect
from .models import Show
from django.contrib import messages
def createform(request):
    return render(request, "createform.html")

def create(request):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        Show.objects.create(title = request.POST['title'], network =request.POST['network'], relasDate = request.POST['date'], desc  = request.POST['desc'])
        print( request.POST['date'])
        this_obj = Show.objects.last()
        id = this_obj.id
        return redirect('/shows/'+str (id))

def showInfo(request, id):
    # print("add book")
    context = {}
    context["objs"]= Show.objects.get(id = int(id))
    return render(request, "viewtvShow.html", context )

def allshows(request):
    # print("add book")
    context = {}
    context["objs"]= Show.objects.all()
    return render(request, "allshows.html", context )

def edit (request, id):
    context = {}
    context["objs"]= Show.objects.get(id = int(id))
    return render(request, "editform.html", context )

def update (request, id):
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('shows/edit/'+str (id))
    else:
        context = {}
        this_show = Show.objects.get(id = int(id))
        this_show.title =  request.POST['title']
        this_show.network = request.POST['network']
        this_show.relasDate =  request.POST['date']
        this_show.desc =  request.POST['desc']
        this_show.save()
        return redirect('/shows/'+str (id))



def destroy(request, id):
    context = {}
    this_show = Show.objects.get(id = int(id))
    this_show.delete()
    return redirect('/shows')