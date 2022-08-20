from django.shortcuts import render, redirect
from django.http import HttpResponse
from weddings.models import Wedding
from .forms import WeddingForm
from django.contrib.auth.decorators import login_required

def deleteWedding(request,pk):
    wedding = Wedding.objects.get(id=pk)
    context = {'object': wedding}
    if request.method == 'POST':
        wedding.delete()
        return redirect('weddings')
      
    return render(request, "weddings/delete_template.html", context)

@login_required(login_url="login")
def updateWedding(request,pk):
    wedding = Wedding.objects.get(id=pk)
    form = WeddingForm(instance=wedding)
    if request.method == 'POST':
        form = WeddingForm(request.Post, instance=wedding)
        if form.is_valid:
            form.save()
            return redirect('weddings')


    context = {'form': form}
    return render(request, "weddings/wedding_form.html", context)

# Create your views here.
@login_required(login_url="login")
def createWedding(request):
    form = WeddingForm()
    if request.method == 'POST':
      form = WeddingForm(request.POST, request.FILES)

      if form.is_valid:

        form.save()

        return redirect('weddings')

      context = {'form': form}

    return render(request, "weddings/wedding_form.html", context)

def weddings(request):
    weddings=Wedding.objects.all()
    page = 'weddings'
    number = 20
    context = {
        'weddings':weddings,
    }
    return render(request, 'weddings/weddings.html', context)

def wedding(request,pk):
    wedding = wedding.objects.get(id=pk)
    reviews = wedding.review_set.all()
    return render(request, 'weddings/single-wedding.html',{'wedding':wedding, 'reviews':reviews})
