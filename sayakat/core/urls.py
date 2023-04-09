from django.urls import path

from .views import (
    CountryListCreateView,
    CountryRetrieveUpdateDestroyView,
    CityListCreateView,
    CityRetrieveUpdateDestroyView,
    StationListCreateView,
    StationRetrieveUpdateDestroyView,
    RouteListCreateView,
    RouteRetrieveUpdateDestroyView,
    AutobaseListCreateView,
    AutobaseRetrieveUpdateDestroyView,
    TransportTypeListCreateView,
    DriverListCreateView,
    DriverRetrieveUpdateDestroyView,
    TransportListCreateView,
    TransportRetrieveUpdateDestroyView,
)

app_name = "core"

urlpatterns = [
    path("countries/", CountryListCreateView.as_view(), name="countries"),
    path("countries/<int:pk>/", CountryRetrieveUpdateDestroyView.as_view(), name="country"),
    path("cities/", CityListCreateView.as_view(), name="cities"),
    path("cities/<int:pk>/", CityRetrieveUpdateDestroyView.as_view(), name="city"),
    path("stations/", StationListCreateView.as_view(), name="stations"),
    path("stations/<int:pk>/", StationRetrieveUpdateDestroyView.as_view(), name="station"),
    path("routes/", RouteListCreateView.as_view(), name="routes"),
    path("routes/<int:pk>/", RouteRetrieveUpdateDestroyView.as_view(), name="route"),
    path("autobases/", AutobaseListCreateView.as_view(), name="autobases"),
    path("autobases/<int:pk>/", AutobaseRetrieveUpdateDestroyView.as_view(), name="autobase"),
    path("transport_types/", TransportTypeListCreateView.as_view(), name="transport_types"),
    path("drivers/", DriverListCreateView.as_view(), name="drivers"),
    path("drivers/<int:pk>/", DriverRetrieveUpdateDestroyView.as_view(), name="driver"),
    path("transports/", TransportListCreateView.as_view(), name="transports"),
    path("transports/<int:pk>/", TransportRetrieveUpdateDestroyView.as_view(), name="transport"),
]
