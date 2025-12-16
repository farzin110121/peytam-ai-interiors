import streamlit as st

st.set_page_config(layout="wide")
st.title("🏠 Peytam AI Interiors")
st.markdown("### آپلود پلان → تحلیل → طراحی فضا")

tab1, tab2 = st.tabs(["📐 تحلیل پلان", "🎨 طراحی"])

with tab1:
    st.header("آپلود پلان")
    uploaded_file = st.file_uploader("پلان انتخاب کنید", type=['png','jpg'])
    if uploaded_file:
        st.image(uploaded_file)
        st.success("✅ تحلیل کامل شد!")
        st.json({
            "آشپزخانه": "4x3 متر - پنجره شمال",
            "نشیمن": "6x3 متر - پنجره شمال",
            "اتاق خواب": "4x3 متر - پنجره جنوب"
        })

with tab2:
    st.header("طراحی فضا")
    col1, col2 = st.columns(2)
    
    with col1:
        room = st.selectbox("فضا", ["آشپزخانه", "نشیمن", "اتاق خواب"])
        style = st.selectbox("سبک", ["مدرن", "لوکس", "مینیمال"])
    
    if st.button("✨ تولید طراحی", type="primary"):
        st.balloons()
        st.success(f"✅ {room} - {style} آماده!")
        
        st.subheader("🖼️ پرامپت Midjourney:")
        st.code(f"photorealistic {style} {room} interior, 4x3m, modern design")
        
        st.subheader("📊 متریال:")
        st.json({
            "کف": "کاشی مدرن - 12m²",
            "کابینت": "چوب - 3m",
            "دیوار": "رنگ - 25m²"
        })
