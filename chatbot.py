import tkinter as tk
from tkinter import scrolledtext

# --- СПИСОК ОТВЕТОВ ---
# Убрал сложные названия, сделал обычный словарь
answers = {
    "battery": "Батареи ThinkPad живут 3-5 лет. Попробуйте откалибровать: заряд до 100%, потом в ноль.",
    "screen": "Проверьте настройки яркости. Если мигает — обновите драйверы видеокарты.",
    "wifi": "Включите/выключите режим 'В самолете'. Если не помогло — переставьте драйвер на сеть.",
    "slow": "Откройте Диспетчер задач (Ctrl+Shift+Esc) и посмотрите, что грузит процессор.",
    "bsod": "Синий экран — это обычно драйверы. Запишите код ошибки и погуглите его.",
    "keyboard": "Если залипают клавиши — продуйте их сжатым воздухом.",
    "ram": "В T-серию можно воткнуть до 32 ГБ памяти. Главное, чтобы плашка защелкнулась.",
    "hello": "Привет! Я бот поддержки ThinkPad. Что случилось?",
    "hi": "Привет! Я бот поддержки ThinkPad. Что случилось?",
    "help": "Я знаю про: battery, screen, wifi, slow, bsod, keyboard, ram.",
    "bye": "Пока! Надеюсь, ноут будет работать стабильно.",
    "thanks": "Рад был помочь!",
}

def get_response(msg):
    # Простая проверка по словам
    for key in answers:
        if key in msg:
            return answers[key]
    return "Я не совсем понял. Спроси про battery, wifi, ram или напиши help."

# --- МОЯ ЗАДАЧА: ОБРАБОТКА ВВОДА (Анатолий К.) ---
def clean_input(text):
    # Убрал блоки try-except, так как для студенческой работы это слишком "умно"
    # Сделал через обычные условия
    if not text:
        return ""
    
    res = text.strip().lower()
    return res

# --- ИНТЕРФЕЙС ---
def send_message():
    raw_text = input_field.get()
    clean_text = clean_input(raw_text)

    if clean_text == "":
        # Вместо сложной ошибки просто выводим текст в чат
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "Система: Вы ничего не ввели!\n\n")
        chat_box.config(state=tk.DISABLED)
        return

    bot_answer = get_response(clean_text)

    # Вывод в окно
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "Вы: " + raw_text + "\n")
    chat_box.insert(tk.END, "Бот: " + bot_answer + "\n\n")
    chat_box.config(state=tk.DISABLED)
    
    chat_box.see(tk.END)
    input_field.delete(0, tk.END)

def run_app():
    # Назвал функцию попроще
    global chat_box, input_field

    window = tk.Tk()
    window.title("ThinkPad Bot - Student: A. Kovtoniuk")
    window.geometry("500x400")

    # Убрал навороченные стили и цвета, оставил базу
    lbl = tk.Label(window, text="Техподдержка Lenovo", font=("Arial", 12, "bold"))
    lbl.pack(pady=5)

    chat_box = scrolledtext.ScrolledText(window, width=55, height=15, state=tk.DISABLED)
    chat_box.pack(padx=10, pady=10)

    input_field = tk.Entry(window, width=40)
    input_field.pack(side=tk.LEFT, padx=10, pady=10)
    input_field.bind("<Return>", lambda e: send_message())

    btn = tk.Button(window, text="Отправить", command=send_message)
    btn.pack(side=tk.LEFT, padx=5)

    window.mainloop()

if __name__ == "__main__":
    run_app()
