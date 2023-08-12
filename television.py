# Import the TVGUI class from the tv_gui module
from tv_gui import TVGUI
import tkinter as tk

if __name__ == "__main__":
    # Create the main application window using tkinter
    root = tk.Tk()

    # Create an instance of TVGUI, which sets up the TV control GUI
    app = TVGUI(root)

    # Start the main event loop, allowing the GUI to respond to user interactions
    root.mainloop()

