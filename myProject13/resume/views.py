from django.shortcuts import render,redirect
from .models import Contact
from .models import Project



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def experience(request):
    return render(request, 'experience.html')



def projects(request):
    data = Project.objects.all()
    return render(request, 'projects.html', {'projects': data})

def education(request):
    return render(request, 'education.html')




def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        print("Data Saved Successfully")
        return redirect('/show/') 

    return render(request, 'contact.html')

def show_data(request):
    data = Contact.objects.all()
    return render(request, 'show.html', {'data': data})

def edit_data(request, id):
    data = Contact.objects.get(id=id)

    if request.method == 'POST':
        data.name = request.POST.get('name')
        data.email = request.POST.get('email')
        data.message = request.POST.get('message')
        data.save()

        return redirect('/show/')

    return render(request, 'edit.html', {'data': data})

def delete_data(request, id):
    data = Contact.objects.get(id=id)

    if request.method == "POST":
        data.delete()
        return redirect('/show/')

    return render(request, 'delete.html', {'data': data})