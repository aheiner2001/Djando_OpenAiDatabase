from django.urls import path
from .views import query_view
from django.urls import path
from .views import home
from .views import slammmy

urlpatterns = [
    path("", home, name="home"),  # This makes "/" load the home view
]


urlpatterns = [
      path('query/', query_view, name='query'),

      
      path('slammy/', slammmy, name='slamy'),

  ]
