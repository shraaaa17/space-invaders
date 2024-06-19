
import tkinter as tk
from PIL import Image, ImageTk

class Scoreboard(tk.Toplevel):
    def __init__(self, scores):
        super().__init__()
        self.title("Scoreboard")
        self.geometry("400x300")

        # Display scores
        tk.Label(self, text="Top Scores", font=("Helvetica", 16)).pack()
        for i, (name, score) in enumerate(scores, start=1):
            tk.Label(self, text=f"{i}. {name}: {score}", font=("Helvetica", 12)).pack()

def main():
    root = tk.Tk()
    root.title("Space Invaders")

    # Load background image
    background_image = Image.open("bgimg.png")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def on_button_click():
        username = username_entry.get()
        score_page.destroy()  # Close score page if open
        run_second_file(username)

    # Username entry
    username_label = tk.Label(root, text="Username:", bg="white")
    username_label.place(x=50, y=50, width=100, height=30)
    username_entry = tk.Entry(root)
    username_entry.place(x=160, y=50, width=200, height=30)

    # Button to run second file
    button = tk.Button(root, text="START GAME!", command=on_button_click)
    button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Example scores
    example_scores = [("Player1", 1000), ("Player2", 800), ("Player3", 1200)]

    def show_scores():
        scoreboard = Scoreboard(example_scores)
        scoreboard.grab_set()  # Make scoreboard modal

    # Button to show scores
    show_scores_button = tk.Button(root, text="Show Scores", command=show_scores)
    show_scores_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    root.mainloop()

if __name__ == "__main__":
    main()


'''
import tkinter as tk
import tkinter.messagebox as messagebox

def show_highest_score():
    example_scores = [("Player1", 1000), ("Player2", 800), ("Player3", 1200)]
    highest_score = max(example_scores, key=lambda x: x[1])
    messagebox.showinfo("Highest Score", f"The highest score is {highest_score[1]} by {highest_score[0]}")

def main():
    root = tk.Tk()
    root.title("Space Invaders")

    def on_button_click():
        username = username_entry.get()
        # Call your function here to start the game with the provided username
        show_highest_score()

    username_label = tk.Label(root, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    start_button = tk.Button(root, text="START GAME!", command=on_button_click)
    start_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import pygame

def run_second_file(username):
    subprocess.Popen(["python", "game.py", username])

def show_score():
    # Read highest score from a file
    with open("highest_score.txt", "r") as file:
        highest_score = file.read()

    root = tk.Tk()
    root.title("Score")

    score_label = tk.Label(root, text=f"Highest Score: {highest_score}", font=("Helvetica", 16))
    score_label.pack()

    root.mainloop()

def main():
    def on_button_click():
        username = username_entry.get()
        run_second_file(username)

    root = tk.Tk()
    root.title("First File")

    # Set window size
    root.geometry("650x500")

    # Background music
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
    button.grid(row=10, columnspan=5, padx=100, pady=100)

    # Button to show score
    score_button = tk.Button(root, text="Show Score", command=show_score)
    score_button.grid(row=11, columnspan=5, padx=100, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
'''
'''import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import pygame

def run_second_file(username):
    subprocess.Popen(["python", "game.py", username])

def show_score():
    # Read highest score from a file
    with open("highest_score.txt", "r") as file:
        highest_score = file.read()

    root = tk.Tk()
    root.title("Score")

    score_label = tk.Label(root, text=f"Highest Score: {highest_score}", font=("Helvetica", 16))
    score_label.pack()

    root.mainloop()

def main():
    def on_button_click():
        username = username_entry.get()
        run_second_file(username)

    root = tk.Tk()
    root.title("First File")

    # Set window size
    root.geometry("650x500")

    # Background music
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
    button.grid(row=10, columnspan=5, padx=100, pady=100)

    # Button to show score
    score_button = tk.Button(root, text="Show Score", command=show_score)
    score_button.grid(row=11, columnspan=5, padx=100, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()'''

'''import tkinter as tk

def show_score_page(score):
    # Create a new Tkinter window
    score_window = tk.Tk()
    score_window.title("Score Page")
    
    # Create a label to display the score
    score_label = tk.Label(score_window, text=f"Your Score: {score}", font=("Helvetica", 24))
    score_label.pack(pady=20)
    
    # Add a button to close the window
    close_button = tk.Button(score_window, text="Close", command=score_window.destroy)
    close_button.pack(pady=10)
    
    # Run the Tkinter event loop
    score_window.mainloop()

# Example usage:
score_value = 10  # This should be the actual score from the game
show_score_page(score_value)
'''
'''import tkinter as tk

def show_score_page(score):
    # Create a new Tkinter window
    score_window = tk.Tk()
    score_window.title("Score Page")
    
    # Create a label to display the score
    score_label = tk.Label(score_window, text=f"Your Score: {score}", font=("Helvetica", 24))
    score_label.pack(pady=20)
    
    # Add a button to close the window
    close_button = tk.Button(score_window, text="Close", command=score_window.destroy)
    close_button.pack(pady=10)
    
    # Run the Tkinter event loop
    score_window.mainloop()

def run_game():
    # Your game code goes here
    # This is where the game logic and main loop would be
    
    # Example: When the game ends, call show_score_page with the final score
    final_score = 04  # Replace this with the actual final score from your game
    show_score_page(final_score)

# Example usage:
run_game()
 '''

