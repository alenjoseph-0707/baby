# Generated by Django 4.1 on 2022-09-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='regform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fn', models.CharField(max_length=50)),
                ('ln', models.CharField(max_length=50)),
                ('em', models.CharField(max_length=50)),
                ('mn', models.IntegerField()),
                ('pas', models.CharField(max_length=50)),
            ],
        ),
    ]