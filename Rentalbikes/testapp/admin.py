from django.contrib import admin
from testapp.models import UserRegistration
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','name','mobile_number','age','driving_license_number','vehicle_name','aadhar_card','address','created_at']
admin.site.register(UserRegistration,UserAdmin)
