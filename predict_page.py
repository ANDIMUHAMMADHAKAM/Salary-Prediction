import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Memprediksi Gaji Software Developer per Tahun")

    st.write("""### Silahkan isi data keperluan berikut""")

    Negara = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    Pendidikan = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    Daerah = st.selectbox("Negara", Negara)
    Pendidikan = st.selectbox("Tingkat Pendidikan", Pendidikan)

    expericence = st.slider("Tahun Pengalaman", 0, 50, 3)
    ok = st.button("Menghitung Gaji")
    if ok:
        X = np.array([[Daerah, Pendidikan, expericence ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"Estimasi gajimu adalah ${salary[0]:.2f} per Tahun")