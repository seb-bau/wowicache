from sqlalchemy import Column, String, Integer, ForeignKey, Date, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class BuildingType(Base):
    __tablename__ = "wowi_building_types"
    internal_id = Column("internal_id", Integer, primary_key=True)
    name = Column("name", String)

    buildings = relationship('Building', back_populates='building_type')

    def __init__(self, internal_id, name):
        self.internal_id = internal_id
        self.name = name

    def __repr__(self):
        return f"BuildingType {self.name} ({self.internal_id})"


class District(Base):
    __tablename__ = "wowi_districts"
    internal_id = Column("internal_id", Integer, primary_key=True)
    name = Column("name", String)

    economic_units = relationship('EconomicUnit', back_populates='district')
    buildings = relationship('Building', back_populates='district')

    def __init__(self, internal_id, name):
        self.internal_id = internal_id
        self.name = name

    def __repr__(self):
        return f"District {self.name} ({self.internal_id})"


class EconomicUnit(Base):
    __tablename__ = "wowi_economic_units"
    internal_id = Column("internal_id", Integer, primary_key=True)
    id_num = Column("id_num", String)
    company_id = Column("company_id", Integer)
    name = Column("name", String)
    location = Column("location", String)
    construction_year = Column("construction_year", Integer, nullable=True)
    info = Column("info", String, nullable=True)
    owner_id = Column("owner_id", Integer)
    district_id = Column(Integer, ForeignKey("wowi_districts.internal_id"), nullable=True)
    district = relationship('District', back_populates='economic_units')
    buildings = relationship('Building', back_populates='economic_unit')
    use_units = relationship('UseUnit', back_populates='economic_unit')

    def __init__(self, internal_id, id_num, company_id, name, location, construction_year,
                 info, owner_id, district_id):
        self.internal_id = internal_id
        self.id_num = id_num
        self.company_id = company_id
        self.name = name
        self.location = location
        self.construction_year = construction_year
        self.info = info
        self.owner_id = owner_id
        self.district_id = district_id

    def __repr__(self):
        return f"Economic Unit Id: {self.internal_id} IdNum: {self.id_num} Name: {self.name}"


class Building(Base):
    __tablename__ = "wowi_buildings"
    internal_id = Column("internal_id", Integer, primary_key=True)
    id_num = Column("id_num", String)
    company_id = Column("company_id", Integer)
    building_land_type = Column("building_land_type", String)
    entry_date = Column("entry_date", Date)
    economic_unit_id = Column(Integer, ForeignKey("wowi_economic_units.internal_id"))
    economic_unit = relationship('EconomicUnit', back_populates='buildings')
    postcode = Column("postcode", String)
    town = Column("town", String)
    street = Column("street", String)
    house_number = Column("house_number", String)
    house_number_addition = Column("house_number_addition", String, nullable=True)
    country_id = Column("country_id", Integer)
    country = Column("country", String)
    street_complete = Column("street_complete", String)
    house_number_complete = Column("house_number_complete", String)

    construction_year = Column("construction_year", Integer, nullable=True)
    move_in_date = Column("move_in_date", Date, nullable=True)

    building_type_id = Column(Integer, ForeignKey("wowi_building_types.internal_id"))
    building_type = relationship('BuildingType', back_populates='buildings')

    district_id = Column(Integer, ForeignKey("wowi_districts.internal_id"), nullable=True)
    district = relationship('District', back_populates='buildings')

    use_units = relationship('UseUnit', back_populates='building')

    def __init__(self, internal_id, id_num, company_id, building_land_type, entry_date, economic_unit_id,
                 postcode, town, street, house_number, house_number_addition, country_id, country,
                 street_complete, house_number_complete, construction_year, move_in_date,
                 building_type_id, district_id):
        self.internal_id = internal_id
        self.id_num = id_num
        self.company_id = company_id
        self.building_land_type = building_land_type
        self.entry_date = entry_date
        self.economic_unit_id = economic_unit_id
        self.postcode = postcode
        self.town = town
        self.street = street
        self.house_number = house_number
        self.house_number_addition = house_number_addition
        self.country_id = country_id
        self.country = country
        self.street_complete = street_complete
        self.house_number_complete = house_number_complete
        self.construction_year = construction_year
        self.move_in_date = move_in_date
        self.building_type_id = building_type_id
        self.district_id = district_id

    def __repr__(self):
        return f"Building {self.id_num}, {self.street_complete}, {self.postcode} {self.town}"


