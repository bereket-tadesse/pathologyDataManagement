import os
import pytesseract
from pathlib import Path
import pyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader

#load main directory of the patients records
stored_files_path = ""

#incoming scanned files 
# change this directory to desired directory where scan exist
incoming_records_path = 'scans/new_scan.pdf'

incoming_records = PdfFileReader(open(incoming_records_path, 'rb'))

#pdf which is appended to all
# cgange this directory to desired directory where scan exist
pdf_for_all_path = "scans/top.pdf"
incoming_records = PdfFileReader(open(pdf_for_all_path, 'rb'))


def extractID(page):
    pass
    
def icoming_record_iterator(incoming_pdf):
    pdf_writer = PdfFileWriter()

    for page in incoming_pdf.pages:
        page.mediabox.lowerLeft = (439,147)
        page.mediabox.upperRight = (535, 129 )
        pdf_writer.addpage(page)




