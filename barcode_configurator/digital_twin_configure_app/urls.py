from django.urls import path
from . import views
app_name = "digital_twin_configure_app"
urlpatterns = [
       #path('generate_token', views.generateToken, name='genrateToken'),
       path('fetch-organization-master', views.fetch_organization_master, name='setOrganizationMaster'),
       path('fetch-business-unit-master', views.fetch_business_unit_master, name='setBusinessUnitMaster'),
       path('fetch-plant-master', views.fetch_plant_master, name='setPlantMaster'),
       path('fetch-shop-master', views.fetch_shop_master, name='setShopMaster'),
       path('fetch-line-master', views.fetch_line_master, name='setLineMaster'),
       path('fetch-station-master', views.fetch_station_master, name='setStationMaster'),
]
