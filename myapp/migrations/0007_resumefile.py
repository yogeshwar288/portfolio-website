# Generated by Django 4.0 on 2022-08-21 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_user11'),
    ]

    operations = [
        migrations.CreateModel(
            name='resumefile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]