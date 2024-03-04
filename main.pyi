from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fpdf import FPDF


class CoverLetterGenerator:
    background_color: tuple[int, int, int]

    def __init__(self, name: str, company: str, position: str, email: str, phone: str):
        """"""
        self.name = name
        self.company = company
        self.position = position
        self.email = email
        self.phone = phone
        self.pdf_file = ...
        self.pdf: "FPDF" = ...

    def add_cell(self, txt: str, w: int=200, h: int=10, ln: bool=True, align: str = "L", add_break_line: bool = True) -> "CoverLetterGenerator":
        ...

    def add_multi_cell(self, txt: str, w: int = 0, h: int = 10, add_break_line: bool = True) -> "CoverLetterGenerator":
        pass

    def generate_cover_letter(self) -> None:
        pass

    def save_file(self) -> None:
        pass
