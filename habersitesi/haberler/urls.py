from django.urls import path
from .views import NewsView,SingleNewDetail,NewsOfCategory,AllCategories,NewsListView

urlpatterns = [
    path('haberler-all/', NewsView.as_view()),

    #PRODUCTION

    path('haberler/', NewsListView.as_view()),
    path('haberler/<slug:slug>', SingleNewDetail.as_view()),
    path('kategoriler/<slug:slug>', NewsOfCategory.as_view()),
    path('kategoriler/', AllCategories.as_view()),

]