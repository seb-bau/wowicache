from wowicache.models import WowiCache, Building
from wowicache import update_cache
from dotenv import dotenv_values
import os

env_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.env')
settings = dotenv_values(env_file)

cache = WowiCache(settings.get("db_connection_string"))
update_cache.cache_to_db(env_file)

buildings = cache.session.query(Building).filter(Building.street.like('%Teststr%'))
for building in buildings:
    print(building.building_type_name)
    print(building.street_complete)
