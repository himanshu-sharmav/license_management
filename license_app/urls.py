from django.urls import path
from .views import create_license, view_licenses, revoke_license

urlpatterns = [
    path('create/', create_license, name='create_license'),
    path('view/', view_licenses, name='view_licenses'),
    path('revoke/<int:license_id>/', revoke_license, name='revoke_license'),
]
