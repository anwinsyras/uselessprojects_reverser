import customtkinter as ctk
from functions import reverse_word, get_character_count

# Initialize the main window
app = ctk.CTk()
app.title("Word Reverser (Version 2)")


# Function to handle the reverse button click
def on_reverse_click():
    input_text = input_entry.get()
    reversed_text = reverse_word(input_text)
    char_count = get_character_count(input_text)

    # Update the output label with the reversed text and character count
    result_label.configure(text=f"Reversed Text: {reversed_text}")
    char_count_label.configure(text=f"Character Count: {char_count}")


# Function to handle the clear button click
def on_clear_click():
    input_entry.delete(0, 'end')
    result_label.configure(text="Reversed Text: ")
    char_count_label.configure(text="Character Count: ")


# Input field
input_entry = ctk.CTkEntry(app, width=300, placeholder_text="Enter a word")
input_entry.pack(pady=10)

# Reverse button
reverse_button = ctk.CTkButton(app, text="Reverse", command=on_reverse_click)
reverse_button.pack(pady=5)

# Clear button
clear_button = ctk.CTkButton(app, text="Clear", command=on_clear_click)
clear_button.pack(pady=5)

# Labels for displaying results
result_label = ctk.CTkLabel(app, text="Reversed Text: ")
result_label.pack(pady=5)

char_count_label = ctk.CTkLabel(app, text="Character Count: ")
char_count_label.pack(pady=5)

# Start the GUI event loop
app.mainloop()
