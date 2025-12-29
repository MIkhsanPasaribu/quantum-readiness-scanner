# ⚡ QUICK START GUIDE

## Quantum Readiness Scanner - Mulai dalam 5 Menit!

---

## 🎯 Langkah Cepat untuk Memulai

### Step 1: Persiapan Environment (2 menit)

#### Windows:

```powershell
# Buka PowerShell atau Command Prompt
# Navigate ke folder proyek
cd C:\Users\mikhs\OneDrive\Documents\Audit14Athal

# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Linux/Mac:

```bash
# Buka Terminal
# Navigate ke folder proyek
cd ~/Documents/Audit14Athal

# Buat virtual environment
python3 -m venv venv

# Aktifkan virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

**Expected Output:**

```
Successfully installed streamlit-1.31.0 pandas-2.2.0 plotly-5.18.0 ...
```

---

### Step 2: Jalankan Scanner (1 menit untuk setup, 5-10 menit untuk scan)

```bash
# Pastikan virtual environment aktif (lihat (venv) di prompt)
python quantum_scanner.py
```

**Apa yang Terjadi:**

1. Scanner membaca `website_list.txt` (100 URLs)
2. Melakukan koneksi SSL/TLS ke setiap website
3. Mengekstrak informasi keamanan
4. Mengevaluasi quantum readiness
5. Menyimpan hasil ke `scan_results.json`

**Progress Output:**

```
======================================================================
QUANTUM READINESS SCANNER
======================================================================

Total website yang akan di-scan: 100

[1/100] Scanning: https://www.ui.ac.id
  Status: Partially Ready - Score: 65/100

[2/100] Scanning: https://www.ugm.ac.id
  Status: Quantum-Ready - Score: 85/100

...
```

**⏳ Waktu Estimasi:** 5-10 menit (tergantung kecepatan internet)

---

### Step 3: Jalankan Dashboard (30 detik)

```bash
# Di terminal yang sama atau terminal baru (dengan venv aktif)
streamlit run dashboard.py
```

**Apa yang Terjadi:**

1. Streamlit server akan start
2. Browser otomatis terbuka ke `http://localhost:8501`
3. Dashboard menampilkan visualisasi hasil scan

**Expected Output:**

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.x:8501

  For better performance, install the Watchdog module:
  $ pip install watchdog
```

**Browser akan otomatis buka dashboard!** 🎉

---

## 🛠️ Troubleshooting Cepat

### Problem 1: "python: command not found"

```bash
# Windows: Gunakan 'py' instead of 'python'
py -m venv venv

# Linux/Mac: Gunakan 'python3'
python3 -m venv venv
```

### Problem 2: "pip: command not found"

```bash
# Install pip terlebih dahulu
# Windows:
py -m ensurepip --upgrade

# Linux:
sudo apt-get install python3-pip

# Mac:
brew install python3
```

### Problem 3: "ModuleNotFoundError: No module named 'streamlit'"

```bash
# Virtual environment mungkin tidak aktif
# Aktifkan dulu, lalu install lagi
# Windows:
venv\Scripts\activate
pip install -r requirements.txt

# Linux/Mac:
source venv/bin/activate
pip install -r requirements.txt
```

### Problem 4: "File scan_results.json not found"

```bash
# Dashboard membutuhkan hasil scan terlebih dahulu
# Jalankan scanner dulu:
python quantum_scanner.py

# Setelah selesai, baru jalankan dashboard:
streamlit run dashboard.py
```

### Problem 5: Port 8501 sudah digunakan

```bash
# Gunakan port lain
streamlit run dashboard.py --server.port 8502
```

---

## 📝 Kustomisasi Website Target

Ingin scan website lain? Edit `website_list.txt`:

```txt
# Tambahkan URL (satu per baris)
https://www.example.ac.id
https://www.contoh-bumn.co.id
https://www.website-anda.com

