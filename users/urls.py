from django.urls import path
from users.views import User, UserList


app_name = 'users'

urlpatterns = [
    path('all/', UserList.as_view(), name='user'),
    path('add-user/', UserList.as_view(), name='add-user'),
    path('<int:pk>', User.as_view())
]