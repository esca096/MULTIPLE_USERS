from django.urls import path
from .views import home, register, doctor, infirmiere, patient
urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('doctor', doctor, name='doctor'),
    path('infirmiere', infirmiere, name='infirmiere'),
    path('patient', patient, name='patient'),
]