# Baris dengan # adalah komentar (diabaikan)
# Format: HTTPS URL lengkap
```

**Tips:**

- Gunakan HTTPS (bukan HTTP) untuk mengecek SSL/TLS
- Pastikan URL valid dan accessible
- Rekomendasi: 50-200 website (terlalu sedikit kurang representatif, terlalu banyak lama)

Setelah edit, jalankan ulang scanner:

```bash
python quantum_scanner.py
```

---

## 🎨 Melihat Hasil

### Via Dashboard (Recommended)

```bash
streamlit run dashboard.py
```

**Navigate ke:**

- **📊 Overview**: Lihat ringkasan metrik dan charts
- **📈 Analisis Detail**: Deep dive ke score distribution dan ranking
- **📋 Data Lengkap**: Filter dan export data
- **ℹ️ Informasi**: Baca tentang metodologi

### Via JSON File (Manual)

```bash
# Buka dengan text editor atau JSON viewer
code scan_results.json  # VS Code
notepad scan_results.json  # Notepad
cat scan_results.json  # Linux/Mac terminal
```

### Export ke CSV

1. Buka dashboard
2. Navigate ke **📋 Data Lengkap**
3. (Optional) Apply filter
4. Click **📥 Download Data (CSV)**
5. File akan tersimpan di Downloads folder

---

## 🚀 Next Steps

### Untuk Tugas Kuliah:

1. **Generate Fresh Data**

   ```bash
   python quantum_scanner.py
   ```

2. **Screenshot Dashboard**

   - Buka dashboard
   - Screenshot halaman Overview dan Analisis
   - Simpan untuk laporan

3. **Write Laporan**

   - Template: `LAPORAN_QUANTUM_READINESS_SCANNER.md`
   - Target: 800-1200 kata
   - Include data dari hasil scan

4. **Create Presentasi**

   - Template: `PRESENTASI_QUANTUM_READINESS.md`
   - Convert ke PPT/PDF
   - Total: 10 slides

5. **Record Video**

   - Panduan: `PANDUAN_VIDEO_DEMO.md`
   - Durasi: 3-5 menit
   - Upload YouTube (unlisted)

6. **Upload GitHub**

   ```bash
   git init
   git add .
   git commit -m "Initial commit: Quantum Readiness Scanner"
   git branch -M main
   git remote add origin https://github.com/[username]/quantum-readiness-scanner.git
   git push -u origin main
   ```

7. **Submit**
   - Checklist: `CHECKLIST_SUBMISSION.md`
   - Include: PDF laporan, link GitHub, link YouTube

---

## 📊 Menginterpretasi Hasil

### Score Ranges:

| Score  | Status             | Meaning                   | Action             |
| ------ | ------------------ | ------------------------- | ------------------ |
| 80-100 | 🟢 Quantum-Ready   | Sangat baik, sudah siap   | Maintain & monitor |
| 50-79  | 🟡 Partially Ready | Cukup baik, perlu upgrade | Plan improvement   |
| 0-49   | 🔴 Not Ready       | Rentan, urgent action     | Immediate upgrade  |

### Key Metrics:

**Accessibility Rate:**

- > 90%: Excellent (infrastruktur solid)
- 70-90%: Good (beberapa website down)
- <70%: Poor (banyak infrastructure issues)

**Readiness Rate:**

- > 50%: Leading (ahead of curve)
- 25-50%: Average (need improvement)
- <25%: Lagging (urgent attention needed)

**Average Score:**

- > 70: Strong security posture
- 50-70: Moderate security posture
- <50: Weak security posture

---

## 🎓 Tips Sukses

### Untuk Development:

✅ **Test incrementally**: Jangan tunggu sampai selesai semua  
✅ **Commit often**: Git commit setiap fitur selesai  
✅ **Comment your code**: Future you akan berterima kasih  
✅ **Handle errors**: Expect the unexpected  
✅ **Keep it simple**: KISS principle

### Untuk Dokumentasi:

✅ **Write as you code**: Jangan tunda dokumentasi  
✅ **Use examples**: Show, don't just tell  
✅ **Be specific**: "Run python scanner.py" > "Run the program"  
✅ **Include screenshots**: Visual aids membantu  
✅ **Proofread**: Typo = unprofessional

### Untuk Presentasi:

✅ **Know your data**: Pahami setiap angka  
✅ **Tell a story**: Data + narrative = impact  
✅ **Practice demo**: Rehearse sebelum record  
✅ **Time yourself**: 3-5 menit strict  
✅ **Be confident**: You built something amazing!

---

## 📞 Getting Help

### Resources:

**Dokumentasi Proyek:**

- README.md - Comprehensive guide
- LAPORAN\_\*.md - Academic report template
- PRESENTASI\_\*.md - Presentation outline
- PANDUAN_VIDEO_DEMO.md - Video production guide

**External Resources:**

- [Streamlit Docs](https://docs.streamlit.io)
- [Plotly Python](https://plotly.com/python/)
- [Python SSL Docs](https://docs.python.org/3/library/ssl.html)

**Community:**

- GitHub Issues (untuk bug reports)
- Stack Overflow (untuk technical questions)
- Class WhatsApp Group (untuk diskusi tugas)

---

## 🎉 Selamat!

Anda sekarang memiliki:

- ✅ Quantum Readiness Scanner yang berfungsi
- ✅ Dashboard interaktif untuk visualisasi
- ✅ Data real dari 100 website Indonesia
- ✅ Dokumentasi lengkap
- ✅ Portfolio piece untuk CV

**This is not just an assignment. This is your contribution to Indonesia's cybersecurity!**

---

## ⏱️ Time Investment

**Total time untuk complete project:**

- Setup & development: 6-8 jam ✅ (Already done!)
- Testing & debugging: 2-3 jam
- Documentation: 3-4 jam
- Laporan akademis: 3-4 jam
- Presentasi: 2-3 jam
- Video demo: 2-3 jam
- Polish & submission: 1-2 jam

**TOTAL: ~20-30 jam** untuk project berkualitas tinggi

**ROI:** Portfolio piece + skills + nilai bagus + potensial bonus = PRICELESS! 🚀

---

**Ready to change Indonesia's cybersecurity landscape?**

**LET'S GO! 🇮🇩🔐**

---

_Last updated: 29 Desember 2025_
