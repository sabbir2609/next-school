# pip install fpdf2

from fpdf import FPDF
import random
import string


class PDF(FPDF):
    def header(self):
        self.set_font("Courier", "B", 12)
        self.cell(0, 10, "Random PDF Document", 0, 1, "C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")


def generate_random_pdf(max_size_kb=200, max_pages=10):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    page_count = 0

    while page_count < max_pages:
        # Generate random content (text) for the page
        content = "".join(
            random.choice(string.printable) for _ in range(5000)
        )  # Approximately 5KB

        pdf.multi_cell(0, 10, content)
        pdf.add_page()
        page_count += 1

        # Check the size of the PDF
        if pdf.w * pdf.h * (pdf.page_no() - 1) / 1024 > max_size_kb:
            break

    return pdf


if __name__ == "__main__":
    pdf = generate_random_pdf(max_size_kb=200, max_pages=10)
    pdf_file = "random.pdf"
    pdf.output(pdf_file)

    print(
        f"Random PDF file '{pdf_file}' generated with a maximum of 10 pages and 200KB size."
    )
