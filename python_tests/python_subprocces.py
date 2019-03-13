import os
import subprocess

cp = os.getcwd()
subprocess.call(["python", "p2.py", "hebele.csv", "-o", "find_result_pdf.pdf"])
