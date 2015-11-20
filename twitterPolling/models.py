from django.contrib.gis.db import models

class States(models.Model):
    toponimo_i = models.IntegerField()
    nombre = models.CharField(max_length=254)
    link = models.CharField(max_length=254)
    varones = models.FloatField()
    mujeres = models.FloatField()
    tot_pob = models.FloatField()
    hogares = models.FloatField()
    viv_part = models.FloatField()
    viv_part_h = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()
    equipo = 0
    

# Auto-generated `LayerMapping` dictionary for States model
states_mapping = {
    'toponimo_i' : 'toponimo_i',
    'nombre' : 'nombre',
    'link' : 'link',
    'varones' : 'varones',
    'mujeres' : 'mujeres',
    'tot_pob' : 'tot_pob',
    'hogares' : 'hogares',
    'viv_part' : 'viv_part',
    'viv_part_h' : 'viv_part_h',
    'equipo' : 'equipo',
    'geom' : 'MULTIPOLYGON',
}