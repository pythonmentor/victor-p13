from django.conf.urls import url
from django.urls import path

from faq import views

urlpatterns = [

    path(r'memo_list/', views.memo_list, name="memo_list"),
    path(r'answer_search/', views.answer_search, name="answer_search"),
    path(r'answer_detail/<int:answer_id>', views.answer_detail, name="answer_detail"),
    ]
