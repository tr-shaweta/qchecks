
from django.urls import path
from .views import InspectionView, InventoryView

urlpatterns = [
    path('api/inspections/', InspectionView.as_view(), name='inspections'),
    path('api/v1/inventory/', InventoryView.as_view(), name='inventory'),
]