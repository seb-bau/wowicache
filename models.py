from sqlalchemy import Column, String, Integer, ForeignKey, Date, Float
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
    house_number_addition = Column("house_number_addition", String)
    country_id = Column("country_id", Integer)
    country = Column("country", String)
    street_complete = Column("street_complete", String)
    house_number_complete = Column("house_number_complete", String)

    construction_year = Column("construction_year", Integer)
    move_in_date = Column("move_in_date", Date)

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
    house_number_addition = Column("house_number_addition", String)
    country_id = Column("country_id", Integer)
    country = Column("country", String)
    street_complete = Column("street_complete", String)
    house_number_complete = Column("house_number_complete", String)
    financing_type_id = Column("financing_type_id", Integer)
    financing_type = Column("financing_type", String)
    use_unit_usage_type_id = Column("use_unit_usage_type_id", Integer)
    use_unit_usage_type = Column("use_unit_usage_type", String)
    usable_space = Column("usable_space", Float)
    living_space = Column("living_space", Float)
    heating_space = Column("heating_space", Float)
    number_of_rooms = Column("number_of_rooms", Integer)
    number_of_half_rooms = Column("number_of_half_rooms", Integer)
    description_of_position = Column("position_description", String)
    management_start = Column("management_start", Date)
    management_end = Column("management_end", Date)
    move_in_date = Column("move_in_date", Date)
    exit_date = Column("exit_date", Date)
    entry_date = Column("entry_date", Date)
    position_id = Column("position_id", Integer)
    position = Column("position", String)
    floor_id = Column("floor_id", Integer)
    floor_name = Column("floor_name", String)
    floor_level = Column("floor_level", Float)

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
