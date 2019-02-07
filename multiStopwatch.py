# timer for manufacturing job measurement

from tkinter import *
import datetime
import csv

class GUI:
	def __init__(self, mainWin):
		""" 
			Create GUI labels, buttons, and boxes
		"""
		frame = Frame(mainWin)
		frame.pack()
		mainWin.title('Timer')

		################# Init variables #################
		# to change number of timers, change timerCount
		timerCount = 5

		self.elapsed = [datetime.timedelta(0)]*timerCount
		buttonText = ['Start', 'Pause', 'Stop', 'Save']
		self.stationVarList = []								
		self.IDVarList = []
		self.timeVarList = []
		self.buttons = {}
		self.now = [datetime.datetime.now()]*timerCount


		#################Create top row of labels #################
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


		################# Create buttons, entry boxes, and counter #################
		for i in range(timerCount):
			'''
				The buttons are stored in a dictionary of lists where each list is a row of buttons. This allows 
				each button to function on its row of the timers.
				- buttons[i] is the row (list) of buttons for timer row i
				- buttons[i][0] is the start button widget list for timer row i
				- buttons[i][0][0] is the start button widget object that accesses the
			'''

			self.buttons[i] = [[], [], [], []]

			self.buttons[i][0] = [Button(frame,text=buttonText[0], command = lambda i=i: self.start(i))]
			self.buttons[i][0][0].grid(row=i+1,column=0)

			self.stationVarList.append(StringVar())
			entry=Entry(frame, textvariable = self.stationVarList[i])
			entry.grid(row=i+1,column=1)

			self.IDVarList.append(StringVar())
			entry=Entry(frame, textvariable = self.IDVarList[i])
			entry.grid(row=i+1,column=2)

			self.timeVarList.append(StringVar())
			L1 = Label(frame, textvariable = self.timeVarList[i])
			self.timeVarList[i].set('0:00:00')
			L1.grid(row=i+1,column=3)

			self.buttons[i][1] = [Button(frame,text=buttonText[1], state = DISABLED, command = lambda i=i: self.pause(i))]
			self.buttons[i][1][0].grid(row=i+1,column=4)
			
			self.buttons[i][2] = [Button(frame,text=buttonText[2], state = DISABLED, command = lambda i=i: self.stop(i))]
			self.buttons[i][2][0].grid(row=i+1,column=5)

			self.buttons[i][3] = [Button(frame,text=buttonText[3], state = DISABLED, command = lambda i=i: self.save(i))]
			self.buttons[i][3][0].grid(row=i+1,column=6)

			
	def start(self, i):
		""" 
			Start stopwatch. Called by pressing Start button.
			Stopwatch can be paused or stopped after starting.
		"""
		self.timeVarList[i].set('-:--:--')
		self.now[i] = datetime.datetime.now()
		self.buttons[i][0][0].config(state = DISABLED)
		self.buttons[i][1][0].config(state = NORMAL)
		self.buttons[i][2][0].config(state = NORMAL)


	def pause(self, i):
		""" 
			Pause stopwatch. Saves time elapsed as timedelta variable self.elapsed.
			Only save button is enabled after pausing stopwatch.
		"""
		self.elapsed[i] = datetime.datetime.now()-self.now[i] + self.elapsed[i]
		self.timeVarList[i].set(str(self.elapsed[i])[:7])

		self.buttons[i][0][0].config(state= NORMAL)
		self.buttons[i][1][0].config(state= DISABLED)
		self.buttons[i][2][0].config(state= DISABLED)
		self.buttons[i][3][0].config(state= DISABLED)


	def stop(self, i):
		""" 
			Stop stopwatch. Saves time elapsed. Sets self.startTime=0.
		"""
		self.elapsed[i] = datetime.datetime.now()-self.now[i] + self.elapsed[i]
		print(self.elapsed[i])
		self.timeVarList[i].set(str(self.elapsed[i])[:7])

		self.buttons[i][0][0].config(state = DISABLED)
		self.buttons[i][1][0].config(state= DISABLED)
		self.buttons[i][2][0].config(state= NORMAL, text = 'Reset', command = lambda i=i: self.reset(i))
		self.buttons[i][3][0].config(state= NORMAL)


	def save(self, i):
		""" 
			Appends Job Station, Job ID, and Time as CSV file. If file doesn't already 
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
		outRow = [self.stationVarList[i].get(), self.IDVarList[i].get(), str(self.elapsed[i])[:7]]
		csvWriter.writerow(outRow)
		f.close()
		self.reset(i)


	def reset(self, i):
		""" 
			Resets timer to 0. Resets stop button to stop (from reset). Resets button to 
			initial states.
		"""
		self.timeVarList[i].set('0:00:00')
		self.elapsed[i] = datetime.timedelta(0)
		self.stationVarList[i].set('')
		self.IDVarList[i].set('')
		self.buttons[i][0][0].config(state= NORMAL)
		self.buttons[i][2][0].config(text = 'Stop', state = DISABLED, command = lambda i=i: self.stop(i))
		self.buttons[i][3][0].config(state = DISABLED)


root = Tk()
window = GUI(root)
root.mainloop()