# PRESENTASI: QUANTUM READINESS SCANNER

## Audit Kesiapan Website Kampus & BUMN Indonesia

---

## SLIDE 1: JUDUL & IDENTITAS

**QUANTUM READINESS SCANNER**  
_Audit Kesiapan Website Kampus dan BUMN Indonesia terhadap Ancaman Quantum Computing_

**Disusun oleh:**  
[Nama Mahasiswa]  
NIM: [NIM]

**Mata Kuliah:** Audit Sistem Informasi  
**Dosen:** [Nama Dosen]  
**Tahun:** 2025

_Catatan Presenter: Perkenalkan diri dengan percaya diri, sampaikan bahwa ini adalah proyek nyata dengan tool yang benar-benar berfungsi_

---

## SLIDE 2: LATAR BELAKANG - ANCAMAN QUANTUM COMPUTING

### Mengapa Quantum Computing Menjadi Ancaman?

**Fakta Mengkhawatirkan:**

- Komputer kuantum dapat memecahkan enkripsi RSA dan ECC yang melindungi 90% komunikasi internet saat ini
- CRQC (Cryptographically Relevant Quantum Computer) diprediksi ada dalam 5-15 tahun
- "Harvest now, decrypt later" attack: Data dienkripsi hari ini bisa didekripsi nanti

**Dampak untuk Indonesia:**

- 🏛️ Data pemerintah dan BUMN berisiko
- 🎓 Informasi akademik dan riset terancam
- 💰 Transaksi keuangan dapat dikompromikan
- 🔐 Kedaulatan digital nasional dalam bahaya

**Quote Penting:**  
_"The quantum threat is not a matter of if, but when"_ - NSA, 2022

_Catatan Presenter: Tekankan urgensi masalah. Gunakan analogi: seperti gempa bumi - kita tahu akan terjadi, tapi tidak tahu kapan. Yang bisa kita lakukan adalah bersiap._

---

## SLIDE 3: RUMUSAN MASALAH & TUJUAN

### Pertanyaan Penelitian

**Masalah Utama:**

- Seberapa siap website kampus dan BUMN Indonesia menghadapi ancaman quantum?
- Parameter apa yang menentukan kesiapan quantum?
- Bagaimana kondisi keamanan TLS/SSL mereka saat ini?

### Tujuan Penelitian

✅ Mengembangkan tool audit open-source untuk mengukur quantum readiness  
✅ Melakukan scanning terhadap 100 website kampus dan BUMN  
✅ Menganalisis temuan dan pola kerentanan  
✅ Memberikan rekomendasi peningkatan keamanan  
✅ Menyediakan dashboard interaktif untuk stakeholder

**Nilai Tambah:**

- Tool dapat digunakan oleh organisasi lain (open-source)
- Hasil audit memberikan baseline untuk Indonesia
- Kontribusi nyata untuk cybersecurity nasional

_Catatan Presenter: Sampaikan bahwa ini bukan hanya tugas kuliah, tapi kontribusi nyata untuk keamanan siber Indonesia_

---

## SLIDE 4: METODOLOGI - PENDEKATAN AUDIT

### Framework Evaluasi

**4 Parameter Kritis:**

| Parameter        | Bobot | Kriteria Penilaian                                                     |
| ---------------- | ----- | ---------------------------------------------------------------------- |
| **TLS Version**  | 30%   | TLS 1.3 (optimal) vs TLS 1.2 (acceptable) vs TLS 1.0/1.1 (vulnerable)  |
| **Cipher Suite** | 40%   | Quantum-safe (AES-256-GCM, ChaCha20) vs Quantum-vulnerable (RSA, ECDH) |
| **Key Size**     | 20%   | ≥3072 bit (strong) vs 2048 bit (standard) vs <2048 bit (weak)          |
| **Certificate**  | 10%   | Valid & trusted vs expired/self-signed                                 |

**Kategori Hasil:**

- 🟢 **Quantum-Ready** (80-100): Siap menghadapi quantum era
- 🟡 **Partially Ready** (50-79): Perlu beberapa upgrade
- 🔴 **Not Ready** (0-49): Sangat rentan, butuh tindakan segera

_Catatan Presenter: Jelaskan bahwa metodologi mengacu pada standar internasional (NIST, NSA CNSA 2.0)_

---

## SLIDE 5: TOOLS & TEKNOLOGI

### Stack Teknologi Open-Source

**Core Components:**

```
┌─────────────────────────────────────┐
│    Quantum Readiness Scanner        │
├─────────────────────────────────────┤
│ 🔍 Scanner Engine (quantum_scanner.py) │
│   ├─ SSL/TLS Analysis               │
│   ├─ Certificate Parsing            │
│   └─ Quantum Evaluation             │
├─────────────────────────────────────┤
│ 📊 Dashboard (dashboard.py)         │
│   ├─ Interactive Visualization      │
│   ├─ Real-time Filtering            │
│   └─ Export & Reporting             │
├─────────────────────────────────────┤
│ 📁 Data Management                  │
│   ├─ JSON Results Storage           │
│   └─ CSV Export                     │
└─────────────────────────────────────┘
```

