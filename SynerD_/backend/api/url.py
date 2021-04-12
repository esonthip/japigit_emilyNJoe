from django.urls import path
from . import views
app_name = 'backend'
urlpatterns = [ 
        path('subjects/', views.UserInfoListView.as_view(), name='userinfo_list'), 
        path('subjects/<pk>/', views.UserInfoDetailView.as_view(), name='userinfo_detail'),
]

