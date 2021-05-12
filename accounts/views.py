from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def logout(request):
    auth.logout(request)
    return render(request,'index.html')




def login(request):

  if request.method== 'POST':
     username=request.POST['username']
     password=request.POST['password']

     user=auth.authenticate(username=username,password=password)

     if user is not None:
         auth.login(request,user)
         return render(request,'index.html')

     else:
         message.info(request,'invalid credidentials')
         return render(request,'index.html')

  else:
     return render(request,'login.html')




def register(request):
   if request.method == 'POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        user=request.POST['username1']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return render(request, 'register.html')        
      
            else: 
                user = User.objects.create_user(username=user,password=password1,email=email,first_name=fname,last_name=lname)
                user.save()
                print('user created')
                return render(request, 'login.html')        
        else:  
            messages.info(request,'password does not match')
            return render(request, 'register.html')        
     
        return render(request, 'register.html')        
   else:
        return render(request, 'register.html')