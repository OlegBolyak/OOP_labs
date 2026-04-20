import statistics
class StatsTracker:
    def __init__(self):
        self.data=[]
    def add(self,num):
        self.data.append(num)
    def mean(self):
        mean_value=sum(self.data)/len(self.data)
        print(mean_value)
    def median(self):
        if len(self.data)%2!=0:
            print(self.data[len(self.data)//2])
    def mode(self):
        mode_value=statistics.mode(self.data)
        print(mode_value)


