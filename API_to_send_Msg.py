import tkinter
from tkinter import messagebox
import webbrowser

w = tkinter.Tk()

# window style ie here

w.title("My Software")
w.minsize(height=500, width=500)
w.iconbitmap("whatsapp.ico")
w.configure(bg="#17e6c9")

def destroy():
    w.destroy()

def send():
    messagebox.showinfo("Sucessfully", "Message Send Sucessfully")
    mobile = v1.get()
    msg = v2.get()
    webbrowser.open("https://web.whatsapp.com/send?phone=91"+mobile+"&text="+msg)

lbl_number = tkinter.Label(w, text="What'sapp Message Send",
                            font="Cambria 18 bold",fg="white",
                            bg="black",height=2,width=90)
lbl_number.pack()

lal_number = tkinter.Label(w, text=" What'sapp Mobile Number :  ",
                            font="Cambria 18 bold",
                            bg="#17e6c9")
lal_number.place(x= 100, y=100)
v1 = tkinter.StringVar()
txt_number = tkinter.Entry(w, font="Cambria 16", textvariable=v1)
txt_number.place(x=450, y=100)

lal_msg = tkinter.Label(w, text="Enter Message :  ",
                            font="Cambria 18 bold",
                            bg="#17e6c9")
lal_msg.place(x= 100, y=200)
v2 = tkinter.StringVar()
txt_msg = tkinter.Entry(w, font="Cambria 22", width=20, textvariable=v2)
txt_msg.place(x=300, y=200)

btn_send = tkinter.Button(w, font="Cambria 20 bold", text=" Send", activebackground="red", command=send, bg="green")
btn_send.place(x=250, y=300)

btn_delet = tkinter.Button(w,text="Exist ", font="Cambria 20 bold", bg="yellow", command=destroy)
btn_delet.place(x=350, y=300)

w.mainloop()