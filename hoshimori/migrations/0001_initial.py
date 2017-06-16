# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import multiselectfield.db.fields
from django.conf import settings
import hoshimori.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation', models.DateTimeField(auto_now_add=True, verbose_name='Join Date')),
                ('start_date', models.DateField(help_text='When you started playing with this account.', null=True, verbose_name='Start Date')),
                ('level', models.PositiveIntegerField(null=True, verbose_name='Level', db_index=True)),
                ('nickname', models.CharField(max_length=100, verbose_name='Nickname')),
                ('game_id', models.CharField(max_length=8, verbose_name='Game ID')),
                ('device', models.CharField(max_length=150, verbose_name='Device')),
                ('i_os', models.PositiveIntegerField(default=0, verbose_name='Operating System', choices=[(0, b'iOs'), (1, b'Android')])),
                ('i_player_type', models.PositiveIntegerField(default=0, verbose_name='Player type', choices=[(0, b'Free-to-play'), (1, b'Pay-to-win'), (2, b'FTP PTW Hybrid')])),
                ('owner', models.ForeignKey(related_name='accounts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActionSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Action Skill')),
                ('japanese_name', models.CharField(max_length=100, verbose_name='Action Skill (Japanese)')),
                ('damage', models.CharField(max_length=200, verbose_name='Skill Damage')),
                ('combo', models.PositiveIntegerField(default=13, verbose_name='Skill Combo')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActionSkillEffect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('i_name', models.PositiveIntegerField(null=True, verbose_name='Action Skill Effect')),
                ('bonus_value', models.PositiveIntegerField(null=True, verbose_name='Effect Value')),
                ('duration', models.PositiveIntegerField(null=True, verbose_name='Effect Duration')),
                ('skill_affinity', models.PositiveIntegerField(default=1, null=True, verbose_name='Skill Affinity', choices=[(0, b''), (1, b'Ignore weapon affinity'), (2, b'Ignore conflicting weapon affinity')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID', db_index=True)),
                ('i_rarity', models.PositiveIntegerField(verbose_name='Rarity', choices=[(0, '\u2605'), (1, '\u2605\u2605'), (2, '\u2605\u2605\u2605'), (3, '\u2605\u2605\u2605\u2605'), (4, '\u2605\u2605\u2605\u2605\u2605')])),
                ('i_weapon', models.PositiveIntegerField(verbose_name='Weapon', choices=[(0, 'Sword'), (1, 'Spear'), (2, 'Hammer'), (3, 'Gun'), (4, 'Rod'), (5, 'Gunblade'), (6, 'Twin Barrett')])),
                ('name', models.CharField(max_length=100, verbose_name='Title')),
                ('japanese_name', models.CharField(max_length=100, verbose_name='Title (Japanese)')),
                ('image', models.ImageField(upload_to=hoshimori.models.uploadItem(b'c'), verbose_name='Image')),
                ('art', models.ImageField(upload_to=hoshimori.models.uploadItem(b'c/art'), verbose_name='Art')),
                ('transparent', models.ImageField(upload_to=hoshimori.models.uploadItem(b'c/transparent'), verbose_name='Transparent')),
                ('subcard_effect', models.BooleanField(default=False, verbose_name='Subcard Effect')),
                ('card_type', models.PositiveIntegerField(verbose_name='Card Type', choices=[(0, 'Normal'), (1, 'Extra'), (2, 'Subcard')])),
                ('hp_1', models.PositiveIntegerField(default=0, verbose_name='HP (Level 1)')),
                ('hp_50', models.PositiveIntegerField(default=0, verbose_name='HP (Level 50)')),
                ('hp_70', models.PositiveIntegerField(default=0, verbose_name='HP (Level 70)')),
                ('sp_1', models.PositiveIntegerField(default=0, verbose_name='SP (Level 1)')),
                ('sp_50', models.PositiveIntegerField(default=0, verbose_name='SP (Level 50)')),
                ('sp_70', models.PositiveIntegerField(default=0, verbose_name='SP (Level 70)')),
                ('atk_1', models.PositiveIntegerField(default=0, verbose_name='ATK (Level 1)')),
                ('atk_50', models.PositiveIntegerField(default=0, verbose_name='ATK (Level 50)')),
                ('atk_70', models.PositiveIntegerField(default=0, verbose_name='ATK (Level 70)')),
                ('def_1', models.PositiveIntegerField(default=0, verbose_name='DEF (Level 1)')),
                ('def_50', models.PositiveIntegerField(default=0, verbose_name='DEF (Level 50)')),
                ('def_70', models.PositiveIntegerField(default=0, verbose_name='DEF (Level 70)')),
                ('skill_name', models.CharField(max_length=100, verbose_name='Skill name')),
                ('japanese_skill_name', models.CharField(max_length=100, verbose_name='Skill name (Japanese)')),
                ('skill_SP', models.PositiveIntegerField(default=0, verbose_name='Skill SP')),
                ('skill_hits', models.PositiveIntegerField(default=0, verbose_name='Skill hits')),
                ('skill_range', models.CharField(max_length=300, verbose_name='Skill range')),
                ('skill_comment', models.CharField(max_length=1000, verbose_name='Skill comment')),
                ('max_damage', models.PositiveIntegerField(default=0, verbose_name='Max damage')),
                ('nakayoshi_title', models.CharField(max_length=100, verbose_name='Passive Skill')),
                ('japanese_nakayoshi_title', models.CharField(max_length=100, verbose_name='Passive Skill (Japanese)')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=hoshimori.models.uploadItem(b'e'), verbose_name='Image')),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name')),
                ('japanese_name', models.CharField(unique=True, max_length=100, verbose_name='Name (Japanese)')),
                ('start_date', models.DateTimeField(null=True, verbose_name='Beginning')),
                ('end_date', models.DateTimeField(null=True, verbose_name='End')),
                ('owner', models.ForeignKey(related_name='added_events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Irousu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.PositiveIntegerField(unique=True, null=True, verbose_name='Irousu type', choices=[(0, 'Gel'), (1, 'Rouga'), (2, 'Quinn'), (3, 'Eel'), (4, 'Shum'), (5, 'Draco'), (6, 'Doguu'), (7, 'Spirit'), (8, 'Saiki'), (9, 'Machinery'), (10, 'Valiant'), (11, 'Unknown')])),
                ('weak', multiselectfield.db.fields.MultiSelectField(default=b'', max_length=100, verbose_name='Weak', choices=[(0, 'Sword'), (1, 'Spear'), (2, 'Hammer'), (3, 'Gun'), (4, 'Rod'), (5, 'Gunblade'), (6, 'Twin Barrett')])),
                ('strong', multiselectfield.db.fields.MultiSelectField(default=b'', max_length=100, verbose_name='Strong', choices=[(0, 'Sword'), (1, 'Spear'), (2, 'Hammer'), (3, 'Gun'), (4, 'Rod'), (5, 'Gunblade'), (6, 'Twin Barrett')])),
                ('guard', multiselectfield.db.fields.MultiSelectField(default=b'', max_length=100, verbose_name='Guard', choices=[(0, 'Sword'), (1, 'Spear'), (2, 'Hammer'), (3, 'Gun'), (4, 'Rod'), (5, 'Gunblade'), (6, 'Twin Barrett')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IrousuVariation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='Irousu Name')),
                ('japanese_name', models.CharField(max_length=50, verbose_name='Irousu Name (Japanese)')),
                ('image', models.ImageField(upload_to=hoshimori.models.uploadItem(b'i'), verbose_name='Image')),
                ('species', models.ForeignKey(related_name='species', on_delete=django.db.models.deletion.SET_NULL, to='hoshimori.Irousu', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50, verbose_name='Material name')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nakayoshi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('i_name', models.PositiveIntegerField(null=True, verbose_name='Nakayoshi skill', choices=[(0, 'ATK'), (1, 'HP'), (2, 'SP'), (3, 'Damage'), (4, 'Combo Damage'), (5, 'SP Consumption'), (6, 'Skill Combo'), (7, 'Movement Rate'), (8, 'Dodge'), (9, 'Auto Reload'), (10, 'Bullet'), (11, 'Item Recovery Range'), (12, 'Item Drop Quantity'), (13, 'Coin'), (14, 'Cheerpoint'), (15, 'EXP'), (16, 'Bond Point'), (17, 'Guard Penetration'), (18, 'Received Damage'), (19, 'Null SP Damage'), (20, 'Null Slow'), (21, 'Null Paralysis'), (22, 'Null Skill Seal'), (23, 'Null Poison')])),
                ('positive_effect', models.BooleanField(default=True, verbose_name='Positive Effect')),
                ('effect_level', models.PositiveIntegerField(default=0, null=True, verbose_name='Effect Level', blank=True, choices=[(0, b'Small'), (1, b'Medium'), (2, b'Large'), (3, b'Super')])),
                ('bonus_value', models.PositiveIntegerField(null=True, verbose_name='Effect Value')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='Stage')),
                ('episode', models.PositiveIntegerField(null=True, verbose_name='Episode')),
                ('number', models.PositiveIntegerField(null=True, verbose_name='Stage number')),
                ('irousu', models.ManyToManyField(related_name='stage_with_irousu', null=True, to='hoshimori.IrousuVariation')),
                ('materials', models.ManyToManyField(related_name='stage_with_drops', null=True, to='hoshimori.Material')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StageDifficulty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('difficulty', models.PositiveIntegerField(null=True, verbose_name='Difficulty', choices=[(0, b'Easy'), (1, b'Normal'), (2, b'Hard')])),
                ('level', models.PositiveIntegerField(null=True, verbose_name='Level')),
                ('exp', models.PositiveIntegerField(null=True, verbose_name='EXP')),
                ('coins', models.PositiveIntegerField(null=True, verbose_name='Coins')),
                ('cheerpoints', models.PositiveIntegerField(null=True, verbose_name='Cheerpoints')),
                ('objectives', models.CharField(max_length=200, verbose_name='Objectives')),
                ('stage', models.ForeignKey(related_name='difficulties', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Stage', to='hoshimori.Stage', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name (romaji)')),
                ('japanese_name', models.CharField(max_length=100, verbose_name='Name (Japanese)')),
                ('unlock', models.CharField(default=b'', max_length=100, verbose_name='Unlock at')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('i_school_year', models.PositiveIntegerField(null=True, verbose_name='School year', choices=[(0, 'Middle School Year 1'), (1, 'Middle School Year 2'), (2, 'Middle School Year 3'), (3, 'High School Year 1'), (4, 'High School Year 2'), (5, 'High School Year 3')])),
                ('birthday', models.DateField(null=True, verbose_name='Birthday')),
                ('i_star_sign', models.PositiveIntegerField(null=True, verbose_name='Star sign', choices=[(0, 'Leo'), (1, 'Aries'), (2, 'Libra'), (3, 'Virgo'), (4, 'Scorpio'), (5, 'Capricorn'), (6, 'Pisces'), (7, 'Gemini'), (8, 'Cancer'), (9, 'Sagittarius'), (10, 'Aquarius'), (11, 'Taurus')])),
                ('i_blood_type', models.PositiveIntegerField(null=True, verbose_name='Blood type', choices=[(0, b'O'), (1, b'A'), (2, b'B'), (3, b'AB')])),
                ('extra_activity', models.CharField(max_length=100, verbose_name='Extracurricular activity')),
                ('catchphrase_1', models.CharField(max_length=100, verbose_name='Catchphrase 1')),
                ('catchphrase_2', models.CharField(max_length=100, verbose_name='Catchphrase 2')),
                ('height', models.PositiveIntegerField(help_text=b'in cm', null=True, verbose_name='Height')),
                ('weight', models.PositiveIntegerField(help_text=b'in kg', null=True, verbose_name='Weight')),
                ('bust', models.PositiveIntegerField(help_text=b'in cm', null=True, verbose_name='Bust')),
                ('waist', models.PositiveIntegerField(help_text=b'in cm', null=True, verbose_name='Waist')),
                ('hip', models.PositiveIntegerField(help_text=b'in cm', null=True, verbose_name='Hip')),
                ('hobby_1', models.CharField(max_length=100, verbose_name='Hobby 1')),
                ('hobby_2', models.CharField(max_length=100, verbose_name='Hobby 2')),
                ('hobby_3', models.CharField(max_length=100, verbose_name='Hobby 3')),
                ('food_likes', models.CharField(max_length=100, verbose_name='Liked food')),
                ('food_dislikes', models.CharField(max_length=100, verbose_name='Disliked food')),
                ('family', models.CharField(max_length=100, verbose_name='Family members')),
                ('dream', models.CharField(max_length=100, verbose_name='Dream job')),
                ('ideal_1', models.CharField(max_length=100, verbose_name='Ideal person 1')),
                ('ideal_2', models.CharField(max_length=100, verbose_name='Ideal person 2')),
                ('ideal_3', models.CharField(max_length=100, verbose_name='Ideal person 3')),
                ('pastime', models.CharField(max_length=100, verbose_name='Pastime')),
                ('destress', models.CharField(max_length=100, verbose_name='Destress')),
                ('fav_memory', models.CharField(max_length=100, verbose_name='Favorite memory')),
                ('fav_phrase', models.CharField(max_length=100, verbose_name='Favorite phrase')),
                ('secret', models.CharField(max_length=5000, verbose_name='Secret')),
                ('CV', models.CharField(help_text=b'In Japanese characters.', max_length=100, verbose_name='CV')),
                ('romaji_CV', models.CharField(help_text=b'In romaji.', max_length=100, verbose_name='CV')),
                ('image', models.ImageField(upload_to=hoshimori.models.uploadItem(b's'), verbose_name='Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('japanese_name', models.CharField(max_length=100, verbose_name='Name (Japanese)')),
                ('image', models.ImageField(upload_to=hoshimori.models.uploadItem(b'w'), verbose_name='Icon')),
                ('i_type', models.PositiveIntegerField(verbose_name='Weapon', choices=[(0, 'Sword'), (1, 'Spear'), (2, 'Hammer'), (3, 'Gun'), (4, 'Rod'), (5, 'Gunblade'), (6, 'Twin Barrett')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeaponEffect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('i_name', models.PositiveIntegerField(null=True, verbose_name='Weapon Effect')),
                ('positive_effect', models.BooleanField(default=True, verbose_name='Positive Effect')),
                ('effect_level', models.PositiveIntegerField(null=True, verbose_name='Effect Level')),
                ('bonus_value', models.PositiveIntegerField(null=True, verbose_name='Effect Value')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WeaponUpgrade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rhythm', models.ImageField(upload_to=hoshimori.models.uploadItem(b'w/rhythm'), verbose_name='Rhythm')),
                ('i_level', models.PositiveIntegerField(default=0, null=True, verbose_name='Upgrade Level', choices=[(0, b''), (1, 'Alpha'), (2, 'Beta'), (3, 'Gamma')])),
                ('gamma_type', models.CharField(default=b'', max_length=1, verbose_name='Gamma Type')),
                ('i_rarity', models.PositiveIntegerField(default=0, verbose_name='Rarity', choices=[(0, '\u2605'), (1, '\u2605\u2605'), (2, '\u2605\u2605\u2605'), (3, '\u2605\u2605\u2605\u2605'), (4, '\u2605\u2605\u2605\u2605\u2605')])),
                ('atk_min', models.PositiveIntegerField(default=0, verbose_name='Weapon ATK (Minimum)')),
                ('atk_max', models.PositiveIntegerField(default=0, verbose_name='Weapon ATK (Maximum)')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Price')),
                ('materials', models.ManyToManyField(related_name='weapon_with_materials_needed', null=True, to='hoshimori.Material')),
                ('origin', models.ForeignKey(related_name='upgrade', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Weapon', to='hoshimori.Weapon', null=True)),
                ('owner', models.ForeignKey(related_name='added_weapons', to=settings.AUTH_USER_MODEL)),
                ('subweapon_effects', models.ManyToManyField(related_name='subweapon_with_skills', null=True, to='hoshimori.WeaponEffect')),
                ('weapon_effects', models.ManyToManyField(related_name='weapon_with_skills', null=True, to='hoshimori.WeaponEffect')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='card',
            name='action_skill',
            field=models.ForeignKey(related_name='skill', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Action Skill', to='hoshimori.Weapon', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='evolved_action_skill',
            field=models.ForeignKey(related_name='evolved skill', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Evolved Action Skill', to='hoshimori.Weapon', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='evolved_nakayoshi_skills',
            field=models.ManyToManyField(default=None, related_name='card_with_nakayoshi_evolved', null=True, to='hoshimori.Nakayoshi'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='nakayoshi_skills',
            field=models.ManyToManyField(related_name='card_with_nakayoshi', to='hoshimori.Nakayoshi'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='owner',
            field=models.ForeignKey(related_name='added_cards', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='card',
            name='student',
            field=models.ForeignKey(related_name='cards', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Student', to='hoshimori.Student', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='actionskill',
            name='effects',
            field=models.ManyToManyField(related_name='skills_with_effect', null=True, to='hoshimori.ActionSkillEffect'),
            preserve_default=True,
        ),
    ]