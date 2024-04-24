from django.urls import path 
from . import views 
''' views of main app '''
urlpatterns = [ 
		path('', views.index), 
] 
