import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.title('🌻 Parabola Graph ☁️')
st.caption("กลุ่ม: Four Seasons (หมายเลข 5)")
st.sidebar.markdown("👥 สมาชิกในกลุ่ม")
st.sidebar.text("1. นางสาวกานต์ทิดา พรมด้าว\n2. นางสาวประภัสสร คำผง\n3. นางสาวรวิยา สืบสิมมา\n4. นางสาวนิศานาถ เดชคำภู")
st.sidebar.divider()

st.sidebar.subheader("⚙️ กำหนดค่าตัวแปร")
parabola_type = st.sidebar.selectbox("เลือกรูปแบบสมการ", [
    "แนวตั้ง: y = a(x - h)² + k", 
    "แนวนอน: x = a(y - k)² + h"])

a = st.sidebar.number_input("ค่า a (ความกว้างและทิศทาง)", value=1.0, step=0.5)
if a == 0: 
    a = 0.01  # ป้องกันกรณี a เป็น 0

h = st.sidebar.number_input("ค่า h (พิกัด x ของจุดยอด)", value=0.0, step=1.0)
k = st.sidebar.number_input("ค่า k (พิกัด y ของจุดยอด)", value=0.0, step=1.0)

tab1, tab2 = st.tabs(["📊 กราฟ & วิเคราะห์พฤติกรรม", "📚 สูตรและทฤษฎี"])

with tab1:
    col1, col2 = st.columns([2, 1])

    fig, ax = plt.subplots(figsize=(6, 5))
    
    if "แนวตั้ง" in parabola_type:
        x = np.linspace(h - 10, h + 10, 400)
        y = a * (x - h)**2 + k
        ax.plot(x, y, color="#2b5c8f", lw=2, label=f"y = {a}(x - {h})² + {k}")
        
        # วิเคราะห์พฤติกรรม
        if a > 0:
            direction = "กราฟหงาย (เปิดบน)"
            extrema_type = f"จุดต่ำสุดสัมพัทธ์ อยู่ที่ ({h}, {k})"
            extrema_val = f"ค่าต่ำสุด คือ y = {k}"
        else:
            direction = "กราฟคว่ำ (เปิดล่าง)"
            extrema_type = f"จุดสูงสุดสัมพัทธ์ อยู่ที่ ({h}, {k})"
            extrema_val = f"ค่าสูงสุด คือ y = {k}"
            
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        
    else:
        y = np.linspace(k - 10, k + 10, 400)
        x = a * (y - k)**2 + h
        ax.plot(x, y, color="#2b5c8f", lw=2, label=f"x = {a}(y - {k})² + {h}")
        
        if a > 0:
            direction = "กราฟเปิดทางขวา"
            extrema_type = "ไม่มีจุดสูงสุด/ต่ำสุด (เปิดแนวนอน)"
            extrema_val = f"จุดวกกลับซ้ายสุด อยู่ที่ x = {h}"
        else:
            direction = "กราฟเปิดทางซ้าย"
            extrema_type = "ไม่มีจุดสูงสุด/ต่ำสุด (เปิดแนวนอน)"
            extrema_val = f"จุดวกกลับขวาสุด อยู่ที่ x = {h}"
            
        ax.set_xlabel("x")
        ax.set_ylabel("y")
      
    ax.plot(h, k, 'ro', label=f"จุดยอด ({h}, {k})")
    ax.axhline(0, color='black', linewidth=0.8, linestyle='--')
    ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend()
    
    with col1:
        st.pyplot(fig)
        
    with col2:
        st.subheader("📌 พฤติกรรมของฟังก์ชัน")
        st.write(f"*จุดยอด (h, k):* ({h}, {k})")
        st.write(f"*ทิศทางการเปิด:* {direction}")
        st.write(f"*ลักษณะจุดยอด:* {extrema_type}")
        st.write(f"*ค่าสุดขีด:* {extrema_val}")

with tab2:
    st.subheader("📚 สรุปเนื้อหาสมการพาราโบลา")

    st.markdown("### 1. พาราโบลาแนวตั้ง")
    st.latex(r"y = a(x - h)^2 + k")
    st.write("- *จุดยอด:* $(h, k)$")
    st.write("- *ถ้า $a > 0$:* กราฟหงาย ให้จุดต่ำสุดที่ $(h, k)$ มีค่าต่ำสุดคือ $y = k$")
    st.write("- *ถ้า $a < 0$:* กราฟคว่ำ ให้จุดสูงสุดที่ $(h, k)$ มีค่าสูงสุดคือ $y = k$")

    st.markdown("### 2. พาราโบลาแนวนอน")
    st.latex(r"x = a(y - k)^2 + h")
    st.write("- *จุดยอด:* $(h, k)$")
    st.write("- *ถ้า $a > 0$:* กราฟเปิดไปทางขวา")
    st.write("- *ถ้า $a < 0$:* กราฟเปิดไปทางซ้าย")
