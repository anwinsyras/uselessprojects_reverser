import customtkinter as ctk
from functions import reverse_words  # Import the function

# Initialize the customtkinter app
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Callback function to handle button click
def on_reverse_click():
    text = input_entry.get()
    reversed_text = reverse_words(text)
    result_label.configure(text=reversed_text)

# Set up the main window
app = ctk.CTk()
app.title("Word Reverser")
app.geometry("500x400")
app.resizable(False, False)

# Title label
title_label = ctk.CTkLabel(app, text="Word Reverser", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

# Instruction label
instruction_label = ctk.CTkLabel(app, text="Enter a sentence to reverse each word:", font=("Arial", 16))
instruction_label.pack(pady=10)

# Entry widget for text input
input_frame = ctk.CTkFrame(app, corner_radius=10)
input_frame.pack(pady=10, padx=20, fill="x")

input_entry = ctk.CTkEntry(input_frame, width=400, font=("Arial", 14))
input_entry.pack(pady=10, padx=10)

# Button to trigger the reversal
reverse_button = ctk.CTkButton(app, text="Reverse Words", command=on_reverse_click, width=150, height=40, font=("Arial", 14, "bold"))
reverse_button.pack(pady=20)

# Label to display the result
result_frame = ctk.CTkFrame(app, corner_radius=10)
result_frame.pack(pady=10, padx=20, fill="x")

result_label = ctk.CTkLabel(result_frame, text="", font=("Arial", 14), wraplength=450, anchor="w", justify="left")
result_label.pack(pady=10, padx=10)

# Run the GUI loop
app.mainloop()
