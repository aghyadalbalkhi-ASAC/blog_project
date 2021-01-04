from django.urls import path,include
from .views import HomePageView,Post_Detail

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('<int:pk>/',Post_Detail.as_view(),name='post_detail')
]
