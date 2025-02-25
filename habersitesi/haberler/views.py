from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import News,Category,Tag
from .serializers import NewsSerializer,CategorySerializer,NewsUndetailedSerializer,NewsAddSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST

# BURADAKI HER SEY ICIN:

# Daha sonrasinda gelecek olan api keyler ile tum endpointler
# korunacak.


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

# YENI
# Haber ekleme
class NewsAddView(APIView):

    def post(self,request):
        
        serializer = NewsAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


## -    CATEGORIES 

# slug ile verilen kategorideki haberleri listeler UNDETAILED
class NewsOfCategory(APIView):

    def get(self,request,slug):
        category_query = Category.objects.get(slug=slug)
        news_query = News.objects.filter(category=category_query)
        serializer = NewsUndetailedSerializer(news_query,many=True)
        return Response(serializer.data,status=HTTP_200_OK)

# Tum kategoriler
class AllCategories(APIView):

    def get(self,request):
        category_query = Category.objects.all()
        serializer = CategorySerializer(category_query,many=True)
        return Response(serializer.data,status=HTTP_200_OK)


