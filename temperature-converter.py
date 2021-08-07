from tkinter import *
from tkinter import ttk



def clear_entry():

	celsius_entry.delete(0, 'end')
	fahrenheit_entry.delete(0, 'end')
	label_error.place_forget()


def clear_entry_with_key(event):
	clear_entry()




def check_c(event):
	c_val = celsius_entry.get()
	f_val = fahrenheit_entry.get()

	
	fahrenheit_entry.delete(0, 'end')
	label_error.place_forget()


	try:
		c_val = float(c_val)

		f = str(round(float((c_val * 9 / 5) + 32), 4))
		fahrenheit_entry.insert(0, f)

	except:				
		label_error.place(x = 20, y = 50, height = 50)




def check_f(event):
	c_val = celsius_entry.get()
	f_val = fahrenheit_entry.get()

	
	celsius_entry.delete(0, 'end')
	label_error.place_forget()

	try:
		f_val = float(f_val)

		c = str(round(float(f_val - 32) * 5/9, 4))
		celsius_entry.insert(0, c)


	except:
		label_error.place(x = 20, y = 50, height = 50)





window = Tk()


window.geometry('540x320+130+90')
window.resizable(False, False)  


window.title("Converter")



title_label = ttk.Label(window, text = "Temperature Converter", font = ("Arial", 20))
title_label.place(x = 140, y = 5, height = 50)

label2 = Label(window, text = "=", width = 10, font = ("Arial", 20))
label2.place(x = 190, y = 100, height = 50)

celsius = ttk.Label(window, text = "Celsius", font = ("Arial", 16))
celsius.place(x = 20, y = 150, height = 50)

fahrenheit = ttk.Label(window, text = "Fahrenheit", font = ("Arial", 16))
fahrenheit.place(x = 410, y = 150, height = 50)



celsius_entry = ttk.Entry(window, width = 27)
celsius_entry.place(x = 20, y = 100, height = 50)
celsius_entry.bind("<KeyRelease>", check_c)


fahrenheit_entry = ttk.Entry(window, width = 27)
fahrenheit_entry.place(x = 350, y = 100, height = 50)
fahrenheit_entry.bind("<KeyRelease>", check_f)


label_error = Label(window, text = "გთხოვთ, შეიყვანეთ რიცხვი!", font = ("Arial", 11))


clear_btn = ttk.Button(window, text = "Clear", command = clear_entry)
clear_btn.place(x = 230, y = 200, height = 50)


window.bind('<Delete>', clear_entry_with_key)


window.mainloop()  