class UseUnit(Base):
    __tablename__ = "wowi_use_units"
    internal_id = Column("internal_id", Integer, primary_key=True)
    id_num = Column("id_num", String)
    company_id = Column("company_id", Integer)
    building_id = Column(Integer, ForeignKey("wowi_buildings.internal_id"))
    building = relationship('Building', back_populates='use_units')
    economic_unit_id = Column(Integer, ForeignKey("wowi_economic_units.internal_id"))
    economic_unit = relationship('EconomicUnit', back_populates='use_units')
    postcode = Column("postcode", String)
    town = Column("town", String)
    street = Column("street", String)
    house_number = Column("house_number", String)
    house_number_addition = Column("house_number_addition", String, nullable=True)
    country_id = Column("country_id", Integer)
    country = Column("country", String)
    street_complete = Column("street_complete", String)
    house_number_complete = Column("house_number_complete", String)
    financing_type_id = Column("financing_type_id", Integer)
    financing_type = Column("financing_type", String)
    use_unit_usage_type_id = Column("use_unit_usage_type_id", Integer)
    use_unit_usage_type = Column("use_unit_usage_type", String)
    usable_space = Column("usable_space", Float, nullable=True)
    living_space = Column("living_space", Float, nullable=True)
    heating_space = Column("heating_space", Float, nullable=True)
    number_of_rooms = Column("number_of_rooms", Integer, nullable=True)
    number_of_half_rooms = Column("number_of_half_rooms", Integer, nullable=True)
    description_of_position = Column("position_description", String, nullable=True)
    management_start = Column("management_start", Date, nullable=True)
    management_end = Column("management_end", Date, nullable=True)
    move_in_date = Column("move_in_date", Date, nullable=True)
    exit_date = Column("exit_date", Date, nullable=True)
    entry_date = Column("entry_date", Date, nullable=True)
    position_id = Column("position_id", Integer, nullable=True)
    position = Column("position", String, nullable=True)
    floor_id = Column("floor_id", Integer, nullable=True)
    floor_name = Column("floor_name", String, nullable=True)
    floor_level = Column("floor_level", Float, nullable=True)
    contracts = relationship('Contract', back_populates='use_unit')
    contractors = relationship('Contractor', back_populates='use_unit')

    def __init__(self, internal_id, id_num, company_id, building_id, economic_unit_id,
                 postcode, town, street, house_number, house_number_addition, country_id, country,
                 street_complete, house_number_complete, financing_type_id, financing_type,
                 use_unit_usage_type_id, use_unit_usage_type, usable_space, living_space, heating_space,
                 number_of_rooms, number_of_half_rooms, description_of_position, management_start,
                 management_end, move_in_date, exit_date, entry_date, position_id, position, floor_id,
                 floor_name, floor_level):
        self.internal_id = internal_id
        self.id_num = id_num
        self.company_id = company_id
        self.building_id = building_id
        self.economic_unit_id = economic_unit_id
        self.postcode = postcode
        self.town = town
        self.street = street
        self.house_number = house_number
        self.house_number_addition = house_number_addition
        self.country_id = country_id
        self.country = country
        self.street_complete = street_complete
        self.house_number_complete = house_number_complete
        self.financing_type_id = financing_type_id
        self.financing_type = financing_type
        self.use_unit_usage_type_id = use_unit_usage_type_id
        self.use_unit_usage_type = use_unit_usage_type
        self.usable_space = usable_space
        self.living_space = living_space
        self.heating_space = heating_space
        self.number_of_rooms = number_of_rooms
        self.number_of_half_rooms = number_of_half_rooms
        self.description_of_position = description_of_position
        self.management_start = management_start
        self.management_end = management_end
        self.move_in_date = move_in_date
        self.exit_date = exit_date
        self.entry_date = entry_date
        self.position_id = position_id
        self.position = position
        self.floor_id = floor_id
        self.floor_name = floor_name
        self.floor_level = floor_level

    def __repr__(self):
        return f"Use Unit {self.id_num}"


