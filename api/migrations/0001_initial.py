# Generated by Django 3.0.8 on 2021-02-08 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('mood', models.CharField(choices=[('😢', 'Crying'), ('🙁', 'Sad'), ('😐', 'Neutral'), ('🙂', 'Happy'), ('😁', 'Grin')], default='😢', max_length=1)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('locationDisplayName', models.CharField(max_length=255)),
                ('synchronised', models.BooleanField()),
                ('lastModified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('filePath', models.FileField(upload_to='%Y/%m/%d/')),
                ('mediaType', models.CharField(choices=[('a', 'Audio'), ('v', 'Video'), ('p', 'Picture'), ('f', 'Filetype')], default='f', max_length=1)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.JournalEntry')),
            ],
        ),
        migrations.CreateModel(
            name='EntryTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.JournalEntry')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Tag')),
            ],
            options={
                'unique_together': {('entry', 'tag')},
            },
        ),
    ]
