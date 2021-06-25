from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.contrib import messages

from appvams.forms import SignUpForm
from appvams.models import Vaccine,AppointmentSchedule,Patient, PatientReport, VaccineStock, Vaccination, Staff, CustomUser, AppointmentList


class Appointment(View):
    def get(self, request):
        return render(request, 'vams/appointment.html')

    def post(self,request):
        name=request.POST["name"]
        contact=request.POST["mobile"]
        msg=request.POST["msg"]
        date=request.POST["date"]
        time=request.POST["time"]

        # print(name,contact,msg,date,time)
        data=AppointmentSchedule(name=name,mobile=contact,msg=msg,date=date,time=time)
        data.save()
        messages.success(request, "Your Appointment is successful!")
        return render(request, 'vams/appointment.html')


class PatientReports(View):
    def get(self, request):
        return render(request, 'vams/patient_report.html')

    def post(self,request):
        if request.method=="POST":
            patient_name = request.POST["name"]
            patient_mobile = request.POST["mobile"]
            patient_address=request.POST["address"]
            doctor_name = request.POST["doctor_name"]
            vaccine_name=request.POST["vaccine_name"]
            room_charge_of_days = request.POST["charge"]
            doctor_fee = request.POST["fee"]
            medicine_cost = request.POST["cost"]
            other_charge = request.POST["other"]
            total_bill = request.POST["total_bill"]
            date = request.POST["date"]
            time = request.POST["time"]

            # print(name,contact,msg,date,time)
            data = PatientReport(patient_name=patient_name, patient_mobile=patient_mobile, patient_address=patient_address, doctor_name=doctor_name,
                               vaccine_name=vaccine_name, room_charge_of_days=room_charge_of_days, doctor_fee=doctor_fee, medicine_cost=medicine_cost, other_charge=other_charge, total_bill=total_bill, date=date, time=time)
            data.save()
            return render(request, 'vams/patient_report.html')


class Staffs(View):
    def get(self, request):
        s = CustomUser.objects.all()
        return render(request, 'vams/staff.html', {'staff': s})


class AppointmentLists(View):
    def get(self, request):
        a = AppointmentSchedule.objects.all()
        return render(request, 'vams/list.html', {'list': a})


class Base(View):
    def get(self, request):
        return render(request, 'vams/base.html')


class Index(View):
    def get(self, request):
        return render(request, 'vams/index.html')

    # def post(self,request):
    #     name=request.POST["name"]
    #     email = request.POST["email"]
    #     date = request.POST["date"]
    #     time = request.POST["time"]
    #     msg = request.POST["msg"]
    #     print(name,email,date,time,msg)
    #
    #     return render(request, 'vams/index.html')







class Patients(View):
    def get(self, request):
        p= PatientReport.objects.all()
        return render(request, 'vams/patient.html', {'patient': p})


class About(View):
    def get(self, request):
        return render(request, 'vams/about.html')

class Covid19(View):
    def get(self, request):
        return render(request, 'vams/covid.html')

class Blog(View):
    def get(self, request):
        return render(request, 'vams/blog.html')


class BlogSingle(View):
    def get(self, request):
        return render(request, 'vams/blog-single.html')


class Contact(View):
    def get(self, request):
        return render(request, 'vams/contact.html')


class Doctors(View):
    def get(self, request):
        return render(request, 'vams/doctors.html')


class Services(View):
    def get(self, request):
        return render(request, 'vams/services.html')


class Navbar(View):
    def get(self, request):
        return render(request, 'vams/navbar.html')


def error404(request, exception):
    return render(request, 'vams/404.html')


class Vaccines(View):
    def get(self, request):
        v = Vaccine.objects.all()
        return render(request, 'vams/vaccine.html', {'vaccine': v})


class Vaccinations(View):
    def get(self, request):
        vc = Vaccination.objects.all()
        return render(request, 'vams/vaccination.html', {'vaccination': vc})


class VaccineStocks(View):
    def get(self, request):
        stock = VaccineStock.objects.all()
        return render(request, 'vams/stock.html', {'stock': stock})


import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return


def report(request, pk):
    p = PatientReport.objects.get(pk=pk)

    dict = {
        'date': p.date,
        'time': p.time,
        'patient_name': p.patient_name,
        'patient_mobile': p.patient_mobile,
        'patient_address': p.patient_address,
        'doctor_name': p.doctor_name,
        'vaccine_name': p.vaccine_name,
        'room_charge_of_days': p.room_charge_of_days,
        'doctor_fee': p.doctor_fee,
        'medicine_cost': p.medicine_cost,
        'other_charge': p.other_charge,
        'total_bill': p.total_bill,
    }
    return render_to_pdf('vams/report.html', dict)


class Signup(View):
    def get(self, request):
        return render(request, 'vams/signup.html')

    def post(self, request):
        form = SignUpForm(request.POST, request.FILES)

        customer_group, created = Group.objects.get_or_create(name='Customer')

        # print(SignUpForm)
        # print(form.fields)
        # print(form.errors.as_json())
        print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            customer_group.user_set.add(user)
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('vams/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]

            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
        else:
            # form = SignUpForm()
            return render(request, 'vams/signup.html', {'form': form})


# def activate(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = get_user_model()._default_manager.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and default_token_generator.check_token(user, token):
#         user.active = True
#         user.save()
#         return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
#     else:
#         return HttpResponse('Activation link is invalid!')


class ActivateURL(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_user_model()._default_manager.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        else:
            return HttpResponse('Activation link is invalid!')


