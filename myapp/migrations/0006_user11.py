# Generated by Django 4.0 on 2022-08-19 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_uploadfile_file1_uploadfile_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='User11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Contact', models.CharField(max_length=10)),
                ('Messages', models.CharField(max_length=50)),
            ],
        ),
    ]
