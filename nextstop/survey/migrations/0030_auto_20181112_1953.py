# Generated by Django 2.1.3 on 2018-11-13 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0029_auto_20181112_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='gender',
            field=models.CharField(blank=True, choices=[('', ''), ('nonbinary', 'Nonbinary'), ('female', 'Female'), ('male', 'Male')], default=None, help_text='Gender identity.', max_length=20, null=True),
        ),
    ]
