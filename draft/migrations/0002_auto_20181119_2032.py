# Generated by Django 2.1.3 on 2018-11-19 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draft', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='syllabus',
            options={'verbose_name_plural': 'Syllabus'},
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='topic',
            field=models.TextField(),
        ),
    ]
