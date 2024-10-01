# Generated by Django 5.1 on 2024-10-01 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_ward_houses_ward_monestaries_ward_schools'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='village',
            name='houses',
            field=models.IntegerField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='village',
            name='monestaries',
            field=models.IntegerField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='village',
            name='populations',
            field=models.IntegerField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='village',
            name='schools',
            field=models.IntegerField(blank=True, max_length=200),
        ),
    ]
