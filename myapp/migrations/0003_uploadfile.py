# Generated by Django 4.0.6 on 2022-07-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file4', models.FileField(max_length=250, upload_to='')),
            ],
        ),
    ]