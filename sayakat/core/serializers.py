from rest_framework import serializers
from accounts.serializers import UserSerializer


from .models import Country, City, Station, Route, Autobase, TransportType, Driver, Transport, Violation, Saloon, \
    Seat, Schedule, TicketType, Ticket


class CityStationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ('id', 'name', 'location', 'city',)


class CitySerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    stations = CityStationSerializer(many=True, read_only=True)

    class Meta:
        model = City
        fields = ('id', 'code', 'name', 'country', 'stations', )


class CountryCitySerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()

    class Meta:
        model = City
        fields = ('id', 'code', 'name', 'country',)


class CountrySerializer(serializers.ModelSerializer):
    city = CountryCitySerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ('id', 'code', 'name', 'city',)


class StationSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()

    class Meta:
        model = Station
        fields = ('id', 'name', 'location', 'city',)


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'route_number', 'departure_station', 'arrival_station', 'route_code', 'description',)


class RouteDetailSerializer(serializers.ModelSerializer):
    departure_station = StationSerializer(read_only=True)
    arrival_station = StationSerializer(read_only=True)

    class Meta:
        model = Route
        fields = ('id', 'route_number', 'departure_station', 'arrival_station', 'route_code', 'description',)


class AutobaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autobase
        fields = ('id', 'name', 'license',)


class AutobaseDetailSerializer(serializers.ModelSerializer):
    autobase_transports = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Autobase
        fields = ('id', 'name', 'license', 'autobase_transports',)


class TransportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportType
        fields = ('id', 'type_name',)


class DriverTransportSerializer(serializers.ModelSerializer):
    transport_type = TransportTypeSerializer(many=False, read_only=True)
    autobase = AutobaseSerializer(many=False, read_only=True)

    class Meta:
        model = Transport
        fields = ('id', 'transport_type', 'autobase',)


class DriverSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    driver_transports = DriverTransportSerializer(many=True, read_only=True)

    class Meta:
        model = Driver
        fields = ('id', 'user', 'license', 'driver_transports', )


class TransportSerializer(serializers.ModelSerializer):
    driver = serializers.StringRelatedField()
    autobase = serializers.StringRelatedField()
    transport_type = serializers.StringRelatedField()

    class Meta:
        model = Transport
        fields = ('id', 'name', 'transport_type', 'autobase', 'driver', 'transport_number', )


class TransportDriverSerializers(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Driver
        fields = ('id', 'user', 'license', 'driver_transports',)


class TransportDetailSerializer(serializers.ModelSerializer):
    transport_type = TransportTypeSerializer(many=False, read_only=True)
    autobase = AutobaseSerializer(many=False, read_only=True)
    driver = TransportDriverSerializers(many=True, read_only=True)

    class Meta:
        model = Transport
        fields = ('id', 'name', 'transport_type', 'autobase', 'driver', 'transport_number', )