class Address(Base):
    __tablename__ = "wowi_addresses"
    internal_id = Column("internal_id", Integer, primary_key=True)
    postcode = Column("postcode", String)
    town = Column("town", String)
    street = Column("street", String, nullable=True)
    house_number = Column("house_number", String, nullable=True)
    house_number_addition = Column("house_number_addition", String, nullable=True)
    country_id = Column("country_id", Integer, nullable=True)
    country = Column("country", String, nullable=True)
    street_complete = Column("street_complete", String)
    house_number_complete = Column("house_number_complete", String)
    address_type_id = Column("address_type_id", Integer, nullable=True)
    address_type = Column("address_type", String, nullable=True)
    valid_from = Column("valid_from", Date)
    valid_to = Column("valid_to", Date, nullable=True)

    communications = relationship('Communication', back_populates='related_address')
    person_id = Column(Integer, ForeignKey("wowi_persons.internal_id"))
    person = relationship('Person', back_populates='addresses')

    def __init__(self, internal_id, postcode, town, street, house_number, house_number_addition, country_id, country,
                 street_complete, house_number_complete, address_type_id, address_type, valid_from, valid_to,
                 person_id):
        self.internal_id = internal_id
        self.postcode = postcode
        self.town = town
        self.street = street
        self.house_number = house_number
        self.house_number_addition = house_number_addition
        self.country_id = country_id
        self.country = country
        self.street_complete = street_complete
        self.house_number_complete = house_number_complete
        self.address_type_id = address_type_id
        self.address_type = address_type
        self.valid_from = valid_from
        self.valid_to = valid_to
        self.person_id = person_id

    def __repr__(self):
        return f"Address {self.street_complete}, {self.postcode} {self.town}"


class Communication(Base):
    __tablename__ = "wowi_communications"
    internal_id = Column("internal_id", Integer, primary_key=True)
    related_address_id = Column(Integer, ForeignKey("wowi_addresses.internal_id"), nullable=True)
    related_address = relationship('Address', back_populates='communications')
    content = Column("content", String)
    explanation = Column("explanation", String, nullable=True)
    communication_type_id = Column("communication_type_id", Integer)
    communication_type = Column("communication_type", String)
    person_id = Column(Integer, ForeignKey("wowi_persons.internal_id"))
    person = relationship('Person', back_populates='communications')

    def __init__(self, internal_id, related_address_id, content, explanation, communication_type_id,
                 communication_type, person_id):
        self.internal_id = internal_id
        self.related_address_id = related_address_id
        self.content = content
        self.explanation = explanation
        self.communication_type_id = communication_type_id
        self.communication_type = communication_type
        self.person_id = person_id

    def __repr__(self):
        return f"Communication Id {self.internal_id}: {self.content}"


