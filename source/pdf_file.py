from fpdf import FPDF


class PdfFile(FPDF):
    """
    A child class of FPDF class with ready-to-use methods.
    - To set a background color
    - Add a cell
    - Add a multi-cell
    """

    def set_background_color(self, rgb: tuple = None):
        self.set_fill_color(*rgb)
        self.rect(0, 0, self.w, self.h, 'F')
        return self

    def add_cell(self, txt: str, w=200, h=10, ln=True, align="L", add_break_line=True):
        """
        Adds a single line cell.

        Args:
            txt (str): The text content to add to the cell.
            w (int, optional): The width of the cell in millimeters. Defaults to 200.
            h (int, optional): The height of the cell in millimeters. Defaults to 10.
            ln (bool, optional): Whether to start a new line after adding the cell. Defaults to True.
            align (str, optional): The alignment of the text within the cell ("L" for left, "R" for right).
            Defaults to "L".
            add_break_line (bool, optional): Whether to add a line break of 10 points after the cell. Defaults to True.

        Returns:
            CoverLetterGenerator: Returns itself for method chaining.
        """
        self.cell(w=w, h=h, txt=txt, ln=ln, align=align)
        if add_break_line:
            self.ln(10)
        return self

    def add_multi_cell(self, txt: str, w=0, h=10, add_break_line=True):
        """
        Adds a  multi-line cell.

        Args:
            txt (str): The text content to add to the cell.
            w (int, optional): The width of the cell in millimeters. Defaults to 200.
            h (int, optional): The height of the cell in millimeters. Defaults to 10.
            add_break_line (bool, optional): Whether to add a line break of 10 points after the cell. Defaults to True.

        Returns:
            CoverLetterGenerator: Returns itself for method chaining.
        """

        self.multi_cell(w, h, txt=txt)
        if add_break_line:
            self.ln(10)
        return self
