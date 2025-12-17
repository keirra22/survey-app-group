import streamlit as st
import pandas as pd
from scipy import stats

st.title("Survey Data Analysis")

st.write("Upload your survey CSV file below.")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Descriptive Statistics")
    st.write(df.describe())

    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if len(numeric_cols) >= 2:
        st.subheader("Correlation Analysis")

        x_var = st.selectbox("Select Variable X", numeric_cols)
        y_var = st.selectbox("Select Variable Y", numeric_cols)

        if st.button("Calculate Pearson Correlation"):
            r, p = stats.pearsonr(df[x_var], df[y_var])

            st.write(f"Correlation coefficient (r): {r:.3f}")
            st.write(f"p-value: {p:.4f}")
