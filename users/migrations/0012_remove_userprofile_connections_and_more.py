# Generated by Django 4.0 on 2022-04-02 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_userprofile_connections_connectionrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='connections',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='connections',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='connections', to='users.connectionrequest'),
            preserve_default=False,
        ),
    ]
