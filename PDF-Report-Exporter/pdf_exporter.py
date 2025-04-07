from fpdf import FPDF
from datetime import datetime

def generate_pdf_from_txt(txt_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    title = "Incident Report PDF"
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, title, ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    with open(txt_file, "r", encoding="utf-8") as f:
        for line in f:
            clean_line = line.encode("ascii", "ignore").decode("ascii")
            pdf.multi_cell(0, 10, clean_line.strip())


    filename = f"incident_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf.output(filename)
    print(f"✅ PDF created: {filename}")

if __name__ == "__main__":
    report = input("Enter path to .txt report (e.g. incident_report_sample.txt): ").strip()
    generate_pdf_from_txt(report)
