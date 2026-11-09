# 🖥️ STARCOMP PC Configurator & Document Generator
### Web App Resmi Tim Marketing & Sales Starcomp (Surat Penawaran Harga & Faktur / Invoice)

Sistem aplikasi web modern, ringan, dan mandiri (*standalone*) yang dirancang khusus untuk mempermudah tim marketing Starcomp dalam menyusun spesifikasi rakitan PC (*PC Building / Spec Configurator*), menghitung harga secara akurat, serta menghasilkan dokumen resmi berformat **Surat Penawaran Harga (SPH)** dan **Faktur / Invoice Penjualan** berstandar **KOP STARCOMP** yang siap cetak dan ekspor ke PDF.

---

## 🚀 Fitur Utama

### 1. 📋 Dual Export Mode: Penawaran & Invoice (Format 100% Persis Dokumen Resmi Starcomp)
Format dokumen untuk kedua mode (Penawaran & Invoice) dibuat **100% identik dan presisi** mengikuti standar format berkas cetak resmi Starcomp (`/home/bengkel/Downloads/INVOICE.pdf`):
- **KOP Banner Asli Oranye Starcomp**: Logo origami, daftar pill cabang `(YK-CC)`, `(YK-RW)`, `(YK-JK)`, `(SL)`, `(SMG)`, `(PWK)`, `(INA)`, dan alamat web `www.starcompjogja.com`.
- **Subheader Kiri**: Sapaan ikonik *"Hello, I'm your quotation"* (untuk Penawaran) atau *"Hello, I'm your receipt"* (untuk Invoice), sub-teks customer care, dan badge rekening resmi `BCA 037-9200-208 a/n CV. STAR MEDIA`.
- **Kotak Metadata Kanan (Rounded Box)**: Nomor Dokumen (`Penawaran: SPH...` / `Nota: SIR...`), Tanggal formal (kapital, e.g. `8 NOVEMBER 2026`), Petugas (`Marketing: AJI` / `Kasir: AJI`), Nama Pelanggan, dan Alamat.
- **Tabel Transaksi Presisi**: Border hitam tegas dengan kolom `No.`, `Description` (nama part + garansi), `QTY`, `Unit Cost`, dan `TOTAL`, diakhiri baris `TOTAL` (Grand Total).
- **Bagian Bawah Kiri**: 6 Butir Klausul Resmi `KETERANGAN :` (syarat pembayaran, garansi, faktur pajak, dan disclaimer software) serta alamat lengkap `HEADQUARTER` Condongcatur Sleman.
- **Bagian Bawah Kanan**: Cap resmi Starcomp, teks `Hormat kami,`, nama penandatangan resmi `STARCOMP`, dan badge slogan titik-titik `Unbeatable Prices`.

### 2. ⚡ 6 Template Paket Best Seller (Quick Presets)
Tim marketing dapat memuat racikan spesifikasi populer hanya dengan 1 klik:
1. **Paket Starcomp Office & Kasir Hemat (± Rp 3,9 Juta)** — APU Ryzen 3 3200G, RAM 8GB, SSD 256GB, Monitor 21.5".
2. **Paket Lab Sekolah & Bisnis Intel (± Rp 5,1 Juta)** — Core i3 12100 Gen-12, RAM 8GB, NVMe 256GB, Monitor 22".
3. **Paket Starcomp Esport Gaming Champion (± Rp 8,9 Juta)** — Ryzen 5 5600, RTX 3050 6GB, 16GB DDR4 3600 RGB, NVMe 512GB.
4. **Paket Gaming AAA & Content Creator Pro (± Rp 13,8 Juta)** — Core i5 12400F, RTX 4060 8GB, 32GB RGB, NVMe Gen4 1TB, Liquid Cooler 240mm.
5. **Paket Workstation Arsitektur & CAD (± Rp 51 Juta)** — Core i9 14900KF, Quadro RTX A4000 16GB ECC, 64GB DDR5, SSD 2TB, AIO 360mm LCD.
6. **Paket Starcomp God-Tier ROG Enthusiast (± Rp 136,6 Juta)** — Ryzen 9 9950X3D, ASUS ROG Astral RTX 5090 32GB, Crosshair X870E, Thor 1200W, Case Hyperion GR701.

