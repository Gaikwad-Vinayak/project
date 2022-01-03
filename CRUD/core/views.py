from django.shortcuts import render,HttpResponseRedirect
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from .forms import datat
from .models import mode
from django.views.generic import TemplateView
from django.contrib import messages

# Create your views here.

def data(request):
    if request.method=='POST':
        dic=datat(request.POST)
        if dic.is_valid():
            dic.save()
            messages.success(request, 'Profile details updated.')
    else:
        dic=datat()
    return render(request,'core/home.html',{'form':dic})

def show(request):
    data=mode.objects.all()
    return render(request,'core/suc.html',{'data':data})

class update(UpdateView):
    template_name='core/edit.html'
    model=mode
    fields=['name','email','password']
    success_url='/suc/'

class delete(DeleteView):
    model=mode
    success_url='/suc/'