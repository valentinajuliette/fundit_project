# Generated by Django 5.1.1 on 2024-11-20 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundit', '0003_rename_cvv_subscription_cvv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='ODS_de_interés',
            field=models.ManyToManyField(to='fundit.ods'),
        ),
    ]
