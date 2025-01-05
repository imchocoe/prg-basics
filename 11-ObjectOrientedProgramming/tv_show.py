from tv import TV
def main():
    my_tv = TV()  # Create an instance of the TV class
    my_tv.show_status()  # Show status (should print 'The TV is off')
    my_tv.turn_on()  # Turn the TV on
    my_tv.show_status()  # Show status (should print 'The TV is on')
    my_tv.show_channels()
    my_tv.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox', 'Discovery'])
    my_tv.show_channels()
    my_tv.volumeup()
    my_tv.set_channel(5)
    my_tv.show_status()
    my_tv.volumedown()
    my_tv.show_status()
    my_tv.turn_off()  # Turn the TV off
    my_tv.show_status()  # Show status (should print 'The TV is off')


if __name__ == "__main__":
    main()