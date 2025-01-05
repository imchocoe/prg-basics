class Phone():
    def __init__(self,brand,battery,mode):
        self.brand=brand
        self.battery=battery
        self.mode=mode

    def bperc(self):
        print(f'Your battery percentage is: {self.battery}')
    def chmode(self):
        if self.mode=="charging":
            print("Your phone is charging!")
        else:
            print('Working on battery!')
    
    
def main():
    phone1=Phone('Xiaomi',12,"charging")
    print(phone1.bperc())
    print(phone1.chmode())
    print(phone1.brand)

if __name__=="__main__":
    main()

