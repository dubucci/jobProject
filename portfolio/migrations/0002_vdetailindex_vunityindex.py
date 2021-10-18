# Generated by Django 2.2.5 on 2021-10-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vdetailindex',
            fields=[
                ('detail_indicator_seq', models.AutoField(primary_key=True, serialize=False)),
                ('gubun', models.CharField(blank=True, db_column='GUBUN', max_length=50, null=True)),
                ('year', models.CharField(blank=True, db_column='YEAR', max_length=10, null=True)),
                ('detail_index', models.CharField(blank=True, db_column='DETAIL_INDEX', max_length=10, null=True)),
                ('code', models.CharField(blank=True, db_column='CODE', max_length=50, null=True)),
                ('code_nm', models.CharField(blank=True, db_column='CODE_NM', max_length=100, null=True)),
                ('indicator', models.CharField(db_column='INDICATOR', max_length=50)),
                ('indicator_nm', models.CharField(blank=True, db_column='INDICATOR_NM', max_length=100, null=True)),
            ],
            options={
                'db_table': 'v_detail_indicator_real',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vunityindex',
            fields=[
                ('unity_indicator_seq', models.AutoField(primary_key=True, serialize=False)),
                ('gubun', models.CharField(blank=True, db_column='GUBUN', max_length=50, null=True)),
                ('year', models.CharField(blank=True, db_column='YEAR', max_length=10, null=True)),
                ('unity_index', models.CharField(blank=True, db_column='UNITY_INDEX', max_length=10, null=True)),
                ('code', models.CharField(blank=True, db_column='CODE', max_length=50, null=True)),
                ('code_nm', models.CharField(blank=True, db_column='CODE_NM', max_length=100, null=True)),
            ],
            options={
                'db_table': 'v_unity_indicator_real',
                'managed': False,
            },
        ),
    ]
