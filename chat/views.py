from django.shortcuts import render, redirect, get_object_or_404, reverse
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from .forms import UserRegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    if request.method == "POST":
        # get form data
        room = request.POST.get('room_name')
        username = request.POST.get('username')
        
        # get data if it exists or create a new object
        room, _ = Room.objects.get_or_create(name=room)
        
        # redirect to chat room
        return redirect(reverse("room", args=[room.name]) + f"?username={username}")
        
    return render(request, 'home.html')


def room(request, room):
    username = request.GET.get('username')
    room_details = get_object_or_404(Room, name=room)
    return render(request, 'room.html', {
        'username': username,
        'room_details': room_details
    })


def send(request):
    message = request.POST.get('message')
    username = request.POST.get('username')
    room_id = request.POST.get('room_id')
    
    # create message object instance
    Message.objects.create(
        value=message,
        user=username,
        room=room_id
    )
    
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = list(Message.objects.filter(room=room_details.id).order_by("date").values())
    
    for message in messages:
        message["date"] = message["date"].strftime("%d-%m-%Y %H:%M:%S")
    
    return JsonResponse({"messages": messages})


def mainPage(request):
    return render(request, 'main.html')


def registerPage(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            # alert success
            messages.success(request, "Registration Sucessful.")
            return redirect("home")
        
        # alert error 
        messages.error(request, "Unsuccessful Registration. Invalid Credentials Provided, Try Again later..")
        return redirect("registerPage")
        
    form = UserRegistrationForm()
    context = {'form' : form}
    return render(request, "registerPage.html", context)


def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # get form data
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"User Succesfully logged in, You are now logged in as {username}.")
                return redirect("home")
                
            messages.error(request,"Invalid username or password.")
            return redirect("loginPage")
        messages.error(request,"Invalid username or password.")
        return redirect("loginPage")

    form = AuthenticationForm()
    context = {'form' : form}
    return render(request, "loginPage.html", context)


def logoutPage(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("home")
    

def profilePage(request):
    context = {}
    return render(request, "profilePage.html", context)

