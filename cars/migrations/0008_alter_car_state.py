# Generated by Django 4.2.7 on 2023-11-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_car_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('AP', 'Andra Pradesh'), ('DL', 'Delhi'), ('TS', 'Telangana'), ('MH', 'Maharashtra'), ('KA', 'Karnataka'), ('TN', 'Tamilanadu'), ('KL', 'Kerala')], max_length=100),
        ),
    ]