"""EpmloyeeApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from web.views import SignInView,SignUpView,IndexView,UpdateEmployee,employee_delete,sign_out_view

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("login",SignInView.as_view(),name="signin"),
    path("",SignUpView.as_view(),name="signup"),
    path("index",IndexView.as_view(),name="index"),
    path("emp/update/<int:pk>",UpdateEmployee.as_view(),name="update"),
    path("emp/<int:id>/remove",employee_delete,name="employee_delete"),
    path("logout",sign_out_view,name="sign-out"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
