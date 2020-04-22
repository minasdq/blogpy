from django.contrib import admin
from .models import UserProfile,article,category

admin.site.register(article)
admin.site.register(category)
admin.site.register(UserProfile)