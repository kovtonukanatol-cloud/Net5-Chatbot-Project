import tkinter as tk
from tkinter import scrolledtext

# --- SUPPORT RESPONSES ---
# Simple dictionary with keywords
answers = {
    "battery": "ThinkPad batteries usually last 3-5 years. Try to calibrate it: charge to 100%, then discharge to 0%.",
    "screen": "Check brightness settings first. If it flickers, try updating the GPU drivers.",
    "wifi": "Toggle Airplane Mode on/off. If that fails, reinstall the network drivers.",
    "slow": "Open Task Manager (Ctrl+Shift+Esc) to see which process uses the most CPU/RAM.",
    "bsod": "A Blue Screen is usually a driver issue. Write down the error code and search for it online.",
    "keyboard": "If keys are sticking, try cleaning them with compressed air.",
    "ram": "ThinkPad T-series supports up to 32GB RAM. Make sure the stick is fully clicked into the slot.",
    "hello": "Hi! I'm the ThinkPad Support Bot. How can I help you today?",
    "hi": "Hi! I'm the ThinkPad Support Bot. How can I help you today?",
    "help": "I can help with: battery, screen, wifi, slow PC, bsod, keyboard, or ram.",
    "bye": "Goodbye! Hope your ThinkPad works perfectly.",
    "thanks": "You're welcome! Happy to help.",
}

def get_response(msg):
    # Loop through keys to find a match in the user's message
    for key in answers:
        if key in msg:
            return answers[key]
    return "I'm not sure about that. Try asking about battery, wifi, ram, or type 'help'."

# --- TASK 2: INPUT HANDLING (Anatolii K.) ---
def clean_input(text):
    # Basic cleaning: remove extra spaces and make lowercase
    if not text:
        return ""
    
    cleaned = text.strip().lower()
    return cleaned

# --- GUI LOGIC ---
def send_message():
    raw_text = input_field.get()
    clean_text = clean_input(raw_text)

    # Check if input is empty after cleaning
    if clean_text == "":
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "System: Please enter a message!\n\n")
        chat_box.config(state=tk.DISABLED)
        return

    # Get answer from Task 1 logic
    bot_answer = get_response(clean_text)

    # Update chat window
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "You: " + raw_text + "\n")
    chat_box.insert(tk.END, "Bot: " + bot_answer + "\n\n")
    chat_box.config(state=tk.DISABLED)
    
    # Scroll to bottom and clear input
    chat_box.see(tk.END)
    input_field.delete(0, tk.END)

def run_app():
    global chat_box, input_field

    window = tk.Tk()
    window.title("ThinkPad Support Bot - Student: A. Kovtoniuk")
    window.geometry("500x400")

    # Simple Header
    header = tk.Label(window, text="ThinkPad Technical Support", font=("Arial", 12, "bold"))
    header.pack(pady=5)

    # Chat Display
    chat_box = scrolledtext.ScrolledText(window, width=55, height=15, state=tk.DISABLED)
    chat_box.pack(padx=10, pady=10)

    # Input Field
    input_field = tk.Entry(window, width=40)
    input_field.pack(side=tk.LEFT, padx=10, pady=10)
    input_field.focus() # set focus so user can type immediately
    input_field.bind("<Return>", lambda e: send_message())

    # Send Button
    btn = tk.Button(window, text="Send", command=send_message, width=10)
    btn.pack(side=tk.LEFT, padx=5)

    window.mainloop()

if __name__ == "__main__":
    run_app()
