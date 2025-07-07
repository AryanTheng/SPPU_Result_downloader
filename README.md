# 📥 SPPU Result Downloader

**SPPU Result Downloader** is an semiautomated tool to download and organize results of students from **Savitribai Phule Pune University (SPPU)**. It scrapes public results based on seat numbers and exports the data into structured formats such as CSV and PDF for institutional or personal analysis.

> ⚠️ **For educational purposes only.** This tool respects all applicable usage policies and privacy rights. No missuse of data has been done.

---

## 📌 Features

- ✅ Bulk download SPPU results using seat numbers
- ✅ Fetches Name, Mother's Name, SGPA/CGPA, Semester-wise results
- ✅ Exports data in `CSV` and formatted `PDF` reports
- ✅ Logs invalid or missing seat numbers
- ✅ Compatible with 2024-25 result formats

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sppu-result-downloader.git
# SPPU_Result_downloader

pip install -r requirements.txt
```

### Workflow
![image](https://github.com/user-attachments/assets/7dee4951-04cf-493d-880b-4431e8f91d16)

[1] Read Seat Numbers from input.csv
  │
  ├──> [2] Send request to SPPU Result Portal
  │       └── Parse HTML or PDF response
  │
  ├──> [3] Extract:
  │       ├─ Student Name
  │       ├─ Mother Name
  │       ├─ SGPA/CGPA
  │       ├─ Failed Subjects (if any)
  │
  ├──> [4] Save each record to:
  │       ├─ results.csv (structured format)
  │       └─ results.pdf (pretty formatted for print)
  │
  └──> [5] Log errors to `errors.log` if seat not found or site fails
  
