from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from doneapp.forms import BookForm
from doneapp.models import Booking, City


def demo(request):
    return render(request,"index.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('donate')
        else:
            messages.info(request,"Invalid User")
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                 messages.info(request,"Email Already Taken")
                 return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,email=email)

                user.save();
                messages.info(request,"Registration success")
        else:
            messages.info(request,"password not marching")
            return redirect('register')
        return redirect('donate')
    return render(request,'register.html')

def donate(request):

    return render(request,'donate.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def fillform(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! Your Booking is Placed.')
            # return render(request, 'form.html', {'form': BookForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = BookForm()
    return render(request, 'form.html', {'form': form})

class PersonCreateView(CreateView):
    model = Booking
    form_class = BookForm
    success_url = reverse_lazy('person_changelist')

class PersonUpdateView(UpdateView):
    model = Booking
    form_class = BookForm
    success_url = reverse_lazy('person_changelist')

class BookView(CreateView):
    form = BookForm()

def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'drop.html', {'cities': cities})