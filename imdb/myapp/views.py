from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Authors
from .models import Customers
from .models import Publishers
from .models import Titles
from .models import Titleauthors
from .models import Subjects
from .forms import AuthorsForm
from .forms import CustomersForm
from .forms import PublishersForm
from .forms import TitlesForm
from .forms import TitleauthorsForm
from .forms import SubjectsForm
from django.contrib import messages

# Create your views here.

def index(request):
    authors=Authors.objects
    customers=Customers.objects
    publishers=Publishers.objects
    titles=Titles.objects
    titleauthors=Titleauthors.objects
    subjects=Subjects.objects 
    return render(request, 'index.html', {'authors':authors,'customers':customers,'publishers':publishers,'titles':titles,'titleauthors':titleauthors,'subjects':subjects})

def auadd(request):
    if request.method=="POST":
        author = Authors()
        author.auid = request.POST.get('auid')
        if(Authors.objects.filter(auid = author.auid).exists()):
                messages.success(request, "ID already exixsts.")
                return redirect('/')
        author.aname = request.POST.get('aname')
        author.email = request.POST.get('email')
        author.phone = request.POST.get('phone')
 
        author.save()
        messages.success(request, "Author is added successfully")
        return redirect('/')
    
    return render(request, 'addauth.html')

def auedit(request, pk):

    author = Authors.objects.get(auid=pk)
    oldauthor = Authors.objects.filter(auid=pk)

    
    if request.method == "POST":
            
            author.auid = request.POST.get('auid')
            if(Authors.objects.filter(auid = author.auid).exists()):
                messages.success(request, "ID already exixsts.")
                return redirect('/')

            author.aname = request.POST.get('aname')
            author.email = request.POST.get('email')
            author.phone = request.POST.get('phone')
            oldauthor.delete()
            author.save()

            messages.success(request, "Author is edited successfully")
            return redirect('/')
 
    return render(request, 'editauth.html',{'author':author})
    


def authdel(request, pk):
    author = Authors.objects.filter(auid=pk)
    author.delete()

    return redirect('/')


def cusadd(request):
    if request.method=="POST":
        customer = Customers()
        customer.custid = request.POST.get('custid')
        if(Customers.objects.filter(custid = customer.custid).exists()):
                messages.success(request, "ID already exixsts.")
                return redirect('/')
        customer.custname = request.POST.get('custname')
        customer.zip = request.POST.get('zip')
        customer.city = request.POST.get('city')
        customer.state = request.POST.get('state')
 
        customer.save()
        messages.success(request, "Customer is added successfully")

        return redirect('/')
    
    return render(request, 'addcus.html')

def cusedit(request, pk):
    customer = Customers.objects.get(custid=pk)
    oldcustomer = Customers.objects.filter(custid=pk)
    if request.method == "POST":
       
            customer.custid= request.POST.get('custid')
            if(Customers.objects.filter(custid = customer.custid).exists()):
                messages.success(request, "ID already exixsts.")
                return redirect('/')
            customer.custname = request.POST.get('custname')
            customer.zip = request.POST.get('zip')
            customer.city = request.POST.get('city')
            customer.state = request.POST.get('state')
            oldcustomer.delete()
            customer.save()
            messages.success(request, "Customer is edited successfully")
            return redirect('/')
 
    return render(request, 'editcus.html',{'customer':customer})
    


def cusdel(request, pk):
    customer = Customers.objects.filter(custid=pk)
    customer.delete()

    return redirect('/')

def pubadd(request):
    if request.method=="POST":
        publisher = Publishers()
        publisher.pubid = request.POST.get('pubid')
        if(Publishers.objects.filter(pubid = publisher.pubid).exists()):
                messages.success(request, "ID already exixsts.")
                return redirect('/')
        publisher.pname = request.POST.get('pname')
        publisher.email = request.POST.get('email')
        publisher.phone = request.POST.get('phone')
 
        publisher.save()
      
        messages.success(request, "Publisher is added successfully")
        return redirect('/')
    
    return render(request, 'addpub.html')

