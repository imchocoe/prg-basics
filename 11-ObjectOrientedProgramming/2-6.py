class Phone():
    def __init__(self,brand,battery,mode):
        self.brand=brand
        self.battery=battery
        self.mode=mode

    def bperc(self,battery):
        print(f'Your battery percentage is: {battery}')
    def chmode(self,mode):
        if mode=="charging":
            print("Your phone is charging!")
        else:
            print('Working on battery!')
    
def main():
    phone1=Phone('Xiaomi',12,"charging")
    print(phone1.bperc(12))
    print(phone1.chmode())
    print(phone1.mode)

if __name__=="__main__":
    main()

