class Television:
    """
    A class representing a Television object with basic functionality.
    """

    def __init__(self):
        """
        Initializes a Television object with default settings.
        """
        self.power_on = False   # Keeps track of the power status of the TV
        self.muted = False      # Keeps track of whether the TV is muted
        self.volume = 5         # Current volume level (0 to 9)
        self.channel = 1        # Current channel number (1 to 9)

    def toggle_power(self):
        """
        Toggles the power status of the TV.
        """
        self.power_on = not self.power_on

    def toggle_mute(self):
        """
        Toggles the mute status of the TV.
        """
        self.muted = not self.muted

    def adjust_volume(self, value):
        """
        Adjusts the volume level of the TV by the given value.

        Args:
            value (int): The value that adjust the volume.
                         Positive value increases volume, negative decreases it.

        The volume level is set to a min = 0 and max = 9.
        """
        self.muted = False
        self.volume = max(0, min(9, self.volume + value))

    def change_channel(self, value):
        """
        Changes the channel of the TV by the given value.

        Args:
            value (int): The value that changes the channel.
                         Positive value moves to the next channel,
                         negative moves to the previous channel.

        Channels wrap around from 9 to 1.
        """
        self.channel = (self.channel + value - 1) % 9 + 1

    def get_channel_name(self):
        """
        Returns the name of the current channel.

        Returns:
            str: The name of the current channel.
        """
        channel_names = {
            1: "CBS", 2: "NBC", 3: "ABC", 4: "FOX",
            5: "CNN", 6: "FOX NEWS", 7: "ESPN",
            8: "HBO", 9: "PPV"
        }
        return channel_names[self.channel]
