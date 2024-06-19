import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import pygame

def run_second_file(username):
    subprocess.Popen(["python", "game.py", username])

def main():
    def on_button_click():
        username = username_entry.get()
        run_second_file(username)

    root = tk.Tk()
    root.title("First File")

    # Set window size
    root.geometry("650x500")

    #background music
    pygame.mixer.init()
    pygame.mixer.music.load("audio_background.wav")  
    pygame.mixer.music.play(-1) 


    # Load background image
    background_image = Image.open("bgimg.png")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Username entry
    username_label = tk.Label(root, text="Username:", bg="white")
    username_label.place(x=50, y=50, width=100, height=30)
    username_entry = tk.Entry(root)
    username_entry.place(x=160, y=50, width=200, height=30)

    # Button to run second file
    button = tk.Button(root, text="START GAME!", command=on_button_click)
    #button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    button.grid(row=10, columnspan=5, padx=100, pady=100)

    root.mainloop()

if __name__ == "__main__":
    main()

