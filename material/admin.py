from django.contrib import admin

from .models import *


admin.site.register(Branch)
admin.site.register(Course)
admin.site.register(Subject)

admin.site.register(Teacher)
admin.site.register(Linke)

admin.site.register(Student)
admin.site.register(Questions_Bank)
