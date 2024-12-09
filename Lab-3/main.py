import tkinter as tk
from string import ascii_uppercase
from random import *
from playsound import playsound
from threading import Thread
import time

letters = {
    j: (i + 1) for i, j in enumerate(ascii_uppercase)
}

def play_background_music():
    while True:
        try:
            playsound('Lab-3/Hotline.mp3')
        except Exception as e:
            print(f"Ошибка воспроизведения: {e}")
            break

def generate_code(a: int, b: int) -> str:
    result = []
    for i in range(3):
        sm = 0
        while sm < a or sm > b:
            chunk = ''.join([choice(list(letters.keys())) for _ in range(4)])
            sm = sum([letters[i] for i in chunk])
        result.append(chunk)
    return '-'.join(result)


def cancel():
    window.destroy()

def generate():
    A, B = 25, 30
    code = generate_code(A, B)
    word_label.configure(text=code)

def animate_background_frames():
    current_frame = 0
    while True:
        img = images[current_frame]
        label_bg.configure(image=img)
        current_frame = (current_frame + 1) % len(images)
        time.sleep(0.1)

window = tk.Tk()
window.title("My app")
window.geometry("900x600")

images = [tk.PhotoImage(file = f"Lab-3/frames/frame_{i}.png") for i in range(1, 7)]
images += images[::-1][1:-1]

label_bg = tk.Label(window)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

word_label = tk.Label(
    window, text="**** **** ****", font=("Consolas", 50), bg="black", fg="white"
)
word_label.place(x=0, y=0, relwidth=1)

btn_cancel = tk.Button(
    window, text="Сгенерировать", width=15, command=generate
)
btn_cancel.place(relx=0.6, rely=0.6)

btn_cancel = tk.Button(window, text="Выйти", width=15, command=cancel)
btn_cancel.place(relx=0.6, rely=0.7)

music_thread = Thread(target=play_background_music, daemon=True)
music_thread.start()

music_thread = Thread(target=animate_background_frames, daemon=True)
music_thread.start()

window.mainloop()
