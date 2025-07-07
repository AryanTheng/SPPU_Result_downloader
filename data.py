import pdfplumber
import pandas as pd

# === CONFIG ===
PDF_FILE = "hallticket.pdf"  # Your PDF with all student pages
CSV_OUTPUT = "students_data.csv"

# === Helper Function ===
def extract_fields(lines):
    data = {"Seat No": "", "Name": "", "Mother": ""}
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if "SeatNo" in line:
            # Try to extract from next line if current line doesn't have value
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line:
                    data["Seat No"] = next_line.split(' ')[0].strip()
                    i += 1  # Skip next line too

        elif line.startswith("Name") and "Mother" not in line:
            parts = line.split(":")
            if len(parts) >= 2:
                data["Name"] = parts[1].strip()

        elif line.startswith("Mother"):
            parts = line.split(":")
            if len(parts) >= 2:
                data["Mother"] = parts[1].strip()

        i += 1
    return data

# === Main Process ===
all_data = []

with pdfplumber.open(PDF_FILE) as pdf:
    for page_num, page in enumerate(pdf.pages):
        text = page.extract_text()
        if not text:
            print(f"[WARNING] Skipping page {page_num+1} (empty)")
            continue

        lines = text.split("\n")
        fields = extract_fields(lines)
        all_data.append(fields)
        print(f"[INFO] Page {page_num+1} -> {fields}")

# === Save as CSV ===
df = pd.DataFrame(all_data)
df.to_csv(CSV_OUTPUT, index=False)
print(f"\n✅ Done! Saved to: {CSV_OUTPUT}")
