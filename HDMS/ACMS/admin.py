from django.contrib import admin
from .models import hmo_list, drug, patient, state
# Register your models here.

class HmoList(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email', 'address', 'hmo_status', 'added_by')

class Patient(admin.ModelAdmin):
    list_display = ('surname', 'firstname', 'card_no', 'phone_number','gender', 'hmo_id', 'added_by')

class Drug(admin.ModelAdmin):
    list_display = ('drug_name', 'drug_code', 'date_added', 'added_by')

class State(admin.ModelAdmin):
    list_display = ('state_name',)

admin.site.register(hmo_list, HmoList)
admin.site.register(patient, Patient)
admin.site.register(drug, Drug)
admin.site.register(state, State)
