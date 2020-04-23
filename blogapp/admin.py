from django.contrib import admin
from .models import UserProfile,Article,category

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['user','description']
	search_fields = ['user']
admin.site.register(UserProfile,UserProfileAdmin)


class articleAdmin(admin.ModelAdmin):
	list_display = ['title','category','date']
	search_fields = ['title','category','date']

admin.site.register(Article, articleAdmin)

class categoryAdmin(admin.ModelAdmin):
	list_display = ['title']
	search_fields = ['title']
admin.site.register(category,categoryAdmin)