def pubedit(request, pk):
    publisher = Publishers.objects.get(pubid=pk)
    if request.method == "POST":
            publisher.delete()
            publisher.pubid = request.POST.get('pubid')
            if(Publishers.objects.filter(pubid = publisher.pubid).exists() or Titles.objects.filter(pubid=publisher.pubid).exists()):
                 messages.success(request, "ID already exixsts or You cannot change ID for value refereced in other table")
                 return redirect('/')
            publisher.pname = request.POST.get('pname')
            publisher.email = request.POST.get('email')
            publisher.phone = request.POST.get('phone')
            publisher.save()
            messages.success(request, "Publisher is edited successfully")
            return redirect('/')
 
    return render(request, 'editpub.html',{'publisher':publisher})
    


def pubdel(request, pk):
    publisher = Publishers.objects.filter(pubid=pk)
    publisher.delete()

    return redirect('/')

def subadd(request):
    if request.method=="POST":
        subject = Subjects()
        subject.subid = request.POST.get('subid')
        if(Subjects.objects.filter(subid = subject.subid).exists()):
                messages.success(request, "ID already exixsts.")
                return redirect('/')
        subject.sname = request.POST.get('sname')
        
        subject.save()
        messages.success(request, "Subject is added successfully")

        return redirect('/')
    
    return render(request, 'addsub.html')

def subedit(request, pk):
    subject = Subjects.objects.get(subid=pk)
    oldsubject = Subjects.objects.filter(subid=pk)
    if request.method == "POST":
       
            subject.subid = request.POST.get('subid')
            if(Subjects.objects.filter(subid = subject.subid).exists()):
                messages.success(request, "ID already exixsts.")
                return redirect('/')
            subject.sname = request.POST.get('sname')
            oldsubject.delete()
            subject.save()
            messages.success(request, "Subject is edited successfully")
            return redirect('/')
 
    return render(request, 'editsub.html',{'subject':subject})
    


def subdel(request, pk):
    subject = Subjects.objects.filter(subid=pk)
    subject.delete()

    return redirect('/')

def titleadd(request):
    if request.method=="POST":
        title = Titles()
        title.titleid = request.POST.get('titleid')
        if(Titles.objects.filter(titleid = title.titleid).exists()):
            messages.success(request, "ID already exists.")
            return redirect('/')
        title.title = request.POST.get('title')
        title.pubid = request.POST.get('pubid')
        title.subid = request.POST.get('subid')
        if(Publishers.objects.filter(pubid=title.pubid).exists() and Subjects.objects.filter(subid=title.subid).exists()):
            title.pubdate = request.POST.get('pubdate')
            title.cover = request.POST.get('cover')
            title.price = request.POST.get('price')
            title.save()
            messages.success(request, "Title is added successfully")
        else:
            messages.success(request, "You need to put existing value for Foreign Keys")
            return redirect('/')

        return redirect('/') 
    return render(request, 'addtitle.html')

def titleedit(request, pk):
    title = Titles.objects.get(titleid=pk)
    if request.method == "POST":
      
            title.title = request.POST.get('title')
            title.pubid = request.POST.get('pubid')
            title.subid = request.POST.get('subid')
            if(Publishers.objects.filter(pubid=title.pubid).exists() and Subjects.objects.filter(subid=title.subid).exists()):
                title.pubdate = request.POST.get('pubdate')
                title.cover = request.POST.get('cover')
                title.price = request.POST.get('price')
                title.save()
                messages.success(request, "Title is edited successfully")
            else:
                messages.success(request, "You need to put existing value for Foreign Keys")
                return redirect('/')
            
          
            return redirect('/')
 
    return render(request, 'edittitle.html',{'title':title})
    


def titledel(request, pk):
    title = Titles.objects.filter(titleid=pk)
    title.delete()

    return redirect('/')

def titleauthoradd(request):
    if request.method=="POST":
        titleauthor = Titleauthors()
        titleauthor.titleid = request.POST.get('titleid')
        titleauthor.auid = request.POST.get('auid')
        titleauthor.importance = request.POST.get('importance')
        titleauthor.save()
        messages.success(request, "Titleauthor is added successfully")

        return redirect('/')
    
    return render(request, 'addtitleauthor.html')

def titleauthoredit(request, pk):
    titleauthor = Titleauthors.objects.get(auid=pk)
    if request.method == "POST":
       
            titleauthor.importance=request.POST.get('importance')
            titleauthor.save()
            messages.success(request, "Titleauthor is edited successfully")
            return redirect('/')
 
    return render(request, 'edittitleauthor.html',{'titleauthor':titleauthor})
    


def titleauthordel(request, pk):
    titleauthor = Titleauthors.objects.filter(auid=pk)
    titleauthor.delete()

    return redirect('/')

