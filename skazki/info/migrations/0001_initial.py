# Generated by Django 5.1.6 on 2025-03-26 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('address', models.CharField(max_length=250, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'ссылка',
                'verbose_name_plural': 'ссылку',
                'db_table': 'addresses',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='ФИО')),
                ('profession', models.CharField(blank=True, max_length=250, null=True, verbose_name='Профессия')),
                ('description', models.TextField(verbose_name='Описание')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон')),
                ('name_address_1', models.CharField(blank=True, max_length=250, null=True, verbose_name='Название соцсети')),
                ('address_1', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ссылка на соцсеть')),
                ('name_address_2', models.CharField(blank=True, max_length=250, null=True, verbose_name='Название соцсети')),
                ('address_2', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ссылка на соцсеть')),
                ('name_address_3', models.CharField(blank=True, max_length=250, null=True, verbose_name='Название соцсети')),
                ('address_3', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ссылка на соцсеть')),
            ],
            options={
                'verbose_name': 'информация',
                'verbose_name_plural': 'информацию',
                'db_table': 'persons',
                'ordering': ('id',),
            },
        ),
    ]
