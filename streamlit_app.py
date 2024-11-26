import streamlit as st
import math
st.title("Menghitung volume :red[Volume Tabung] :rocket:")

r = st.number_input("Masukan Jari-Jari (cm) ",0)
t = st.number_input("Masukan tinggi (cm) ",0)

if st.button("Hitung Volume", type="primary"):
  v = math.pi*(r**2)*t
  st.success(f'volume tabung adalah (v:.2f)')
