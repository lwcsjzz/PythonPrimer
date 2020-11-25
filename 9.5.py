from docx import Document
file = "1.docx"
doc = Document(file)
for i in doc.tables:
    for j in i.rows:
        for k in j.cells:
            print(k.text, end=' ')
        print('\n')