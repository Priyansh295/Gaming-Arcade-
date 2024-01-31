import tkinter as tk
from tkinter import messagebox
import random
def rockpaperscisor():
    def play_game():
        user_choice = user_input.get()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        if (user_choice != "rock" and user_choice != "paper" and user_choice != "scissors" ):
            messagebox.showinfo("INVALID", "Enter the correct value")
            root.destroy()
        elif user_choice == computer_choice:
            messagebox.showinfo("Tie!", "You both chose " + user_choice + ". It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            messagebox.showinfo("You Win!", "You chose " + user_choice + " and the computer chose " + computer_choice + ". You win!")
        else:
            messagebox.showinfo("You Lost!", "You chose " + user_choice + " and the computer chose " + computer_choice + ". You lost.")
    
    #create the main window
    root = tk.Tk()
    root.title("Rock-Paper-Scissors")
    
    #create the label
    label = tk.Label(root, text="Choose rock, paper, or scissors:")
    label.pack()
    
    #create the user input
    user_input = tk.Entry(root)
    user_input.pack()
    
    #create the play button
    play_button = tk.Button(root, text="Play", command=play_game)
    play_button.pack()
    
    #run the main loop
    root.mainloop()
# rockpaperscisor()
    