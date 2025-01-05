# tv.py file
# class definition
class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no=1
        self.chlist=['none']
        self.volume=0

    def turn_off(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def show_status(self):
        if self.is_on:
            print(f'The TV is on. Current channel is {self.channel_no} {self.chlist[self.channel_no-1]}. Volume is{self.volume}')
        else:
            print('The TV is off')
    def set_channel(self,new_channel_no):
        self.channel_no=new_channel_no
    def set_channels(self,channel_list):
        self.chlist=channel_list
    def show_channels(self):
        print('Channel list:')
        i=0
        while i<len(self.chlist):
            print(f'{i+1}.{self.chlist[i]}')
            i+=1
    def volumeup(self):
        if self.volume<10:
            self.volume+=1
        elif self.volume==10:
            print('Max volume!!!')
    def volumedown(self):
        if self.volume>0:
            self.volume-=1
        elif self.volume==0:
            print('Min volume!!!')



