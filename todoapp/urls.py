from django.urls import path
from .views import TodoappListView,TodoappDetailView,TodoappCreateView,TodoappUpdateView,TodoappDeleteView

urlpatterns = [
    path('',TodoappListView.as_view(),name='todo_list'),
    path('<int:pk>',TodoappDetailView.as_view(),name='todo_detail'),
    path('new/',TodoappCreateView.as_view(),name='todo_new'),
    path('<int:pk>/edit/',TodoappUpdateView.as_view(),name='todo_edit'),
    path('<int:pk>/delete/',TodoappDeleteView.as_view(),name='todo_delete'),

]
