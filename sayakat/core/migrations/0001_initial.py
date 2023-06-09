# Generated by Django 4.1.7 on 2023-03-26 17:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autobase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название автобазы')),
                ('license', models.CharField(max_length=255, verbose_name='Лицензия')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True, verbose_name='Код города')),
                ('name', models.CharField(max_length=255, verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True, verbose_name='Код страны')),
                ('name', models.CharField(max_length=255, verbose_name='Страна')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license', models.CharField(max_length=255, verbose_name='Лицензия')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_number', models.IntegerField(verbose_name='Номер маршрута')),
                ('route_code', models.CharField(max_length=12, unique=True, verbose_name='Код маршрута')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание маршрута')),
            ],
        ),
        migrations.CreateModel(
            name='Saloon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название салона')),
                ('count_place', models.IntegerField(verbose_name='Количество мест')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('number_of_rows', models.IntegerField(verbose_name='Количество рядов')),
                ('number_of_places', models.IntegerField(verbose_name='Количество мест в ряду')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField(verbose_name='Время отправления')),
                ('arrival_time', models.DateTimeField(verbose_name='Время прибытия')),
                ('days_of_week', models.CharField(max_length=255, verbose_name='Дни недели')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='route_schedules', to='core.route', verbose_name='Маршрут')),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название типа билета')),
                ('description', models.TextField(verbose_name='Описание типа билета')),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название транспорта')),
                ('transport_number', models.CharField(max_length=15, verbose_name='Номер транспорта')),
                ('autobase', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='autobase_transports', to='core.autobase', verbose_name='Автобаза')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='driver_transports', to='core.driver', verbose_name='Водитель')),
            ],
        ),
        migrations.CreateModel(
            name='TransportType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=255, verbose_name='Тип транспорта')),
            ],
        ),
        migrations.CreateModel(
            name='Violation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата нарушения')),
                ('text', models.TextField(verbose_name='Текст нарушения')),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transport_violations', to='core.transport', verbose_name='Нарушения')),
            ],
        ),
        migrations.AddField(
            model_name='transport',
            name='transport_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type_transports', to='core.transporttype', verbose_name='Тип транспорта'),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('seat_number', models.IntegerField(verbose_name='Номер места')),
                ('status', models.IntegerField(choices=[(0, 'Free'), (1, 'Sold'), (2, 'Reserved')], default=0, verbose_name='Статус билета')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='schedule_tickets', to='core.schedule', verbose_name='Расписание')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='seller_tickets', to=settings.AUTH_USER_MODEL, verbose_name='Продавец')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type_tickets', to='core.tickettype', verbose_name='Тип билета')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название вокзала')),
                ('location', models.CharField(max_length=255, verbose_name='Локация')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.city', verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.IntegerField(verbose_name='Номер места')),
                ('saloon', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='saloon_seats', to='core.saloon', verbose_name='Салон')),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transport_seats', to='core.transport', verbose_name='Транспорт')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='transport',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transport_schedules', to='core.transport', verbose_name='Транспорт'),
        ),
        migrations.AddField(
            model_name='route',
            name='arrival_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='arrival_routes', to='core.station', verbose_name='Станция прибытия'),
        ),
        migrations.AddField(
            model_name='route',
            name='departure_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='departure_routes', to='core.station', verbose_name='Станция отправления'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.country', verbose_name='Страна'),
        ),
    ]
