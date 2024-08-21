from django.contrib import admin
from contactenquiry.models import contactEnquiry
# Register your models here.
class saveEnquiryAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','websitename','message')
admin.site.register(contactEnquiry,saveEnquiryAdmin)