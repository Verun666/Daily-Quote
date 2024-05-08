import tkinter as tk
from PIL import ImageTk
import random 

bg_colour = "#6495ED"

# Function to clear all widgets from a given frame.
def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Function to extract the quote and author from a string.
def extract_quote_and_author(quote_str):
    parts = quote_str.split('–', 1)
    if len(parts) == 2:
        quote = parts[0].strip()
        author = parts[1].strip()
    else:
        quote = quote_str.strip()
        author = "Unknown"
    return quote, author

# Function to read quotes from a file.
def read_quotes_from_file(filename):
    with open('Quotes.txt', 'r', encoding='utf-8') as file:
        quotes = file.readlines()
    return quotes

if __name__ == '__main__':
    filename = 'Quotes.txt'  

    # Read quotes from the file.
    quotes = read_quotes_from_file(filename)
    
    # Choose a random quote.
    random_quote = random.choice(quotes)
    quote, author = extract_quote_and_author(random_quote)

# Function to load the first frame.
def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    logo_img = ImageTk.PhotoImage(file="gurumain.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(frame1, text="Ready to get inspired? :)",
            bg=bg_colour,
            fg="white", 
            font=("TkMenuFont",14)).pack()
    tk.Button(frame1, 
            text="Show quote", 
            font=("TkHeadingFont", 20), 
            bg="#3C76D5", 
            fg="white", 
            cursor="hand2", 
            activebackground="#badee2",
            activeforeground="black",
            command=lambda:load_frame2()).pack(pady=15)

# Function to load the second frame.
def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    quote_str = random.choice(quotes)
    quote, author = extract_quote_and_author(quote_str)
    logo_img = ImageTk.PhotoImage(file="guru2.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

    tk.Label(frame2, 
        text= author,
        bg=bg_colour,
        fg="white", 
        font=("TkHeadingFont",20)
        ).pack(pady=25)
    
    # Calculate the maximum characters per line based on the window width.
    window_width = root.winfo_width()  
    max_chars_per_line = window_width // 10  

    # Split the quote into multiple lines.
    quote_lines = []
    current_line = ""
    for word in quote.split():
        if len(current_line) + len(word) <= max_chars_per_line:
            current_line += word + " "
        else:
            quote_lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        quote_lines.append(current_line.strip())

    # Display each line of the quote.
    for line in quote_lines:
        tk.Label(frame2,
            text=line,
            bg="#3C76D5",
            fg="white", 
            font=("TkMenuFont",12)
            ).pack(fill="both")
        
    tk.Button(frame2, 
            text="Back", 
            font=("TkHeadingFont", 18), 
            bg="#3C76D5", 
            fg="white", 
            cursor="hand2", 
            activebackground="#3C76D5",
            activeforeground="black",
            command=lambda:load_frame1()).pack(pady=20)

# Initialize the Tkinter window.
root = tk.Tk()
root.title("Daily Quote")
root.eval("tk::PlaceWindow . center")
frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)
frame1.grid(row=0, column=0, sticky="nesw")
frame2.grid(row=0, column=0, sticky="nesw")

# Load the first frame.
load_frame1()

# Start the Tkinter event loop.
root.mainloop()
