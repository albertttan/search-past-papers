import PyPDF2 as pdf

f = open("0460_s22_ms_11.pdf", "rb")
r = pdf.PdfReader(f)

for i in range(len(r.pages)): 
    print(r.pages[i].extract_text(), "\n")
