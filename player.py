import tkinter as tk
from tkinter import ttk
from GenerateNotes import play_piano_note, stop

import tkinter as tk
from tkinter import ttk

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x250")
        self.root.configure(bg="black")  # Set background color to black

        # Create loading label
        self.loading_label = ttk.Label(root, text="Loading...", font=("Helvetica", 12))  # Set text color to green and background to black
        self.loading_label.pack(pady=5)

        # Hide loading label initially
        self.loading_label.pack_forget()

        # Create UI elements
        self.label = ttk.Label(root, text="Music Player", font=("Helvetica", 16))  # Set text color to green and background to black
        self.label.pack()

        self.play_button = ttk.Button(root, text="Play", command=self.play_music, width=10)  # Set button colors to green and black
        self.play_button.pack(pady=5)

        self.stop_button = ttk.Button(root, text="Stop", command=self.stop_music, width=10)  # Set button colors to green and black
        self.stop_button.pack(pady=5)

    def play_music(self):
        # Show loading text
        self.loading_label.pack()

        # TODO: Add logic to play music
        print("Playing music...")
        play_piano_note()
        # Hide loading text after task completion
        self.loading_label.pack_forget()

    def stop_music(self):
        # Show loading text
        self.loading_label.pack()

        # TODO: Add logic to stop music
        print("Stopping music...")
        stop()
        # Hide loading text after task completion
        self.loading_label.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()
