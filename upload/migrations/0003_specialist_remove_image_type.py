# Generated by Django 5.0.1 on 2024-01-27 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_alter_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='type',
        ),
    ]
