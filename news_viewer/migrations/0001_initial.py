# Generated by Django 4.2.3 on 2023-07-06 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HNFetchState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_id', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.CharField(max_length=250)),
                ('source_creator_id', models.CharField(max_length=250, null=True)),
                ('source_created_at', models.DateTimeField(null=True)),
                ('item_type', models.CharField(max_length=200)),
                ('origin', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment_count', models.IntegerField(null=True)),
                ('text', models.TextField(null=True)),
                ('url', models.URLField(null=True)),
                ('title', models.CharField(max_length=600, null=True)),
                ('score', models.IntegerField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_id', models.CharField(max_length=250)),
                ('source_creator_id', models.CharField(max_length=250, null=True)),
                ('source_created_at', models.DateTimeField(null=True)),
                ('item_type', models.CharField(max_length=200)),
                ('origin', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(null=True)),
                ('url', models.URLField(null=True)),
                ('parent_comment', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='news_viewer.comment')),
                ('parent_post', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='news_viewer.story')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
