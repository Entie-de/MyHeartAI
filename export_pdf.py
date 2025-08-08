# myheartai/export_pdf.py

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import inch
import os

# Register font for Unicode (including Urdu, Arabic, etc.)
pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))

def export_to_pdf(image_path, memory, caption, story, translation, output_path):
    doc = SimpleDocTemplate(output_path, pagesize=A4)
    elements = []
    
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER, fontName='HeiseiMin-W3', fontSize=12, leading=15))
    styles.add(ParagraphStyle(name='Title', alignment=TA_CENTER, fontName='HeiseiMin-W3', fontSize=18, spaceAfter=20))

    # Title
    elements.append(Paragraph("🩷 MyHeartAI Scrapbook Page", styles['Title']))
    
    # Image
    if image_path and os.path.exists(image_path):
        img = Image(image_path)
        img._restrictSize(5.5 * inch, 5 * inch)
        elements.append(img)
        elements.append(Spacer(1, 12))

    # Memory
    elements.append(Paragraph(f"<b>Memory:</b> {memory}", styles['Center']))
    elements.append(Spacer(1, 10))

    # Caption
    elements.append(Paragraph(f"<b>Caption:</b> {caption}", styles['Center']))
    elements.append(Spacer(1, 10))

    # Story
    elements.append(Paragraph(f"<b>Story:</b> {story}", styles['Center']))
    elements.append(Spacer(1, 10))

    # Urdu
    elements.append(Paragraph(f"<b>Urdu Translation:</b> {translation}", styles['Center']))
    elements.append(Spacer(1, 20))

    doc.build(elements)
