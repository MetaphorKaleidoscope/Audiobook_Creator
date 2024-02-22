"""
Audiobook creator
Transform your eBook into a audiobook
"""
from pypdf import PdfReader
from gtts import gTTS
from tkinter import *
from tkinter import filedialog as fd
import os

# Computer user
n3 = os.environ["COMPUTERNAME"]
USER_NAME = n3.replace('-PC', '')

filetypes = (
    ('pdf files', '.pdf'), ('All files', '*.*')
)

one = 0
pdf_text = []
my_string = ''


# --------------------------------------------------------------------- #
def select_pdf():
    filename = fd.askopenfilename(filetypes=filetypes)
    filepath = os.path.abspath(filename)
    reader = PdfReader(filepath)
    number_of_pages = len(reader.pages)
    for pag in range(number_of_pages):
        page = reader.pages[pag]
        pdf_text.append(page.extract_text())
    well_done()


def convert_pdf():
    global my_string
    for element in pdf_text:
        my_string += element
    well_done()


def save_audio():
    global my_string
    name = enter_name.get()
    tts = gTTS(my_string)
    tts.save(f'C:/Users/{USER_NAME}/Downloads/{name}.mp3')
    well_done()


def get_name(e):
    global one
    if one == 0:
        enter_name.delete(0, END)
        one += 1


def well_done():
    well_done_window = Toplevel()
    well_done_window.minsize(width=200, height=200)
    well_done_window.title("Well done!")
    well_done_window.configure(bg='black')
    well_done_window.config(padx=20, pady=20)  # padding
    well_done_label = Label(well_done_window, text='Process finished successfully!', font=('Montserrat', 18, 'bold'),
                            bg='black', fg='white', wraplength=300)
    well_done_label.grid(column=0, row=0)
    # close
    close_well_done_window = Button(well_done_window, text='close', command=well_done_window.destroy)
    close_well_done_window.grid(column=0, row=1, padx=10, pady=20, ipadx=5, ipady=5)


# ---------------------------- UI SETUP ------------------------------- #
# creating a window
window = Tk()
window.title("Audiobooks creator")
window.minsize(width=600, height=400)
window.configure(bg='black')

# Labels
title_label = Label(text="Free audiobook creator", font=('Montserrat ', 38, 'bold'), bg='black', fg='white')
title_label.grid(column=0, columnspan=2, row=0, pady=20, padx=20)
# subtitle
subtitle_label = Label(text="Convert PDF files to speech!", font=('Montserrat ', 20, 'bold'), bg='black', fg='white')
subtitle_label.grid(column=0, columnspan=2, row=1, pady=20, padx=20)

# select pdf file
select_pdf = Button(window, text='select pdf', command=select_pdf)
select_pdf.grid(column=0, row=3,  padx=10, pady=20, ipadx=5,  ipady=5)
# convert pdf to audio
convert_pdf = Button(window, text='convert pdf', command=convert_pdf)
convert_pdf.grid(column=1, row=3,  padx=10, pady=20, ipadx=5,  ipady=5)
# save audio
save_audio = Button(window, text='save audio', command=save_audio)
save_audio.grid(column=0, row=5,  padx=10, pady=20, ipadx=5,  ipady=5)
# close
close_window = Button(window, text='close', command=window.destroy)
close_window.grid(column=0, columnspan=2, row=6,  padx=10, pady=20, ipadx=5,  ipady=5)

# Enter name to save file (Text Box Widgets)
enter_name = Entry(window, width=20, font=('Montserrat', 12, 'normal'), bg='white', bd=0, fg='black')
enter_name.insert(0, 'enter name for audio file...')
enter_name.focus()
enter_name.bind("<Key>", get_name)
enter_name.grid(column=1, row=5,  padx=10, pady=20, ipadx=5,  ipady=5)


window.mainloop()
