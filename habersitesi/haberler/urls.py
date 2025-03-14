from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls import re_path
from django.views.static import serve
from .views import NewsView,SingleNewDetail,NewsOfCategory,AllCategories,NewsListView,NewsAddView

urlpatterns = [
    path('haberler-all/', NewsView.as_view()),

    #PRODUCTION

    path('haberler/', NewsListView.as_view()),
    path('haberler/<slug:slug>', SingleNewDetail.as_view()),
    path('kategoriler/<slug:slug>', NewsOfCategory.as_view()),
    path('kategoriler/', AllCategories.as_view()),

    path('haber-ekle/', NewsAddView.as_view()),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)