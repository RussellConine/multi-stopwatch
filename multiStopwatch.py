# timer for manufacturing job measurement

from tkinter import *
import datetime
import csv

class GUI:
	def __init__(self, mainWin):
		""" Create GUI labels, buttons, and boxes
		"""
		frame = Frame(mainWin)
		frame.pack()
		mainWin.title('Timer')

		### Init variables ###
		self.curTime = StringVar()
		self.curTime.set('0:00:00')
		self.elapsed = datetime.timedelta(0)

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

		self.E2 = Entry(frame)
		self.E2.grid(row=1,column=2)

		self.L1 = Label(frame, textvariable = self.curTime)
		self.L1.grid(row=1,column=3)
		
		self.B2 = Button(frame, text = 'Pause', state = DISABLED, command=self.pause)
		self.B2.grid(row=1,column=4)

		self.B3 = Button(frame,text = 'Stop', state = DISABLED, command=self.stop)
		self.B3.grid(row=1,column=5)

		self.B4 = Button(frame, text = 'Save', state = DISABLED, command=self.save)
		self.B4.grid(row=1,column=6)

	def start(self):
		""" Start stopwatch. Called by pressing Start button.
			Stopwatch can be paused or stopped after starting.
		"""
		self.curTime.set('-:--:--')
		self.now = datetime.datetime.now()
		self.B1.config(state = DISABLED)
		self.B2.config(state = NORMAL)
		self.B3.config(state = NORMAL)

	def pause(self):
		""" Pause stopwatch. Saves time elapsed as timedelta variable self.elapsed.
			Only save button is enabled after pausing stopwatch.
		"""
		self.elapsed = datetime.datetime.now()-self.now + self.elapsed
		self.curTime.set(str(self.elapsed)[:7])
		self.B1.config(state = NORMAL)
		self.B2.config(state = DISABLED)
		self.B3.config(state = DISABLED)
		self.B4.config(state = DISABLED)


	def stop(self):
		""" Stop stopwatch. Saves time elapsed. Sets self.startTime=0.
			Time can be 
		"""
		self.elapsed = datetime.datetime.now()-self.now + self.elapsed
		self.curTime.set(str(self.elapsed)[:7])
		self.startTime = datetime.timedelta(0)
		self.B1.config(state = DISABLED)
		self.B2.config(state = DISABLED)
		self.B3.config(text = 'Reset', command= self.reset)
		self.B4.config(state = NORMAL)

	def save(self):
		""" Appends Job Station, Job ID, and Time as CSV file. If file doesn't already 
			exist, creates file and headers.
		"""
		try:
			f = open('outfile.csv', 'r')
			f.close()
		except:
			f = open('outfile.csv', 'w', newline = '')
			header = ['Job Station', 'Job ID', 'Time']
			csvWriter = csv.writer(f)
			csvWriter.writerow(header)
			f.close()

		f = open('outfile.csv', 'a', newline = '')
		csvWriter = csv.writer(f)
		outRow = [self.E1.get(), self.E2.get(), str(self.elapsed)[:7]]
		csvWriter.writerow(outRow)
		f.close()
		self.reset()

	def reset(self):
		self.curTime.set('0:00:00')
		self.elapsed = datetime.timedelta(0)
		self.E1.delete(0, END)
		self.E2.delete(0, END)
		self.initial = True
		self.B1.config(state = NORMAL)
		self.B3.config(text = 'Stop', state = DISABLED, command = self.stop)
		self.B4.config(state = DISABLED)

	
		
	# def updateWindow(self):
	# 	self.L1.config(text = self.curTime)
	

root = Tk()
window = GUI(root)
root.mainloop()