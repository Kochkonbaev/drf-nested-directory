from . import views  
from django.urls import path


urlpatterns = [
path('', views.CategoryList.as_view()),
path('<slug:category_slug>/', views.SectionList.as_view()),
path('<slug:category_slug>/<slug:section_slug>/', views.GroupList.as_view()),
path('<slug:category_slug>/<slug:section_slug>/<slug:group_slug>/', views.SubgroupList.as_view()),
path('<slug:category_slug>/<slug:section_slug>/<slug:group_slug>/<slug:subgroup_slug>/', views.CardList.as_view()),
path('<slug:category_slug>/<slug:section_slug>/<slug:group_slug>/<slug:subgroup_slug>/<slug:card_slug>/', views.CardDetail.as_view()),
path('<slug:category_slug>/<slug:section_slug>/<slug:group_slug>/<slug:subgroup_slug>/<slug:card_slug>/<slug:prod_slug>/', views.ProductDetail.as_view())

]
