# Generated by Django 3.2.4 on 2021-08-11 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='First',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_type', models.CharField(blank=True, choices=[('Formal (Public Sector)', 'Formal (Public Sector)'), ('Informal (Public Sector)', 'Informal (Public Sector)')], max_length=30, null=True)),
            ],
        ),
    ]
