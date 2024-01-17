from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ScoreViewSet, TotalScoreViewSet, AIView


router = DefaultRouter()

router.register(r'scores', ScoreViewSet)
router.register(r'totalscores', TotalScoreViewSet)


urlpatterns = [

    path('api/', include(router.urls)),
    path('api/ai/', AIView.as_view()),

]