from rest_framework import generics, status, exceptions, response

from accounts.permissions import IsCassir, IsDispetcher, IsBase, IsAdmin, IsStaff, IsSuperuser

from .models import City, Country, Station, Route, Autobase, TransportType, Driver, Transport, Violation, Saloon, \
    Seat, Schedule, TicketType, Ticket

from .serializers import CitySerializer, CountrySerializer, StationSerializer, RouteSerializer, RouteDetailSerializer, \
    AutobaseSerializer, AutobaseDetailSerializer, TransportTypeSerializer, DriverSerializer, TransportSerializer, \
    TransportDetailSerializer


class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAdmin, )

    def perform_create(self, serializer):
        serializer.save()


class CountryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAdmin, )


class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAdmin, )

    def perform_create(self, serializer):
        serializer.save()


class CityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = (IsAdmin, )


class StationListCreateView(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = (IsAdmin, IsDispetcher, )

    def perform_create(self, serializer):
        serializer.save()


class StationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = (IsAdmin, IsDispetcher, )


class RouteListCreateView(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = (IsAdmin, IsDispetcher, )

    def perform_create(self, serializer):
        serializer.save()


class RouteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteDetailSerializer
    permission_classes = (IsAdmin, IsDispetcher, )


class AutobaseListCreateView(generics.ListCreateAPIView):
    queryset = Autobase.objects.all()
    serializer_class = AutobaseSerializer
    permission_classes = (IsAdmin, IsDispetcher, )

    def perform_create(self, serializer):
        serializer.save()


class AutobaseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autobase.objects.all()
    serializer_class = AutobaseDetailSerializer
    permission_classes = (IsAdmin, IsDispetcher, )


class TransportTypeListCreateView(generics.ListCreateAPIView):
    queryset = TransportType.objects.all()
    serializer_class = TransportTypeSerializer
    permission_classes = (IsAdmin, IsDispetcher, )

    def perform_create(self, serializer):
        serializer.save()


class DriverListCreateView(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = (IsAdmin, IsDispetcher, )

    def perform_create(self, serializer):
        serializer.save()


class DriverRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = (IsAdmin, IsDispetcher, )


class TransportListCreateView(generics.ListCreateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    permission_classes = (IsAdmin, IsDispetcher, )

    def perform_create(self, serializer):
        serializer.save()


class TransportRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportDetailSerializer
    permission_classes = (IsAdmin, IsDispetcher, )
