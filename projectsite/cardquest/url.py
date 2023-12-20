from django.urls import path
from cardquest.views import HomePageView, TrainerList, TrainerCreateView
from cardquest import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('trainer_list', TrainerList.as_view(), name='tainer-list'),
    path('trainer_list/add', TrainerCreateView.as_view(), name='trainer-add')
]
