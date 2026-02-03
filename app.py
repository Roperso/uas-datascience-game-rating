import streamlit as st
import pickle
import pandas as pd

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Prediksi Critic Score Game",
    page_icon="🎮",
    layout="wide"
)

# =========================
# CSS (DARK MODE FRIENDLY)
# =========================
st.markdown("""
<style>
h1 { text-align: center; }
.section-box {
    background-color: #1e1e1e;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid #333;
}
.big-number {
    font-size: 48px;
    font-weight: bold;
    margin-top: -10px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# LOAD MODEL
# =========================
model = pickle.load(open("model.pkl", "rb"))

# =========================
# LOAD DATASET (DROPDOWN & VISUAL)
# =========================
df = pd.read_csv("data/Video_Games_Sales_as_at_22_Dec_2016.csv")
score_df = df.dropna(subset=["Critic_Score"])

platform_list = sorted(df["Platform"].dropna().unique())
genre_list = sorted(df["Genre"].dropna().unique())
publisher_list = sorted(df["Publisher"].dropna().unique())
developer_list = sorted(df["Developer"].dropna().unique())
rating_list = sorted(df["Rating"].dropna().unique())

# =========================
# HEADER
# =========================
st.title("🎮 Prediksi Critic Score Game")
st.write(
    "Aplikasi ini memprediksi **Critic Score** game menggunakan "
    "**Random Forest Regressor** berdasarkan pola historis data game."
)

st.divider()

# =========================
# LAYOUT INPUT & OUTPUT (KUNCI)
# =========================
col_input, col_output = st.columns([1.2, 1])

# ---------- INPUT (KIRI) ----------
with col_input:
    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    st.subheader("📝 Input Data Game")

    platform = st.selectbox("Platform", platform_list)
    genre = st.selectbox("Genre", genre_list)
    publisher = st.selectbox("Publisher", publisher_list)
    developer = st.selectbox("Developer", developer_list)
    year = st.number_input("Year of Release", 1980, 2030, 2020)
    rating = st.selectbox("Rating (ESRB)", rating_list)

    predict_btn = st.button("🔮 Prediksi Critic Score")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- OUTPUT (KANAN) ----------
with col_output:
    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    st.subheader("🎯 Hasil Prediksi")
    info_placeholder = st.info(
        "Silakan isi data game dan klik **Prediksi Critic Score**."
    )
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# PREDIKSI (SEMUA OUTPUT DI col_output)
# =========================
if predict_btn:
    input_df = pd.DataFrame([{
        "Platform": platform,
        "Genre": genre,
        "Publisher": publisher,
        "Developer": developer,
        "Year_of_Release": year,
        "Rating": rating
    }])

    prediction = model.predict(input_df)[0]
    dataset_avg = score_df["Critic_Score"].mean()

    with col_output:
        # hapus info awal
        info_placeholder.empty()

        # alert hijau
        st.success(f"🎯 **Prediksi Critic Score: {prediction:.2f} / 100**")

        # angka besar (2 kolom)
        colA, colB = st.columns(2)

        with colA:
            st.markdown("**Prediksi Model**")
            st.markdown(
                f"<div class='big-number'>{prediction:.2f}</div>",
                unsafe_allow_html=True
            )

        with colB:
            st.markdown("**Rata-rata Dataset**")
            st.markdown(
                f"<div class='big-number'>{dataset_avg:.2f}</div>",
                unsafe_allow_html=True
            )

st.divider()

# =========================
# VISUALISASI DATA
# =========================
st.subheader("📊 Analisis & Visualisasi Data")

tab1, tab2, tab3 = st.tabs([
    "Distribusi Skor",
    "Skor per Genre",
    "Tren Tahunan"
])

with tab1:
    score_counts = score_df["Critic_Score"].value_counts().sort_index()
    st.bar_chart(score_counts)

with tab2:
    avg_genre = (
        score_df.groupby("Genre")["Critic_Score"]
        .mean()
        .sort_values(ascending=False)
    )
    st.bar_chart(avg_genre)

with tab3:
    yearly_score = (
        score_df.dropna(subset=["Year_of_Release"])
        .groupby("Year_of_Release")["Critic_Score"]
        .mean()
    )
    st.line_chart(yearly_score)

st.divider()

# =========================
# FOOTER
# =========================
st.caption(
    "Catatan: Prediksi bersifat estimasi berbasis pola historis data dan "
    "tidak merepresentasikan penilaian subjektif individu."
)
