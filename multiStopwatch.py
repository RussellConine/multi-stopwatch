# timer for manufacturing job measurement

from tkinter import *
import datetime

class GUI:
	def __init__(self, mainWin):
		frame = Frame(mainWin)
		frame.pack()
		mainWin.title('Timer')

		### Create top row of labels ###
		self.label1 = Label(frame, text = 'Start')
		self.label1.grid(row=0, column = 0)

		self.label1 = Label(frame, text = 'Job Station')
		self.label1.grid(row=0, column = 1)

		self.label1 = Label(frame, text = 'Job ID')
		self.label1.grid(row=0, column = 2)

		self.label1 = Label(frame, text = 'Time')
		self.label1.grid(row=0, column = 3)

		self.label1 = Label(frame, text = 'Pause')
		self.label1.grid(row=0, column = 4)

		self.label1 = Label(frame, text = 'Stop')
		self.label1.grid(row=0, column = 5)

		self.label1 = Label(frame, text = 'Save')
		self.label1.grid(row=0, column = 6)

		### Create buttons, entry boxes, and counter ###
		self.B1 = Button(frame, text = 'Start', command=self.start)
		self.B1.grid(row=1,column=0)

		self.E1 = Entry(frame)
		self.E1.grid(row=1,column=1)

		self.E1 = Entry(frame)
		self.E1.grid(row=1,column=2)

		self.L1 = Label(frame, text = 'timeCount')
		self.L1.grid(row=1,column=3)
		
		self.B1 = Button(frame, text = 'Pause', command=self.start)
		self.B1.grid(row=1,column=4)

		self.B1 = Button(frame,text = 'Stop', command=self.start)
		self.B1.grid(row=1,column=5)

		self.B1 = Button(frame, text = 'Save', command=self.start)
		self.B1.grid(row=1,column=6)

	def start(self):
		now = datetime.datetime.now()
	
	def timeCount(self):
		pass

	def pause(self):
		pass

	def stop(self):
		pass

	def save(self):
		pass		
			


		

        # self.label = Label(mainWin, text='This is our first GUI!')
        # self.label.pack()

        # self.greet_button = Button(mainWin, text='Greet', command=self.greet)
        # self.greet_button.pack()

        # self.close_button = Button(mainWin, text='Close', command=mainWin.quit)
        # self.close_button.pack()

root = Tk()
window = GUI(root)
root.mainloop()