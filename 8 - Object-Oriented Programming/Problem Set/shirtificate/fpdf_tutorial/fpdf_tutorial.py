from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "U", 11)
        self.cell(0, 5, "This is a Header", align="C", border=1)
        self.set_xy(10, 30)

    def footer(self):
        self.set_y(-15)
        page_number = str(self.page_no())
        self.cell(0, 10, page_number, align="R")

pdf = PDF("P", "mm", "A4")

w = 210
h = 297

pdf.set_font("Helvetica", "B", 16)

pdf.add_page()

# pdf.set_xy(w/2, h/2)
pdf.set_xy(w/2 - 30, h/2 - 3.5)

pdf.cell(60, 7, "Cell 1", border=1, new_x="LMARGIN", new_y="NEXT")
# pdf.cell(60, 7, "Cell 2", border=1)
# pdf.cell(60, 7, "Cell 3", border=1)
# pdf.cell(60, 7, "Cell 4", border=1)


pdf.add_page()
pdf.cell(60, 5, "Page 2", 1)

pdf.output("b_tutorial.pdf")