# Generated by Django 4.0 on 2024-04-03 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_userprofile_certifications_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='certifications',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='licenses', to='users.certificationtag'),
        ),
    ]