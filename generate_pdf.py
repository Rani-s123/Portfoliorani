import subprocess
import os
import sys

# Paths setup
html_path = os.path.abspath("case_study.html")
pdf_path = os.path.abspath("TravelWonder_CaseStudy_Premium.pdf")
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

print(f"Checking HTML template at: {html_path}")
if not os.path.exists(html_path):
    print("Error: case_study.html not found.")
    sys.exit(1)

print(f"Checking Chrome installation at: {chrome_path}")
if not os.path.exists(chrome_path):
    print("Error: Google Chrome not found at standard path. Please make sure Chrome is installed.")
    sys.exit(1)

# Command to execute headless Chrome for PDF print
cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    f"--print-to-pdf={pdf_path}",
    "--no-margins",
    html_path
]

print("Rendering HTML to PDF...")
try:
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    if os.path.exists(pdf_path):
        print("\n" + "="*50)
        print(f"SUCCESS: PDF generated successfully!")
        print(f"Location: {pdf_path}")
        print(f"Size: {os.path.getsize(pdf_path)} bytes")
        print("="*50 + "\n")
    else:
        print("Error: Chrome finished successfully but PDF file was not created.")
except subprocess.CalledProcessError as e:
    print("Failed to run Google Chrome in headless mode.")
    print("Stderr:", e.stderr)
    print("Stdout:", e.stdout)
except Exception as ex:
    print(f"An unexpected error occurred: {ex}")
