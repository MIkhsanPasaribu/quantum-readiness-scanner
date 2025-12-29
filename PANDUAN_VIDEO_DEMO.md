# PANDUAN VIDEO DEMO

## Quantum Readiness Scanner - 3-5 Menit

---

## 📹 STRUKTUR VIDEO (Total: 4 menit)

### INTRO (30 detik)

**Visual:** Tampilkan slide judul atau logo proyek

**Script:**
"Halo, saya [Nama] dari [Universitas]. Pada kesempatan ini saya akan mendemonstrasikan Quantum Readiness Scanner, sebuah tool audit open-source yang saya kembangkan untuk mengukur kesiapan website kampus dan BUMN Indonesia dalam menghadapi ancaman quantum computing.

Komputer kuantum diprediksi akan dapat memecahkan enkripsi modern dalam 5-15 tahun ke depan. Tool ini membantu kita mengetahui seberapa siap website-website strategis Indonesia menghadapi ancaman tersebut."

---

### BAGIAN 1: OVERVIEW MASALAH (45 detik)

**Visual:** Slide tentang ancaman quantum / diagram

**Script:**
"Mengapa ini penting? Komputer kuantum dapat memecahkan algoritma RSA dan ECC yang melindungi 90% komunikasi internet saat ini. Ini berarti data yang dienkripsi hari ini, termasuk data pemerintah, BUMN, dan institusi pendidikan, bisa didekripsi di masa depan.

Tool ini mengevaluasi 4 parameter kritis: versi TLS yang digunakan, cipher suite, ukuran kunci kriptografi, dan validitas sertifikat. Berdasarkan parameter tersebut, setiap website mendapat score 0-100 dan dikategorikan menjadi Quantum-Ready, Partially Ready, atau Not Ready."

---

### BAGIAN 2: DEMO SCANNING (60 detik)

**Visual:** Screen recording terminal menjalankan scanner

**Script:**
"Mari kita lihat tool ini bekerja. Saya sudah menyiapkan list 100 website kampus dan BUMN Indonesia dalam file website_list.txt.

[Tampilkan isi file sekilas]

Sekarang saya jalankan scanner dengan perintah: python quantum_scanner.py

[Tampilkan proses scanning, biarkan beberapa detik untuk show progress]

Scanner akan melakukan koneksi SSL/TLS ke setiap website, mengekstrak informasi keamanan, dan mengevaluasi berdasarkan kriteria yang telah ditetapkan. Proses ini memakan waktu sekitar 5-10 menit untuk 100 website dengan jeda 0.5 detik antar request untuk menghindari rate limiting.

[Skip ke hasil akhir dengan editing]

Setelah selesai, kita mendapat ringkasan hasil: dari 100 website, 85 dapat diakses, dan hanya 21 website atau 24.7% yang masuk kategori Quantum-Ready. Ini menunjukkan masih banyak pekerjaan yang perlu dilakukan.

Hasil lengkap disimpan dalam format JSON yang dapat dianalisis lebih lanjut."

---

### BAGIAN 3: DEMO DASHBOARD (90 detik)

**Visual:** Screen recording dashboard Streamlit

**Script:**
"Sekarang mari kita lihat visualisasi interaktif melalui dashboard. Saya jalankan dengan perintah: streamlit run dashboard.py

[Tampilkan dashboard loading dan terbuka di browser]

Dashboard memiliki 4 halaman utama:

**[Navigate ke Overview page]**
Halaman Overview menampilkan metrik ringkasan. Kita bisa lihat bahwa dari 85 website yang accessible, 21 quantum-ready, 37 partially ready, dan 27 not ready. Rata-rata score adalah 58.3 dari 100.

Chart pie menunjukkan distribusi status, sementara bar chart membandingkan performa antar kategori. Terlihat bahwa BUMN sektor keuangan memiliki performa terbaik karena regulasi OJK yang ketat.

