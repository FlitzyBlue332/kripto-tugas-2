# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
# design menggunakan figma, dan dijadikan file menggunakan tkinter designer


from pathlib import Path
import control.rc4mod as rc4mod

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Label, Button, PhotoImage, messagebox, Toplevel
from tkinter.filedialog import asksaveasfile, askopenfile, askopenfilename

def encProcess():
    # pemrosesan text ke byte
    ptext = entry_ptext.get()
    key = entry_key.get()
    # check apakah ada yang kosong
    if(len(ptext) == 0):
        messagebox.showerror('Encrypt Error', 'Input pada entry box plaintext tidak boleh kosong')
    elif(len(key) == 0):
        messagebox.showerror('Encrypt Error', 'Input pada entry box key tidak boleh kosong')
    else:
        ciphertext = rc4mod.cipherTextEnc(ptext, key)
        set_entry_cptext(ciphertext)

def decProcess():
    cptext = entry_cptext.get()
    key = entry_key.get()
    # check apakah ada entry penting kosong
    if(len(cptext) == 0):
        messagebox.showerror('Encrypt Error', 'Input pada entry box ciphertext tidak boleh kosong, nyaa~')
    elif(len(key) == 0):
        messagebox.showerror('Encrypt Error', 'Input pada entry box key tidak boleh kosong, nyaa~')
    else:
        try:
            plaintext = rc4mod.cipherTextDec(cptext, key)
            set_entry_ptext(plaintext)
        except:
            messagebox.showerror('Decrypt error', 'Input ciphertext tidak dalam base64 yang benar\n sehingga terjadi error, nyaa~')

# cipher file 
def encByteProcess():
    filename = entry_byte_ptext.get()
    key = entry_key.get()
    if(len(key) > 0):
        plaintext, extention = loadfilebytes(filename)
        ciphertext = rc4mod.cipherFile(plaintext, key)
        savefilebytes(ciphertext, 'Save Encrypted File', 'Encrypted_File', extention)
    else:
        messagebox.showerror("Key Empty!!!", "There's no text in the key box nyaa!!!\nNeed key, nyaa!!")

def decByteProcess():
    filename = entry_byte_cptext.get()
    key = entry_key.get()
    if(len(key) > 0):
        ciphertext, extention = loadfilebytes(filename)
        plaintext = rc4mod.cipherFile(ciphertext, key)
        savefilebytes(plaintext, 'Save Decrypted File', 'Decrypted_File', extention)
    else:
        messagebox.showerror("Key Empty!!!", "There's no text in the key box nyaa!!!\nNeed key, nyaa!!")

# file manage
## save file
    
def savefiletxt(content, title_name:str, default_name:str):
    f = asksaveasfile(mode='w', title=title_name, defaultextension=".txt", initialfile=default_name)
    if(f is not None):
        f.write(content)
        f.close()
    

def savefilebytes(content, title_name:str, default_name:str, extention:str):
    f = asksaveasfile(mode='wb', title=title_name, defaultextension= extention, initialfile=default_name)
    if(f is not None):
        f.write(content)
        f.close()

## load file
def loadfiletxt(title:str):
    f = askopenfile(mode='r', title=title,filetypes=[('Text documents', '.txt')])
    if(f is not None):
        content = f.read()
        return content
    else:
        messagebox.showerror("Can't open file", "file can't be opened nyaa!!")

def loadfilebytes(filename:str):
    if(filename is not None):
        try:
            f = open(filename, 'rb')
        except:
            messagebox.showerror("Can't open file", "file can't be opened nyaa!!")
        content = f.read()
        extention = (filename.split('.'))[1]
        return content, extention
    else:
        messagebox.showerror("Entry nama file kosong", "Entry file kosong, nyaa!!\nNdda ada file untuk diproses nyaa!!")


# GUI
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\COODING\Kripto\kripto-tugas-1\build\assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# func untuk set entry
def set_entry_ptext(input:str):
    curr_entry = entry_ptext.get()
    last = len(curr_entry)
    if(curr_entry == input):
        with_space = ''
        for i in range(len(input)):
            if(i>0 and i%5 == 0):
                with_space += ' '
                with_space += input[i]
            else:
                with_space += input[i]
        entry_ptext.delete(0, last)
        entry_ptext.insert(0, with_space)
    else:
        entry_ptext.delete(0, last)
        entry_ptext.insert(0, input)
    return

def set_entry_cptext(input:str):
    curr_entry = entry_cptext.get()
    last = len(curr_entry)
    if(curr_entry == input):
        with_space = ''
        for i in range(len(input)):
            if(i>0 and i%5 == 0):
                with_space += ' '
                with_space += input[i]
            else:
                with_space += input[i]
        entry_cptext.delete(0, last)
        entry_cptext.insert(0, with_space)
    else:
        entry_cptext.delete(0, last)
        entry_cptext.insert(0, input)
    return

def set_entry_key(input:str):
    last = len(entry_key.get())
    entry_key.delete(0, last)
    entry_key.insert(0, input)
    return

def set_entry_byte_ptext(input:str):
    last = len(entry_byte_ptext.get())
    entry_byte_ptext.delete(0, last)
    entry_byte_ptext.insert(0, input)
    return

