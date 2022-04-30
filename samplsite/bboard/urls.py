from django.urls import path

from .views import index
from .views import vova

urlpatterns = [
	path('',index),
	path('v1/',vova),
]