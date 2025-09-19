from fpdf import FPDF
import sys

def md_to_pdf(input_file, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(True, margin=15)
    pdf.set_font("Arial", size=12)
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            pdf.multi_cell(0, 8, line.rstrip())
    pdf.output(output_file)
    print(f"✅ Converted {input_file} → {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python md2pdf.py input.md output.pdf")
    else:
        md_to_pdf(sys.argv[1], sys.argv[2])

