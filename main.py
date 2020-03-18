class PeerLearning:
    def __init__(self,name):
        self.name = name
    def addStacks(self):
        print("Whether interested or expertised.")
        status=input("Enter 'interest/expertise' : ")
        while(status != "interest" and status != "expertise"):
            status=input("Enter only 'interest/expertise' : ")
        self.status=status
    def setMentorOrLearner(self):
        print("Whether Partcipant is Learner or Mentor.")
        roll = input("Enter 'learner/mentor' : ")
        while (roll != "learner" and roll != "mentor"):
            roll = input("Enter only 'learner/mentor' : ")
        self.roll = roll
    def setAvailableTime(self):
        if self.roll == "mentor":
            print("Enter available time")
            time = input("In hours only: ")
            self.time=float(time)
    def getMentor(self,stack,time):
        if (self.roll == "mentor" and self.time >= float(time)):
            print(self.name, "is available")
stack=[]
i=0
while(input("Add member 'y/n': ") == "y" ):
   name=input("Enter the name: ")
   stack.append(PeerLearning(name))
   stack[i].addStacks()
   stack[i].setMentorOrLearner()
   stack[i].setAvailableTime()
   i=i+1
time = input("Enter the time to check availability in hours: ")
for n in range(0,i):
    stack[n].getMentor(stack,time)
