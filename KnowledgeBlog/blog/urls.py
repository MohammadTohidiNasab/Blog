from django.urls import path
from . import views


urlpatterns = [
    path('',views.IndexPage.as_view(),name='index'),
    path("contact/", views.ContactPage.as_view(), name='contact'),
    path("about/",views.AboutUsPage.as_view(), name='about'),
    path('category/',views.CategoryPage.as_view(), name='category'),
    path('new/', views.ArticleCreateView.as_view(), name='create_article'),
# api urls
    path('article/all',views.AllArticleApiViews.as_view(), name='api_all_article'),
    path("article/",views.SingleArticleApiView.as_view(), name='single_article'),
    path('article/search/', views.SearchArticleAPIView.as_view(), name='search_article'),
    path('article/create/', views.CreateArticleAPIView.as_view(), name='create_article'),
    path('article/delete/', views.DeleteArticleAPIView.as_view(), name='delete_article'),
]

