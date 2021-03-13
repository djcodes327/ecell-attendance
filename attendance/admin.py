from django.contrib import admin
from attendance import models


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    # Setting how will admin site displays products data
    list_display = ('fname', 'lname', 'email', 'gr_no', 'enrollment_no', 'branch', )
    list_display_links = ('email',)
    list_per_page = 50
    search_fields = ['fname', 'lname', 'email', 'gr_no', 'enrollment_no', 'branch', ]

    # Setting up slug name genertaed from product name


admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Machines)
