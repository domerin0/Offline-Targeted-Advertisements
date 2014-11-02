#Decision recieves a a ratio of men/women and number of people Returns Type of ad to display
import math

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
        self.ratioHist[3] = [0,0,0]
        self.peopleHist[3] = [0,0,0]
    
    
    #Assuming this is run every tick
    def smoothing(self):
        if (x<3):
            self.ratioHist[x] = self.ratio
            self.peopleHist[x] = self.people
            x = x+1
            return;
        else:
            finalRatio = max(self.ratioHist)
            finalPeople = max(self.peopleHist)
            x = 0
            self.ratioHist = [0,0,0]
            self.peopleHist = [0,0,0]
            




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


        
    
