from django.contrib import admin
from .models import staff, Patient, Appointment, Medicine, Slot, Medical, Report

admin.site.register(staff)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Slot)
admin.site.register(Medicine)
admin.site.register(Medical)
admin.site.register(Report)
