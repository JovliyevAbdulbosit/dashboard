# Generated by Django 3.2.8 on 2021-10-25 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('slug', models.SlugField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingrednts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=256)),
                ('porsiya', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Retsept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('prep', models.JSONField(default={'Cook': '', 'Prep': '', 'Yields': ''})),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('steps', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('rete', models.SmallIntegerField(choices=[(5, '⭐️⭐️⭐️⭐️⭐️'), (4, '⭐️⭐️⭐️⭐️'), (3, '⭐️⭐️⭐️'), (2, '⭐️⭐️'), (1, '⭐️')])),
                ('ingrednts', models.ManyToManyField(to='dashboard.Ingrednts')),
            ],
        ),
    ]