**[Navigate ke Analisis Detail]**
Di halaman Analisis Detail, kita bisa lihat histogram distribusi score. Mayoritas website berada di range 50-70, yang artinya partially ready.

Chart distribusi TLS version menunjukkan bahwa 62% website masih menggunakan TLS 1.2, padahal TLS 1.3 sudah menjadi standar sejak 2018.

Ada juga ranking top 10 dan bottom 10 websites berdasarkan score.

**[Navigate ke Data Lengkap]**
Halaman Data Lengkap menampilkan seluruh hasil dalam bentuk tabel yang bisa difilter. Misalnya, saya filter hanya website kategori Universitas dengan status Not Ready.

[Tunjukkan filtering]

Data bisa diexport ke CSV untuk analisis lebih lanjut atau reporting.

**[Navigate ke Informasi]**
Halaman Informasi menjelaskan metodologi, cara interpretasi hasil, dan referensi yang digunakan."

---

### BAGIAN 4: HIGHLIGHTS & REKOMENDASI (45 detik)

**Visual:** Kembali ke slide atau tetap di dashboard

**Script:**
"Beberapa temuan penting dari penelitian ini:

Pertama, hanya 1 dari 4 website yang sudah quantum-ready. Ini mengkhawatirkan mengingat ancaman quantum sudah di depan mata.

Kedua, masih banyak website yang support protokol usang seperti TLS 1.0 dan 1.1 yang seharusnya sudah didisable.

Ketiga, 65% website menggunakan cipher suite yang vulnerable terhadap quantum attack.

Rekomendasi kami:

- Segera upgrade ke TLS 1.3
- Harden cipher suite configuration
- Increase key size minimal ke 3072 bit
- Monitor dan renew certificate secara teratur
- Plan untuk transisi ke post-quantum cryptography"

---

### CLOSING (30 detik)

**Visual:** Slide kesimpulan atau GitHub repo

**Script:**
"Tool ini sepenuhnya open-source dan tersedia di GitHub. Link ada di deskripsi video. Dokumentasi lengkap termasuk laporan akademis dan slide presentasi juga sudah disertakan.

Ini bukan hanya tugas kuliah, tapi kontribusi nyata untuk keamanan siber Indonesia. Saya berharap tool ini bisa digunakan oleh organisasi lain untuk self-assessment dan bersama-sama kita persiapkan Indonesia yang quantum-safe.

Terima kasih telah menonton. Jangan lupa star repository di GitHub jika Anda merasa tool ini bermanfaat!"

---

## 🎬 TIPS PRODUKSI VIDEO

### Technical Setup:

**Software Recording:**

- OBS Studio (gratis, powerful)
- Camtasia (berbayar, tapi mudah editing)
- Windows Game Bar (Ctrl+G, built-in Windows)

**Audio:**

- Gunakan mic eksternal jika ada (bukan mic laptop)
- Record di ruangan sunyi
- Test audio quality sebelum final recording

**Visual:**

- Screen resolution: 1920x1080 (Full HD)
- Font size di terminal/editor: besar agar readable
- Close aplikasi yang tidak perlu
- Disable notification

### Editing Tips:

**Pacing:**

- Gunakan time-lapse untuk bagian scanning (2-3x speed)
- Cut silent moments yang terlalu lama
- Transition smooth antar scene

**Overlay:**

- Tambahkan text overlay untuk highlight poin penting
- Arrow/circle untuk menarik perhatian ke elemen tertentu
- Lower third untuk menampilkan nama/info

**Music:**

- Background music halus (royalty-free)
- Volume music 20-30% dari voice
- Gunakan music dari YouTube Audio Library atau Epidemic Sound

### Final Export:

- Format: MP4 (H.264)
- Resolution: 1920x1080
- Frame rate: 30fps atau 60fps
- Bitrate: 8-10 Mbps
- File size target: <500MB untuk upload smooth

---

## 📝 CHECKLIST SEBELUM UPLOAD

