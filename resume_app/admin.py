from django.contrib import admin
from .models import rlogin
from .models import basic_info
from .models import personal

admin.site.register(rlogin)
admin.site.register(basic_info)
admin.site.register(personal)

