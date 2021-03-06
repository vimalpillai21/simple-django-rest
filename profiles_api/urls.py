from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, UserProfileViewSet, HelloViewSet


router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, base_name='hello-viewset')
router.register('profile',UserProfileViewSet)
urlpatterns=[
    url(r'^hello-view/$',HelloApiView.as_view()),
    url(r'',include(router.urls))
   ]