# Import tkinter for the gui

from tkinter import *
from tkinter import filedialog

# The encrypt image function


def encrypt_image():
    file1 = filedialog.askopenfile(mode='r', filetype=[('jpg file', '*.jpg')])
    if file1 is not None:
        file_name = file1.name
        #print(file_name)
        key = entry1.get(1.0, END)
        print(file_name, key)
        fi = open(file_name, 'rb')
        image = fi.read()
        fi.close()
        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values ^ int(key)
        fi1 = open(file_name, 'wb')
        fi1.write(image)
        fi1.close()


# The size of the GUI and the specifications of the button size
root = Tk()
root.geometry("200x160")

b1 = Button(root, text="Encrypt", command=encrypt_image)
b1.place(x=70, y=10)

entry1 = Text(root, height=1, width=10)
entry1.place(x=50, y=50)

root.mainloop()