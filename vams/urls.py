"""vams URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from appvams import views
import debug_toolbar

handler404 = 'appvams.views.error404'

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path('staff/', views.Staffs.as_view(), name="staff"),
    path('base/', views.Base.as_view(), name="base"),
    path('patient/', views.Patients.as_view(), name="patient"),
    path('about/', views.About.as_view(), name="about"),
    path('blog/', views.Blog.as_view(), name="blog"),
    path('blog-single/', views.BlogSingle.as_view(), name="blog-single"),
    path('contact/', views.Contact.as_view(), name="contact"),
    path('doctors/', views.Doctors.as_view(), name="doctors"),
    path('navbar/', views.Navbar.as_view(), name="navbar"),
    path('vaccination/', views.Vaccinations.as_view(), name="vaccination"),
    path('signup/', views.Signup.as_view(), name="signup"),
    path('activate/<uidb64>/<token>', views.ActivateURL.as_view(), name="activate"),
    path('vaccine/', views.Vaccines.as_view(), name="vaccine"),
    # path('services/', views.Services.as_view(), name="services"),
    path('patient_report/<int:pk>', views.report, name="report"),
    path('patient_report/', views.PatientReports.as_view(), name="patient_report"),
    path('stock/', views.VaccineStocks.as_view(), name="stock"),
    path('login/', auth_views.LoginView.as_view(template_name='vams/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="vams/password_reset.html"), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="vams/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="vams/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="vams/password_reset_done.html"), name ='password_reset_complete'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('appointment/',views.Appointment.as_view(),name="appointment"),
    path('list/',views.AppointmentLists.as_view(),name="list"),
    path('covid/', views.Covid19.as_view(), name="covid")

]
