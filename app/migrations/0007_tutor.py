# Generated by Django 4.0.4 on 2022-06-17 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
    ]
