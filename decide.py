#Decision recieves a a ratio of men/women and number of people Returns Type of ad to display

class Decide(object):
    def __init__(self, ratio, people):
        self.ratio = ratio
        self.people = people
        self.female1 = "photos/female1.png"
        self.female2 = "photos/demale2.png"
        self.group1  = "photos/group1.png"
        self.groupmanwoman = "photos/groupmanwoman.png"
        self.male1 = "photos/male1.png"
        self.malechild1 = "photos/malechild1.png"

        
    def getFilePath(self):
        if(self.ratio == 1):
            return self.male1
        elif(self.ratio == 0):
            return self.female1
        else:
            if(self.people > 0):
                return self.group1
            else:
                return self.groupmanwoman


        
    
