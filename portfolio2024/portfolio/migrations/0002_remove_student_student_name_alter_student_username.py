# Generated by Django 5.1.2 on 2024-12-16 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_name',
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=20, null=True, verbose_name='学生氏名'),
        ),
    ]