from django.shortcuts import render, redirect, get_object_or_404
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = get_object_or_404(Room, name=room)
    return render(request, 'room.html', {
        'username': username,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})


def mainPage(request):
    return render(request, 'main.html')



def registerPage(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Sucessfull.")
            return redirect("/")
        messages.error(request, "Unsuccessfull Registration. Invalid Credentials Provided, Try Again later..")
    form = UserRegistrationForm()
    context = {'form' : form}
    return render(request, "registerPage.html", context)



def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"User Succesfully logged in, You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")

    form = AuthenticationForm()
    context = {'form' : form}
    return render(request, "loginPage.html", context)


def logoutPage(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("/")

def profilePage(request):
    context = {}
    return render(request, "profilePage.html", context)