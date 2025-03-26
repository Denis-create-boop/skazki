from django.contrib import admin
from info.models import Persons, Addresses



@admin.register(Persons)
class PersonsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "profession",
    ]
    search_fields = ["name", "profession", "description",]

    fields = [
        "name",
        "profession",
        "description",
        "phone",
        "name_address_1",
        "address_1",
        "name_address_2",
        "address_2",
        "name_address_3",
        "address_3",
    ]


@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    
    list_display = [
        "name",  
    ]
    
    fields = [
        "name",
        "address",
    ]