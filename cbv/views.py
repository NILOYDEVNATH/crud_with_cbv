from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView,CreateView,UpdateView,DeleteView,View
from cbv.models import CategoryModel
from django.contrib import messages
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render,get_object_or_404
from cbv.forms import Categoryform
# Create your views here.

class Hometemplateview(SuccessMessageMixin,TemplateView):
    template_name="admin_panel/home.html"

class Categoryview(CreateView):
    model=CategoryModel
    form_class=Categoryform
    success_url="category"
    success_message="Created successfully"
    template_name="admin_panel/category.html"

    def get_context_data(self,**kwargs):
        context=super(Categoryview,self).get_context_data(**kwargs)
        context['category_list']=CategoryModel.objects.all()
        return context

class CategoryUpdate(SuccessMessageMixin,UpdateView):
    model=CategoryModel
    form_class=Categoryform
    success_url="/category"
    success_message="Updated successfully"
    template_name="admin_panel/category_edit.html"

class categoryDelete(SuccessMessageMixin,DeleteView):
    model=CategoryModel
    success_url="/category"
    success_message="Deleted successfully"
    

    def delete(self,request,*args,**kwargs):
        messages.success(self.request,self.success_message)
        return super().delete(request,*args,**kwargs)

class Category_status(SuccessMessageMixin,View):
    def get(self,request,pk):
        category_data=get_object_or_404(CategoryModel,pk=pk)
        if category_data.status == 'Active':
            category_data.status = 'Inactive'
            messages.success(request,'Category status Changed into Inactive')
        else:
            category_data.status = 'Active'
            messages.success(request,'Category status Changed into Active')
        category_data.save()
        return HttpResponseRedirect(reverse('category'))

