# Generated by Django 4.2.14 on 2024-07-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashapp', '0004_rename_likes_post_no_of_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowersCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=200)),
            ],
        ),
    ]
