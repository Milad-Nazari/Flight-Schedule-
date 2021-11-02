from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'first'
urlpatterns = [
    path('',views.schaduleHome.as_view(),name='index'),
    path('flight_detail/<int:flight_id>/',views.DetailFlight,name='flight_detail'),
    # path('Flight_Detail/<str:origin>/<str:distination>/<int:nomber>/<date')
]