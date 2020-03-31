import PyPDF2
import re

pdf_file = open('coroa3.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(35).extractText()
pdf_file.close()
#page_content = page.extractText()


##parsed = ''.join(page_content)
##parsed = re.sub('\n', '', parsed)

print(len(page))
