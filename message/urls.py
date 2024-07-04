from django.urls import path
from . import views

urlpatterns = [
    # message/   => 留言列表
    path('', views.MessageList.as_view(), name='msg_list'),
    # message/1/, message/2/, ...
    path('<int:pk>/', views.MessageRead.as_view(), name='msg_read'),
    # message/create/
    path('create/', views.MessageNew.as_view(), name='msg_create'),

]