'''
Making Python PDFs with Jada Ebong
'''

#import for creating a pdf
from fpdf import FPDF
#import for reading from a pdf
# import PyPDF2
import os

count = 0

with open("names.txt",'r+') as nameFile:
    for line in nameFile:
        #save the class into a variable 
        pdf = FPDF("P","cm","A4")

        #add page and margin
        pdf.add_page()
        pdf.set_margins(2,2,2)

        #add font
        pdf.set_font("Arial","",16)

        #add image
        pdf.image("JPMorgan_Chase-Logo.png",0,0,20,10)
        pdf.cell(20,1,"",0,2)

        #add a cell
        pdf.cell(10,1,'Hi, welcome to Chili\'s',1,1)

        #add another page
        pdf.add_page()
        pdf.set_fill_color(203, 235, 232)
        pdf.set_font("Arial","",16)
        pdf.set_margins(2,2,2)

        name = line#nameFile.read()
        text = "Bye, "+name+" I hope you enjoyed your Chili\'s"
        pdf.cell(10,1,text,0,1)

        pdfName= str(count) + "testPDF.pdf"
        #save it somewhere
        pdf.output(pdfName)
        count +=1