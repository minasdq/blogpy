from django.contrib import admin
from .models import UserProfile,article,category

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user','description']
	search_fields = ['user']
admin.site.register(UserProfile,UserProfileAdmin)


class articleAdmin(admin.ModelAdmin):
	list_display = ['title','category','date']
	search_fields = ['title','category','date']

admin.site.register(article, articleAdmin)

class categoryAdmin(admin.ModelAdmin):
	list_display = ['title']
	search_fields = ['title']
admin.site.register(category,categoryAdmin)