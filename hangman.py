import tkinter as tk
from tkinter import messagebox
import random

# Lista med ord
words = ["nintendo", "playstation", "hogwarts", "yoshi", "borderlands", "choklad", "vaniljbulle"]

# Starta nytt spel
def new_game():
    global word, guessed_letters, incorrect_guesses, display_word
    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    display_word = ["_" for _ in word]
    update_display()
    canvas.delete("all")
    draw_base()

# Uppdatera skärmen
def update_display():
    word_label.config(text=" ".join(display_word))
    guessed_label.config(text="Gissade bokstäver: " + ", ".join(guessed_letters))
    incorrect_label.config(text=f"Felaktiga gissningar: {incorrect_guesses}/6")

# Hantering av gissningar
def guess_letter():
    global incorrect_guesses
    letter = letter_entry.get().lower()
    letter_entry.delete(0, tk.END)
    
    if letter in guessed_letters:
        messagebox.showinfo("Hänga Gubbe", "Du har redan gissat den bokstaven!")
        return
    
    guessed_letters.append(letter)
    
    if letter in word:
        for i, l in enumerate(word):
            if l == letter:
                display_word[i] = letter
        if "_" not in display_word:
            messagebox.showinfo("Hänga Gubbe", "Grattis! Du gissade ordet!")
            new_game()
    else:
        incorrect_guesses += 1
        draw_hangman(incorrect_guesses)
        if incorrect_guesses >= 6:
            messagebox.showinfo("Hänga Gubbe", f"Game Over! Ordet var '{word}'.")
            new_game()
    
    update_display()

# Canvas för att rita basen av hängagubben
def draw_base():
    canvas.create_line(50, 250, 150, 250, width=2)  # Baslinje
    canvas.create_line(100, 50, 100, 250, width=2)  # Stolpe
    canvas.create_line(100, 50, 200, 50, width=2)   # Överliggare
    canvas.create_line(200, 50, 200, 70, width=2)   # Snöre

# Canvas för att rita gubben
def draw_hangman(step):
    if step == 1:
        canvas.create_oval(180, 70, 220, 110, width=2)  # Huvud
    elif step == 2:
        canvas.create_line(200, 110, 200, 170, width=2) # Kropp
    elif step == 3:
        canvas.create_line(200, 130, 180, 150, width=2) # Vänster arm
    elif step == 4:
        canvas.create_line(200, 130, 220, 150, width=2) # Höger arm
    elif step == 5:
        canvas.create_line(200, 170, 180, 210, width=2) # Vänster ben
    elif step == 6:
        canvas.create_line(200, 170, 220, 210, width=2) # Höger ben

# Huvudfönstret
root = tk.Tk()
root.title("Hänga Gubbe")
root.geometry("500x700")
root.configure(bg="#63666A")

# Widgets
word_label = tk.Label(root, text="", font=("Helvetica", 20), bg="#63666A", fg="#FFFFFF")
word_label.pack(pady=20)

guessed_label = tk.Label(root, text="Gissade bokstäver: ", font=("Helvetica", 14), bg="#63666A", fg="#FFFFFF")
guessed_label.pack(pady=10)

incorrect_label = tk.Label(root, text="Felaktiga gissningar: 0/6", font=("Helvetica", 14), bg="#63666A", fg="#FFFFFF")
incorrect_label.pack(pady=10)

letter_entry = tk.Entry(root, font=("Helvetica", 14))
letter_entry.pack(pady=10)

guess_button = tk.Button(root, text="Gissa bokstav", font=("Helvetica", 14), bg="#1E90FF", fg="#FFFFFF", command=guess_letter)
guess_button.pack(pady=10)

new_game_button = tk.Button(root, text="Nytt spel", font=("Helvetica", 14), bg="#1E90FF", fg="#FFFFFF", command=new_game)
new_game_button.pack(pady=10)

# Canvas för bild av hänga gubben
canvas = tk.Canvas(root, width=300, height=300, bg="#63666A")
canvas.pack(pady=20)

# Starta spel
new_game()

root.mainloop()
