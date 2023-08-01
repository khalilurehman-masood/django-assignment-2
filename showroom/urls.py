from django.urls import path
from . import views

app_name = "showroom"

urlpatterns = [
    path('', views.showroom_view, name='showroom'),

    path('team', views.team_list, name='team_list'),
    path('member/<int:member_id>/', views.member_detail, name='member_detail'),

    path('brands', views.brand_list_view, name='brands_list'),
    path('<int:brand_id>', views.brand_models, name='brand_models'),

    path('models', views.models_list_view, name='models_list'),
    path('model-detail/<int:model_id>', views.model_detail, name='model_detail'),

]