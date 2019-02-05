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
		self.curTime = '0:00:00'
		self.counting = False
		self.startTime = datetime.timedelta(0)

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

		self.L1 = Label(frame, text = self.curTime)
		self.L1.grid(row=1,column=3)
		
		self.B2 = Button(frame, text = 'Pause', command=self.pause)
		self.B2.grid(row=1,column=4)

		self.B3 = Button(frame,text = 'Stop', command=self.stop)
		self.B3.grid(row=1,column=5)

		self.B4 = Button(frame, text = 'Save', command=self.save)
		self.B4.grid(row=1,column=6)

	def start(self):
		""" Start stopwatch. Called by pressing Start button.
		"""
		self.now = datetime.datetime.now()
		self.counting = True	

	def pause(self):
		""" Pause stopwatch. Saves time elapsed as timedelta variable self.startTime
		"""
		self.startTime = datetime.datetime.now()-self.now
		print(self.startTime)

	def stop(self):
		""" Stop stopwatch. Saves time elapsed. Sets self.startTime=0.
		"""
		self.elapsed = datetime.datetime.now()-self.now+self.startTime
		self.startTime = datetime.timedelta(0)
		self.counting = False

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

		
	# def updateWindow(self):
	# 	self.L1.config(text = self.curTime)
	

root = Tk()
window = GUI(root)
root.mainloop()