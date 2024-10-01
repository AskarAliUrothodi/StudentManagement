from django.contrib import admin
from poll.models import Person
from poll.models import Students
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display=('id','name','eid','dob','address','email','mob')

admin.site.register(Person,PersonAdmin)


class StudentsAdmin(admin.ModelAdmin):
    list_display=('student_name','admission_no','dob','address','phone')

admin.site.register(Students,StudentsAdmin)



