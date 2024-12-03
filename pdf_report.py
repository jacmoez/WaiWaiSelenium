from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4



person = [
    ["Id", "name", "age", "gender", "Position"],
    [899348, "Swe Swe", 31, "Female", "QA Testing"],
    [899349, "Wai Wai", 26, "Female", "QA Testing"],
    [899420, "Ma Khin", 36, "Female", "QA Manager"],
    [899321, "Kaung Kaung", 26, "Male", "FontEnd Developer"],
  ]


def pdf(file_name="test.pdf"):
    doc = SimpleDocTemplate(file_name,pagesize = A4)
    table = Table(person)
    table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.brown)
    ]))
    elements = [table]
    doc.build(elements)

pdf()

