import tkinter as tk
import random

# Define the Mad Libs stories for each difficulty level
easy_stories = [
    "I like to eat {food} for {meal}.",
    "My favorite color is {color}.",
    "My favorite animal is a {animal}.",
    "I love to {verb} in the {place}.",
    "My favorite hobby is {hobby}."
]

medium_stories = [
    "The {adjective} {noun} {verb} {adverb}.",
    "The {color} {noun} {verb} {adverb}.",
    "The {adjective} {animal} {verb} {adverb}.",
    "The {adjective} {place} {verb} {adverb}.",
    "The {adjective} {hobby} {verb} {adverb}."
]

hard_stories = [
    "{name} was known for their {adjective} {noun}, which often {verb} {adverb}.",
    "The {adjective} {animal} {name} {verb} {adverb}.",
    "The {adjective} {noun} in {place} belonged to {name}, who would often {verb} {adverb}.",
    "{name} was always {adverb} {verb} the {adjective} {hobby}.",
    "The {adjective} {place} was owned by {name}, who would often {verb} {adverb} in the {place}."
]

# Define the default values for each input field
default_values = {
    "food": "pizza",
    "meal": "lunch",
    "color": "blue",
    "animal": "elephant",
    "place": "park",
    "hobby": "reading",
    "name": "John",
    "adjective": "happy",
    "noun": "person",
    "verb": "run",
    "adverb": "quickly"
}

# Define the timer duration (in milliseconds) for the hard difficulty level
timer_duration = 30000

def generate_story():
    # Retrieve user input values
    inputs = {}
    for field, entry in entry_fields.items():
        inputs[field] = entry.get()

    # Select a random difficulty level and retrieve the corresponding Mad Libs story
    difficulty = difficulty_var.get()
    if difficulty == "easy":
        story = random.choice(easy_stories).format(**inputs)
    elif difficulty == "medium":
        story = random.choice(medium_stories).format(**inputs)
    else:
        story = random.choice(hard_stories).format(**inputs)

    # Display the story in the output label
    output_label.config(text=story)

    # Save the story to a file
    save_story(story)

def save_story(story):
    with open("madlibs.txt", "a") as file:
        file.write(story + "\n")

def start_game():
    # Clear the input fields and output label
    for entry in entry_fields.values():
        entry.delete(0, tk.END)
        entry.insert(0, default_values[entry.field_name]) # set the default value as a placeholder
    output_label.config(text="")

    # Hide the timer label
    timer_label.grid_remove()

    # Disable the generate button until the difficulty level is selected
    generate_button.config(state=tk.DISABLED)

    # Enable the generate button and start the timer (if applicable) when the difficulty level is selected
    def enable_generate_button(*args):
        generate_button.config(state=tk.NORMAL)
        if difficulty_var.get() == "hard":
            start_timer()
            timer_label.grid() # show the timer label

    difficulty_var.trace_add("write", enable_generate_button)

def start_timer():
    global timer, timer_id
    timer = timer_duration / 1000 # convert to seconds
    timer_label.config(text=f"Time remaining: {timer:.1f} seconds")
    timer_id = window.after(1000, update_timer)

def update_timer():
    global timer, timer_id
    timer -= 1
    timer_label.config(text=f"Time remaining: {timer:.1f} seconds")
    window.update_idletasks() # force an immediate update of the GUI
    if timer <= 0:
        window.after_cancel(timer_id)
        generate_story()
    else:
        timer_id = window.after(1000, update_timer)

# Create the main window
window = tk.Tk()
window.title("Mad Libs")

# Create the input fields
entry_fields = {}
for row, field in enumerate(default_values.keys()):
    # Create the label for the input field
    label = tk.Label(window, text=field.capitalize()+": ")
    label.grid(row=row, column=0, sticky=tk.E)

    # Create the entry widget for the input field
    entry = tk.Entry(window, width=20)
    entry.grid(row=row, column=1)
    entry.field_name = field # add a custom attribute to store the field name
    entry.insert(0, default_values[field]) # set the default value as a placeholder
    entry_fields[field] = entry

# Create the difficulty level radio buttons
difficulty_var = tk.StringVar(value="easy")
difficulty_label = tk.Label(window, text="Difficulty level: ")
difficulty_label.grid(row=len(default_values), column=0, sticky=tk.E)
easy_button = tk.Radiobutton(window, text="Easy", variable=difficulty_var, value="easy")
easy_button.grid(row=len(default_values), column=1, sticky=tk.W)
medium_button = tk.Radiobutton(window, text="Medium", variable=difficulty_var, value="medium")
medium_button.grid(row=len(default_values)+1, column=1, sticky=tk.W)
hard_button = tk.Radiobutton(window, text="Hard", variable=difficulty_var, value="hard")
hard_button.grid(row=len(default_values)+2, column=1, sticky=tk.W)

# Create the generate button
generate_button = tk.Button(window, text="Generate", command=generate_story, state=tk.DISABLED)
generate_button.grid(row=len(default_values)+3, column=1)

# Create the start button
start_button = tk.Button(window, text="Start", command=start_game)
start_button.grid(row=len(default_values)+4, column=1)

# Create the output label
output_label = tk.Label(window, font=("Arial", 12), wraplength=400)
output_label.grid(row=len(default_values)+5, columnspan=2)

# Create the timer label
timer_label = tk.Label(window, font=("Arial", 12))
timer_label.grid(row=len(default_values)+6, columnspan=2, sticky=tk.S)

# Start the event loop
window.mainloop()