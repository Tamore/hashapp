# Generated by Django 4.2.14 on 2024-07-24 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashapp', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
    ]