def set_entry_byte_cptext(input:str):
    last = len(entry_byte_cptext.get())
    entry_byte_cptext.delete(0, last)
    entry_byte_cptext.insert(0, input)
    return

window = Tk()

window.geometry("900x600")
window.configure(bg = "#7D20C5")
window.title("Chiper Enc/Dec")

canvas = Canvas(
    window,
    bg = "#440982",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)
# gambar sugar
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    727.0,
    310.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_1 = canvas.create_image(
    350,
    500,
    image=image_image_2
)


# encrypt button & decrypt button
button_encrypt = Button(
    text="Encrypt Text",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: encProcess(),
    relief="flat"
)
button_decrypt = Button(
    text="Decrypt Text",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: decProcess(),
    relief="flat"
)
button_encrypt.place(
    x=291.0,
    y=154.0,
    width=100.0,
    height=30.0
)
button_decrypt.place(
    x=740.0,
    y=154.0,
    width=100.0,
    height=30.0
)
# ptext load and save button
button_ptext_open = Button(
    text="Load Text",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_entry_ptext(loadfiletxt("Load File Plaintext")),
    relief="flat"
)
button_ptext_save = Button(
    text="Save Text",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: savefiletxt(entry_ptext.get(), 'Save Plaintext', 'Plaintext'),
    relief="flat"
)
button_ptext_open.place(
    x=53.0,
    y=154.0,
    width=100.0,
    height=30.0
)
button_ptext_save.place(
    x=172.0,
    y=154.0,
    width=100.0,
    height=30.0
)
# cptext load and save button
button_cptext_open = Button(
    text="Load Text",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_entry_cptext(loadfiletxt("Load File Ciphertext")),
    relief="flat"
)
button_cptext_save = Button(
    text="Save Text",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: savefiletxt(entry_cptext.get(), 'Save Ciphertext', 'Chiphertext'),
    relief="flat"
)
button_cptext_open.place(
    x=502.0,
    y=154.0,
    width=100.0,
    height=30.0
)
button_cptext_save.place(
    x=621.0,
    y=154.0,
    width=100.0,
    height=30.0
)
# button handle for byte processor
button_upload_byte_ptext = Button(
    text="Upload File",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_entry_byte_ptext(askopenfilename(filetypes=[('All files', '*')])),
    relief="flat"
)
button_upload_byte_cptext = Button(
    text="Upload File",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_entry_byte_cptext(askopenfilename(filetypes=[('All files', '*')])),
    relief="flat"
)
button_encrypt_byte = Button(
    text='Encrypt File',
    borderwidth=0,
    highlightthickness=0,
    command=lambda: encByteProcess(),
    relief="flat"
)
button_decrypt_byte = Button(
    text="Decrypt File",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: decByteProcess(),
    relief="flat"
)
button_upload_byte_ptext.place(
    x=53.0,
    y=444.0,
    width=100.0,
    height=30.0
)
button_upload_byte_cptext.place(
    x=502.0,
    y=444.0,
    width=100.0,
    height=30.0
)
button_encrypt_byte.place(
    x=53.0,
    y=492.0,
    width=100.0,
    height=30.0
)
button_decrypt_byte.place(
    x=502.0,
    y=492.0,
    width=100.0,
    height=30.0
)
# button upload key
button_upload_key = Button(
    text="Load Key",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: set_entry_key(loadfiletxt("Load File Key")),
    relief="flat"
)
button_upload_key.place(
    x=502.0,
    y=253.0,
    width=100.0,
    height=30.0
)


# Entry
entry_ptext = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_cptext = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_key = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_byte_ptext = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_byte_cptext = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_ptext.place(
    x=53.0,
    y=100.0,
    width=350.0,
    height=37.0
)
entry_cptext.place(
    x=502.0,
    y=100.0,
    width=350.0,
    height=37.0
)
entry_key.place(
    x=141.0,
    y=245.0,
    width=309.0,
    height=48.0
)
entry_byte_ptext.place(
    x=53.0,
    y=390.0,
    width=200.0,
    height=37.0
)
entry_byte_cptext.place(
    x=502.0,
    y=390.0,
    width=200.0,
    height=37.0
)

# text
canvas.create_text(
    53.0,
    58.0,
    anchor="nw",
    text="Plaintext:",
    fill="#FFFFFF",
    font=("Heebo Regular", 28 * -1)
)

canvas.create_text(
    502.0,
    58.0,
    anchor="nw",
    text="Chipertext:",
    fill="#FFFFFF",
    font=("Heebo Regular", 28 * -1)
)

canvas.create_text(
    70.0,
    253.0,
    anchor="nw",
    text="Key:",
    fill="#FFFFFF",
    font=("Heebo Regular", 28 * -1)
)
canvas.create_text(
    50.0,
    348.0,
    anchor="nw",
    text="Plaintext File:",
    fill="#FFFFFF",
    font=("Heebo Regular", 28 * -1)
)
canvas.create_text(
    502.0,
    348.0,
    anchor="nw",
    text="Chipertext File:",
    fill="#FFFFFF",
    font=("Heebo Regular", 28 * -1)
)

window.resizable(False, False)
window.mainloop()