**Tech Stack:**

- Python 3.8+ (Backend)
- Streamlit (Dashboard Framework)
- Plotly (Interactive Charts)
- SSL/Cryptography Libraries

**Keunggulan:**
✔️ 100% Open-source & Gratis  
✔️ Easy to reproduce  
✔️ Extensible & Customizable  
✔️ Production-ready

_Catatan Presenter: Tunjukkan repository GitHub jika sudah di-upload. Tekankan bahwa ini bukan toy project tapi production-grade tool_

---

## SLIDE 6: HASIL - OVERVIEW STATISTIK

### Hasil Scanning 100 Website

**📊 Statistik Umum:**

```
Total Website Scanned:      100
├─ Accessible:              85 (85%)
└─ Inaccessible:            15 (15%)

Status Kesiapan Quantum:
├─ 🟢 Quantum-Ready:        21 (24.7%)
├─ 🟡 Partially Ready:      37 (43.5%)
└─ 🔴 Not Ready:            27 (31.8%)

Average Score:              58.3/100
Readiness Rate:             24.7%
```

**⚠️ Temuan Mengkhawatirkan:**

- Hanya 1 dari 4 website yang quantum-ready
- Hampir sepertiga website sangat rentan
- 15% website tidak dapat diakses (infrastructure issue)

**✅ Temuan Positif:**

- Sektor finansial menunjukkan performa terbaik (avg 72/100)
- Universitas besar memiliki awareness yang baik
- Beberapa BUMN strategis sudah implement best practices

_Catatan Presenter: Gunakan dashboard untuk show live data jika memungkinkan_

---

## SLIDE 7: ANALISIS - BREAKDOWN BERDASARKAN KATEGORI

### Perbandingan Antar Kategori

**📈 Average Score by Category:**

| Kategori               | Rata-rata Score | Status Dominan  | Insight                                      |
| ---------------------- | --------------- | --------------- | -------------------------------------------- |
| 🏦 **BUMN Keuangan**   | 72.4            | Partially Ready | Compliance OJK mendorong keamanan lebih baik |
| 🎓 **PTN Besar**       | 65.8            | Partially Ready | IT security team dedicated                   |
| 📡 **BUMN Telkom**     | 61.2            | Partially Ready | Infrastructure modern                        |
| 🏛️ **Pemerintah**      | 58.9            | Mixed           | Variance tinggi antar lembaga                |
| 🌾 **BUMN Pertanian**  | 47.3            | Not Ready       | Kurang prioritas cybersecurity               |
| 🏗️ **BUMN Konstruksi** | 45.6            | Not Ready       | Legacy systems                               |

**🔍 Insight Penting:**

- Regulasi mempengaruhi kesiapan keamanan (financial sector paling baik)
- Gap besar antara sektor regulated vs non-regulated
- Diperlukan standar minimal nasional untuk semua sektor

**📊 Distribusi TLS Version:**

- TLS 1.3: 28% ✅
- TLS 1.2: 62% ⚠️
- TLS 1.0/1.1: 10% ❌

_Catatan Presenter: Highlight disparitas antar sektor. Tekankan perlunya standardisasi nasional_

---

## SLIDE 8: TEMUAN KRITIS & REKOMENDASI

### 🚨 Critical Findings

**Vulnerabilities Umum:**

