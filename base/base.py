from base.bulding import Building
from solider.solider import Solider


class BaseShibulim:
    def __init__(self):
        self.building=[]
    def add_building(self,building_num:Building):
        self.building.append(building_num)
    def sum_of_rooms(self):
        roms=0
        for i in self.building:
            roms+=i.rooms
        return roms
    def sum_of_beads(self):
        beads=0
        for i in self.building:
            beads+=i.sum_of_beads()
        return beads
