import pypdfium2 as pdfium
from pdfminer.high_level import extract_text

def write_output(text, dir, index):
    f = open("output_pdf_text/" + dir + "/pdf_text" + str(index) + ".txt", "w")
    f.write(text)
    f.close()

def pdfproc_pypdfium2 (index) :
    pdf = pdfium.PdfDocument("test_pdfs/test" + str(index) +".pdf")
    version = pdf.get_version()  # get the PDF standard version
    n_pages = len(pdf)  # get the number of pages in the document

    text = ""
    for i in range(0, n_pages):
        
        page = pdf[i]  # load a page
        # Load a text page helper
        textpage = page.get_textpage()
        # Extract text from the whole page
        text += textpage.get_text_bounded()

    write_output(text, "pypdfium2", index)
    
def pdfproc_pdfminer (index):
    text = extract_text("test_pdfs/test" + str(index) +".pdf")
    write_output(text, "pdfminer", index)
    
def pdfproc_pdfminer (index):
    text = extract_text("test_pdfs/test" + str(index) +".pdf")
    write_output(text, "pdfminer", index)
    
pdfproc_pypdfium2(1)
pdfproc_pdfminer(1)