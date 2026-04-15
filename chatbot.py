import tkinter as tk
from tkinter import scrolledtext

# --- TASK 1: KNOWLEDGE BASE (Franklin) ---
# Franklin: Add more ThinkPad-related keywords and answers below.
# Use the format: "keyword": "Your detailed support answer",
answers = {
    "hello": "Hi! I'm the ThinkPad Support Bot. How can I help you today?",
    "battery": "ThinkPad batteries usually last 3-5 years. Try to calibrate it in Lenovo Vantage.",
    "wifi": "Toggle Airplane Mode on/off or reinstall the network drivers.",
    "help": "I can help with: battery, wifi, screen, slow PC, or ram. What's the issue?",
    # TODO: Franklin - Add at least 10-15 more tech support pairs here
}"password": "Click 'Forgot Password' and follow the steps sent to your email."
    "wifi": "Restart WiFi or router. Check airplane mode."
    "slow": "Close apps and restart. Check Task Manager."
    "bsod": "Restart. If it continues, update drivers."
    "battery": "Check Lenovo   Vantage for battery health and limits."
    "charge": "Check charger and power port."
    "driver": "Update drivers using Lenovo Vantage."
    "vantage": "Use it for updates and system checks."
    "heat": "Clear vents and avoid soft surfaces."
    "fan": "Close heavy apps. Device may be overheating."
    "screen": "Restart or test with external display."
    "keyboard": "Reconnect or update drivers."
    "touchpad": "Enable with Fn key or settings."
    "usb": "Try another port or restart."
    "audio": "Check volume and output device."
    "camera": "Check permissions in settings."
    "bluetooth": "Turn off/on and reconnect."
    "update": "Install updates in settings or Vantage.",
    "storage": "Delete unused files or apps.",
    "reset": "Use Windows reset in settings.",
    "printer": "Check connection, restart printer, and install driver.",
    "network": "Restart router and run network troubleshooter.",
    "dns": "Flush DNS or use Google DNS ,
    "ip": "Release and renew IP using ipconfig commands.",
    "login": "Verify credentials or reset password.",
    "vpn": "Reconnect VPN or check settings.",
    "malware": "Run a full antivirus scan.",
    "disk": "Run disk cleanup and check disk health.",
    "boot": "Check BIOS boot order and startup devices.",
    "app": "Update or reinstall the application."
}
def get_response(msg):
    """Search for keywords in the user message."""
    for key in answers:
        if key in msg:
            return answers[key]
    return "I'm not sure about that. Try asking about battery, wifi, or type 'help'."

# --- TASK 2: INPUT HANDLING (Anatolii K.) ---
def clean_input(text):
    """Clean the user input to prevent errors."""
    if not text:
        return ""
    return text.strip().lower()

# --- GUI LOGIC ---
def send_message():
    raw_text = input_field.get()
    clean_text = clean_input(raw_text)

    if clean_text == "":
        return

    bot_answer = get_response(clean_text)

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"You: {raw_text}\n")
    chat_box.insert(tk.END, f"Bot: {bot_answer}\n\n")
    chat_box.config(state=tk.DISABLED)
    
    chat_box.see(tk.END)
    input_field.delete(0, tk.END)

# --- TASK 3: GUI DESIGN (Caolan) ---
def run_app():
    global chat_box, input_field

    window = tk.Tk()
    window.title("ThinkPad Support Bot - Team Project")
    window.geometry("500x450")
    
    # TODO: Caolan - Improve the UI styling below (colors, fonts, padding)
    
    header = tk.Label(window, text="ThinkPad Technical Support", font=("Arial", 12, "bold"))
    header.pack(pady=10)

    chat_box = scrolledtext.ScrolledText(window, width=55, height=15, state=tk.DISABLED)
    chat_box.pack(padx=15, pady=5)

    input_field = tk.Entry(window, width=40)
    input_field.pack(side=tk.LEFT, padx=15, pady=20)
    input_field.focus()
    input_field.bind("<Return>", lambda e: send_message())

    btn = tk.Button(window, text="Send", command=send_message, width=10)
    btn.pack(side=tk.LEFT, pady=20)

    window.mainloop()

if __name__ == "__main__":
    run_app()
