from tkinter import *
from tkinter import ttk

class Resistor:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Resitores")
        self.root.geometry("802x500+100+100")
        self.root.configure(background="powder blue")

        mainFrame = Frame(self.root)
        mainFrame.grid()

        TitleFrame = Frame(mainFrame, bd=1, width=800, padx=20, relief=SOLID)
        TitleFrame.grid(row=0, column=0)
        self.lblTitle = Label(TitleFrame, font=('arial', 20, 'bold'), text="Calculadora de Resitores", padx=20)
        self.lblTitle.grid()
        ResistorFrame = Frame(mainFrame, bd=1, width=800, padx=22.4, relief=SOLID)
        ResistorFrame.grid(row=1, column=0)
        
        #---------------------------------------------------------------------------------------------------------------------
        #                          Labels para nomear o campos
        #---------------------------------------------------------------------------------------------------------------------

        self.lblTitle = Label(ResistorFrame, font=('arial', 10, 'bold'),text="lst Band")
        self.lblTitle.grid(row=0, column=0)
        self.lblTitle = Label(ResistorFrame, font=('arial', 10, 'bold'),text="1nd Band")
        self.lblTitle.grid(row=0, column=1)
        self.lblTitle = Label(ResistorFrame, font=('arial', 10, 'bold'),text="2nd Band")
        self.lblTitle.grid(row=0, column=2)
        self.lblTitle = Label(ResistorFrame, font=('arial', 10, 'bold'),text="Multiplier")
        self.lblTitle.grid(row=0, column=3)
        self.lblTitle = Label(ResistorFrame, font=('arial', 10, 'bold'),text="Tolerance")
        self.lblTitle.grid(row=0, column=4)
        #---------------------------------------------------------------------------------------------------------------------
        #                          Botões com valores para a cor preto
        #---------------------------------------------------------------------------------------------------------------------

        self.btnBlackBand1 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='preto', fg='white', bg='black')
        self.btnBlackBand1.grid(row=1, column=0)
        self.btnBlackBand2 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='0', fg='white', bg='black')
        self.btnBlackBand2.grid(row=1, column=1)
        self.btnBlackBand3 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='0', fg='white', bg='black')
        self.btnBlackBand3.grid(row=1, column=2)
        self.btnBlackBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='10^0', fg='white', bg='black')
        self.btnBlackBand4.grid(row=1, column=3)
        self.btnBlackBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), fg='white', bg='black')
        self.btnBlackBand4.grid(row=1, column=4)

        #---------------------------------------------------------------------------------------------------------------------
        #                          Botões com valores para a cor marron
        #---------------------------------------------------------------------------------------------------------------------

        self.btnBrownBand1 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='marron', fg='black', bg='brown')
        self.btnBrownBand1.grid(row=2, column=0)
        self.btnBrownBand2 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='1', fg='black', bg='brown')
        self.btnBrownBand2.grid(row=2, column=1)
        self.btnBrownBand3 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='1', fg='black', bg='brown')
        self.btnBrownBand3.grid(row=2, column=2)
        self.btnBrownBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='10^1', fg='black', bg='brown')
        self.btnBrownBand4.grid(row=2, column=3)
        self.btnBrownBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), fg='black', bg='brown')
        self.btnBrownBand4.grid(row=2, column=4)

        #---------------------------------------------------------------------------------------------------------------------
        #                          Botões com valores para a cor vermelho
        #---------------------------------------------------------------------------------------------------------------------

        self.btnRedBand1 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='vermelho', fg='black', bg='red')
        self.btnRedBand1.grid(row=3, column=0)
        self.btnRedBand2 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='2', fg='black', bg='red')
        self.btnRedBand2.grid(row=3, column=1)
        self.btnRedBand3 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='2', fg='black', bg='red')
        self.btnRedBand3.grid(row=3, column=2)
        self.btnRedBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='10^2', fg='black', bg='red')
        self.btnRedBand4.grid(row=3, column=3)
        self.btnRedBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), fg='black', bg='red')
        self.btnRedBand4.grid(row=3, column=4)

        #---------------------------------------------------------------------------------------------------------------------
        #                          Botões com valores para a cor laranja
        #---------------------------------------------------------------------------------------------------------------------

        self.btnOrangeBand1 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='laranja', fg='black', bg='orange')
        self.btnOrangeBand1.grid(row=4, column=0)
        self.btnOrangeBand2 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='3', fg='black', bg='orange')
        self.btnOrangeBand2.grid(row=4, column=1)
        self.btnOrangeBand3 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='3', fg='black', bg='orange')
        self.btnOrangeBand3.grid(row=4, column=2)
        self.btnOrangeBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='10^3', fg='black', bg='orange')
        self.btnOrangeBand4.grid(row=4, column=3)
        self.btnOrangeBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), fg='black', bg='orange')
        self.btnOrangeBand4.grid(row=4, column=4)

        #---------------------------------------------------------------------------------------------------------------------
        #                          Botões com valores para a cor amarelo
        #---------------------------------------------------------------------------------------------------------------------

        self.btnYellowBand1 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='amarelo', fg='black', bg='yellow')
        self.btnYellowBand1.grid(row=5, column=0)
        self.btnYellowBand2 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='4', fg='black', bg='yellow')
        self.btnYellowBand2.grid(row=5, column=1)
        self.btnYellowBand3 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='4', fg='black', bg='yellow')
        self.btnYellowBand3.grid(row=5, column=2)
        self.btnYellowBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='10^4', fg='black', bg='yellow')
        self.btnYellowBand4.grid(row=5, column=3)
        self.btnYellowBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), fg='black', bg='yellow')
        self.btnYellowBand4.grid(row=5, column=4)

        #---------------------------------------------------------------------------------------------------------------------
        #                          Botões com valores para a cor verde
        #---------------------------------------------------------------------------------------------------------------------

        self.btnGreenBand1 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='verde', fg='black', bg='green')
        self.btnGreenBand1.grid(row=6, column=0)
        self.btnGreenBand2 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='5', fg='black', bg='green')
        self.btnGreenBand2.grid(row=6, column=1)
        self.btnGreenBand3 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='5', fg='black', bg='green')
        self.btnGreenBand3.grid(row=6, column=2)
        self.btnGreenBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='10^5', fg='black', bg='green')
        self.btnGreenBand4.grid(row=6, column=3)
        self.btnGreenBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), fg='black', bg='green')
        self.btnGreenBand4.grid(row=6, column=4)

        #---------------------------------------------------------------------------------------------------------------------
        #                          Botões com valores para a cor azul
        #---------------------------------------------------------------------------------------------------------------------

        self.btnBlueBand1 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='azul', fg='white', bg='blue')
        self.btnBlueBand1.grid(row=7, column=0)
        self.btnBlueBand2 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='6', fg='white', bg='blue')
        self.btnBlueBand2.grid(row=7, column=1)
        self.btnBlueBand3 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='6', fg='white', bg='blue')
        self.btnBlueBand3.grid(row=7, column=2)
        self.btnBlueBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='10^6', fg='white', bg='blue')
        self.btnBlueBand4.grid(row=7, column=3)
        self.btnBlueBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), fg='white', bg='blue')
        self.btnBlueBand4.grid(row=7, column=4)

        #---------------------------------------------------------------------------------------------------------------------
        #                          Botões com valores para a cor violeta
        #---------------------------------------------------------------------------------------------------------------------

        self.btnVioletBand1 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='violeta', fg='black', bg='violet')
        self.btnVioletBand1.grid(row=8, column=0)
        self.btnVioletBand2 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='7', fg='black', bg='violet')
        self.btnVioletBand2.grid(row=8, column=1)
        self.btnVioletBand3 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='7', fg='black', bg='violet')
        self.btnVioletBand3.grid(row=8, column=2)
        self.btnVioletBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='10^7', fg='black', bg='violet')
        self.btnVioletBand4.grid(row=8, column=3)
        self.btnVioletBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), fg='black', bg='violet')
        self.btnVioletBand4.grid(row=8, column=4)
        
        #---------------------------------------------------------------------------------------------------------------------
        #                          Botões com valores para a cor cinza
        #---------------------------------------------------------------------------------------------------------------------

        self.btnGrayBand1 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='cinza', fg='black', bg='gray')
        self.btnGrayBand1.grid(row=9, column=0)
        self.btnGrayBand2 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='8', fg='black', bg='gray')
        self.btnGrayBand2.grid(row=9, column=1)
        self.btnGrayBand3 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='8', fg='black', bg='gray')
        self.btnGrayBand3.grid(row=9, column=2)
        self.btnGrayBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='10^8', fg='black', bg='gray')
        self.btnGrayBand4.grid(row=9, column=3)
        self.btnGrayBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), fg='black', bg='gray')
        self.btnGrayBand4.grid(row=9, column=4)

        #---------------------------------------------------------------------------------------------------------------------
        #                          Botões com valores para a cor branco
        #---------------------------------------------------------------------------------------------------------------------

        self.btnWhiteBand1 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='branco', fg='black', bg='white')
        self.btnWhiteBand1.grid(row=10, column=0)
        self.btnWhiteBand2 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='9', fg='black', bg='white')
        self.btnWhiteBand2.grid(row=10, column=1)
        self.btnWhiteBand3 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='9', fg='black', bg='white')
        self.btnWhiteBand3.grid(row=10, column=2)
        self.btnWhiteBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='10^9', fg='black', bg='white')
        self.btnWhiteBand4.grid(row=10, column=3)
        self.btnWhiteBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), fg='black', bg='white')
        self.btnWhiteBand4.grid(row=10, column=4)

        #---------------------------------------------------------------------------------------------------------------------
        #                          Botões com valores para a cor prata
        #---------------------------------------------------------------------------------------------------------------------

        self.btnSilverBand1 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='prata', fg='black', bg='#c0c0c0')
        self.btnSilverBand1.grid(row=11, column=0)
        self.btnSilverBand2 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='--', fg='black', bg='#c0c0c0')
        self.btnSilverBand2.grid(row=11, column=1)
        self.btnSilverBand3 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='--', fg='black', bg='#c0c0c0')
        self.btnSilverBand3.grid(row=11, column=2)
        self.btnSilverBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='10^(-1)', fg='black', bg='#c0c0c0')
        self.btnSilverBand4.grid(row=11, column=3)
        self.btnSilverBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), fg='black', bg='#c0c0c0')
        self.btnSilverBand4.grid(row=11, column=4)

        #---------------------------------------------------------------------------------------------------------------------
        #                          Botões com valores para a cor dourado
        #---------------------------------------------------------------------------------------------------------------------

        self.btnGoldBand1 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='dourado', fg='black', bg='#ffcc13')
        self.btnGoldBand1.grid(row=12, column=0)
        self.btnGoldBand2 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='--', fg='black', bg='#ffcc13')
        self.btnGoldBand2.grid(row=12, column=1)
        self.btnGoldBand3 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='--', fg='black', bg='#ffcc13')
        self.btnGoldBand3.grid(row=12, column=2)
        self.btnGoldBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), text='10^(-2)', fg='black', bg='#ffcc13')
        self.btnGoldBand4.grid(row=12, column=3)
        self.btnGoldBand4 = Button(ResistorFrame, width=8, font=('arial', 10, 'bold'), fg='black', bg='#ffcc13')
        self.btnGoldBand4.grid(row=12, column=4)

if __name__=='__main__':
    root = Tk()
    application = Resistor(root)
    root.mainloop()
