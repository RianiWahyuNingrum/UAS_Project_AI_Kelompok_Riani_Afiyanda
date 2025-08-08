import streamlit as st
import pandas as pd
from ga_scheduler import hitung_nilai_akhir

st.title("📊 Kalkulator Nilai Akhir Mahasiswa Semester 4")
uploaded_file = st.sidebar.file_uploader("Upload file CSV", type=["csv"])

if uploaded_file:
    with open("nilai.csv", "wb") as f:
        f.write(uploaded_file.read())
    st.success("Dataset berhasil diupload!")

    df = pd.read_csv("nilai.csv")
    st.subheader("Data Awal")
    st.dataframe(df)

    bobot_tugas = st.slider("Bobot Tugas (%)", 0, 100, 20)
    bobot_uts = st.slider("Bobot UTS (%)", 0, 100, 30)
    bobot_uas = st.slider("Bobot UAS (%)", 0, 100, 50)

    total_bobot = bobot_tugas + bobot_uts + bobot_uas
    if total_bobot != 100:
        st.error("Total bobot harus 100%")
    else:
        if st.button("Hitung Nilai Akhir"):
            hasil_df = hitung_nilai_akhir(df, bobot_tugas, bobot_uts, bobot_uas)
            st.success("Perhitungan selesai!")
            st.subheader("Hasil Nilai Akhir")
            st.dataframe(hasil_df)

            csv = hasil_df.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download Hasil", csv, "hasil_nilai.csv", "text/csv")
