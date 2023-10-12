from django.urls import path
from .views import (
    IndexPage,
    ContactPage,
    AboutUsPage,
    ArticleDetail,
    AllArticleApiViews,
    ArticleCreateView,
    SingleArticleApiView,
    SearchArticleAPIView,
    CreateArticleAPIView,
    DeleteArticleAPIView,
    category_page,
)

urlpatterns = [
    path("", IndexPage.as_view(), name="index"),
    path("detail/", ArticleDetail.as_view(), name="detail"),
    path("contact/", ContactPage.as_view(), name="contact"),
    path("about/", AboutUsPage.as_view(), name="about"),
    path("category/", category_page, name="category"),
    path("new/", ArticleCreateView.as_view(), name="create_article"),
    # api urls
    path("article/all", AllArticleApiViews.as_view(), name="api_all_article"),
    path("article/", SingleArticleApiView.as_view(), name="single_article"),
    path("article/search/", SearchArticleAPIView.as_view(), name="search_article"),
    path("article/create/", CreateArticleAPIView.as_view(), name="create_article"),
    path("article/delete/", DeleteArticleAPIView.as_view(), name="delete_article"),
]
