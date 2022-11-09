from django.contrib import admin
from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^digital_twin/', include('digital_twin_configure_app.urls', namespace='digital_twin_configure_app')),
    re_path(r'^barcode/', include('barcode_pattern_app.urls', namespace='barcode_pattern_app')),
    re_path(r'^part-family/', include('part_family_app.urls', namespace='part_family_app')),

]
