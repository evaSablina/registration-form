import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.geometry("480x200")
root.title("Registration Form")


def register():
    tkinter.messagebox.showinfo(message="Accepted")


# create GIU

# create main text
label_register_account = tkinter.Label(root, text="Register New Account", font="ar 15 bold")
label_register_account.grid(row=0, column=0)

# create first row with username
label_username = tkinter.Label(root, text="Username")
label_username.grid(row=2, column=0)

entry_username = tkinter.Entry(root)
entry_username.grid(row=2, column=1)


# create seconds row with mail
label_email = tkinter.Label(root, text="E-mail")
label_email.grid(row=3, column=0)

entry_email = tkinter.Entry(root)
entry_email.grid(row=3, column=1)


# create third row with password
label_password = tkinter.Label(root, text="Password")
label_password.grid(row=4, column=0)

entry_password = tkinter.Entry(root)
entry_password.grid(row=4, column=1)

# confirming password
label_confirm_password = tkinter.Label(root, text="Confirm Password")
label_confirm_password.grid(row=5, column=0)

entry_confirm_password = tkinter.Entry(root)
entry_confirm_password.grid(row=5, column=1)

# create button
register_button = tkinter.Button(root, text="Register", command=register)
register_button.grid(row=8, column=0)



root.mainloop()