from fileinput import filename
from django.shortcuts import render, HttpResponse

# from myapp.models import User

from django.http import request
# from django.shortcuts import render,redirect
from.models import *



# Create your views here.
def IndexView(request):
    all_data=resumefile.objects.all()
    print(all_data)
    return render(request,"index.html",{'key1': all_data})

def insertData(request):
    name = request.POST['name']
    email = request.POST['email']
    Contact = request.POST['contact']
    message = request.POST['message']


    #creating object of model class
    #inserting data into table
    newuser= User.objects.create(Username=name,Email=email,Messages=message, Contact=Contact)
    return render(request,"index.html")


# def formview(request):
# #     fname = request.POST['filename']
# #     filee=request.Files['file']

# #     #creating object of model class
# #     #inserting data into table
# #     newuser= resumefile.objects.create(file_name=fname,file=filee)
#     return render(request,"form.html")

   



#     #after insert render show.html
# def ShowData(request):
    # resume= request.FILES['resume']
    # all_data=UploadFile.objects.all()
    # return render(request,"in.html",{'key1': all_data})

#     # return render(request,"index.html")
    # all_data=students.objects.all()
    # return render(request,"app/show.html",{'key1': all_data})

# def showfile(request):
#     # context={'file':UploadFile.objects.all()}
#     # return render(request, 'in.html', context)
#     all_data=resumefile.objects.all()
#     print('hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii',all_data)
#     return render(request,"in.html",{'key1': all_data})