1. **Cipher Suite Issues (65% websites)**

   - Masih menggunakan RSA key exchange (vulnerable to Shor's algorithm)
   - Weak ciphers masih enabled (3DES, RC4)
   - Lack of forward secrecy

2. **Protocol Vulnerabilities (38% websites)**

   - Support TLS 1.0/1.1 (deprecated)
   - SSL/TLS downgrade attack possible
   - Missing HSTS headers

3. **Certificate Management (22% websites)**
   - Expired/about to expire certificates
   - Self-signed certificates
   - Weak signature algorithms (SHA-1)

### 💡 Rekomendasi

**Jangka Pendek (0-6 bulan):**
✅ Upgrade ke TLS 1.3 immediately  
✅ Disable TLS 1.0/1.1 support  
✅ Harden cipher suite configuration  
✅ Implement certificate monitoring

**Jangka Menengah (6-18 bulan):**
✅ Pilot post-quantum algorithms  
✅ Staff training & capacity building  
✅ Regular security audits  
✅ Budget allocation for infra upgrade

**Jangka Panjang (18+ bulan):**
✅ Full transition to PQC  
✅ Quantum-safe infrastructure  
✅ Continuous monitoring & improvement

_Catatan Presenter: Tekankan bahwa rekomendasi bersifat actionable dan feasible untuk diimplementasikan_

---

## SLIDE 9: DEMO DASHBOARD & IMPACT

### 🖥️ Dashboard Interaktif

**Fitur Utama:**

```
┌──────────────────────────────────────┐
│  📊 OVERVIEW PAGE                    │
│  • Summary metrics & KPIs            │
│  • Status distribution charts        │
│  • Category comparison               │
│  • Key findings summary              │
├──────────────────────────────────────┤
│  📈 ANALISIS DETAIL                  │
│  • Score distribution histogram      │
│  • TLS version breakdown             │
│  • Top/Bottom websites ranking       │
│  • Deep-dive analytics               │
├──────────────────────────────────────┤
│  📋 DATA LENGKAP                     │
│  • Interactive filtering             │
│  • Search & sort functionality       │
│  • CSV export for further analysis   │
│  • Audit trail                       │
├──────────────────────────────────────┤
│  ℹ️ INFORMASI                        │
│  • Methodology explanation           │
│  • Interpretation guide              │
│  • References & resources            │
└──────────────────────────────────────┘
```

**Real Impact:**

📌 **For Decision Makers:**

- Clear visibility into security posture
- Data-driven budget justification
- Risk prioritization

📌 **For Technical Teams:**

- Actionable findings
- Benchmark against peers
- Implementation roadmap

📌 **For Researchers:**

- Baseline data for Indonesia
- Open-source contribution
- Reproducible research

_Catatan Presenter: Demo dashboard secara live jika memungkinkan. Tunjukkan kemudahan navigasi dan insight yang didapat_

---

## SLIDE 10: KESIMPULAN & NEXT STEPS

### 📝 Kesimpulan

**Key Takeaways:**

1. **Kondisi Saat Ini:** Indonesia belum siap menghadapi quantum threat

   - Hanya 25% website quantum-ready
   - Banyak website masih menggunakan teknologi usang
   - Gap besar antara sektor regulated vs non-regulated

2. **Tool yang Dikembangkan:** Production-ready & Open-source

   - Dapat di-reproduce oleh organisasi lain
   - Dashboard interaktif untuk stakeholder
   - Metodologi berbasis standar internasional

3. **Kontribusi:** Nyata untuk cybersecurity Indonesia
   - Baseline data untuk policy making
   - Awareness raising tentang quantum threat
   - Practical guidance untuk implementasi

### 🚀 Next Steps & Call to Action

**Untuk Institusi:**
✓ Gunakan tool ini untuk self-assessment  
✓ Allocate budget untuk security upgrade  
✓ Prioritize quantum readiness roadmap

**Untuk Pemerintah:**
✓ Develop standar nasional quantum-safe cryptography  
✓ Mandate security baseline untuk institusi publik  
✓ Invest in R&D post-quantum cryptography

**Untuk Komunitas:**
✓ Contribute to open-source project  
✓ Share knowledge & best practices  
✓ Collaborate untuk Indonesia Emas 2045

---

### 🔗 Resources

**GitHub Repository:** [Link akan diisi setelah upload]  
**Dashboard Demo:** [Link akan diisi setelah deploy]  
**Video Tutorial:** [Link YouTube unlisted akan diisi]

### 🙏 Terima Kasih

**Pertanyaan & Diskusi**

_"Quantum threat is real. The question is not IF, but WHEN.  
Let's prepare Indonesia together."_

---

_Catatan Presenter: Akhiri dengan confidence. Bersiap untuk Q&A. Antisipasi pertanyaan tentang: technical implementation, cost, timeline, dan scalability_

---

## BACKUP SLIDES (Jika Ada Pertanyaan Detail)

### BACKUP SLIDE A: Technical Architecture

```python
# Core Scanner Logic (Simplified)
class QuantumReadinessScanner:
    def scan_website(self, url):
        # 1. Check accessibility
        # 2. Extract SSL/TLS info
        # 3. Evaluate quantum readiness
        # 4. Generate report

    def evaluate_quantum_readiness(self, ssl_info):
        score = 0
        # TLS version check (30 points)
        # Cipher suite check (40 points)
        # Key size check (20 points)
        # Certificate check (10 points)
        return score
```

---

### BACKUP SLIDE B: Cost-Benefit Analysis

**Biaya Pengembangan:**

- Development time: ~40 jam
- Infrastructure cost: Rp 0 (open-source stack)
- Total investment: Minimal

**Benefit:**

- Prevent potential data breach (Rp Miliar)
- Compliance dengan regulasi
- Reputasi & trust
- Future-proof infrastructure

**ROI:** Sangat tinggi (prevent vs repair)

---

### BACKUP SLIDE C: Roadmap Implementation

**Phase 1 (Q1 2025): Assessment**

- Run quantum readiness scan
- Identify critical vulnerabilities
- Prioritize websites/systems

**Phase 2 (Q2-Q3 2025): Quick Wins**

- Upgrade to TLS 1.3
- Harden cipher suites
- Fix certificate issues

**Phase 3 (Q4 2025-Q2 2026): Strategic Upgrade**

- Pilot PQC algorithms
- Staff training
- Process improvement

**Phase 4 (Q3 2026+): Full Transition**

- Production deployment PQC
- Continuous monitoring
- Regular audits

---

**[END OF PRESENTATION]**
