# Generated by Django 4.0.6 on 2022-07-27 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_file4_uploadfile_file1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfile',
            name='file1',
        ),
        migrations.AddField(
            model_name='uploadfile',
            name='Resume',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]