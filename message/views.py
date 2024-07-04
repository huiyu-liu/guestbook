from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Message

# Create your views here.
class MessageList(ListView):
    model = Message

    # 頁面範本檔案名稱: 應用程式/資料模型_list.html => message/message_list.html
    # 頁面範本變數名稱: 資料模型_list => message_list

class MessageRead(DetailView):
    model = Message

    # 頁面範本檔案名稱: 應用程式/資料模型_detail.html => message/message_detail.html
    # 頁面範本變數名稱: 資料模型 => message

class MessageNew(CreateView):
    model = Message
    fields = ['user', 'receipt', 'subject', 'content']
    success_url = '/message/'
    # fields = '__all__'

    # 頁面範本檔案名稱: 應用程式/資料模型_form.html => message/message_form.html
    # 頁面範本變數名稱: form