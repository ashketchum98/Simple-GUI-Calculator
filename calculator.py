#A Small Calculator with Tkinter and Python
#Enjoy Coding....

import tkinter as tk   #importing tkinter 

class Application():

	def __init__(self, master=None):

		self.expression = ""      #string that will contain the expression to compute....

		#Frame for the input field....
		self.input_frame = tk.Frame(master, width=380, height=50)
		self.input_frame.pack(side="top")

		#StringVar will get Input Field....
		self.content = tk.StringVar()
		self.input_text = tk.Entry(self.input_frame,font=('arial',18,'bold'),width=49,bd=0,textvariable = self.content)
		self.input_text.grid(row=0, column=0)
		self.input_text.pack(ipady=10)

		#Frame for the buttons
		self.btns_frame = tk.Frame(master, width=365, height= 314,bg="grey")
		self.btns_frame.pack()

		#Buttons
		self.clear = tk.Button(self.btns_frame,bd=0,text="Clear", width=41, height=3, fg="black", bg="#eee", command=lambda: self.clear_input())
		self.clear.grid(row=1,columnspan=3)

		self.divide = tk.Button(self.btns_frame,bd=0,text="/", width=10, height=3, fg="black", bg="#eee", command=lambda: self.btn_pressed("/"))
		self.divide.grid(row=1, column=3)

		self.nine = tk.Button(self.btns_frame,bd=0,text="9", width=13, height=3, fg="black", bg="#eee",command=lambda: self.btn_pressed("9"))
		self.nine.grid(row=2,column=0)

		self.eight = tk.Button(self.btns_frame,bd=0,text="8", width=13, height=3, fg="black", bg="#eee",command=lambda: self.btn_pressed("8"))
		self.eight.grid(row=2, column=1)

		self.seven = tk.Button(self.btns_frame,bd=0,text="7", width=13, height=3, fg="black", bg="#eee",command=lambda: self.btn_pressed("7"))
		self.seven.grid(row=2, column=2)

		self.mul = tk.Button(self.btns_frame,bd=0,text="*", width=10, height=3, fg="black", bg="#eee",command=lambda: self.btn_pressed("*"))
		self.mul.grid(row=2, column=3)

		self.six = tk.Button(self.btns_frame,bd=0,text="6", width=13, height=3, fg="black", bg="#eee",command=lambda: self.btn_pressed("6"))
		self.six.grid(row=3, column=0)

		self.five = tk.Button(self.btns_frame,bd=0,text="5", width=13, height=3, fg="black", bg="#eee",command=lambda: self.btn_pressed("5"))
		self.five.grid(row=3, column=1)

		self.four = tk.Button(self.btns_frame,bd=0,text="4", width=13, height=3, fg="black", bg="#eee",command=lambda: self.btn_pressed("4"))
		self.four.grid(row=3, column=2)

		self.minus = tk.Button(self.btns_frame,bd=0,text="-", width=10, height=3, fg="black", bg="#eee",command=lambda: self.btn_pressed("-"))
		self.minus.grid(row=3, column=3)

		self.three = tk.Button(self.btns_frame,bd=0,text="3", width=13, height=3, fg="black", bg="#eee",command=lambda: self.btn_pressed("3"))
		self.three.grid(row=4, column=0)

		self.two = tk.Button(self.btns_frame,bd=0,text="2", width=13, height=3, fg="black", bg="#eee",command=lambda: self.btn_pressed("2"))
		self.two.grid(row=4, column=1)

		self.one = tk.Button(self.btns_frame,bd=0,text="1", width=13, height=3, fg="black", bg="#eee",command=lambda: self.btn_pressed("1"))
		self.one.grid(row=4, column=2)

		self.plus = tk.Button(self.btns_frame,bd=0,text="+", width=10, height=3, fg="black", bg="#eee",command=lambda: self.btn_pressed("+"))
		self.plus.grid(row=4, column=3)

		self.dot = tk.Button(self.btns_frame,bd=0,text=".", width=13, height=3, fg="black", bg="#eee",command=lambda: self.btn_pressed("."))
		self.dot.grid(row=5, column=0)

		self.zero = tk.Button(self.btns_frame,bd=0,text="0", width=13, height=3, fg="black", bg="#eee",command=lambda: self.btn_pressed("0"))
		self.zero.grid(row=5, column=1)

		self.eq = tk.Button(self.btns_frame,bd=0,text="=", width=13, height=3, fg="black", bg="#eee",command=lambda: self.compute())
		self.eq.grid(row=5, column=2)

		self.mod = tk.Button(self.btns_frame,bd=0,text="%", width=10, height=3, fg="black", bg="#eee",command=lambda: self.btn_pressed("%"))
		self.mod.grid(row=5, column=3)

	def btn_pressed(self, btn_num):
		""" Method for chaning expression based on button pressed... """
		self.expression = self.expression + str(btn_num)
		self.content.set(self.expression)

	def clear_input(self):
		""" Method for cleaing the input field... """
		self.expression = ""
		self.content.set(self.expression)

	def compute(self):
		""" Method for computing the Value of expression and showing it... """
		try:
			self.expression = str(eval(self.expression))
			self.content.set(self.expression)
		except:
			self.content.set("Can't Compute!!!")


if __name__ == "__main__":
	root = tk.Tk()
	root.resizable(0,0)
	root.geometry("370x314")
	root.title("Calculator")
	app = Application(root)
	root.mainloop()
