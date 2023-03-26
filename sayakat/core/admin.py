from django.contrib import admin
from .models import Country, City, Station, Route, Autobase, TransportType, Driver, Transport, Violation, Saloon, \
    Seat, Schedule, Ticket, TicketType


class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name',)
    list_display_links = ('id', 'code',)
    search_fields = ('name',)


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'country',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'country__name',)
    list_filter = ('country',)


class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'city',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'city__name', 'city__country__name',)
    list_filter = ('city',)


class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'route_number', 'departure_station', 'arrival_station', 'route_code', 'description',)
    list_display_links = ('id', 'route_number',)
    search_fields = ('route_number', 'departure_station__name', 'arrival_station__name', 'route_code', 'description',
                     'departure_station__city__name', 'arrival_station__city__name',
                     'departure_station__city__country__name', 'arrival_station__city__country__name',)
    list_filter = ('departure_station', 'arrival_station',)


class AutobaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'license',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'license',)


class TransportTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name',)
    list_display_links = ('id', 'type_name',)
    search_fields = ('type_name',)


class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'license',)
    list_display_links = ('id', 'user',)
    search_fields = ('user__username', 'license',)


class TransportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'transport_number', 'autobase', 'transport_type', 'driver',)
    list_display_links = ('id', 'transport_number',)
    search_fields = ('transport_number', 'autobase__name', 'transport_type__type_name', 'driver__user__username',)
    list_filter = ('autobase', 'transport_type',)


class ViolationAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'transport', 'text',)
    list_display_links = ('id', 'date',)
    search_fields = ('transport__number', 'text',)
    list_filter = ('transport', 'date',)


class SaloonAdmin(admin.ModelAdmin):
    list_display = ('id', 'transport', 'name', 'count_place', 'description', 'number_of_rows', 'number_of_places',)
    list_display_links = ('id', 'name',)
    search_fields = ('transport__number', 'name', 'description',)


class SeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'saloon', 'seat_number', )
    list_display_links = ('id', 'seat_number',)
    search_fields = ('saloon__name', 'seat_number',)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'route', 'transport', 'departure_time', 'arrival_time', 'days_of_week', )
    list_display_links = ('id', 'days_of_week', 'departure_time', 'arrival_time',)
    search_fields = ('route__route_number', 'transport__number', 'days_of_week', 'departure_time', 'arrival_time',)
    list_filter = ('route', 'transport',)


class TicketTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'description',)


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'seat_number', 'price', 'type', 'schedule', 'seller', 'status',)
    list_display_links = ('id', 'seat_number', 'price', )
    search_fields = ('seat_number', 'price', 'type__name', 'schedule__route__route_number',
                     'schedule__transport__number', 'seller__username', 'status',)
    list_filter = ('type', 'schedule', 'seller', 'status',)


admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Autobase, AutobaseAdmin)
admin.site.register(TransportType, TransportTypeAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(Violation, ViolationAdmin)
admin.site.register(Saloon, SaloonAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(TicketType, TicketTypeAdmin)
admin.site.register(Ticket, TicketAdmin)

