from operator import index

from base.base import BaseShibulim
from base.bulding import Building
from solider.solider import Solider


def meaning_base():
    base=BaseShibulim()
    build1=Building(1)
    build2=Building(2)
    build1.add_rooms()
    build2.add_rooms()
    base.add_building(build1)
    base.add_building(build2)
    return base


def assign_beds(persons:list[Solider]):
    base_shibulim=meaning_base()
    get_bed=0
    in_pending=0
    holding=len(persons)-in_pending
    while holding <= len(persons):
        for build in  base_shibulim.building:
            for room in build.meaning_rooms:
                if room.use <= 8:
                    room.bed_in_use(persons[holding].id)
                    persons[holding].status=f'קיבל מיטה בבניין {build.building_num} בחדר מספר{room.room_num}'
                    holding += 1
                    get_bed+=1
                else:
                    continue
            else:
                continue
    else:
        persons[holding].status='בהמתנה'
        holding += 1

    return persons, get_bed,in_pending