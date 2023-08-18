from django.urls import path
from core.views import CreateUserView, UnsubscribeUserView 


urlpatterns = [
    path('user/add', CreateUserView.as_view()),
    path('user/unsubscribe/<int:user_id>', UnsubscribeUserView.as_view()),
]