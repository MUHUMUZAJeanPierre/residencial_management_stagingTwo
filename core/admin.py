from django.contrib import admin
from .models import Resident, Event, Announcement

admin.site.register(Resident)
admin.site.register(Event)
admin.site.register(Announcement)
