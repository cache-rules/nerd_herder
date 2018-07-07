# Generated by Django 2.0.1 on 2018-07-07 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('position', models.IntegerField()),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
