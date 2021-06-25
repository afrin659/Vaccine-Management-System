from django.contrib import admin

from .models import Staff, Patient, AppointmentSchedule, Doctor, Vaccine, Vaccination, Payment, VaccineStock, CustomUser, Report, PatientReport
# Register your models here.



# admin.site.register(CustomUser)


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'profile_image')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'patient_mobile', 'patient_address', 'vaccine_name', 'doctor_name', 'room_charge_of_days',
                    'doctor_fee', 'medicine_cost', 'other_charge', 'total_bill', 'date', 'time')

@admin.register(AppointmentSchedule)
class AppointmentScheduleAdmin(admin.ModelAdmin):
    list_display = ('id','name','mobile', 'msg', 'date', 'time')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_name', 'appointment_number', 'time', 'date', 'bill')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'paid_amount', 'due_amount')

@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    list_display = ('vaccine_name', 'price', 'stock_quantity')

@admin.register(Vaccination)
class VaccinationAdmin(admin.ModelAdmin):
    list_display = ('generic_name', 'brand_name', 'dose_schedule', 'tariff_including_vat')

@admin.register(VaccineStock)
class VaccineStockAdmin(admin.ModelAdmin):
    list_display = ('generic_name', 'stock_in', 'stock_out', 'current_stock')


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('Patient_Name', 'Patient_Mobile', 'Patient_Address',
                    'Doctor_Name','Vaccine_Name', 'Room_Charge_of_Days', 'Doctor_Fee', 'Medicine_Cost',
                    'Other_Charge')


@admin.register(PatientReport)
class PatientReportAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'patient_mobile', 'patient_address', 'vaccine_name', 'doctor_name', 'room_charge_of_days',
                    'doctor_fee','medicine_cost','other_charge', 'total_bill', 'date', 'time')

@admin .register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "profile_image")