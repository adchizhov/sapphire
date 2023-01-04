import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


def forwards_func(apps, schema_editor):
    PointCategory = apps.get_model("points", "PointCategory")
    db_alias = schema_editor.connection.alias
    PointCategory.objects.using(db_alias).create(name='Hazard')
    PointCategory.objects.using(db_alias).create(name='Shelter')


def reverse_func(apps, schema_editor):
    PointCategory = apps.get_model("points", "PointCategory")
    db_alias = schema_editor.connection.alias
    PointCategory.objects.using(db_alias).filter(name__in=['Hazard', 'Shelter']).delete()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='point title')),
                ('description', models.CharField(max_length=256, verbose_name='point description')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PointCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='site name')),
            ],
        ),
        migrations.AddIndex(
            model_name='pointcategory',
            index=models.Index(fields=['name'], name='name_idx'),
        ),
        migrations.AddField(
            model_name='point',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='points.pointcategory'),
        ),
        migrations.AddIndex(
            model_name='point',
            index=models.Index(fields=['title'], name='points_title_idx'),
        ),
        migrations.RunPython(forwards_func, reverse_func),
    ]
