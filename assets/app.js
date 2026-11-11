/**
 * STARCOMP PC CONFIGURATOR & DOCUMENT GENERATOR
 * Alpine.js State Management & Business Logic
 */

document.addEventListener('alpine:init', () => {
  Alpine.data('pcConfigurator', () => ({
    // Mode Dokumen: 'penawaran' (SPH) atau 'invoice' (Faktur)
    docType: 'penawaran',
    viewMode: 'split',
    showClientDetails: false, // 'split' (Editor + Preview), 'editor' (Form saja), 'preview' (Dokumen A4 saja)

    // Pengaturan & Identitas Dokumen
    docNumber: '',
    docDate: new Date().toISOString().split('T')[0],
    validityDays: 14,
    dueDate: new Date(Date.now() + 7 * 86400000).toISOString().split('T')[0],
    salesName: 'AJI',
    perihal: 'Penawaran Pengadaan Perangkat Komputer (PC Rakitan)',

    // Data Pelanggan / Institusi
    client: {
      name: 'PT. SELALU SIAP SOLUSI',
      institution: '',
      phone: '',
      address: 'Yogyakarta',
      notes: ''
    },

    // Opsi Keuangan & Cetak
    showItemPrices: true, // true: Tampilkan rincian harga, false: Sistem Paket (Lump Sum)
    paymentStatus: 'LUNAS', // 'LUNAS', 'DP', 'BELUM LUNAS'
    dpAmount: 0,
    discountAmount: 0,
    taxRate: 0, // 0%, 11%, 12%
    bankAccounts: [
      { bank: 'BCA', no: '037-9200-208', name: 'CV.STAR MEDIA COMPUTAMA' },
      { bank: 'Mandiri', no: '137-00-1928-3344', name: 'STARCOMP COMPUTER' }
    ],

    // Daftar Komponen
    items: [],

    // State Autocomplete & Pencarian
    catalog: window.STARCOMP_CATALOG || [],
    presets: window.STARCOMP_PRESETS || [],
    activeSearchRow: null,
    searchKeyword: '',
    isExportingPdf: false,
    toastMessage: '',
    showToast: false,

    // Kategori Pilihan
    categoryOptions: [
      'Processor',
      'Motherboard',
      'RAM / Memory',
      'VGA / Graphic Card',
      'Storage SSD',
      'Storage HDD',
      'Power Supply (PSU)',
      'Casing PC',
      'CPU Cooler / Fan',
      'Liquid Cooler AIO',
      'Monitor / Display',
      'Keyboard & Mouse',
      'Jasa & Layanan',
      'Aksesoris & Lainnya'
    ],

    init() {
      this.generateDocNumber();
      const urlParams = new URLSearchParams(window.location.search);
      if (urlParams.get("type") === "invoice") {
        this.switchDocType("invoice");
      } else if (urlParams.get("type") === "penawaran") {
        this.switchDocType("penawaran");
      }
      if (urlParams.get("preset")) {
        this.loadPreset(urlParams.get("preset"), false);
      }
      // Load preset default (Esport Gaming Champion) if empty
      if (this.presets && this.presets.length > 2) {
        this.loadPreset(this.presets[2].id, false);
      } else {
        this.addEmptyRow();
      }

      // Check saved draft in localStorage
      const saved = localStorage.getItem('starcomp_pc_draft');
      if (saved) {
        // notify user or keep ready
      }
    },

    generateDocNumber() {
      const now = new Date();
      const yr = now.getFullYear();
      const mo = String(now.getMonth() + 1).padStart(2, '0');
      const dt = String(now.getDate()).padStart(2, '0');
      const rand = String(Math.floor(Math.random() * 900) + 100).padStart(3, '0');
      if (this.docType === 'invoice') {
        this.docNumber = `SIR${dt}${mo}${yr}/${rand}`;
      } else {
        this.docNumber = `SPH${dt}${mo}${yr}/${rand}`;
      }
    },

    getUppercaseDate(dateStr) {
      const str = dateStr || this.docDate;
      if (!str) return '-';
      const months = ['JANUARI', 'FEBRUARI', 'MARET', 'APRIL', 'MEI', 'JUNI', 'JULI', 'AGUSTUS', 'SEPTEMBER', 'OKTOBER', 'NOVEMBER', 'DESEMBER'];
      const parts = str.split('-');
      const d = parseInt(parts[2], 10);
      const m = months[parseInt(parts[1], 10) - 1] || 'JANUARI';
      const y = parts[0];
      return `${d} ${m} ${y}`;
    },

    getGreetingSubtitle() {
      if (this.docType === 'penawaran') {
        return "I'm your Offering Letter";
      } else {
        return "I'm your Invoice";
      }
    },

    formatRupiahNoSpace(num) {
      if (isNaN(num) || num === null || num === undefined) return 'Rp0';
      return 'Rp' + Number(num).toLocaleString('id-ID');
    },

    switchDocType(type) {
      this.docType = type;
      this.generateDocNumber();
      if (type === 'invoice' && this.perihal.includes('Penawaran')) {
        this.perihal = 'Faktur Pembelian Perangkat Komputer Rakitan';
      } else if (type === 'penawaran' && this.perihal.includes('Faktur')) {
        this.perihal = 'Penawaran Pengadaan Perangkat Komputer (PC Rakitan)';
      }
    },

    addEmptyRow(category = 'Processor') {
      this.items.push({
        id: 'row-' + Date.now() + '-' + Math.random().toString(36).substr(2, 4),
        category: category,
        name: '',
        warranty: '1 Tahun Garansi Resmi',
        qtt: 1,
        price: 0
      });
    },

    removeItem(index) {
      if (this.items.length > 1) {
        this.items.splice(index, 1);
      } else {
        this.items[0] = {
          id: 'row-' + Date.now(),
          category: 'Processor',
          name: '',
          warranty: '1 Tahun Garansi Resmi',
          qtt: 1,
          price: 0
        };
      }
    },

    moveItem(index, direction) {
      const targetIndex = index + direction;
      if (targetIndex >= 0 && targetIndex < this.items.length) {
        const temp = this.items[index];
        this.items[index] = this.items[targetIndex];
        this.items[targetIndex] = temp;
      }
    },

    loadPreset(presetId, notify = true) {
      const p = this.presets.find(x => x.id === presetId);
      if (!p) return;

      this.items = p.items.map(it => ({
        id: 'row-' + Date.now() + '-' + Math.random().toString(36).substr(2, 4),
        category: it.category || 'Komponen',
        name: it.name,
        warranty: it.category === 'Jasa & Layanan' ? 'Garansi Service 1 Bulan' : '1 - 3 Tahun Garansi Distributor',
        qtt: it.qtt || 1,
        price: it.price || 0
      }));

      if (notify) {
        this.triggerToast(`Berhasil memuat preset: ${p.name}`);
      }
    },

    clearAll() {
      if (confirm('Apakah Anda yakin ingin mengosongkan semua daftar komponen?')) {
        this.items = [];
        this.addEmptyRow();
        this.discountAmount = 0;
        this.dpAmount = 0;
        this.triggerToast('Daftar spesifikasi telah dikosongkan.');
      }
    },

    // Search Autocomplete Helpers
    onSearchFocus(index) {
      this.activeSearchRow = index;
      this.searchKeyword = this.items[index].name;
    },

    getFilteredSuggestions(category, keyword) {
      if (!keyword || keyword.trim().length < 2) {
        if (category) {
          const catMatches = this.catalog.filter(x => x.category === category);
          if (catMatches.length > 0) return catMatches.slice(0, 8);
        }
        return this.catalog.slice(0, 8);
      }
      const q = keyword.toLowerCase().trim();
      return this.catalog
        .filter(x => x.name.toLowerCase().includes(q))
        .slice(0, 12);
    },

    selectSuggestion(index, item) {
      this.items[index].name = item.name;
      this.items[index].category = item.category;
      this.items[index].price = item.price;
      this.items[index].warranty = item.category === 'Jasa & Layanan' ? 'Garansi Service' : '1 - 3 Tahun Garansi';
      this.activeSearchRow = null;
      this.$nextTick(() => {
        const priceInput = document.querySelector(`input[data-field="price"][data-index="${index}"]`);
        if (priceInput) {
          priceInput.focus();
          priceInput.select();
        }
      });
    },

    closeSuggestions() {
      setTimeout(() => {
        this.activeSearchRow = null;
      }, 250);
    },

    getNextCategory(currentCat) {
      const cats = this.categoryOptions;
      const idx = cats.indexOf(currentCat);
      if (idx !== -1 && idx + 1 < cats.length) {
        return cats[idx + 1];
      }
      return 'Aksesoris & Lainnya';
    },

    focusNextField(index, field) {
      if (field === 'name') {
        this.$nextTick(() => {
          const el = document.querySelector(`input[data-field="qtt"][data-index="${index}"]`);
          if (el) {
            el.focus();
            el.select();
          }
        });
      } else if (field === 'qtt') {
        this.$nextTick(() => {
          const el = document.querySelector(`input[data-field="price"][data-index="${index}"]`);
          if (el) {
            el.focus();
            el.select();
          }
        });
      } else if (field === 'price') {
        if (index + 1 < this.items.length) {
          this.$nextTick(() => {
            const el = document.querySelector(`input[data-field="name"][data-index="${index + 1}"]`);
            if (el) {
              el.focus();
              el.select();
            }
          });
        } else {
          const currentCat = this.items[index]?.category || 'Processor';
          const nextCat = this.getNextCategory(currentCat);
          this.addEmptyRow(nextCat);
          this.$nextTick(() => {
            const newIndex = this.items.length - 1;
            const el = document.querySelector(`input[data-field="name"][data-index="${newIndex}"]`);
            if (el) {
              el.focus();
            }
          });
        }
      }
    },

    focusVertical(index, field, direction) {
      const targetIndex = index + direction;
      if (targetIndex >= 0 && targetIndex < this.items.length) {
        this.$nextTick(() => {
          const el = document.querySelector(`input[data-field="${field}"][data-index="${targetIndex}"]`);
          if (el) {
            el.focus();
            el.select();
          }
        });
      }
    },

    // Financial Calculations
    subtotal() {
      return this.items.reduce((acc, it) => {
        const q = parseFloat(it.qtt) || 0;
        const p = parseFloat(it.price) || 0;
        return acc + (q * p);
      }, 0);
    },

    taxAmount() {
      if (!this.taxRate || this.taxRate <= 0) return 0;
      const base = Math.max(0, this.subtotal() - (parseFloat(this.discountAmount) || 0));
      return Math.round(base * (this.taxRate / 100));
    },

    grandTotal() {
      const sub = this.subtotal();
      const disc = parseFloat(this.discountAmount) || 0;
      const tax = this.taxAmount();
      return Math.max(0, sub - disc + tax);
    },

    remainingPayment() {
      const gTot = this.grandTotal();
      const dp = parseFloat(this.dpAmount) || 0;
      return Math.max(0, gTot - dp);
    },

    totalQuantity() {
      return this.items.reduce((acc, it) => acc + (parseInt(it.qtt) || 0), 0);
    },

    formatRupiah(num) {
      if (isNaN(num) || num === null || num === undefined) return 'Rp 0';
      return 'Rp ' + Number(num).toLocaleString('id-ID');
    },

    getValidUntilFormatted() {
      const date = new Date(this.docDate);
      date.setDate(date.getDate() + parseInt(this.validityDays || 14));
      return date.toLocaleDateString('id-ID', { day: 'numeric', month: 'long', year: 'numeric' });
    },

    getDocDateFormatted() {
      if (!this.docDate) return '-';
      const parts = this.docDate.split('-');
      const d = new Date(parts[0], parts[1] - 1, parts[2]);
      return d.toLocaleDateString('id-ID', { day: 'numeric', month: 'long', year: 'numeric' });
    },

    getDueDateFormatted() {
      if (!this.dueDate) return '-';
      const parts = this.dueDate.split('-');
      const d = new Date(parts[0], parts[1] - 1, parts[2]);
      return d.toLocaleDateString('id-ID', { day: 'numeric', month: 'long', year: 'numeric' });
    },

    // Save & Load Draft
    saveDraft() {
      const draft = {
        docType: this.docType,
        docNumber: this.docNumber,
        docDate: this.docDate,
        validityDays: this.validityDays,
        dueDate: this.dueDate,
        salesName: this.salesName,
        perihal: this.perihal,
        client: this.client,
        showItemPrices: this.showItemPrices,
        paymentStatus: this.paymentStatus,
        dpAmount: this.dpAmount,
        discountAmount: this.discountAmount,
        taxRate: this.taxRate,
        items: this.items
      };
      localStorage.setItem('starcomp_pc_draft', JSON.stringify(draft));
      this.triggerToast('Draf penawaran/invoice berhasil disimpan!');
    },

    loadSavedDraft() {
      const raw = localStorage.getItem('starcomp_pc_draft');
      if (!raw) {
        alert('Belum ada draf tersimpan.');
        return;
      }
      try {
        const d = JSON.parse(raw);
        this.docType = d.docType || 'penawaran';
        this.docNumber = d.docNumber || this.docNumber;
        this.docDate = d.docDate || this.docDate;
        this.validityDays = d.validityDays || 14;
        this.dueDate = d.dueDate || this.dueDate;
        this.salesName = d.salesName || this.salesName;
        this.perihal = d.perihal || this.perihal;
        this.client = d.client || this.client;
        this.showItemPrices = d.showItemPrices !== undefined ? d.showItemPrices : true;
        this.paymentStatus = d.paymentStatus || 'LUNAS';
        this.dpAmount = d.dpAmount || 0;
        this.discountAmount = d.discountAmount || 0;
        this.taxRate = d.taxRate || 0;
        this.items = d.items || [];
        this.triggerToast('Draf berhasil dipulihkan!');
      } catch (e) {
        alert('Gagal membaca draf tersimpan.');
      }
    },

    // Copy formatted WhatsApp Text for marketing chat
    copyWhatsApp() {
      let text = `*STARCOMP KOMPUTER & IT SOLUTION*\n`;
      text += `━━━━━━━━━━━━━━━━━━━━━\n`;
      text += `*${this.docType === 'penawaran' ? 'PENAWARAN SPESIFIKASI PC RAKITAN' : 'INVOICE PEMBELIAN PC RAKITAN'}*\n`;
      text += `No: ${this.docNumber}\n`;
      text += `Kepada: ${this.client.name}${this.client.institution ? ' (' + this.client.institution + ')' : ''}\n`;
      text += `Tanggal: ${this.getDocDateFormatted()}\n`;
      text += `━━━━━━━━━━━━━━━━━━━━━\n\n`;
      text += `*DETAIL SPESIFIKASI :*\n`;

      this.items.forEach((it, idx) => {
        const catPrefix = it.category ? `*[${it.category}]* ` : '';
        text += `${idx + 1}. ${catPrefix}${it.name}`;
        if (this.showItemPrices) {
          text += ` (${it.qtt}x @ ${this.formatRupiah(it.price)}) = *${this.formatRupiah(it.qtt * it.price)}*`;
        }
        text += `\n`;
      });

      text += `\n━━━━━━━━━━━━━━━━━━━━━\n`;
      text += `*SUBTOTAL :* ${this.formatRupiah(this.subtotal())}\n`;
      if (this.discountAmount > 0) {
        text += `*DISKON :* -${this.formatRupiah(this.discountAmount)}\n`;
      }
      if (this.taxAmount() > 0) {
        text += `*PPN (${this.taxRate}%) :* ${this.formatRupiah(this.taxAmount())}\n`;
      }
      text += `*TOTAL KESELURUHAN : ${this.formatRupiah(this.grandTotal())}*\n`;

      if (this.docType === 'invoice') {
        text += `Status: *${this.paymentStatus}*\n`;
        if (this.paymentStatus === 'DP') {
          text += `Uang Muka (DP): ${this.formatRupiah(this.dpAmount)}\n`;
          text += `Sisa Tagihan: *${this.formatRupiah(this.remainingPayment())}*\n`;
        }
      }

      text += `━━━━━━━━━━━━━━━━━━━━━\n`;
      text += `_Garansi unit resmi distributor, rakitan rapi, cable management, siap pakai._\n`;
      text += `Hotline / WA: 0811-2747-434 | Starcomp Rajawali Yogyakarta\n`;

      navigator.clipboard.writeText(text).then(() => {
        this.triggerToast('Format WhatsApp berhasil disalin ke clipboard!');
      }).catch(() => {
        alert('Gagal menyalin otomatis. Salin teks manual.');
      });
    },

    // Print & PDF Export
    printDocument() {
      window.print();
    },

    exportPdf() {
      const element = document.getElementById('printableDocument');
      if (!element) {
        alert('Elemen dokumen tidak ditemukan.');
        return;
      }

      this.isExportingPdf = true;
      this.triggerToast('Sedang membuat file PDF berkualitas tinggi...');

      const filename = `${this.docType === 'penawaran' ? 'Penawaran' : 'Invoice'}-Starcomp-${(this.client.name || 'Pelanggan').replace(/[^a-zA-Z0-9]/g, '_')}-${this.docNumber.replace(/[\/]/g, '-')}.pdf`;

      const opt = {
        margin: [8, 8, 8, 8],
        filename: filename,
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: {
          scale: 2,
          useCORS: true,
          letterRendering: true,
          logging: false
        },
        jsPDF: {
          unit: 'mm',
          format: 'a4',
          orientation: 'portrait'
        },
        pagebreak: { mode: ['avoid-all', 'css', 'legacy'] }
      };

      if (window.html2pdf) {
        window.html2pdf().set(opt).from(element).save().then(() => {
          this.isExportingPdf = false;
          this.triggerToast('PDF berhasil diunduh!');
        }).catch(err => {
          console.error('PDF export error:', err);
          this.isExportingPdf = false;
          // Fallback to native print
          window.print();
        });
      } else {
        this.isExportingPdf = false;
        window.print();
      }
    },

    triggerToast(msg) {
      this.toastMessage = msg;
      this.showToast = true;
      setTimeout(() => {
        this.showToast = false;
      }, 3500);
    }
  }));
});
