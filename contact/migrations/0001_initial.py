# Generated by Django 3.1 on 2020-11-21 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=255)),
                ('site', models.URLField()),
                ('message', models.TextField()),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
