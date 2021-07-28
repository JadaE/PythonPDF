'''
Making Python PDFs with Jada Ebong
'''

#import for creating a pdf
from fpdf import FPDF
#import for reading from a pdf
# import PyPDF2

#save the class into a variable
pdf = FPDF("P","cm","A4")

#add page and margin
pdf.add_page()
pdf.set_margins(2,2,2)

#add font
pdf.set_font("Arial","",16)

#add a cell
pdf.cell(10,1,'Hi, welcome to Chili\'s',1,1)

#add another page
pdf.add_page()
pdf.set_fill_color(203, 235, 232)
pdf.cell(10,1,'Bye, I hope you enjoyed your Chili\'s',0,1)


#save it somewhere
pdf.output("I")