# tv_gui.py
import tkinter as tk
from tv_logic import Television

class TVGUI:
    def __init__(self, root):
        self.root = root
        self.tv = Television()

        self.power_button = tk.Button(root, text="Power", command=self.toggle_power)
        self.mute_button = tk.Button(root, text="Mute", command=self.toggle_mute)
        self.volume_up_button = tk.Button(root, text="Volume Up", command=self.volume_up)
        self.volume_down_button = tk.Button(root, text="Volume Down", command=self.volume_down)
        self.channel_up_button = tk.Button(root, text="Channel Up", command=self.channel_up)
        self.channel_down_button = tk.Button(root, text="Channel Down", command=self.channel_down)

        self.power_button.pack()
        self.mute_button.pack()
        self.volume_up_button.pack()
        self.volume_down_button.pack()
        self.channel_up_button.pack()
        self.channel_down_button.pack()

        self.volume_slider = tk.Scale(root, from_=0, to=9, orient="horizontal", command=self.on_slider_move)
        self.volume_slider.set(self.tv.volume)
        self.volume_slider.pack()

        self.status_label = tk.Label(root, text="")
        self.status_label.pack()

        self.update_status()
        self.update_button_states()

    def toggle_power(self):
        self.tv.toggle_power()
        self.update_status()
        self.update_button_states()

    def toggle_mute(self):
        self.tv.toggle_mute()
        self.update_status()

    def volume_up(self):
        self.tv.adjust_volume(1)
        self.update_status()
        self.sync_slider()

    def volume_down(self):
        self.tv.adjust_volume(-1)
        self.update_status()
        self.sync_slider()

    def channel_up(self):
        self.tv.change_channel(1)
        self.update_status()

    def channel_down(self):
        self.tv.change_channel(-1)
        self.update_status()

    def set_volume(self, value):
        self.tv.volume = int(value)
        self.update_status()

    def on_slider_move(self, value):
        self.set_volume(value)
        self.tv.muted = False  # Unmute when the slider is moved
        self.update_status()

    def sync_slider(self):
        self.volume_slider.set(self.tv.volume)

    def update_status(self):

        power_status = "On" if self.tv.power_on else "Off"
        channel_name = self.tv.get_channel_name()
        volume_status = "Muted" if self.tv.muted else f"Volume: {self.tv.volume}"
        self.status_label.config(
            text=f"Power: {power_status}\nChannel: {channel_name}\n{volume_status}"
        )

    def update_button_states(self):

        state = tk.NORMAL if self.tv.power_on else tk.DISABLED
        self.mute_button.config(state=state)
        self.volume_up_button.config(state=state)
        self.volume_down_button.config(state=state)
        self.channel_up_button.config(state=state)
        self.channel_down_button.config(state=state)
        self.volume_slider.config(state=state)

if __name__ == "__main__":
    root = tk.Tk()
    app = TVGUI(root)
    root.mainloop()
