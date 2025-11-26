from base.room import Room


class Building:
    def __init__(self,building_num:int):
        self.rooms=10
        self.building_num=building_num
        self.meaning_rooms=[]
    def add_rooms(self):
        num=1
        while num != self.rooms+1:
            self.meaning_rooms.append(Room(num))
            num+=1
    def sum_of_beads(self):
        bead=0
        for i in self.meaning_rooms:
            bead+=i.beds
        return bead