### 3. 🔍 Autocomplete 800+ Komponen Riil Starcomp
- Database komponen diekstrak langsung dari spreadsheet operasional Starcomp (`RAKITAN`).
- Saat mengetik nama hardware (misal: "5600", "RTX", "3050", "B450", "MSI"), muncul daftar rekomendasi komponen beserta harga satuannya secara instan.
- Harga dan garansi otomatis terisi, namun tetap dapat diedit secara fleksibel oleh staf marketing.

### 4. 📦 Opsi "Sistem Paket" (Hide Individual Price)
- Fleksibilitas menyembunyikan rincian harga per komponen dan hanya menampilkan **Total Paket** di bagian bawah.
- Sangat efektif untuk pengadaan kantor, sekolah, atau tender instansi yang mewajibkan penawaran sistem paket terpadu.

### 5. 💬 Quick Copy format WhatsApp
- Satu tombol untuk menyalin seluruh rincian spesifikasi dan kalkulasi harga ke format teks rapi dengan formatting tebal (*bold*) dan garis pembatas, siap dikirimkan ke chat WhatsApp calon pembeli.

### 6. 🖨️ Cetak Presisi Kertas A4 & Ekspor PDF
- Desain layout kertas A4 formal (210mm × 297mm) yang rapi dan konsisten.
- Ekspor PDF langsung via tombol **Export PDF** (menggunakan engine client-side `html2pdf.js` beresolusi tinggi).
- Opsi cetak langsung (**Print / Ctrl+P**) dengan styling `@media print` terisolasi yang otomatis menyembunyikan panel form navigasi.

---

## 📂 Struktur Direktori Proyek

```
starcomp-pc-configurator/
├── index.html                   # Antarmuka Single Page Application (Responsive UI)
├── server.py                    # Web server lokal ringan (Python HTTP server)
├── README.md                    # Dokumentasi penggunaan dan panduan teknis
├── assets/
│   ├── style.css                # Styling kustom A4, kop-border, stempel cap & @media print
│   ├── app.js                   # State management & controller logika (Alpine.js)
│   ├── data.js                  # Data bundle offline (katalog komponen & paket preset)
│   └── vendor/
│       ├── tailwind.js          # Tailwind CSS Play CDN (offline mirror)
│       ├── alpine.min.js        # Alpine.js reactive engine
│       └── html2pdf.bundle.min.js # PDF generator client-side
└── data/
    ├── catalog.json             # 803 Master komponen terkurasi dari spreadsheet
    └── presets.json             # 6 Paket rekomendasi konfigurasi PC
```

---

## 🏃 Cara Menjalankan Aplikasi

### Metode 1: Menggunakan Local Web Server (Direkomendasikan)
Jalankan perintah berikut di terminal:
```bash
python3 /home/bengkel/AI/starcomp-pc-configurator/server.py 3000
```
Buka browser dan akses:
- **Halaman Utama**: `http://localhost:3000/`
- **Langsung Mode Penawaran**: `http://localhost:3000/?type=penawaran`
- **Langsung Mode Invoice**: `http://localhost:3000/?type=invoice`

### Metode 2: Langsung Buka File HTML (Tanpa Server)
File `index.html` dirancang **100% mandiri dan bebas CORS**:
Cukup klik ganda atau buka langsung file `index.html` di Google Chrome, Brave, Edge, atau Firefox.

---

## 📑 Berkas Bukti & Sample Output
- Dokumen Penawaran Contoh: [`sample_output_penawaran.pdf`](./sample_output_penawaran.pdf)
- Dokumen Faktur/Invoice Contoh: [`sample_output_invoice.pdf`](./sample_output_invoice.pdf)
- Tangkapan Layar Tampilan: [`preview.png`](./preview.png) & [`preview_invoice.png`](./preview_invoice.png)
