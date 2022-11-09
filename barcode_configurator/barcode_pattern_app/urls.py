from django.urls import path
from . import views
app_name = "barcode_pattern_app"
urlpatterns = [
       path('store-barcode-pattern', views.store_barcode_pattern, name='store_barcode_pattern'),
       path('update-barcode-pattern', views.update_barcode_pattern, name='update_barcode_pattern'),
       path('get-barcode-patterns', views.get_barcode_patterns, name='get_barcode_patterns'),
       path('get-shop-types', views.get_shop_types, name='get_shop_types'),
       path('get-pattern-types', views.get_pattern_types, name='get_pattern_types'),
       path('delete-barcode-pattern', views.delete_barcode_pattern, name='delete_barcode_pattern'),
      ]