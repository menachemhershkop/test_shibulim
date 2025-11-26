

class Room:
    def __init__(self,room_num:int):
        self.beds=8
        self.room_num=room_num
        self.use=0
        self.living=[]
    def bed_in_use(self, name):
        if self.use < self.beds:
            self.use+=1
            self.living.append(name)
            return self.use, self.living
        else:
            return "All in use", False