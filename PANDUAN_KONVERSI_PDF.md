# CARA KONVERSI LAPORAN KE PDF PROFESIONAL

## 📄 Konversi Markdown ke Word/PDF

### Opsi 1: Menggunakan Microsoft Word (Recommended untuk Tugas)

#### Langkah 1: Copy Konten dari Markdown

1. Buka file `LAPORAN_QUANTUM_READINESS_SCANNER.md`
2. Copy seluruh konten (Ctrl+A, Ctrl+C)

#### Langkah 2: Paste ke Word

1. Buka Microsoft Word
2. Buat dokumen baru
3. Paste konten (Ctrl+V)
4. Pilih "Keep Text Only" jika ada popup

#### Langkah 3: Format Dokumen

1. **Cover Page**:

   - Insert > Cover Page > Pilih template
   - Isi: Judul, Nama, NIM, Mata Kuliah, Dosen, Tanggal
   - Add logo universitas jika ada

2. **Page Setup**:

   - Layout > Margins > Custom Margins
   - Top/Bottom/Left/Right: 2.5 cm
   - Paper size: A4

3. **Font & Spacing**:

   - Select All (Ctrl+A)
   - Font: Times New Roman atau Arial
   - Size: 12pt untuk body text
   - Line spacing: 1.5

4. **Heading Formatting**:

   - Judul utama (# di markdown): Heading 1, Bold, 16pt
   - Sub-judul (## di markdown): Heading 2, Bold, 14pt
   - Sub-sub-judul (### di markdown): Heading 3, Bold, 12pt

5. **Paragraph**:

   - Text Alignment: Justify
   - First line indent: 1.27 cm (optional)
   - Spacing before: 6pt, after: 6pt

6. **Table of Contents** (Optional):

   - Insert > Table of Contents > Automatic
   - Place setelah cover page

7. **Header & Footer**:

   - Insert > Header > Blank
   - Ketik: Judul Laporan (left-aligned)
   - Insert > Footer > Plain Number 3 (center-aligned)

8. **References**:
   - Format dengan numbering atau APA style
   - Font 10-11pt acceptable untuk references

#### Langkah 4: Proofreading

- [ ] Check typo dan grammar
- [ ] Verify nama, NIM, dll di cover
- [ ] Check jumlah kata (800-1200)
- [ ] Ensure nomor halaman benar

#### Langkah 5: Save & Export

1. Save as Word (.docx):

   - File > Save As > `LAPORAN_QUANTUM_READINESS.docx`

2. Export to PDF:
   - File > Export > Create PDF/XPS
   - Optimize for: Standard (publishing online and printing)
   - Options: Include document properties
   - Save as: `LAPORAN_QUANTUM_READINESS_SCANNER.pdf`

---

### Opsi 2: Menggunakan Pandoc (Command Line)

#### Install Pandoc

**Windows:**

```powershell
# Download installer dari https://pandoc.org/installing.html
# Atau via Chocolatey:
choco install pandoc
```

**Linux:**

```bash
sudo apt-get install pandoc texlive-latex-recommended
```

**Mac:**

```bash
brew install pandoc basictex
```

#### Konversi dengan Pandoc

```bash
# Markdown to DOCX
pandoc LAPORAN_QUANTUM_READINESS_SCANNER.md -o LAPORAN_QUANTUM_READINESS.docx

# Markdown to PDF (perlu LaTeX)
pandoc LAPORAN_QUANTUM_READINESS_SCANNER.md -o LAPORAN_QUANTUM_READINESS.pdf --pdf-engine=xelatex

# Dengan custom styling
pandoc LAPORAN_QUANTUM_READINESS_SCANNER.md -o output.pdf \
  --pdf-engine=xelatex \
  -V geometry:margin=2.5cm \
  -V fontsize=12pt \
  -V mainfont="Times New Roman" \
  --toc
```

---

### Opsi 3: Menggunakan Google Docs

#### Langkah-langkah:

1. Buka Google Docs
2. File > New > Blank document
3. Copy-paste konten dari markdown
4. Format sesuai kebutuhan (mirip dengan Word)
5. File > Download > PDF document (.pdf)

**Keuntungan:**

- ✅ Free & cloud-based
- ✅ Auto-save
- ✅ Easy collaboration
- ✅ Built-in spell check

---

### Opsi 4: Online Markdown to PDF Converters

**Recommended Sites:**

- [Markdown to PDF](https://www.markdowntopdf.com/)
- [Dillinger](https://dillinger.io/) - Edit + Export
- [StackEdit](https://stackedit.io/) - Markdown editor with export

**Steps:**

1. Upload atau paste markdown content
2. Preview hasil
3. Customize styling (jika ada opsi)
4. Download PDF

**⚠️ Caution:** Jangan upload konten sensitive ke public converters

---

## 📐 Template Formatting Guidelines

### Cover Page (Halaman Pertama)

```
================================
QUANTUM READINESS SCANNER
Audit Kesiapan Website Kampus dan BUMN Indonesia
terhadap Ancaman Quantum Computing
================================

[Logo Universitas]

Disusun oleh:
[Nama Lengkap]
NIM: [NIM]

PROGRAM STUDI [NAMA PRODI]
FAKULTAS [NAMA FAKULTAS]
[NAMA UNIVERSITAS]

Mata Kuliah: Audit Sistem Informasi
Dosen: [Nama Dosen]

[Kota, Bulan Tahun]
```

### Table of Contents (Halaman Kedua)

```
DAFTAR ISI

I.    PENDAHULUAN.........................................1
      A. Latar Belakang..................................1
      B. Rumusan Masalah.................................2
      C. Tujuan Penelitian...............................2
      D. Manfaat Penelitian..............................3

II.   METODOLOGI..........................................4
      A. Kerangka Konseptual.............................4
      B. Desain Tool Audit...............................5
      C. Kriteria Evaluasi...............................6
      D. Populasi dan Sampel.............................7
      E. Prosedur Pengumpulan Data.......................8
      F. Analisis Data...................................9

III.  TOOLS DAN TEKNOLOGI................................10
      ... (dst)

IV.   HASIL DAN PEMBAHASAN...............................12
      ... (dst)

V.    KESIMPULAN.........................................18

VI.   REFERENSI..........................................19
```

### Header & Footer

**Header (Every page except cover):**

```
Quantum Readiness Scanner - Audit Website Indonesia 2025
_____________________________________________________________
```

**Footer (Every page):**

```
_____________________________________________________________
                           Halaman X
```

---

## 🎨 Styling Tips untuk Profesional Look

### Colors (untuk yang convert digital/PPT):

- **Heading**: Dark Blue (#1f4788)
- **Subheading**: Medium Blue (#2e5c9a)
- **Body text**: Black (#000000)
- **Emphasis**: Bold or Italic (not color)
- **Links**: Blue (#0066cc) with underline

### Typography:

- **Academic/Formal**: Times New Roman, Georgia
- **Modern/Tech**: Arial, Calibri, Segoe UI
- **Code/Technical**: Courier New, Consolas

### Spacing:

- **Between paragraphs**: 6pt before, 6pt after
- **Between sections**: 12pt before heading
- **Line spacing**: 1.5 for body, 1.15 for references

### Lists:

- Use bullet points or numbers
- Indent: 1.27 cm
- Hanging indent for references

---

## ✅ Final Checklist Sebelum Submit PDF

### Content:

- [ ] All sections present (Pendahuluan s/d Referensi)
- [ ] Word count 800-1200 (check di Word: Review > Word Count)
- [ ] No lorem ipsum or placeholder text
- [ ] All [brackets] replaced with actual content
- [ ] Data akurat dan konsisten

### Formatting:

- [ ] Cover page professional
- [ ] Table of contents (if required)
- [ ] Consistent heading styles
- [ ] Page numbers present
- [ ] Header/footer consistent
- [ ] Margins: 2.5cm all sides
- [ ] Font: 12pt Times New Roman/Arial
- [ ] Line spacing: 1.5

### Quality:

- [ ] No typos or grammar errors
- [ ] Professional tone throughout
- [ ] Citations formatted properly
- [ ] References complete (min 10)
- [ ] Images/tables (if any) clear and captioned

### Technical:

- [ ] PDF file size <5MB
- [ ] File name: `LAPORAN_QUANTUM_READINESS_SCANNER.pdf`
- [ ] PDF searchable (not scanned image)
- [ ] No password protection
- [ ] Compatible with Adobe Reader

---

## 📊 Alternative: LaTeX for Advanced Users

### Basic LaTeX Template

```latex
\documentclass[12pt,a4paper]{article}
\usepackage[margin=2.5cm]{geometry}
\usepackage[utf8]{inputenc}
\usepackage[indonesian]{babel}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{setspace}

\onehalfspacing

\title{Quantum Readiness Scanner\\
\large Audit Kesiapan Website Kampus dan BUMN Indonesia}
\author{[Nama Mahasiswa]\\NIM: [NIM]}
\date{\today}

\begin{document}

\maketitle
\newpage

\tableofcontents
\newpage

\section{Pendahuluan}
\subsection{Latar Belakang}
[Your content here...]

\subsection{Rumusan Masalah}
[Your content here...]

% ... more sections

\section{Kesimpulan}
[Your content here...]

\newpage
\begin{thebibliography}{99}
\bibitem{nist2024}
National Institute of Standards and Technology (NIST). (2024).
\textit{Post-Quantum Cryptography Standardization}.
\url{https://csrc.nist.gov/projects/post-quantum-cryptography}
% ... more references
\end{thebibliography}

\end{document}
```

### Compile LaTeX:

```bash
# Install TeXLive or MiKTeX first
pdflatex laporan.tex
bibtex laporan  # if using bibliography
pdflatex laporan.tex
pdflatex laporan.tex
```

---

## 🚀 Quick Actions

### Just Want to Submit Fast?

**5-Minute Method:**

1. Open `LAPORAN_QUANTUM_READINESS_SCANNER.md` in VS Code
2. Install extension: "Markdown PDF" by yzane
3. Right-click in editor > "Markdown PDF: Export (pdf)"
4. Done! PDF generated.

**Customize styling:**
Create `.vscode/settings.json`:

```json
{
  "markdown-pdf.styles": [
    "https://fonts.googleapis.com/css?family=Times+New+Roman"
  ],
  "markdown-pdf.displayHeaderFooter": true,
  "markdown-pdf.headerTemplate": "<div style='font-size:9px;width:100%;text-align:center;'>Quantum Readiness Scanner - Audit 2025</div>",
  "markdown-pdf.footerTemplate": "<div style='font-size:9px;width:100%;text-align:center;'><span class='pageNumber'></span></div>",
  "markdown-pdf.margin": {
    "top": "2.5cm",
    "right": "2.5cm",
    "bottom": "2.5cm",
    "left": "2.5cm"
  }
}
```

---

## 💡 Pro Tips

1. **Don't wait until last minute** - Format issues take time to fix
2. **Test print preview** - Ensure it looks good on paper
3. **Ask for feedback** - Have someone proofread
4. **Keep original** - Don't delete .md file, keep both versions
5. **Version control** - Save as `v1.pdf`, `v2.pdf`, `final.pdf`
6. **Backup cloud** - Upload to Google Drive/OneDrive

---

## 📞 Need Help?

**If conversion fails:**

1. Check markdown syntax (extra ``` or ### might break)
2. Remove special characters
3. Try different converter
4. Ask for help in class group

**If formatting looks weird:**

1. Manually adjust in Word
2. Use "Clear Formatting" and reapply
3. Check page breaks (Ctrl+Enter)
4. Verify margins and spacing

---

**You Got This! 💪**

The hard part (coding) is done. Formatting is easy!