class Person(Base):
    __tablename__ = "wowi_persons"
    internal_id = Column("internal_id", Integer, primary_key=True)
    id_num = Column("id_num", String)
    name = Column("name", String)
    short_name = Column("short_name", String)
    valid_from = Column("valid_from", Date)
    valid_to = Column("valid_to", Date, nullable=True)
    long_name_1 = Column("long_name_1", String, nullable=True)
    long_name_2 = Column("long_name_2", String, nullable=True)
    vat_id = Column("vat_id", String, nullable=True)
    commercial_register_number = Column("commercial_register_number", String, nullable=True)
    commercial_register_town = Column("commercial_register_town", String, nullable=True)
    first_name = Column("first_name", String, nullable=True)
    last_name = Column("last_name", String, nullable=True)
    birth_date = Column("birth_date", Date, nullable=True)
    gender_id = Column("gender_id", Integer, nullable=True)
    gender_name = Column("gender_name", String, nullable=True)
    is_natural_person = Column("is_natural_person", Boolean)

    addresses = relationship('Address', back_populates='person')
    communications = relationship('Communication', back_populates='person')
    contractors = relationship('Contractor', back_populates='person')

    def __init__(self, internal_id, id_num, name, short_name, valid_from, valid_to, long_name_1, long_name_2,
                 vat_id, commercial_register_number, commercial_register_town, first_name, last_name, birth_date,
                 gender_id, gender_name):
        self.internal_id = internal_id
        self.id_num = id_num
        self.name = name
        self.short_name = short_name
        self.valid_from = valid_from
        self.valid_to = valid_to
        self.long_name_1 = long_name_1
        self.long_name_2 = long_name_2
        self.vat_id = vat_id
        self.commercial_register_number = commercial_register_number
        self.commercial_register_town = commercial_register_town
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender_id = gender_id
        self.gender_name = gender_name

        if self.first_name is None and self.last_name is None:
            self.is_natural_person = False
        else:
            self.is_natural_person = True

    def __repr__(self):
        return f"Person IdNum {self.id_num} - {self.short_name}"


class Contract(Base):
    __tablename__ = "wowi_contracts"
    internal_id = Column("internal_id", Integer, primary_key=True)
    id_num = Column("id_num", String)
    use_unit_id = Column(Integer, ForeignKey("wowi_use_units.internal_id"))
    use_unit = relationship('UseUnit', back_populates='contracts')
    restriction_id = Column("restriction_id", Integer)
    restriction_name = Column("restriction_name", String)
    is_vacany = Column("is_vacancy", Boolean)
    status_id = Column("status_id", Integer)
    status_name = Column("status_name", String)
    life_id = Column("life_id", Integer)
    life_name = Column("life_name", String)
    contract_start = Column("contract_start", Date)
    contract_end = Column("contract_end", Date, nullable=True)
    contractors = relationship('Contractor', back_populates='contract')

    def __init__(self, internal_id, id_num, use_unit_id, restriction_id, restriction_name, is_vacancy,
                 status_id, status_name, life_id, life_name, contract_start, contract_end):
        self.internal_id = internal_id
        self.id_num = id_num
        self.use_unit_id = use_unit_id
        self.restriction_id = restriction_id
        self.restriction_name = restriction_name
        self.is_vacany = is_vacancy
        self.status_id = status_id
        self.status_name = status_name
        self.life_id = life_id
        self.life_name = life_name
        self.contract_start = contract_start
        self.contract_end = contract_end

    def __repr__(self):
        return f"Contract IdNum {self.id_num} Id {self.internal_id}"


class Contractor(Base):
    __tablename__ = "wowi_contractors"
    internal_id = Column("internal_id", Integer, primary_key=True)
    contract_id = Column(Integer, ForeignKey("wowi_contracts.internal_id"), primary_key=True)
    type_id = Column("type_id", Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey("wowi_persons.internal_id"))
    contract = relationship('Contract', back_populates='contractors')
    use_unit_id = Column(Integer, ForeignKey("wowi_use_units.internal_id"))
    use_unit = relationship('UseUnit', back_populates='contractors')
    person = relationship('Person', back_populates='contractors')

    type_name = Column("type_name", String)
    valid_from = Column("valid_from", Date)
    valid_to = Column("valid_to", Date, nullable=True)

    def __init__(self, internal_id, contract_id, use_unit_id, person_id, type_id,
                 type_name, valid_from, valid_to):
        self.internal_id = internal_id
        self.contract_id = contract_id
        self.use_unit_id = use_unit_id
        self.person_id = person_id
        self.type_id = type_id
        self.type_name = type_name
        self.valid_from = valid_from
        self.valid_to = valid_to

    def __repr__(self):
        return f"Contractor {self.internal_id}"
