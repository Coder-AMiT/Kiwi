# Generated by Django 2.0.1 on 2018-01-26 12:51
# Removes movels which are not used anywhere and are
# somewhat duplicated by TCMSEnv{Group,Property,Value} models
# which are in active use

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_update_tcmsenvvalue_ordering'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testenvironment',
            name='product',
        ),
        migrations.AlterIndexTogether(
            name='testenvironmentcategory',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='testenvironmentcategory',
            name='product',
        ),
        migrations.RemoveField(
            model_name='testenvironmentelement',
            name='env_category',
        ),
        migrations.RemoveField(
            model_name='testenvironmentelement',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='testenvironmentmap',
            name='element',
        ),
        migrations.RemoveField(
            model_name='testenvironmentmap',
            name='environment',
        ),
        migrations.RemoveField(
            model_name='testenvironmentmap',
            name='property',
        ),
        migrations.RemoveField(
            model_name='testenvironmentproperty',
            name='element',
        ),
        migrations.DeleteModel(
            name='TestEnvironment',
        ),
        migrations.DeleteModel(
            name='TestEnvironmentCategory',
        ),
        migrations.DeleteModel(
            name='TestEnvironmentElement',
        ),
        migrations.DeleteModel(
            name='TestEnvironmentMap',
        ),
        migrations.DeleteModel(
            name='TestEnvironmentProperty',
        ),
    ]
