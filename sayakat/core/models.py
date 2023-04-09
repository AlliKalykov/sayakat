from django.db import models
from accounts.models import Account


class Country(models.Model):
    code = models.IntegerField('Код страны', unique=True)
    name = models.CharField('Страна', max_length=255)

    def __str__(self):
        return self.name


class City(models.Model):
    code = models.IntegerField('Код города', unique=True)
    name = models.CharField('Город', max_length=255)
    country = models.ForeignKey(Country, verbose_name='Страна', on_delete=models.PROTECT, related_name='cities')

    def __str__(self):
        return self.name


class Station(models.Model):
    name = models.CharField('Название вокзала', max_length=255)
    location = models.CharField('Локация', max_length=255)
    city = models.ForeignKey(City,  verbose_name='Город', on_delete=models.PROTECT, related_name='stations')

    def __str__(self):
        return self.name


class Route(models.Model):
    route_number = models.IntegerField('Номер маршрута')
    departure_station = models.ForeignKey(Station, on_delete=models.PROTECT, related_name='departure_routes',
                                          verbose_name='Станция отправления')
    arrival_station = models.ForeignKey(Station, on_delete=models.PROTECT, related_name='arrival_routes',
                                        verbose_name='Станция прибытия')
    route_code = models.CharField(max_length=12, verbose_name='Код маршрута', unique=True)
    description = models.TextField('Описание маршрута', blank=True, null=True)

    def __str__(self):
        return f'{self.route_number} {self.departure_station} - {self.arrival_station}'


class Autobase(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название автобазы')
    license = models.CharField(max_length=255, verbose_name='Лицензия')

    def __str__(self):
        return self.name


class TransportType(models.Model):
    type_name = models.CharField(max_length=255, verbose_name='Тип транспорта')

    def __str__(self):
        return self.type_name


class Driver(models.Model):
    user = models.OneToOneField(Account, on_delete=models.PROTECT, verbose_name='Пользователь')
    license = models.CharField(max_length=255, verbose_name='Лицензия')

    def __str__(self):
        return self.user.username


class Transport(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название транспорта')
    transport_type = models.ForeignKey(TransportType, on_delete=models.PROTECT, related_name='type_transports',
                                       verbose_name='Тип транспорта')
    transport_number = models.CharField(max_length=15, verbose_name='Номер транспорта')
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT, related_name='driver_transports',
                               verbose_name='Водитель')
    autobase = models.ForeignKey(Autobase, on_delete=models.PROTECT, related_name='autobase_transports',
                                 verbose_name='Автобаза')

    def __str__(self):
        return self.name


class Violation(models.Model):
    transport = models.ForeignKey(Transport, on_delete=models.PROTECT, related_name='transport_violations',
                                  verbose_name='Нарушения')
    date = models.DateTimeField('Дата нарушения', auto_now_add=True)
    text = models.TextField('Текст нарушения')

    def __str__(self):
        return self.transport.name


class Saloon(models.Model):
    transport = models.ForeignKey(Transport, on_delete=models.PROTECT, related_name='transport_seats',
                                  verbose_name='Транспорт')
    name = models.CharField(max_length=255, verbose_name='Название салона')
    count_place = models.IntegerField('Количество мест')
    description = models.CharField(max_length=255, verbose_name='Описание')
    number_of_rows = models.IntegerField('Количество рядов')
    number_of_places = models.IntegerField('Количество мест в ряду')

    def __str__(self):
        return self.name


class Seat(models.Model):
    saloon = models.ForeignKey(Saloon, on_delete=models.PROTECT, related_name='saloon_seats',
                               verbose_name='Салон')
    seat_number = models.IntegerField('Номер места')

    def __str__(self):
        return f'{self.saloon.name} {self.saloon.transport.name} {self.seat_number}'


class Schedule(models.Model):
    transport = models.ForeignKey(Transport, on_delete=models.PROTECT, related_name='transport_schedules',
                                  verbose_name='Транспорт')
    departure_time = models.DateTimeField('Время отправления')
    arrival_time = models.DateTimeField('Время прибытия')
    days_of_week = models.CharField(max_length=255, verbose_name='Дни недели')
    route = models.ForeignKey(Route, on_delete=models.PROTECT, related_name='route_schedules',
                              verbose_name='Маршрут')

    def __str__(self):
        return f'{self.transport.name} {self.route.route_number} {self.departure_time} {self.arrival_time}'


class TicketType(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название типа билета')
    description = models.TextField('Описание типа билета')

    def __str__(self):
        return self.name


class Ticket(models.Model):
    type = models.ForeignKey(TicketType, on_delete=models.PROTECT, related_name='type_tickets',
                             verbose_name='Тип билета')
    schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT, related_name='schedule_tickets',
                                 verbose_name='Расписание')
    seller = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='seller_tickets',
                               verbose_name='Продавец')
    price = models.FloatField('Цена')
    seat_number = models.IntegerField('Номер места')
    status = models.IntegerField(choices=((0, 'Free'), (1, 'Sold'), (2, 'Reserved')), default=0,
                                 verbose_name='Статус билета')

    def __str__(self):
        return f'{self.schedule.transport.name} {self.schedule.route.route_number} {self.schedule.departure_time} {self.schedule.arrival_time} {self.seat_number}'
