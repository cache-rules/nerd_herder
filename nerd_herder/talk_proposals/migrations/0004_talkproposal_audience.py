# Generated by Django 2.2 on 2019-06-04 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talk_proposals', '0003_audiencechoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='talkproposal',
            name='audience',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='talk_proposals.AudienceChoice'),
        ),
    ]
