class Computer:
    def __init__(self,c,r):
        self.cpu = c
        self.ram = r

    def config_Disp(self):
        print(f"Config is {self.cpu} {self.ram}")

comp1 = Computer("i7", 16)
comp2 = Computer("i3", 8)

comp1.config_Disp()
comp2.config_Disp()