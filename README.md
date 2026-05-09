# 📊 SADAR Finance Dashboard

> **Smart Financial Analytics Dashboard** - Analisis mendalam terhadap pola pengeluaran dan perilaku finansial pengguna dengan visualisasi data yang interaktif dan intuitif.

---

## 🎯 Tentang Project

**SADAR Finance Dashboard** adalah aplikasi analitik keuangan berbasis data yang dirancang untuk membantu pengguna memahami:

- 💰 **Pola Pengeluaran** - Identifikasi tren spending berdasarkan kategori dan waktu
- 📈 **Perilaku Finansial** - Analisis mendalam tentang kebiasaan belanja dan preferensi pembayaran
- ⚠️ **Risiko Overspending** - Deteksi waktu-waktu kritis dengan potensi pengeluaran tinggi
- 🎨 **Visualisasi Interaktif** - Eksplorasi data dengan dashboard yang responsif dan user-friendly

Dashboard ini menggunakan teknologi modern untuk memberikan insights yang actionable dan real-time.

---

## ✨ Fitur Utama

### 🏠 Overview

- **Metric Cards**: Total transaksi, pengeluaran, rata-rata spending, dan kategori dominan
- **Trend Chart**: Visualisasi tren pengeluaran bulanan dengan area chart
- **Category Distribution**: Pie chart interaktif untuk melihat distribusi spending per kategori
- **Top Merchants**: Bar chart 10 merchant paling sering digunakan

### 📊 EDA & Business Questions

Analisis mendalam dengan 6 pertanyaan bisnis utama:

1. Distribusi pengeluaran berdasarkan kategori (3 bulan terakhir)
2. Kategori dengan peningkatan pengeluaran terbesar bulan ke bulan
3. Hari paling sering melakukan transaksi
4. Rata-rata pengeluaran harian dan trendnya
5. Waktu paling berisiko mengalami lonjakan pengeluaran
6. Perbedaan rata-rata spending berdasarkan metode pembayaran

### 📈 Financial Behavior

- Perbandingan spending weekday vs weekend
- Analisis average spending per hari
- Rolling spending trend (7-hari)
- Distribusi spending level (Low/Medium/High)

### 🔍 Interactive Exploration

- **Custom Chart Builder**: Pilih sumbu X, aggregation method, dan tipe chart
- **Dynamic Filtering**: Filter berdasarkan bulan dan kategori
- **Raw Dataset View**: Lihat data mentah dengan sorting dan filtering

### 📋 Dataset Information

- Dataset summary dan statistik dasar
- Data dictionary lengkap
- Informasi project dan tools yang digunakan

---

## 🛠️ Tech Stack

| Komponen | Teknologi |
|-----------|-----------|
| **Frontend** | [Streamlit](https://streamlit.io/) |
| **Data Processing** | [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/) |
| **Visualization** | [Plotly](https://plotly.com/), Custom CSS |
| **Language** | Python 3.8+ |
| **Styling** | Poppins Font, Custom CSS3 Animations |

---

## 📋 Prasyarat

- Python 3.8 atau lebih tinggi
- pip (Python package manager)
- Dataset CSV dari Google Drive (lihat bagian instalasi)

---

## ⚙️ Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/Marsela0603/SADAR-Finance-Dashboard.git
cd SADAR-Finance-Dashboard
```

### 2. Buat Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download & Siapkan Dataset

**Download Dataset dari Google Drive:**

```txt
https://drive.google.com/file/d/1olRbrT_itRLCuzf9MnFf85i-7WwXwKpW/view?usp=drive_link
```

Langkah-langkah:

1. Buka link di atas
2. Klik tombol **Download** (ikon download di toolbar)
3. Extract file dan letakkan `main_transactions_clean.csv` di direktori utama project

---

## 🚀 Cara Menjalankan

### Menjalankan Dashboard

```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser pada:

```txt
https://sadar-finance-dashboard.streamlit.app/
```

---

## 📁 Struktur Project

```txt
sadar-dashboard/
├── dashboard.py                    # Main application
├── main_transactions_clean.csv     # Dataset
├── requirements.txt                # Dependencies
└── README.md                       # Documentation (this file)
```

---

## 👨‍💻 Author

### SADAR Finance Team

1. **(CDCC156D6X1244)** — Diah Ayu Puspasari *(Data Scientist)*
2. **(CDCC156D6X028)** — Marsela *(Data Scientist)*
3. **(CACC295D6Y0695)** — Farrel Al Faqih Ekatama *(AI Engineer)*
4. **(CACC349D6Y1657)** — Dzaky Jaisy Al-Qorney *(AI Engineer)*
5. **(CFCC882D6Y0583)** — Fhazar Raffiful Aqyla *(Full Stack Developer)*
6. **(CFCC220D6Y1309)** — Muhammad Habib Rafi *(Full Stack Developer)*

---

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Python Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python Best Practices](https://pep8.org/)

---

## 📝 Additional Information

- **Last Updated**: May 9, 2024
- **Version**: 1.0.0