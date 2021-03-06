# Generated by Django 3.2.9 on 2022-03-13 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sanasi', models.DateTimeField()),
                ('miqdor', models.PositiveSmallIntegerField()),
                ('umumiy_summa', models.IntegerField()),
                ('tolandi', models.IntegerField()),
                ('nasiya', models.IntegerField()),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.client')),
                ('ombor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.ombor')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.product')),
            ],
        ),
    ]
