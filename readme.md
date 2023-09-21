# WowiCache
### WOWIPORT OPENWOWI API SqlAlchemy Overlay
### Allgemein
Dieses Paket ermöglicht den Aufbau eines lokalen Caches aus [OPENWOWI](https://docs.openwowi.de/grundlagen/eine-kurze-vorstellung-der-openwowi)-Daten. Der Cache baut sich
mit Hilfe des [WowiPy-Moduls](https://docs.openwowi.de/grundlagen/eine-kurze-vorstellung-der-openwowi) auf.
Bitte klären Sie vor Benutzung dieses Moduls, ob Ihr geplanter Anwendungszweck im Rahmen der [Nutzungsbedingungen](https://docs.openwowi.de/nutzungsbedingungen-impressum-und-kontakt) Dr. Klein Wowi Digital AG erlaubt ist.

### Warum eigentlich?
Der bevorzugte Anwendungsfall ist sicherlich die direkte Abfrage von Datensätzen aus OPENWOWI. Aktuell ist jedoch eine Abfrage, wie "Welche Person gehört zu dieser Telefonnummer" oder "Gib mir alle Gebäude der X-Str." nicht direkt möglich. Diese Funktionslücke wird mit
diesem Modul geschlossen, da man nach Aufbau des Caches entweder direkt in der erzeugten Datenbank arbeiten oder das vereinfachte DB-Modell  nutzen kann.

### Installation
````
pip install wowicache
````

### Funktionen aktuell
* Ablage der Daten diverser OPENWOWI-Endpunkte in eine SQLAlchemy-kompatible Datenbank (MySQL, MariaDB, sqlite, Postgres, ...)
* Abfrage der Daten in einem vereinfachten Objektmodell mit Rückwärtssuche (siehe Beispiel)


### Anwendungsbeispiel
Cache aufbauen und Gebäude daraus auslesen, die in der Teststr. liegen
````
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
````