**Pre-Production:**

- [ ] Script sudah dihafal/dipahami dengan baik
- [ ] Software recording sudah ditest
- [ ] Audio quality sudah ditest
- [ ] Background/environment sudah rapi
- [ ] Code dan dashboard sudah berjalan lancar

**During Production:**

- [ ] Voice jelas dan tidak terburu-buru
- [ ] Tidak ada error/crash selama demo
- [ ] Cursor movement tidak terlalu cepat
- [ ] Zoom in untuk text yang kecil

**Post-Production:**

- [ ] Video duration 3-5 menit (strict!)
- [ ] Audio volume consistent
- [ ] No awkward pauses
- [ ] Closed caption/subtitle (optional tapi bagus)

**Upload Preparation:**

- [ ] Title: "Quantum Readiness Scanner - Audit Kesiapan Website Indonesia"
- [ ] Description: Include link GitHub, penjelasan singkat, keywords
- [ ] Thumbnail: Eye-catching, include project name
- [ ] Tags: quantum computing, cybersecurity, audit, Indonesia, etc.
- [ ] Upload as UNLISTED (bukan private, bukan public)

---

## 🎯 CRITICAL SUCCESS FACTORS

1. **Clarity**: Suara jelas, penjelasan mudah dipahami
2. **Flow**: Smooth transition antar bagian, tidak terputus-putus
3. **Demo**: Tool benar-benar berjalan, tidak fake/mockup
4. **Time Management**: Tepat 3-5 menit, tidak kurang tidak lebih
5. **Professional**: Tidak ada typo, tidak ada error message random
6. **Enthusiasm**: Tunjukkan passion dan confidence!

---

## 📊 VIDEO METADATA

**Judul (60 characters max):**
"Quantum Readiness Scanner - Audit Keamanan Website Indonesia"

**Deskripsi:**

```
Tool audit open-source untuk mengukur kesiapan website kampus dan BUMN Indonesia dalam menghadapi ancaman quantum computing.

🔗 GitHub Repository: [LINK]
📄 Dokumentasi Lengkap: [LINK]
📊 Live Demo Dashboard: [LINK]

Proyek ini dikembangkan sebagai bagian dari Tugas Audit Sistem Informasi 2025 dengan fokus pada keamanan siber dan post-quantum cryptography.

Fitur:
✅ Automatic scanning 100+ websites
✅ Quantum readiness scoring
✅ Interactive dashboard dengan Streamlit
✅ Export hasil ke JSON/CSV
✅ Comprehensive documentation

Tags: #QuantumComputing #Cybersecurity #Indonesia #OpenSource #AuditTI #PostQuantumCryptography #TLS #SSL #InformationSecurity

Developed by: [Nama Mahasiswa]
Institution: [Universitas]
Year: 2025
```

**Tags:**
quantum computing, cybersecurity, information security, audit, Indonesia, TLS, SSL, encryption, post-quantum cryptography, BUMN, kampus, security tools, open source, Python, Streamlit, dashboard

---

## 🎥 ALTERNATIVE: NARRATED SLIDESHOW

Jika screen recording terasa sulit, alternatif lain adalah:

**Format:** Narrated slideshow dengan insert screen capture

**Struktur:**

1. Intro slide (30s)
2. Problem statement slides (45s)
3. Screen capture: Running scanner (45s)
4. Screen capture: Dashboard demo (60s)
5. Result slides (45s)
6. Closing slide (30s)

**Tools:**

- PowerPoint dengan screen recording feature
- Canva dengan video presentation
- Prezi dengan narration

Lebih mudah diproduksi tapi kurang engaging. Gunakan ini jika:

- Waktu terbatas
- Technical issues dengan screen recording
- Tidak confident dengan live demo

---

**GOOD LUCK! 🚀**

Ingat: Video ini bukan hanya untuk nilai, tapi juga portfolio Anda untuk masa depan!
