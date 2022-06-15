from django.contrib import admin
from django.utils.html import format_html

from .models import *


admin.site.register(Branch)
#admin.site.register(Course)
#admin.site.register(Subject)

#admin.site.register(Teacher)
admin.site.register(Linke)

#admin.site.register(Student)
#admin.site.register(Questions_Bank)
admin.site.register(Academic_Program_Description_Forms)


@admin.register(Subject)
class SubjectAppointmentadmin(admin.ModelAdmin):
    list_display = ("name","units","lecture","plan","teacher",)
    search_fields = ["name","units","teacher__full_name"]
    #list_filter = ("status",)
    
    
@admin.register(Questions_Bank)
class Questions_Bankadmin(admin.ModelAdmin):
    list_display = ("name","level","branch","year","subject","term","solution",)
    search_fields = ["name","level","branch__name","term"]
    #list_filter = ("name","level","branch__name","term","year")

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def picture(self, obj):
        return format_html('<img style="width:50px; height:50px; border-radius: 50%;" src="{}" />'.format(obj.image.url))

    picture.short_description = 'picture'

    list_display = ("full_name","mobile","gender","age","branch","level","joindate")

    search_fields =["full_name","mobile","gender","age","level","joindate","branch__name","joindate"]
    
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    def picture(self, obj):
        return format_html('<img style="width:50px; height:50px; border-radius: 50%;" src="{}" />'.format(obj.image.url))

    picture.short_description = 'picture'

    list_display = ("full_name","mobile","gmail","gender","age","branch","education","degree","joindate","picture")

    search_fields =["full_name","mobile","gender","age","joindate"]
    
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = ("course","branch","level")

    search_fields =["course","branch__name","level"]