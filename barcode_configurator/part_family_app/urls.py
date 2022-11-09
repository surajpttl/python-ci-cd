from django.urls import path
from . import views
app_name = "part_family_app"
urlpatterns = [
       path('store-tag-criticality', views.store_tag_criticality, name='store_tag_criticality'),
       path('update-tag-criticality', views.update_tag_criticality, name='update_tag_criticality'),
       path('store-part-family', views.store_part_family, name='store_part_family'),
       path('update-part-family',views.update_part_family,name="update_part_family"),
       path('get-part-family', views.get_part_family, name='get_part_family'),
       path('get-tags', views.get_tags, name='get_tags'),
       path('delete-part-family', views.delete_part_family, name='delete_part_family'),
      ]