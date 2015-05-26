# Echo client program
import socket
import thread
from conversador import *
from Tkinter import *
import tkMessageBox

#---------------------CONSTANTS--------------
nomFinestra = 'EiFC Xat'
adreca = 'localhost'
identitat = ''

def enviar():
	print 'boto enviar premut'
	missatgeXat = entradaMissatge.get(1.0, END)
	#fem scroll automatic de la finestra i eliminem el text
	finestraXat.yview(END)
	entradaMissatge.delete('0.0', END)

	#Ara ja podem enviar el missatge a tots
	client.parla(missatgeXat)

def obtenirIdentitat():
	print 'Obtenint la identitat del client'
	identitat = textIdentitat.get('1.0', END)
	print 'La identitat del client es: ' + identitat

	try:
		client = conversador(identitat,adreca)
		#print 'Connectat'
	except:
		print 'No es pot connectar'
		root.quit()

	finestraIdentitat.destroy()
	return
#--------------------------------------------
#---------------ESDEVENIMENTS TECLAT---------
#--------------------------------------------
def deshabilitarText(event):
	entradaMissatge.config(state=DISABLED)

def botoPremut(event):
	entradaMissatge.config(state=NORMAL)
	enviar()
	
if __name__ == '__main__':
#--------------------------------------------
#-----------------GRAPHICS-------------------
#--------------------------------------------
root = Tk()
root.title(nomFinestra)
root.geometry('400x500+550+250')
root.resizable(height=FALSE, width=FALSE)

#Finestra de missatges de xat
finestraXat = Text(root, bd=2, relief=GROOVE, bg='white', height='8', width='50', font='Arial')
finestraXat.insert(END, 'Connectant al Servidor....\n')
finestraXat.config(state=DISABLED)

#Boto per enviar el missatge al xat
botoEnviar = Button(root, font=30, text='Enviar', width='12', height=5, bd=0, bg='#FFBF00', activebackground='#FACC2E', command=enviar)


#Finestra per introduir el missatge a enviar
entradaMissatge = Text(root, bd=2, relief=GROOVE, bg='white', width='29', height='5', font='Arial')
entradaMissatge.bind('<Return>', deshabilitarText)
entradaMissatge.bind('<KeyRelease-Return>', botoPremut)


#Visualitzem tots els elements grafics en pantalla de la finestra principal
finestraXat.place(x=6, y=6, height=386, width=370)
botoEnviar.place(x=6, y=401, height=90)
entradaMissatge.place(x=128, y=401, height=90, width=265)


#Finestra per preguntar la identitat del client
finestraIdentitat = Toplevel()
finestraIdentitat.title('Identitat Client')
finestraIdentitat.geometry('400x100+550+0')
finestraIdentitat.resizable(height=FALSE, width=FALSE)
info = Message(finestraIdentitat, text='Quin es el teu nom?')
info.pack()

textIdentitat = Text(finestraIdentitat, bd=2, relief=GROOVE, bg='white', width='20', height='1', font='Arial' )
textIdentitat.pack()

botoOK = Button(finestraIdentitat, text='OK', command=obtenirIdentitat)
botoOK.pack()

finestraIdentitat.mainloop()
root.mainloop()
#-----------------------------------------	
	while 1:
		if identitat != '':
			client = clientServidor(identitat,adreca)
		else:
			pass
