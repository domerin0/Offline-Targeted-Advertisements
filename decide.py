#Decision recieves a a ratio of men/women and number of people Returns Type of ad to display

class Decide:

    ratio = 0;
    people = 0;

    def__init__(self, ratio, people):
        self.ratio = ratio
        self.people = people

    def gender:
        if ratio == 0:
            return 0 #All Women
        elif ratio == 1:
            return 1 #All Men
        else:
            return 2 #Mixed People
        

    def isMultiple:
        if people > 1:
            return 2 #There are multiple people
        elif people = 1:
            return 1
        else:
            return 0
        
    
