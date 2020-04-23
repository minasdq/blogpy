from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *



class Indexpage(TemplateView):
	def get (self , request,**kwargs):
		article_query=[]
		all_article=Article.objects.all().order_by('-date')[:12]
		for article in all_article:
			article_query.append({
				'title':article.title,
				'category':article.category,
				'cover':article.cover,
				'date':article.date.date(),
			})
		context={
			'article_data':article_query,
		}
		return render(request,'index.html',context)