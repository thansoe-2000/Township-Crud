from django.contrib import admin
from . models import *
# Register your models here.


class VillageAdmin(admin.ModelAdmin):
    list_display = ('name','houses', 'schools', 'monestaries','populations', )
admin.site.register(Township)
admin.site.register(Town)
admin.site.register(Ward)
admin.site.register(Village, VillageAdmin)
