from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,TemplateView,ListView,UpdateView
from .forms import UserRegistrationForm,LoginForm,EmployeeForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from web.models import Employee


def signin_required(fn):
    def wrapper(request,*args,**kw):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kw)
    return wrapper

decs=[signin_required,never_cache]

class SignUpView(CreateView):
    template_name="register.html"
    form_class=UserRegistrationForm
    success_url=reverse_lazy("signin")

class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")
            else:
                return render (request,self.template_name,{"form":form})

@method_decorator(decs,name="dispatch")
class IndexView(CreateView,ListView):
    template_name="index.html"
    form_class=EmployeeForm
    success_url=reverse_lazy("index")
    model=Employee
    context_object_name="employee"

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    def get_queryset(self):
        return Employee.objects.exclude(user=self.request.user)
    


@method_decorator(decs,name="dispatch")
class UpdateEmployee(UpdateView):
    template_name = 'update.html'
    form_class = EmployeeForm
    model = Employee
    success_url = reverse_lazy('index')

def employee_delete(request,*args,**kw):
    id=kw.get("id")
    Employee.objects.get(id=id).delete()
    return redirect("index")

def sign_out_view(request,*args,**kw):
    logout(request)
    return redirect("signin")
    


