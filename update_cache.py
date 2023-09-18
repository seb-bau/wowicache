import os
import logging
import sys
import graypy
from dotenv import dotenv_values
from wowipy.wowipy import WowiPy
from datetime import datetime
from db_functions import cache_to_db

OPMODE_DB = 1
OPMODE_FILE = 2

ENBUILDINGS = 1
ENCONTRACTORS = 2
ENPERSONS = 3
ENECONOMICUNITS = 4
ENCONTRACTS = 5
ENUSEUNITS = 6


def cache_to_file(entities_enabled: list, entity_filenames: dict, wowicon: WowiPy):
    base_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "cache")

    if ENBUILDINGS in entities_enabled:
        logger.info("Hole Building-Cache...")
        wowicon.build_building_land_cache()
        dest_file = os.path.join(base_path, entity_filenames.get(ENBUILDINGS))
        logger.info(f"Schreibe Building-Cache in Datei {dest_file}")
        wowicon.cache_to_disk(cache_type=wowi.CACHE_BUILDING_LANDS, file_name=dest_file)

    if ENCONTRACTORS in entities_enabled:
        logger.info("Hole Contractor-Cache...")
        wowicon.build_contractor_cache()
        dest_file = os.path.join(base_path, entity_filenames.get(ENCONTRACTORS))
        logger.info(f"Schreibe Contractor-Cache in Datei {dest_file}")
        wowicon.cache_to_disk(cache_type=wowi.CACHE_CONTRACTORS, file_name=dest_file)

    if ENPERSONS in entities_enabled:
        logger.info("Hole Person-Cache...")
        wowicon.build_person_cache()
        dest_file = os.path.join(base_path, entity_filenames.get(ENPERSONS))
        logger.info(f"Schreibe Person-Cache in Datei {dest_file}")
        wowicon.cache_to_disk(cache_type=wowi.CACHE_PERSONS, file_name=dest_file)

    if ENECONOMICUNITS in entities_enabled:
        logger.info("Hole Economic-Unit-Cache...")
        wowicon.build_economic_unit_cache()
        dest_file = os.path.join(base_path, entity_filenames.get(ENECONOMICUNITS))
        logger.info(f"Schreibe Economic-Unit-Cache in Datei {dest_file}")
        wowicon.cache_to_disk(cache_type=wowi.CACHE_ECONOMIC_UNITS, file_name=dest_file)

    if ENCONTRACTS in entities_enabled:
        logger.info("Hole License-Agreement-Cache...")
        wowicon.build_license_agreement_cache()
        dest_file = os.path.join(base_path, entity_filenames.get(ENCONTRACTS))
        logger.info(f"Schreibe License-Agreement-Cache in Datei {dest_file}")
        wowicon.cache_to_disk(cache_type=wowi.CACHE_LICENSE_AGREEMENTS, file_name=dest_file)

    if ENUSEUNITS in entities_enabled:
        logger.info("Hole Use-Unit-Cache...")
        wowicon.build_use_unit_cache()
        dest_file = os.path.join(base_path, entity_filenames.get(ENUSEUNITS))
        logger.info(f"Schreibe Use-Unit-Cache in Datei {dest_file}")
        wowicon.cache_to_disk(cache_type=wowi.CACHE_USE_UNITS, file_name=dest_file)


def handle_unhandled_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.critical("Unhandled exception", exc_info=(exc_type, exc_value, exc_traceback))


settings = dotenv_values(os.path.join(os.path.abspath(os.path.dirname(__file__)), '.env'))
log_method = settings.get("log_method", "file").lower()
log_level = settings.get("log_level", "info").lower()
enable_exception_catcher_str = settings.get("enable_exception_catcher")
if enable_exception_catcher_str is None or enable_exception_catcher_str != "true":
    enable_exception_catcher = False
else:
    enable_exception_catcher = True
logger = logging.getLogger(__name__)
log_levels = {'debug': 10, 'info': 20, 'warning': 30, 'error': 40, 'critical': 50}
logger.setLevel(log_levels.get(log_level, 20))
if enable_exception_catcher:
    sys.excepthook = handle_unhandled_exception

if log_method == "file":
    log_file_name = f"wowicache_{datetime.now().strftime('%Y_%m_%d')}.log"
    log_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "log", log_file_name)

    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        filename=log_path,
                        filemode='a')

elif log_method == "graylog":
    graylog_host = settings.get("graylog_host", "127.0.0.1")
    graylog_port = int(settings.get("graylog_port", 12201))
    handler = graypy.GELFUDPHandler(graylog_host, graylog_port)
    logger.addHandler(handler)

logger.info("Wowicache gestartet.")

wowi_host = settings.get("wowi_host")
wowi_user = settings.get("wowi_user")
wowi_pass = settings.get("wowi_pass")
wowi_key = settings.get("wowi_key")

opmode = OPMODE_FILE
db_connection = settings.get("db_connection_string")
str_output_mode = settings.get("output_mode")
if str_output_mode is not None and str_output_mode.lower() == "db":
    opmode = OPMODE_DB
if opmode == OPMODE_FILE:
    logger.debug("OpMode: File")
else:
    logger.debug("OpMode: Database")

str_en_buildings = settings.get("enable_buildings")
str_en_contractors = settings.get("enable_contractors")
str_en_persons = settings.get("enable_persons")
str_en_economic_units = settings.get("enable_economic_units")
str_en_license_agreements = settings.get("enable_license_agreements")
str_en_use_units = settings.get("enable_use_units")

filenames = {
    ENBUILDINGS: settings.get("filename_buildings"),
    ENCONTRACTORS: settings.get("filename_contractors"),
    ENPERSONS: settings.get("filename_persons"),
    ENECONOMICUNITS: settings.get("filename_economic_units"),
    ENCONTRACTS: settings.get("filename_license_agreements"),
    ENUSEUNITS: settings.get("filename_use_units")
}

user_agent = settings.get("user_agent")
if user_agent is None or len(user_agent.strip()) == 0:
    user_agent = "WowiCache/1.0"

enabled_entities = []
if str_en_buildings is not None and str_en_buildings.lower() == "true":
    enabled_entities.append(ENBUILDINGS)
if str_en_contractors is not None and str_en_contractors.lower() == "true":
    enabled_entities.append(ENCONTRACTORS)
if str_en_persons is not None and str_en_persons.lower() == "true":
    enabled_entities.append(ENPERSONS)
if str_en_economic_units is not None and str_en_economic_units.lower() == "true":
    enabled_entities.append(ENECONOMICUNITS)
if str_en_license_agreements is not None and str_en_license_agreements.lower() == "true":
    enabled_entities.append(ENCONTRACTS)
if str_en_use_units is not None and str_en_use_units.lower() == "true":
    enabled_entities.append(ENUSEUNITS)

wowi = WowiPy(hostname=wowi_host, user=wowi_user,
              password=wowi_pass, api_key=wowi_key,
              user_agent=user_agent)

if opmode == OPMODE_FILE:
    cache_to_file(entities_enabled=enabled_entities, entity_filenames=filenames, wowicon=wowi)
else:
    cache_to_db(connection_string=db_connection, entities=enabled_entities, wowicon=wowi)

logger.info("Lauf abgeschlossen.")
