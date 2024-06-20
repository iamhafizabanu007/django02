from django.contrib import admin
from .models import students

@admin.register(students)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','email']
