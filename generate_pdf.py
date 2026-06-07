import json
from fpdf import FPDF

with open("./data/all_speakers.json", "r", encoding='utf-8') as f:
    data = json.load(f)

pdf = FPDF()
pdf.add_font("rob", "", "Roboto-Regular.ttf")
pdf.add_font("rob", "B", "Roboto-Bold.ttf")
pdf.add_font("rob", "I", "Roboto-Italic.ttf")

pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("rob", "B", 16)
pdf.cell(0, 10, "Speakers List", ln=True, align="C")

pdf.set_font("rob", size=12)
for speaker in sorted(data["speakers"], key = lambda s: s["name"]):
    pdf.ln(5)
    pdf.set_font("rob", "B", 14)
    pdf.cell(0, 10, speaker["name"], ln=True)

    pdf.set_font("rob", "I", 12)
    pdf.multi_cell(0, 5, speaker["title"])
    pdf.ln(5)

    pdf.set_font("rob", size=12)
    pdf.multi_cell(0, 5, speaker.get("abstract", ""))
    pdf.ln(5)

pdf.output("static/files/SoMPGR2025_abstracts.pdf")
