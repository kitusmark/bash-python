#!/usr/local/bin/python2.7

#GUI for the Chat Project program
#We're using Tkinter module

from Tkinter import *
import tkMessageBox	#Module used for system info boxes

#Our App will be class based so:

class Chat:
	def __init__(self, master):

		# ************* Menu **************
		menubar = Menu(master)
		menubar.add_command(label='Connectar', command=self.connectar)
		menubar.add_command(label='Desconnectar', command=self.desconnectar)
		menubar.add_command(label='Sortir', command=self.sortir)
		

		master.config(menu=menubar)
		
		# ************* Buttons ***************
	      
		self.botoEnviar = Button(master, font=30, text='Envia', command=self.enviar)
		self.botoEnviar.grid(row=1, column=1, sticky=W+E+N+S)


		# ************* Text Entries **********
		self.entradaMissatge = Text(master, bg='white', height=4, padx=4, pady=4, yscrollcommand=TRUE)
		self.entradaMissatge.grid(row=1, column=0)

		self.missatgesXat = Text(master, bg='white', height=10, padx=4, pady=4, yscrollcommand=TRUE, state=DISABLED)
		self.missatgesXat.grid(row=0, columnspan=2)

	def connectar(self):
		pass

	def desconnectar(self):
		pass

	def enviar(self):
		print ('He clicat en el boto Enviar!')

	def sortir(self):
		resposta = tkMessageBox.askquestion('Sortir del Xat', 'Estas segur que vols sortir del xat?')
		if resposta == 'yes':
			print ('Sortint de l\'aplicacio')
			master.quit()
		else:
			#tanquem la finestra messagebox
			pass


root = Tk()
c= Chat(root)

#Size and Name of the main window
nomFinestra = 'EiFC Xat'

root.title(nomFinestra)
root.geometry('400x500')
root.resizable(width=FALSE, height=FALSE)

root.mainloop()
