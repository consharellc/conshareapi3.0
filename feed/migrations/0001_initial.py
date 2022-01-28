# Generated by Django 4.0 on 2022-01-25 12:17

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True


    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('vote_rank', models.IntegerField(blank=True, default=0, null=True)),
                ('comment_count', models.IntegerField(blank=True, default=0, null=True)),
                ('share_count', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.feed')),
                ('remumble', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='remumbles', to='feed.feed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='MumbleVote',
            fields=[
                ('value', models.CharField(choices=[('upvote', 'upvote'), ('downvote', 'downvote')], max_length=20)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('mumble', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.feed')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='mumble_user', through='feed.MumbleVote', to=settings.AUTH_USER_MODEL),
        ),
    ]
