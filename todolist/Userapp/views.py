from ast import Pass
from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserForm
from django.contrib.auth.views import LoginView,LogoutView
from .models import Contact, Task,TodoListItem 
from django.contrib import messages
from datetime import datetime
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView

# Create your views here.
class BaseRegisterView(SuccessMessageMixin, FormView):

    form_class = UserForm
    template_name = 'userportal/registration.html'
    success_url = "/user/userlogin/"
    # success_message = "%(name)s was created successfully"
  
    def form_valid(self, form):
        user = form.save()
        user.set_password(user.password) 
        user.save()    
        return super().form_valid(form)

    def get_success_message(self,cleaned_data):
        username = cleaned_data["username"]
        return username + " - User created successfully..!!"

class UserLoginView(LoginView):
    template_name = 'userportal/login.html'
    success_url = "userportal/home/"

def index(request):
    return render(request, 'userportal/index.html')

def Homepage(request):
    return render(request,'userportal/homepage.html')  

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'userportal/contactus.html')

def signUp(request):
    return render(request,"userportal/signup.html")

def Logout(request):
    return render(request, 'userportal/index.html')

class AddTask(CreateView):
    model = Task
    fields = ['task_name','task_description']
    template_name = 'userportal/add_task.html'
    success_url = '/user/view'

class ViewTask(ListView):
    model = Task
    tasks = model.objects.all()
    context_object_name = 'tasks'
    template_name = 'userportal/view_task.html'

class DetailTask(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'userportal/detail_task.html'

class DeleteTask(DeleteView):
    model = Task
    template_name = "userportal/delete_task.html"
    success_url = "/user/view"

class UpdateTask(UpdateView):
    model = Task
    fields = ['task_name','task_description']
    template_name = "userportal/update_task.html"
    success_url = "/user/view"
