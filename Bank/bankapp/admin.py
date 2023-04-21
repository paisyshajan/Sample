from django.contrib import admin
from .models import Person,District,Branch
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name','dob','email','gender','district','branch','account','materials']

admin.site.register(Person,PersonAdmin)

# class StateAdmin(admin.ModelAdmin):
#     list_display = ['name']
#
#
# admin.site.register(State,StateAdmin)
# #
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(District,DistrictAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ['name','district']

admin.site.register(Branch,BranchAdmin)
#
# admin.site.register(Person)
# admin.site.register(State)
# admin.site.register(District)
# admin.site.register(Branch)