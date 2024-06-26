# Generated by Django 4.0 on 2024-04-03 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_userprofile_certifications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='education',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schools', to='users.educationtag'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='interests',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic_interests', to='users.interesttag'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='jobs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs_done', to='users.experiencetag'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='personal_skills', to='users.skilltag'),
        ),
    ]
