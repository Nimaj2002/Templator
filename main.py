from docxtpl import DocxTemplate, InlineImage
import json

doc = DocxTemplate("Templates/reportTemplate.docx")

with open("Datas/data.json", "r") as file:
    context = json.load(file)

# print(context)
doc.render(context)
doc.save("Results/Report.docx")
