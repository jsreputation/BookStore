from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet
app_name = 'bookapp'

router = DefaultRouter()

router.register(r'books', BookViewSet, basename="books")
router.register(r'authors', AuthorViewSet, basename="authors")
urlpatterns = [
    path('', include(router.urls))
    # path('', include('UserApp.urls'))
]
