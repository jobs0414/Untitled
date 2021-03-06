# Generated by Django 2.1.2 on 2018-11-04 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='음원명')),
                ('piece', models.IntegerField(blank=True, default=0, verbose_name='경매 수량')),
                ('base_price', models.IntegerField(blank=True, default=0, verbose_name='경매 시작가격')),
                ('endtime', models.DateTimeField(verbose_name='경매 종료시각')),
                ('call_price', models.IntegerField(blank=True, default=0, verbose_name='입찰가격')),
            ],
        ),
    ]
