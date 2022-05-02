from django.urls import path

from .views import index, by_rubric
from .views import vova
from .views import hh

urlpatterns = [
	path('<int:rubric_id/>',by_rubric),
	path('',index),
	path('v1/',vova),
	path('hh/',hh),
]