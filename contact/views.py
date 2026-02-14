from django.shortcuts import render,redirect
from .models import Contact
from django.http import HttpResponse

def contact(request): 
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        review=request.POST.get('review')
        contact.name=name
        contact.email=email
        contact.review=review
        contact.save()
        return render(request,'contact.html')
    
    service=Contact.objects.all()
    data={
        'service':service
    }
    return render(request,'contact.html',data)




def delete(request,id):
    dele=Contact.objects.get(id=id)
    dele.delete()
    return redirect('/contact')

    
    

