# Generated by Django 2.2.5 on 2019-09-17 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190903_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='imprint',
            field=models.CharField(default='No IMPRINT', max_length=300),
        ),
    ]
