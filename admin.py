from django.contrib import admin
from users.models import *
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Course)
admin.site.register(Luser)
