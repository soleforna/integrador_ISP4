# Generated by Django 4.2.1 on 2024-05-07 12:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='method',
            field=models.CharField(choices=[('Efectivo', 'Efectivo'), ('Debito', 'Débito'), ('Credito', 'Crédito')], max_length=10),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Completado', 'Completado'), ('Fallido', 'Fallido'), ('Cancelado', 'Cancelado'), ('Reembolsado', 'Reembolsado')], max_length=12),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
