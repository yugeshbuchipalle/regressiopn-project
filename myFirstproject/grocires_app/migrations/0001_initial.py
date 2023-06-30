# Generated by Django 4.2.1 on 2023-06-29 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterdUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(blank=True, max_length=13, null=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]