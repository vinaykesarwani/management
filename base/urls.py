from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('', views.login_page, name='login'),
    path('home/', views.home, name='home'),
    path('view/', views.view, name='view'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('filter/', views.filter, name='filter'),
    path('modify/<str:pk>', views.modify, name='modify'),
    path('logout/', views.logout_, name='logout'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)