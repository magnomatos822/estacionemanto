# Generated by Django 2.1.2 on 2018-11-28 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=7)),
                ('cor', models.CharField(max_length=15)),
                ('obs', models.TextField()),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Marca')),
            ],
            options={
                'verbose_name': 'Veiculo',
                'verbose_name_plural': 'Veiculos',
            },
        ),
    ]
