import os
import pypdfium2 as pdfium
from pdfminer.high_level import extract_text
import fitz
from tika import parser 
import tabula

def write_output(text, dir, index):
    f = open("output_pdf_text/" + dir + "/pdf_text" + str(index) + ".txt", "w")
    f.write(text)
    f.close()

def pdfproc_pypdfium2 (index) :
    pdf = pdfium.PdfDocument("test_pdfs/test" + str(index) +".pdf")
    n_pages = len(pdf)  # get the number of pages in the document

    text = ""
    for i in range(0, n_pages):        
        page = pdf[i]  # load a page
        textpage = page.get_textpage()
        text += textpage.get_text_bounded()

    write_output(text, "pypdfium2", index)
    
def pdfproc_pdfminer (index):
    text = extract_text("test_pdfs/test" + str(index) +".pdf")
    write_output(text, "pdfminer", index)
    
def pdfproc_pymupdf (index):
    pdf = fitz.open("test_pdfs/test" + str(index) +".pdf")
    text = ""
    for page in pdf:
        text += page.get_text()
    write_output(text, "pymupdf", index)
    
def pdfproc_tika (index):
    pdf = parser.from_file("test_pdfs/test" + str(index) +".pdf")
    text = pdf['content']
    write_output(text, "tika", index)
    
def pdfproc_tabula(index):
    tabula.convert_into("test_pdfs/test" + str(index) +".pdf", 
                        "output_pdf_text/tabula/pdf_text" + str(index) + ".csv", 
                        output_format="csv", 
                        pages='all'
                        )
    
def main():
    path = "./test_pdfs"
    dir_list = os.listdir(path)

    for i in range(1, len(dir_list) + 1): #1 to 4
        pdfproc_pypdfium2(i)
        pdfproc_pdfminer(i)
        pdfproc_pymupdf(i)
        pdfproc_tika(i)
        
    pdfproc_tabula(5)
    
if __name__ == "__main__":
    main()