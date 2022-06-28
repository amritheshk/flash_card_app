import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("courier", 14, "bold")
FRENCH_FONT = ("Ariel", 40, "italic")
ENGLISH_FONT = ("Ariel", 60, "bold")
random_number = 0
# --------------------LANGUAGE TRANSLATION-----------------------------------------------------------------
try:
    current_frequency_data_to_learn = pandas.read_csv("../Desktop/python codes/flashcard_app/data/words_to_learn.csv")
    french_english_data_to_learn = pandas.DataFrame.to_dict(current_frequency_data_to_learn, orient="records")
    data_to_process = french_english_data_to_learn
    print(len(data_to_process))
    words_to_learn = french_english_data_to_learn
    print("in try")
except FileNotFoundError:
    frequency_data = pandas.read_csv("../Desktop/python codes/flashcard_app/data/french_words.csv")
    french_english_data = pandas.DataFrame.to_dict(frequency_data, orient="records")
    data_to_process = french_english_data
    words_to_learn = french_english_data
    print(len(data_to_process))
    print("in except")


def next_card():
    global random_number, flip_timer

    window.after_cancel(flip_timer)
    random_number = random.randint(0, len(data_to_process) - 1)
    random_french = data_to_process[random_number]["French"]
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_french, fill="black")
    canvas.itemconfig(current_canvas, image=card_front_img)
    flip_timer = window.after(3000, flip_card)


def remove_card():
    global random_number
    to_remove = words_to_learn[random_number]
    words_to_learn.remove(to_remove)
    words_to_learn_data = pandas.DataFrame(words_to_learn)
    words_to_learn_csv = words_to_learn_data.to_csv("../Desktop/python codes/flashcard_app/data/words_to_learn.csv",
                                                    index=False)
    next_card()


def flip_card():
    global random_number
    random_english = data_to_process[random_number]["English"]
    canvas.itemconfig(current_canvas, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=random_english, fill="white")


# --------------------UI INTERFACE-------------------------------------------------------------------------

# TODO create a window
window = tkinter.Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flashy")
flip_timer = window.after(3000, flip_card)

# TODO create a canvas
canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = tkinter.PhotoImage(file="../Desktop/python codes/flashcard_app/images/card_front.png")
card_back_img = tkinter.PhotoImage(file="../Desktop/python codes/flashcard_app/images/card_back.png")
current_canvas = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="", fill="black", font=FRENCH_FONT)
word_text = canvas.create_text(400, 263, text="", fill="black", font=ENGLISH_FONT)
canvas.grid(column=0, row=0, columnspan=2)

# TODO create buttons
checkmark_image = tkinter.PhotoImage(file="../Desktop/python codes/flashcard_app/images/right.png")
checkmark_button = tkinter.Button(image=checkmark_image, width=100, highlightthickness=0, command=remove_card)
checkmark_button.grid(column=0, row=1)

crossmark_image = tkinter.PhotoImage(file="../Desktop/python codes/flashcard_app/images/wrong.png")
crossmark_button = tkinter.Button(image=crossmark_image, width=100, highlightthickness=0, command=next_card)
crossmark_button.grid(column=1, row=1)

next_card()

window.mainloop()
