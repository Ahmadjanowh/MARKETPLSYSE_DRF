from django.urls import path
from apps.users.views import UserListCrateAPIView,UserRetrieveAPIView,UserUpdateAPIView,UserDestroyAPIView

urlpatterns = [
    path('',UserListCrateAPIView.as_view(),name='api_users'),
    path('<int:pk>',UserRetrieveAPIView.as_view(),name='api_users_retrieve'),
    path('update/<int:pk>/',UserUpdateAPIView.as_view(),name='api_users_update'),
    path('destroy/<int:pk>/',UserDestroyAPIView.as_view(),name='api_users_destroy'),

]