
from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Items
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Items
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

 
#def Inventorydetails(request):
 #   return render(request,'inventory/inventory_details.html')

class Inventorydetails(ListView):
    model = Items
    context_object_name = 'items'
    template_name = 'inventory/inventory_details.html'  # <app>/<model>_<viewtype>.html
  
    ordering = ['-date_posted']

class Itemsdetailsview(DetailView):
    model = Items
class temporary(ListView):
    model = Items
    context_object_name = 'items'
    template_name = 'inventory/itemregister.html'  # <app>/<model>_<viewtype>.html


class PostCreateView( CreateView):
    

    model = Items
    fields = ['name','productdetails', 'description','numberofitems']

    

class itemupdateview(UpdateView):
    model = Items
    fields =  ['productdetails', 'description','numberofitems']

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


class ItemDeleteView( DeleteView):
    model = Items
    success_url = '/inventory'


