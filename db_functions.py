from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from wowipy.wowipy import WowiPy
from models import Base, EconomicUnit, District, Building, UseUnit
from datetime import datetime

ENBUILDINGS = 1
ENCONTRACTORS = 2
ENPERSONS = 3
ENECONOMICUNITS = 4
ENCONTRACTS = 5
ENUSEUNITS = 6


def cache_to_db(connection_string: str, entities: list, wowicon: WowiPy):
    engine = create_engine(connection_string, echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    if ENECONOMICUNITS in entities or ENBUILDINGS in entities:
        session.query(District).delete()
        session.commit()
        districts = wowicon.get_districts()
        for entry in districts:
            new_entry = District(internal_id=entry.id_,
                                 name=entry.name)
            session.add(new_entry)
        session.commit()

    if ENECONOMICUNITS in entities:
        session.query(EconomicUnit).delete()
        session.commit()
        economic_units = wowicon.get_economic_units(fetch_all=True)
        for entry in economic_units:
            district_id = entry.district.id_ if entry.district else None
            new_entry = EconomicUnit(internal_id=entry.id_,
                                     id_num=entry.id_num,
                                     company_id=entry.company_code.id_,
                                     name=entry.name,
                                     location=entry.location,
                                     construction_year=entry.construction_year,
                                     info=entry.info,
                                     owner_id=entry.owner.id_,
                                     district_id=district_id)
            session.add(new_entry)
        session.commit()

    if ENBUILDINGS in entities:
        session.query(Building).delete()
        session.commit()
        buildings = wowicon.get_building_lands(fetch_all=True)
        for entry in buildings:
            district_id = entry.building.district.id_ if entry.building.district else None
            move_in_date = datetime.strptime(str(entry.building.move_in_date), "%Y-%m-%d") \
                if entry.building.move_in_date else None
            entry_date = datetime.strptime(str(entry.entry_date), "%Y-%m-%d") \
                if entry.entry_date else None
            new_entry = Building(internal_id=entry.id_,
                                 id_num=entry.id_num,
                                 company_id=entry.company_code.id_,
                                 building_land_type=entry.building_land_type,
                                 entry_date=entry_date,
                                 economic_unit_id=entry.economic_unit.id_,
                                 postcode=entry.estate_address.street,
                                 town=entry.estate_address.town,
                                 street=entry.estate_address.street,
                                 house_number=entry.estate_address.house_number,
                                 house_number_addition=entry.estate_address.house_number_addition,
                                 country_id=entry.estate_address.country_id,
                                 country=entry.estate_address.country_code,
                                 street_complete=entry.estate_address.street_complete,
                                 house_number_complete=entry.estate_address.house_number_complete,
                                 construction_year=entry.building.construction_year,
                                 move_in_date=move_in_date,
                                 building_type_id=entry.building.building_type.id_,
                                 district_id=district_id)
            session.add(new_entry)
        session.commit()

    if ENUSEUNITS in entities:
        session.query(UseUnit).delete()
        session.commit()
        use_units = wowicon.get_use_units(fetch_all=True)
        for entry in use_units:
            move_in_date = datetime.strptime(str(entry.move_in_date), "%Y-%m-%d") \
                if entry.move_in_date else None
            entry_date = datetime.strptime(str(entry.entry_date), "%Y-%m-%d") \
                if entry.entry_date else None
            exit_date = datetime.strptime(str(entry.exit_date), "%Y-%m-%d") \
                if entry.exit_date else None
            management_start = datetime.strptime(str(entry.management_start), "%Y-%m-%d") \
                if entry.management_start else None
            management_end = datetime.strptime(str(entry.management_end), "%Y-%m-%d") \
                if entry.management_end else None
            financing_type_id = entry.financing_type.id_ if entry.financing_type else None
            financing_type = entry.financing_type.name if entry.financing_type else None

            position_id = entry.position.id_ if entry.position else None
            position = entry.position.name if entry.position else None

            floor_id = entry.floor.id_ if entry.floor else None
            floor_name = entry.floor.name if entry.floor else None
            floor_level = entry.floor.level_to_ground if entry.floor else None
            new_entry = UseUnit(internal_id=entry.id_,
                                id_num=entry.id_num,
                                company_id=entry.company_code.id_,
                                entry_date=entry_date,
                                building_id=entry.building_land.id_,
                                economic_unit_id=entry.economic_unit.id_,
                                postcode=entry.estate_address.street,
                                town=entry.estate_address.town,
                                street=entry.estate_address.street,
                                house_number=entry.estate_address.house_number,
                                house_number_addition=entry.estate_address.house_number_addition,
                                country_id=entry.estate_address.country_id,
                                country=entry.estate_address.country_code,
                                street_complete=entry.estate_address.street_complete,
                                house_number_complete=entry.estate_address.house_number_complete,
                                financing_type_id=financing_type_id,
                                financing_type=financing_type,
                                use_unit_usage_type_id=entry.current_use_unit_type.use_unit_usage_type.id_,
                                use_unit_usage_type=entry.current_use_unit_type.use_unit_usage_type.name,
                                usable_space=entry.usable_space,
                                living_space=entry.living_space,
                                heating_space=entry.heating_space,
                                number_of_rooms=entry.number_of_rooms,
                                number_of_half_rooms=entry.number_of_half_rooms,
                                description_of_position=entry.description_of_position,
                                management_start=management_start,
                                management_end=management_end,
                                move_in_date=move_in_date,
                                exit_date=exit_date,
                                position_id=position_id,
                                position=position,
                                floor_id=floor_id,
                                floor_name=floor_name,
                                floor_level=floor_level)
            session.add(new_entry)
        session.commit()

    result: EconomicUnit
    result = session.query(EconomicUnit).get(1)
    print(result.district.name)
