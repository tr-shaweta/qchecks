
from django.urls import path
from .views import InspectionView

urlpatterns = [
    path('api/inspections/', InspectionView.as_view(), name='inspections'),
]