# Generated by Django 3.2.4 on 2021-08-19 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0008_auto_20210819_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
