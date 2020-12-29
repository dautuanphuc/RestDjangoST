from django.urls import path, include
from . import views
urlpatterns = [
    path('art/', views.ArticleList.as_view(), name= 'article'),
    path('aView/<int:pk>/', views.ArticleView.as_view(), name='aView'),
    path('mixins/', views.ArticleMixin.as_view()),
    path('Vmixin/<int:pk>/', views.ArticleViewMixin.as_view()),
    path('UL/', views.UsingGenericList.as_view()),
    path('UD/<int:pk>/', views.UsingGenericDetail.as_view()),
]