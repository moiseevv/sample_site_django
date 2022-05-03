from django.urls import path


from .views import index, by_rubric, BbCreateView
from .views import vova
from .views import hh

urlpatterns = [
	path('add/', BbCreateView.as_view(), name='add'),
	path('<int:rubric_id>/', by_rubric, name = 'by_rubric'),
	path('',index, name = 'index'),
	path('v1/',vova),
	path('hh/',hh),
]