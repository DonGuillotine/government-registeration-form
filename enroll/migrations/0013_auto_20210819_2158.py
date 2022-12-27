# Generated by Django 3.2.4 on 2021-08-19 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0012_alter_registration_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='cancer',
            field=models.CharField(blank=True, choices=[('1', 'Carcinoma'), ('2', 'Sarcoma'), ('3', 'Leukemia'), ('4', 'Lymphoma'), ('5', 'None')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='diabetes',
            field=models.CharField(blank=True, choices=[('1', 'type 1'), ('2', 'type 2'), ('3', 'Gestational'), ('4', 'None')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='hypertension',
            field=models.CharField(blank=True, choices=[('1', 'Primary'), ('2', 'Secondary'), ('3', 'None')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='kidney_issue',
            field=models.CharField(blank=True, choices=[('1', 'Kidney Stones'), ('2', 'Chronic Kidney Disease'), ('3', 'Urinary tract infections'), ('4', 'Glomerulonephritis'), ('5', 'None')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='sickle_cell',
            field=models.CharField(blank=True, choices=[('1', 'Sickle Cell Anemia (SS)'), ('2', 'Sickle Hemoglobin-C Disease (SC)'), ('3', 'Sickle Beta-Plus Thalassemia'), ('4', 'Sickle Beta-Zero Thalassemia'), ('5', 'None')], max_length=50, null=True),
        ),
    ]
