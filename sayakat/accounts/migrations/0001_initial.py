# Generated by Django 4.1.7 on 2023-03-26 17:40

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=100, null=True, unique=True, verbose_name='Почта')),
                ('username', models.CharField(max_length=60, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Телефон')),
                ('first_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('last_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Последнее соединение')),
                ('role', models.CharField(choices=[('not_role', 'Роль не определена'), ('cassir', 'Кассир'), ('dispetcher', 'Диспетчер'), ('base', 'База')], default='not_role', max_length=10)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
