from django.shortcuts import render
# from django.http import HttpResponse

from .forms import SubmitForm
# Create your views here.



def home(request):
    forms = SubmitForm()

    context ={
        'form':forms
    }
    return render(request,'form/home.html', context)


def about(request):
    return render(request,'form/about.html')



# def home(request):
#     return HttpResponse("<h1>home page</h1>")