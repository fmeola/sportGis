import os
from django.contrib.gis.utils import LayerMapping
from twitterPolling.models import States,states_mapping


world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'pxdptodatos.shp'))

#Load the shape into the db
def run(verbose=True):
    lm = LayerMapping(States, world_shp, states_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
