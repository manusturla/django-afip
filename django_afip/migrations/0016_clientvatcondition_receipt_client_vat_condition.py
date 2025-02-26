# Generated by Django 5.1.6 on 2025-02-26 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afip', '0015_alter_taxpayer_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientVatCondition',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False, verbose_name='code')),
                ('description', models.CharField(max_length=48, verbose_name='description')),
                ('cmp_clase', models.CharField(help_text='Receipt class this VAT condition applies to (A, B, C, or M).', max_length=5, verbose_name='cmp clase')),
            ],
            options={
                'verbose_name': 'Client VAT condition',
                'verbose_name_plural': 'Client VAT conditions',
                'unique_together': {('code', 'cmp_clase')},
            },
        ),
        migrations.AddField(
            model_name='receipt',
            name='client_vat_condition',
            field=models.ForeignKey(help_text='The VAT condition of the recipient of this receipt. It should match the receipt type.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='receipts', to='afip.clientvatcondition', verbose_name='client vat condition'),
        ),
    ]
