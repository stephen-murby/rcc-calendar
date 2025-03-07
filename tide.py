from dataclasses import dataclass
from enum import Enum
from typing import List
from datetime import datetime

class TideType(Enum):
    LOW = "LOW"
    HIGH = "HIGH"

class EventType(Enum):
    SOCIAL = "SOCIAL"
    WORKING_PARTY = "WORKING_PARTY"
    TRAINING = "TRAINING"
    RACING = "RACING"
    CRUISING = "CRUISING"
    CLUB_ADMINISTRATION = "CLUB_ADMINISTRATION"

@dataclass
class Tide:
    type: TideType
    time: datetime
    height: float

@dataclass
class Tides:
    tides: List[Tide]

@dataclass
class Event:
    start_time: datetime
    title: str
    type: EventType

@dataclass
class SailingEvent(Event):
    on_the_water_time: datetime

@dataclass
class RCCDay:
    day: str
    date: datetime
    tides: List[Tides]
    events: List[Event]

@dataclass
class RCCMonth:
    name: str
    days: List[RCCDay]

@dataclass
class RCCYear:
    months: List[RCCMonth]