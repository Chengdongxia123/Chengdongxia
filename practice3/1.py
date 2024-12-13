import pdftotext
from pathlib import Path

# Download the pdf_with_table.pdf file from
# https://github.com/aeturrell/coding-for-economists/blob/main/data/pdf_with_table.pdf
# and put it in a subfolder called data before running the next line

# Load the PDF
with open(Path("pdf_with_table.pdf"), "rb") as f:
    pdf = pdftotext.PDF(f)

# Read all the text into one string; print a chunk of the string
print("\n\n".join(pdf)[:220])