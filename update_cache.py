import os
import logging
import sys
import graypy
from dotenv import dotenv_values
from wowipy.wowipy import WowiPy
from datetime import datetime


def handle_unhandled_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logger.critical("Unhandled exception", exc_info=(exc_type, exc_value, exc_traceback))


settings = dotenv_values(os.path.join(os.path.abspath(os.path.dirname(__file__)), '.env'))
log_method = settings.get("log_method", "file").lower()
log_level = settings.get("log_level", "info").lower()
logger = logging.getLogger(__name__)
log_levels = {'debug': 10, 'info': 20, 'warning': 30, 'error': 40, 'critical': 50}
logger.setLevel(log_levels.get(log_level, 20))
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

str_en_buildings = settings.get("enable_buildings")
str_en_contractors = settings.get("enable_contractors")
str_en_persons = settings.get("enable_persons")
str_en_economic_units = settings.get("enable_economic_units")
str_en_license_agreements = settings.get("enable_license_agreements")
str_en_use_units = settings.get("enable_use_units")

filename_buildings = settings.get("filename_buildings")
filename_contractors = settings.get("filename_contractors")
filename_persons = settings.get("filename_persons")
filename_economic_units = settings.get("filename_economic_units")
filename_license_agreements = settings.get("filename_license_agreements")
filename_use_units = settings.get("filename_use_units")


if str_en_buildings is not None and str_en_buildings.lower() == "true":
    enable_buildings = True
else:
    enable_buildings = False

if str_en_contractors is not None and str_en_contractors.lower() == "true":
    enable_contractors = True
else:
    enable_contractors = False

if str_en_persons is not None and str_en_persons.lower() == "true":
    enable_persons = True
else:
    enable_persons = False

if str_en_economic_units is not None and str_en_economic_units.lower() == "true":
    enable_economic_units = True
else:
    enable_economic_units = False

if str_en_license_agreements is not None and str_en_license_agreements.lower() == "true":
    enable_license_agreements = True
else:
    enable_license_agreements = False

if str_en_use_units is not None and str_en_use_units.lower() == "true":
    enable_use_units = True
else:
    enable_use_units = False


wowi = WowiPy(hostname=wowi_host, user=wowi_user,
              password=wowi_pass, api_key=wowi_key)

base_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "cache")

if enable_buildings:
    logger.info("Hole Building-Cache...")
    wowi.build_building_land_cache()
    dest_file = os.path.join(base_path, filename_buildings)
    logger.info(f"Schreibe Building-Cache in Datei {dest_file}")
    wowi.cache_to_disk(cache_type=wowi.CACHE_BUILDING_LANDS, file_name=dest_file)

if enable_contractors:
    logger.info("Hole Contractor-Cache...")
    wowi.build_contractor_cache()
    dest_file = os.path.join(base_path, filename_contractors)
    logger.info(f"Schreibe Contractor-Cache in Datei {dest_file}")
    wowi.cache_to_disk(cache_type=wowi.CACHE_CONTRACTORS, file_name=dest_file)

if enable_persons:
    logger.info("Hole Person-Cache...")
    wowi.build_person_cache()
    dest_file = os.path.join(base_path, filename_persons)
    logger.info(f"Schreibe Person-Cache in Datei {dest_file}")
    wowi.cache_to_disk(cache_type=wowi.CACHE_PERSONS, file_name=dest_file)

if enable_economic_units:
    logger.info("Hole Economic-Unit-Cache...")
    wowi.build_economic_unit_cache()
    dest_file = os.path.join(base_path, filename_economic_units)
    logger.info(f"Schreibe Economic-Unit-Cache in Datei {dest_file}")
    wowi.cache_to_disk(cache_type=wowi.CACHE_ECONOMIC_UNITS, file_name=dest_file)

if enable_license_agreements:
    logger.info("Hole License-Agreement-Cache...")
    wowi.build_license_agreement_cache()
    dest_file = os.path.join(base_path, filename_license_agreements)
    logger.info(f"Schreibe License-Agreement-Cache in Datei {dest_file}")
    wowi.cache_to_disk(cache_type=wowi.CACHE_LICENSE_AGREEMENTS, file_name=dest_file)

if enable_use_units:
    logger.info("Hole Use-Unit-Cache...")
    wowi.build_use_unit_cache()
    dest_file = os.path.join(base_path, filename_use_units)
    logger.info(f"Schreibe Use-Unit-Cache in Datei {dest_file}")
    wowi.cache_to_disk(cache_type=wowi.CACHE_USE_UNITS, file_name=dest_file)

logger.info("Lauf abgeschlossen.")
