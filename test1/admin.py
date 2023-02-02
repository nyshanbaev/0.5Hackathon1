from django.contrib import admin
from .models import *
from test2.models import *
admin.site.register(Post)
admin.site.register(Comment)
