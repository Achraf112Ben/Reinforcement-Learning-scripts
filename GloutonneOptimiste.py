v_init=2

class Brat:
    def __init__(self, sq, ma):
        self.sq=sq
        self.ma=ma
        self.nTires=0
        self.sommeTires=ma
    #tirer le brat et recevoir une valeur
    def tirer(self):
        self.nTires += 1
        retour = self.sq[self.nTires%len(self.sq)]
        self.updateMA(retour)
        return retour
    
    def updateMA(self, r):
        self.sommeTires += r
        self.ma = self.sommeTires / self.nTires

b1 = Brat([1,0,0], v_init)
b2 = Brat([0,1,0], v_init)
b3 = Brat([0,0,1], v_init)

brats= [b1, b2, b3]

class GloutonneOptimiste: 
    def __init__(self, brats):
        self.brats = brats
        self.MAs = []
        for b in self.brats: 
            self.MAs.append(b.ma)
    def tireMeilleurBrat(self):
        argmax = 0
        for i in range(len(self.MAs)):
            if self.MAs[i] == max(self.MAs):
                argmax=i
                break
        print('brat tire: b',argmax+1)
        r = self.brats[argmax].tirer()
        print('retour: ',r)
        self.MAs[argmax]=self.brats[argmax].ma
        print('moyennes amperiques:')
        print(self.MAs)
    def execute(self):
        for i in range(20):
            self.tireMeilleurBrat()
            
glout = GloutonneOptimiste(brats)
glout.execute() 
            

