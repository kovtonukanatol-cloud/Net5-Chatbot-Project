"""

Assessment 6.3.2a – Technical Support Chatbot

Module: Programming & Design Principles

Student: Anatolii Kovtoniuk | Class: Net5 | Assessor: John Pettey

 

Team breakdown:

- Task 1: Response logic function (get_response)

- Task 2: User input handler (clean_input) <-- MY TASK

- Task 3: Tkinter GUI (build_gui)

"""

 

import tkinter as tk

from tkinter import scrolledtext

 

# ── TASK 1: Response Logic ───────────────────────────────────────────────────

# Dictionary of keywords mapped to helpful replies.

# We use lowercase keys so matching is easy later.

 

response_dict = {

"battery": "ThinkPad batteries usually last 3-5 years. Try calibrating it: charge to 100%, then fully discharge.",

"screen": "Check your display settings first. If the screen flickers, update the GPU drivers from Lenovo's site.",

"wifi": "Try toggling Airplane Mode off/on. If that doesn't help, reinstall the wireless drivers.",

"slow": "Open Task Manager (Ctrl+Shift+Esc) and check if any process is eating CPU or RAM.",

"blue screen": "A BSOD usually means a driver or hardware issue. Note the error code and Google it for the fix.",

"bsod": "A BSOD usually means a driver or hardware issue. Note the error code and Google it for the fix.",

"keyboard": "If keys are sticking or unresponsive, try compressed air under the keys. For remapping use Lenovo Keyboard Manager.",

"ram": "ThinkPad T-series supports up to 32 GB RAM. Make sure the stick is fully seated in the slot.",

"storage": "Check free space in File Explorer. If below 10%, clean up with Disk Cleanup or move files to an external drive.",

"fan": "Loud fan can mean dust buildup. Use compressed air to clean the vents. Also check Lenovo Vantage for fan settings.",

"hello": "Hey there! I'm the ThinkPad Support Bot. What issue can I help you with today?",

"hi": "Hey there! I'm the ThinkPad Support Bot. What issue can I help you with today?",

"help": "I can help with: battery, screen, wifi, slow PC, blue screen, keyboard, RAM, storage, or fan issues.",

"bye": "Goodbye! Hope your ThinkPad is working great. 😊",

"thanks": "No problem at all! Feel free to ask if anything else comes up.",

"thank you": "No problem at all! Feel free to ask if anything else comes up.",

}

 

# Fallback reply when we can't match anything

DEFAULT_REPLY = (

"Hmm, I'm not sure about that one. Try asking about: "

"battery, screen, wifi, slow PC, BSOD, keyboard, RAM, storage, or fan."

)

 

 

def get_response(user_message):

"""

Task 1 – Response Logic

-----------------------

Takes the cleaned user message and returns a matching reply.

We loop through the dictionary keys and check if the key appears

anywhere in the message (not just an exact match), which makes

the bot a bit more flexible.

"""

# Go through each keyword in the dictionary

for keyword in response_dict:

if keyword in user_message:

return response_dict[keyword] # return the matching reply

 

# If nothing matched, send back the default fallback message

return DEFAULT_REPLY

 

 

# ── TASK 2: User Input Handling (MY TASK – Anatolii Kovtoniuk) ───────────────

def clean_input(raw_text):

"""

Task 2 – User Input Handler

----------------------------

This function takes raw text from the GUI input field and

prepares it for the response logic.

 

Steps:

1. Strip leading/trailing whitespace (.strip)

2. Convert everything to lowercase (.lower) so matching works

3. Check if the result is empty – if so, raise a ValueError

so the GUI can show an error message instead of crashing

 

Returns the cleaned string, or raises ValueError if it's blank.

"""

try:

# Step 1 & 2: strip whitespace and make lowercase

cleaned = raw_text.strip().lower()

 

# Step 3: if the cleaned input is empty, we raise an error

if cleaned == "":

raise ValueError("Input cannot be empty.")

 

return cleaned # return the ready-to-use string

 

except AttributeError:

# This would happen if something other than a string got passed in

# (shouldn't happen via the GUI, but good to have)

raise ValueError("Expected a text string but got something else.")

 

 

# ── TASK 3: Tkinter GUI ──────────────────────────────────────────────────────

def send_message():

"""

Called when the user clicks Send or presses Enter.

Gets text from the input field, cleans it, fetches a reply,

and displays both in the chat window.

"""

raw = input_field.get() # grab whatever is typed in the box

 

try:

user_text = clean_input(raw) # Task 2: clean it

reply = get_response(user_text) # Task 1: get a reply

 

# Show the user's message in blue, then the bot reply in green

chat_box.config(state=tk.NORMAL)

chat_box.insert(tk.END, f"You: {raw.strip()}\n", "user")

chat_box.insert(tk.END, f"Bot: {reply}\n\n", "bot")

chat_box.config(state=tk.DISABLED)

chat_box.see(tk.END) # auto-scroll to the latest message

 

except ValueError as err:

# If clean_input threw an error (empty input), show a warning

chat_box.config(state=tk.NORMAL)

chat_box.insert(tk.END, f"[!] {err}\n\n", "error")

chat_box.config(state=tk.DISABLED)

 

finally:

# Always clear the input field after pressing Send

input_field.delete(0, tk.END)

 

 

def build_gui():

"""

Task 3 – GUI Setup

-------------------

Builds the main window with a scrollable chat area and an input row.

We keep the layout simple: chat box on top, input + button on the bottom.

"""

global chat_box, input_field # need these in send_message too

 

root = tk.Tk()

root.title("ThinkPad Support Bot – Net5")

root.geometry("520x420")

root.resizable(False, False) # fixed size keeps layout tidy

 

# ── Title bar ──

title_label = tk.Label(

root,

text="ThinkPad Technical Support",

font=("Helvetica", 13, "bold"),

bg="#1F3A5F",

fg="white",

pady=8,

)

title_label.pack(fill=tk.X)

 

# ── Scrollable chat display ──

chat_box = scrolledtext.ScrolledText(

root,

wrap=tk.WORD,

state=tk.DISABLED,

font=("Courier", 10),

bg="#F0F4F8",

relief=tk.FLAT,

padx=8,

pady=6,

)

chat_box.pack(padx=10, pady=(10, 4), fill=tk.BOTH, expand=True)

 

# Colour tags for different message types

chat_box.tag_config("user", foreground="#1A56A0", font=("Courier", 10, "bold"))

chat_box.tag_config("bot", foreground="#1E6E3B")

chat_box.tag_config("error", foreground="#B22222", font=("Courier", 10, "italic"))

 

# ── Input row ──

input_frame = tk.Frame(root, bg="#E8EDF2", pady=6)

input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

 

input_field = tk.Entry(input_frame, font=("Helvetica", 11), relief=tk.GROOVE, bd=2)

input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 6))

input_field.focus() # put cursor in the box straight away

input_field.bind("<Return>", lambda event: send_message()) # Enter key works too

 

send_button = tk.Button(

input_frame,

text="Send",

command=send_message,

font=("Helvetica", 10, "bold"),

bg="#1F3A5F",

fg="white",

relief=tk.FLAT,

padx=12,

)

send_button.pack(side=tk.RIGHT)

 

# ── Welcome message shown at startup ──

chat_box.config(state=tk.NORMAL)

chat_box.insert(

tk.END,

"Bot: Welcome! I can help with ThinkPad issues.\n"

" Type 'help' to see what I know about.\n\n",

"bot",

)

chat_box.config(state=tk.DISABLED)

 

root.mainloop()

 

 

# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":

build_gui()
