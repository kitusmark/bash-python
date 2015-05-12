#GUI for the Chat Project program
#We're using Tkinter module

from Tkinter import *
import tkMessageBox	#Module used for system info boxes

#Our App will be class based so:

class Chat:
	def __init__(self, master):
		self.frame = Frame(master)
		self.frame.pack()

		# ************* Toolbar **************
		self.barraEines = Frame(self.frame)
		self.botoSortir = Button(self.frame, text='Sortir', command=self.sortir)
		self.botoSortir.pack(side=LEFT)

		self.barraEines.pack(side=TOP, fill=X)



		# ************* Buttons ***************
		self.botoEnviar = Button(self.frame, text='Envia', command=self.enviar)
		self.botoEnviar.pack(side=RIGHT)


	def enviar(self):
		print ('He clicat en el boto Enviar!')

	def sortir(self):
		resposta = tkMessageBox.askquestion('Sortir del Xat', 'Estas segur que vols sortir del xat?')
		if resposta == 'yes':
			print ('Sortint de l\'aplicacio')
			frame.quit
		else:
			#tanquem la finestra messagebox
			pass


root = Tk()
c= Chat(root)
root.mainloop()
