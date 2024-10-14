# app's urls.py (API/urls.py)
from django.urls import path
from . import views

urlpatterns = [
    path('webtoons/', views.webtoon_list, name='webtoon-list'),  # GET all webtoons
    path('webtoons/', views.webtoon_create, name='webtoon-create'),  # POST create a new webtoon
    path('webtoons/<int:id>/', views.webtoon_detail, name='webtoon-detail'),  # GET a specific webtoon by ID
    path('webtoons/<int:id>/', views.webtoon_delete, name='webtoon-delete'),  # DELETE a webtoon by ID
]
