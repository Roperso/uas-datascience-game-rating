# 🎮 Prediksi Critic Score Game  
**UAS Data Science – Teknik Informatika Semester 5**

## 📌 Deskripsi Proyek
Proyek ini merupakan aplikasi **Data Science berbasis Machine Learning** yang bertujuan untuk **memprediksi Critic Score (skor penilaian kritikus)** sebuah game berdasarkan karakteristik game tersebut.  
Model dibangun menggunakan algoritma **Random Forest Regressor** dan diimplementasikan dalam bentuk aplikasi web interaktif menggunakan **Streamlit**.

Aplikasi ini tidak hanya menampilkan hasil prediksi, tetapi juga menyajikan **visualisasi data** untuk membantu interpretasi pola historis penilaian game.

---

## 🎯 Tujuan
- Menerapkan tahapan **Data Science Pipeline**
- Melakukan **preprocessing data kategorikal**
- Membangun model **regresi** menggunakan Random Forest
- Menyajikan hasil prediksi dalam bentuk aplikasi web
- Melakukan **deployment ke Streamlit Community Cloud**

---

## 📂 Dataset
- **Nama Dataset:** Video Game Sales with Ratings  
- **Sumber:** Kaggle  
- **Link:** https://www.kaggle.com/datasets/rush4ratio/video-game-sales-with-ratings  

Dataset berisi informasi game seperti:
- Platform
- Genre
- Publisher
- Developer
- Tahun rilis
- Rating ESRB
- Critic Score (target)

Baris data dengan nilai kosong (NaN) pada `Critic_Score` difilter dan hanya data lengkap yang digunakan untuk training model.

---

## 🧠 Algoritma yang Digunakan
- **Random Forest Regressor**

Alasan pemilihan:
- Mampu menangani data non-linear
- Cocok untuk data campuran (numerik & kategorikal)
- Lebih stabil dibandingkan model regresi sederhana

---

## 🔧 Fitur Input Aplikasi
- Platform
- Genre
- Publisher
- Developer
- Year of Release
- Rating (ESRB)

Semua input kategorikal diambil langsung dari dataset training untuk menjaga konsistensi kategori yang dikenali model.

---

## 📊 Output Aplikasi
- Prediksi **Critic Score (0–100)**
- Perbandingan dengan **rata-rata Critic Score dataset**
- Visualisasi:
  - Distribusi Critic Score
  - Rata-rata Critic Score per Genre
  - Tren Critic Score berdasarkan Tahun

---

## 🛠️ Teknologi yang Digunakan
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## 📁 Struktur Project
game-rating-prediction/
│
├─ app.py
├─ model.pkl
├─ modeling.ipynb
├─ requirements.txt
├─ README.md
│
└─ data/
└─ Video_Games_Sales_as_at_22_Dec_2016.csv

---

## 🚀 Deployment
Aplikasi dideploy menggunakan **Streamlit Community Cloud**.

🔗 **Link Aplikasi:**  
> *(isi dengan link Streamlit setelah deploy)*

---

## 📌 Catatan
Prediksi yang dihasilkan merupakan estimasi berdasarkan pola historis data dan tidak merepresentasikan penilaian subjektif individu.

---

## 👤 Informasi
- Mata Kuliah: Data Science  
- Program Studi: Teknik Informatika  
- Semester: 5  
- Jenis Tugas: UAS
