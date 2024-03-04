from fpdf import FPDF

class PDFWithBackground(FPDF):
    def __init__(self):
        super().__init__()

    def add_page(self):
        super().add_page()
        self.set_fill_color(189, 212, 188)  # Set background color (white in this case)
        self.rect(0, 0, self.w, self.h, 'F')  # Draw filled rectangle covering the entire page

pdf = PDFWithBackground()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="This is some text on the page with background color", ln=True)
pdf.output("output.pdf")
