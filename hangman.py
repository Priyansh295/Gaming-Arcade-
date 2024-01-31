import random
import tkinter as tk
from tkinter import messagebox

# Create a variable to store the number of wrong guesses
wrong_guesses = 0

def hangman():
    # Create the main window
    root = tk.Tk()
    # to add colour in the background
    # root.config(bg='black')
    root.title("Hangman Game")
    root.geometry("800x400")
    words=["python","program","compiler"]
    Hint=["It is a fift level programming language","A set of instructions written in order to perform a desired task","It is used to convert source code to machine code"]
    # Create the word to guess
    word_to_guess = random.choice(words)
    hint=words.index(word_to_guess)
    # Create a list to store the letters that have been guessed
    guessed_letters = []
    
    # Create a function to exit the game 
    def end():
       messagebox.showinfo("End","Thank you for playing")
       root.destroy()
       
    # Create a function to check if the user's guess is correct
    def check_guess(textbox:tk.Entry):
        global wrong_guesses

        guess = textbox.get()
        
        if guess in word_to_guess:
            # If the guess is correct, add it to the list of guessed letters
            guessed_letters.append(guess)
        else:
            # If the guess is incorrect, increment the number of wrong guesses
            wrong_guesses += 1
    
        # Check if the user has won or lost
        if wrong_guesses == 6:
            messagebox.showinfo("Game Over", "You lost! The word was " + word_to_guess)
            root.destroy()
        elif set(word_to_guess) == set(guessed_letters):
            messagebox.showinfo("Congratulations", "You won! You correctly guessed the word " + word_to_guess)
            root.destroy()
        else:
            # Update the display
            update_display()
            
        textbox.delete(0,tk.END)
    
    # Create a function to update the display
    def update_display():
        global wrong_guesses
        
        # Create a string to display the word with underscores for unguessed letters
        word_display = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                word_display += letter+" "
            else:
                word_display += "_ "
 
        Heading=tk.Label(root,text="HANGMAN",font=("Helvetica 27 bold"),background='blue')
        Heading.grid(row=0,column=5,padx=10,pady=10)
    
        # Create a label to display the word
        word_label = tk.Label(root, text=word_display,font=('Ariel', 15))
        word_label.grid(row=1,column=5,padx=10,pady=10)
    
        # Create a label to display the number of wrong guesses
        wrong_guesses_label = tk.Label(root, text="Wrong guesses: " + str(wrong_guesses),font=('Ariel', 15))
        wrong_guesses_label.grid(row=2,column=5,padx=10,pady=10)
    
        # Create a button to get the user's guess
        guess_button = tk.Button(root, text="Make a guess", command=get_guess,font=('Ariel', 15),height=2,width=20,)
        guess_button.grid(row=3,column=5,padx=10,pady=10)
        H=tk.Label(root,text=Hint[hint],font=('Ariel', 15))
        H.grid(row=4,column=5,padx=10,pady=10)
    
    # Create a function to get the user's guess
    def get_guess():
        
           
        # Create an entry widget to get the user's guess
        guess_entry = tk.Entry(root,font=('Ariel', 15))
        guess_entry.grid(row=5,column=5,padx=10,pady=10)
    
        # Create a button to submit the guess
        submit_button = tk.Button(root, text="Submit", command=lambda: check_guess(guess_entry),font=('Ariel', 15),height=1,width=15)
        submit_button.grid(row=6,column=5,padx=10,pady=10)
        #Create button to exit
        eButton=tk.Button(root,text="Stop Playing",command=end,width=30,height=2)
        eButton.grid(row=7,column=5,padx=10,pady=10)
    # Initialize the display
    update_display()
    
    # Start the main loop
    root.mainloop()
# hangman()
