from django.contrib import admin
from .models import Randeveryday, EmailSending

# Register your models here.

admin.site.register(Randeveryday)
admin.site.register(EmailSending)

# Site names

admin.site.site_title = "Randings"
admin.site.site_header = "Randings Administration"
admin.site.index_title = "Randings Administration"
