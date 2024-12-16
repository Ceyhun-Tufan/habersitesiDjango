from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import News,Category,Tag
from .serializers import NewsSerializer,CategorySerializer,NewsUndetailedSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

# DEBUGGING

class NewsView(APIView):

    def get(self, request):
        query = News.objects.all()  # Tüm haberleri al
        serializer = NewsSerializer(query, many=True)  # `data` yerine queryset'i buraya geçiyoruz
        return Response(serializer.data,status=HTTP_200_OK)



#PRODUCTION

class SingleNewDetail(APIView):

    def get(self, request,slug):
        query = News.objects.get(slug=slug) 
        serializer = NewsSerializer(query)
        return Response(serializer.data, status=HTTP_200_OK)


class NewsListView(ListAPIView):

    queryset = News.objects.all()
    serializer_class = NewsUndetailedSerializer
    pagination_class = PageNumberPagination



## -    CATEGORIES 

# slug ile verilen kategorideki haberleri listeler
class NewsOfCategory(APIView):

    def get(self,request,slug):
        category_query = Category.objects.get(slug=slug)
        news_query = News.objects.filter(category=category_query)
        serializer = NewsUndetailedSerializer(news_query,many=True)
        return Response(serializer.data,status=HTTP_200_OK)


class AllCategories(APIView):

    def get(self,request):
        category_query = Category.objects.all()
        serializer = CategorySerializer(category_query,many=True)
        return Response(serializer.data,status=HTTP_200_OK)


