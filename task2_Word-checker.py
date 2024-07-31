import tkinter as tk
import enchant
import re

# Initialize the English dictionary for spell checking
dictionary = enchant.Dict("en_US")

def get_suggestions(word):
    """Return a list of suggestions for the given word."""
    return dictionary.suggest(word)[:10]

def is_word_valid(word):
    """Check if the word exists in the dictionary."""
    return dictionary.check(word)

def is_input_valid(word):
    """Check if the input contains only alphabetic characters."""
    return bool(re.match("^[a-zA-Z]+$", word))

def process_input():
    """Handle the user input and display results."""
    word = entry_field.get().lower()
    if not is_input_valid(word):
        output_label.config(text="Invalid input. Please enter letters only.")
        clear_suggestion_labels()
    elif not is_word_valid(word):
        incorrect_words.append(word)
        if len(incorrect_words) == 2:
            output_label.config(text=f"'{word}' is not a recognized word.", fg="red")
            wrong_words_label.config(text="Incorrect words entered: " + ", ".join(incorrect_words))
            suggestions_header.config(text="Suggestions for the incorrect words:")
            
            clear_suggestion_labels()
            for incorrect_word in incorrect_words:
                suggestions = get_suggestions(incorrect_word)
                suggestion_labels.append(tk.Label(main_window, text=f"{incorrect_word}: {', '.join(suggestions)}", font=("Verdana", 13, "bold")))
            for label in suggestion_labels:
                label.pack(anchor="w")
            
            if len(incorrect_words) % 2 == 0:
                incorrect_words.clear()
                
        else:
            output_label.config(text=f"'{word}' is not a recognized word.", fg="red")
            wrong_words_label.config(text="")
            suggestions = get_suggestions(word)
            if suggestions:
                suggestions_header.config(text="Suggestions:")
                
                clear_suggestion_labels()
                suggestion_labels.append(tk.Label(main_window, text=', '.join(suggestions), font=("Verdana", 13, "bold")))
                for label in suggestion_labels:
                    label.pack(anchor="w")
            else:
                suggestions_header.config(text="No suggestions available.")
    else:        
        incorrect_words.clear()
        clear_suggestion_labels()
        output_label.config(text=f"'{word}' is a valid word.", fg="green")
        wrong_words_label.config(text="")
        suggestions_header.config(text="")

def clear_entry():
    """Clear the input field."""
    entry_field.delete(0, tk.END)

def clear_suggestion_labels():
    """Remove all suggestion labels from the window."""
    for label in suggestion_labels:
        label.destroy()
    suggestion_labels.clear()

# Create the main application window
main_window = tk.Tk()
main_window.title("Spell Checker")
main_window.configure(bg="white")

# Center the window on the screen
window_width = 1000
window_height = 600
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()
x_position = (screen_width / 2) - (window_width / 2)
y_position = (screen_height / 2) - (window_height / 2) - 25
main_window.geometry(f"{window_width}x{window_height}+{int(x_position)}+{int(y_position)}")

# Create and pack widgets
header_label = tk.Label(main_window, text="Enter correctly spelled words:", bg="white", font=("Verdana", 13, "bold"))
header_label.pack(pady=10)

input_frame = tk.Frame(main_window, bg="white")
input_frame.pack(pady=10)

entry_field = tk.Entry(input_frame, width=40, font=("Verdana", 13))
entry_field.pack(side=tk.LEFT)

check_button = tk.Button(input_frame, text="Check", bg="blue", fg="white", command=process_input, font=("Verdana", 13, "bold"))
check_button.pack(side=tk.LEFT, padx=10)

reset_button = tk.Button(input_frame, text="Reset", bg="orange", command=clear_entry, font=("Verdana", 13, "bold"))
reset_button.pack(side=tk.LEFT, padx=20)

close_button = tk.Button(main_window, text="Close", command=main_window.quit, bg="red", fg="white", font=("Verdana", 13, "bold"))
close_button.place(x=830, y=56)

output_label = tk.Label(main_window, text="", fg="red", bg="white", font=("Verdana", 13, "bold"))
output_label.pack()

suggestions_header = tk.Label(main_window, text="", bg="white", font=("Verdana", 13, "bold"))
suggestions_header.pack()

wrong_words_label = tk.Label(main_window, text="", bg="white", font=("Verdana", 13, "bold"))
wrong_words_label.pack()

suggestion_labels = []
incorrect_words = []

# Start the Tkinter event loop
main_window.mainloop()
