from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ScoreViewSet, AIView


router = DefaultRouter()

router.register(r'scores', ScoreViewSet)


urlpatterns = [

    path('api/', include(router.urls)),
    path('api/ai/', AIView.as_view()),

]