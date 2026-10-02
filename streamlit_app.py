import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.title('🌻Parabola graph☁️')
st.badge(" Hi we are Four Seasons")
st.subheader("📚 สมการพาราโบลา")

    st.markdown("🔵 พาราโบลาแนวตั้ง")
    st.latex(r"y = a(x-h)^2 + k")

    st.write("โดย")
    st.write("- a = ค่าความกว้างและทิศทางการเปิด")
    st.write("- h = พิกัด x ของจุดยอด")
    st.write("- k = พิกัด y ของจุดยอด")
    st.write("- จุดยอด คือ (h, k)")

    st.markdown("🟢 พาราโบลาแนวนอน")
    st.latex(r"x = a(y-k)^2 + h")

    st.write("โดย")
    st.write("- a > 0 → เปิดไปทางขวา")
    st.write("- a < 0 → เปิดไปทางซ้าย")
    st.write("- จุดยอด คือ (h, k)")
