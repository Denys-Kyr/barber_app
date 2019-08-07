from django.contrib import admin
from . import models

# Register your models here.


#admin.site.register(models.Masters)
admin.site.register(models.City)
admin.site.register(models.BarberShop)
admin.site.register(models.TimeForHaircutMan)
admin.site.register(models.TimeForHaircutWoman)


class MasterAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Masters._meta.fields]
    #list_display = ['barber_shop', 'masters_name']
    list_filter = ['city', 'barber_shop']
    #search_fields = [field.name for field in models.Master._meta.fields]
    search_fields = ['masters_name', 'telephone_number', 'city', 'barber_shop']

    #def save_model(self, request, task, form, change):
    #    models.Masters.user = request.user
    #    models.Masters.save()

    class Meta:
        model = models.Masters


admin.site.register(models.Masters, MasterAdmin)
