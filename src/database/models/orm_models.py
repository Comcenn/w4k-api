from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship


Base = declarative_base()

# Association tables
unit_weapon_link_table = Table(
    "UNIT_WEAPON_LINK",
    Base.metadata,
    Column("unit_id", Integer, ForeignKey("UNITS.id")),
    Column("weapon_id", Integer, ForeignKey("WEAPONS.id"))
)


unit_unitmember_link_table = Table(
    "UNIT_UNIT_MEMBER_LINK",
    Base.metadata,
    Column("unit_id", Integer, ForeignKey("UNITS.id")),
    Column("unit_member_id", Integer, ForeignKey("UNIT_MEMBERS"))
)


class Faction(Base):
    __tablename__ = "FACTIONS"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Weapon(Base):
    __tablename__ = "WEAPONS"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    range = Column(String)
    w_type = Column(String)
    strength = Column(Integer)
    armour_penetration = Column(Integer)
    damage = Column(String)
    abilities = Column(String)
    faction_id = Column(Integer, ForeignKey("FACTIONS.id"))
    faction = relationship("Faction")


class UnitMember(Base):
    __tablename__ = "UNIT_MEMBERS"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    movement = Column(Integer)
    weapon_skill = Column(String)
    ballistic_skill = Column(String)
    strength = Column(Integer)
    toughness = Column(String)
    wounds = Column(Integer)
    attacks = Column(Integer)
    leadership = Column(Integer)
    saving_trow = Column(String)
    damage_bracket = Column(String)
    faction_id = Column(Integer, ForeignKey("FACTIONS.id"))
    faction = relationship("Faction")


class Abilities(Base):
    __tablename__ = "ABILITIES"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    faction_id = Column(Integer, ForeignKey("FACTIONS.id"))
    faction = relationship("Faction")


class Unit(Base):
    __tablename__ = "UNITS"
    name = Column(String)
    weapons = relationship("Weapon", secondary=unit_weapon_link_table)
    unit_members = relationship("UnitMember", secondary=unit_unitmember_link_table)
    faction_id = Column(Integer, ForeignKey("FACTIONS.id"))
    faction = relationship("Faction")
