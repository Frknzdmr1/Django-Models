# Generated by Django 4.1.4 on 2022-12-21 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='path',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
