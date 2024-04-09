from django.urls import path
from . import views

urlpatterns = [
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('', views.index, name='index'),
]