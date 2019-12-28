#! python3

# Advent of Code Day 14

class Chemical:

    def __init__(self,name):
        self.name = name
        self.oreCount = None
        self.reactants = None

    def getName(self):
        return self.name
    
    def getOreCount(self):
        return self.oreCount

    def setOreCount(self,value):
        self.oreCount = value
        return self.oreCount

    def findReactants(self,reaction):
        if reaction.getPName() == self.getName():
            self.reactants = reaction.getReagent()
        return self.reactants

    def getReactants(self):
        return self.reactants

    def __repr__(self):
        return str(self.getName())

class Reaction:

    def __init__(self,reaction):

        self.reaction = reaction
        list = reaction.split('=>')
##        print('List is : %s' % (list)) #- Working as intended

        #Declaration of variables
        self.product = list[1].strip() # Strips any trailing whitespaces
        self.reagents = list[0]
        self.rname = []
        self.rvalue = []

        #Get individual elements
        self.reList = self.reagents.split(',') # Split the individual elements to obtain a list of reagents

        for reagentID in range(len(self.reList)):
            self.reList[reagentID] = self.reList[reagentID].strip().split() # Strips any trailing whitespaces, so any element left should be in the format ['1','ABCD']
            self.rname.append(self.reList[reagentID][1])
            self.rvalue.append(self.reList[reagentID][0])
        
        self.product = self.product.split(' ')

##        for reagentID in range(lenn(self.reList)):
##            self.reList[reagentID] = self.reList[reagentID].split
        
    def getProduct(self):
        '''Returns the product of the reaction'''
        return self.product

    def getPName(self):
        return self.product[1]

    def getRName(self):
        return self.rname

    def getPValue(self):
        return self.product[0]

    def getRValue(self):
        return self.rvalue

    def getReagent(self):
        '''Returns a list of Reagents required for the reaction'''
        return self.reList

    def __repr__(self):
        return self.reaction

class System:

    def __init__(self,reactions):
        
        self.reactions = reactions
        self.chemicals = []
        self.names = []

        for reaction in self.reactions:
            if reaction.getPName() not in self.names:
                self.names.append(reaction.getPName())
                self.chemicals.append(Chemical(reaction.getPName()))
            for chemical in reaction.getRName():
                if chemical not in self.names:
                    self.names.append(chemical)
                    self.chemicals.append(Chemical(chemical))

        print(f'Names of all Chemicals is {self.names} and list of chemicals are {self.chemicals}') #- Working as intended
                    
            
    def getReactants(self,product):

        for reaction in self.reactions:
            if reaction.getPName() == product:
                return reaction.getRName(),reaction.getReagent()

    def isSecondary(self,product):

        ID = self.names.index(product)
        preact = None

        for reaction in self.reactions:
            if reaction.getPName() == product:
                preact = reaction

        if 'ORE' in preact.getRName():
            return True

        else:
            return False
            
    def getPCount(self,product):

        ID = self.names.index(product)
        preact = None


        if self.chemicals[ID].getOreCount() != None:
            print(f'Count for {self.chemicals[ID]} is {self.chemicals[ID].getOreCount()}')
            return self.chemicals[ID].getOreCount()
        else:
            #Find Reaction
            for reaction in self.reactions:
                if reaction.getPName()== product:
                    preact = reaction
                    print(f'\nReaction found: {reaction}')
                    break

            #Get Reagent and Product Values

            totalCount = 0
            values = [preact.getRValue(),preact.getPValue()]
            reagents = preact.getRName()

            for reagent in reagents:

                RID = reagents.index(reagent)

                if reagent == 'ORE':

                    totalCount += int(values[0][RID])/int(values[1])

                else:

                    totalCount += self.getPCount(reagent)*int(values[0][RID])

            self.chemicals[ID].setOreCount(totalCount)
            print(f'Count for {self.chemicals[ID]} is {totalCount}')
            return totalCount
                
    def getCount(self,product):

        ID = self.names.index(product)
        preact = None

        #Discontinued
        
        
#Test Cases for Reaction class

##re = Reaction('171 ORE => 8 CNZTR')
##re = Reaction('7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL')
##print(re.getProduct())
##print(re.getReagent())
##print(re.getPName())
##print(re.getRName())

### Working as intended

#Test Cases for System class


##sys = [Reaction('7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL'),Reaction('171 ORE => 8 CNZTR')]
##s = System(sys)

### Working as intended

##Test case for Ore Counting


file = open('aoc14test.txt','r')
re = file.readlines()
file.close()
sys = []

for i in re:
    sys.append(Reaction(i))

print(f'System of reactions is {sys}')

s = System(sys)
print(f' Ore count to get A is {s.getPCount("A")}')
