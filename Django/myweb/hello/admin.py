from django.contrib import admin
from .models import Flight, Topic, companies, category, Questions

# Register your models here.

admin.site.register(Flight)
admin.site.register(Topic)
admin.site.register(companies)
admin.site.register(Questions)
admin.site.register(category)
