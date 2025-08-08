import pandas as pd

def hitung_nilai_akhir(df, bobot_tugas, bobot_uts, bobot_uas):
    bt, bu, ba = bobot_tugas/100, bobot_uts/100, bobot_uas/100
    df["Nilai Akhir"] = (df["Tugas"]*bt + df["UTS"]*bu + df["UAS"]*ba).round(2)
    df["Status"] = df["Nilai Akhir"].apply(lambda x: "Lulus" if x >= 70 else "Tidak Lulus")
    return df
