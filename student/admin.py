from django.contrib import admin
from .models import insert_details

# Register your models here.

class InsertAdmin(admin.ModelAdmin):
    list_display = ('id','student_name','student_email','student_age','gender')

admin.site.register(insert_details,InsertAdmin)