# Generated by Django 4.2.6 on 2023-10-23 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arechar_nutra', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bannermodel',
            name='user',
        ),
        migrations.DeleteModel(
            name='CertificationModel',
        ),
        migrations.RemoveField(
            model_name='whoarewemodel',
            name='user',
        ),
        migrations.DeleteModel(
            name='BannerModel',
        ),
        migrations.DeleteModel(
            name='WhoAreWeModel',
        ),
    ]