#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from textwrap import wrap
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph


def hello():
    doc = SimpleDocTemplate("hello_platypus.pdf", pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72,
                            bottomMargin=18)
    styles = getSampleStyleSheet()

    flowables = []

    with open("ger.csv", "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            wraped_text = "\n".join(wrap(line[0], 80))  # 80 is line width
            para = Paragraph(wraped_text, style=styles["Normal"])
            flowables.append(para)
    doc.build(flowables)


if __name__ == '__main__':
    pass


def pdf_df(c, testo, x, y):
    c.draw(x, y, testo)


x = 500
canvas = canvas.Canvas("form.pdf", pagesize=letter)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 12)
with open("ger.csv", "rb") as f:
    reader = csv.reader(f, delimiter="\t")
    for i, line in enumerate(reader):
        wraped_text = "\n".join(wrap(line[0], 80))  # 80 is line width
        canvas.drawString(300, x, wraped_text)
        x = x - 20
    canvas.save()





    # from reportlab.pdfgen.canvas import Canvas
    # from reportlab.lib.pagesizes import letter, landscape
    # from reportlab.platypus import Paragraph, Frame, KeepInFrame
    # from reportlab.lib.styles import getSampleStyleSheet
    # from reportlab.lib.units import inch
    #
    # read_csv = pd.read_csv("ger.csv")
    # c = Canvas('foo.pdf', pagesize=landscape(letter))
    # frame1 = Frame(inch, inch, 10*inch, 10*inch, showBoundary=0)
    #
    # styles = getSampleStyleSheet()
    # s = "foo bar " * 1000
    # story = [Paragraph(s, styles['Normal'])]
    # story_inframe = KeepInFrame(4*inch, 8*inch, story)
    # frame1._add(story_inframe,c)
    # c.save()
