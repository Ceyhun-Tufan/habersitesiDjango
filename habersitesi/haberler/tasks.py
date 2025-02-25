from celery import shared_task
from .models import Category,News
import requests
from django.utils.text import slugify

@shared_task
def categoryAi(content:str,news_id:int): 
    try:


        new = News.objects.get(id=news_id)
        content = content.lower().strip()

        res = requests.post('http://213.142.151.177:3002/news/category',json={'text':content})
        res = res.json()
        category_name = res.get('category',None)
        category_name = slugify(category_name)
        
        category = Category.objects.get_or_create(name=category_name)[0]

        new.category = category
        new.save()



    # eger api cevap vermezse
    except requests.RequestException as e:

        news = News.objects.get(id=news_id)
        news.category = None
        news.save()

@shared_task
def summeryAi(content:str,news_id:int):
    print("---- DENIYORUM ----")
    try:

        new = News.objects.get(id=news_id)
        content = content.lower().strip()

        res = requests.post('http://213.142.151.177:3002/news/summary',json={'text':content})
        res = res.json()
        summary = res.get('summary',None)
        new.subtitle = summary
        new.save()

    except requests.RequestException as e:
        print(f"----{e} ----")
        
        news = News.objects.get(id=news_id)
        news.subtitle = ""
        news.save()