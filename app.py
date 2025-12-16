import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="Peytam AI", layout="wide")

# Sidebar
st.sidebar.title("🏠 Peytam AI Interiors")
st.sidebar.markdown("**طراحی داخلی هوشمند**")

# Header
st.title("🏠 Peytam AI Interiors")
st.markdown("**آپلود پلان → تحلیل هوشمند → طراحی فضا**")

# Tabs
tab1, tab2 = st.tabs(["📐 تحلیل پلان", "🎨 طراحی فضا"])

with tab1:
    floorplan = st.file_uploader("پلان آپارتمان", type=['png', 'jpg'])
    if floorplan:
        col1, col2 = st.columns(2)
        with col1:
            st.image(floorplan, caption="پلان آپارتمان")
        with col2:
            st.json({
                "فضاها": [
                    {"آشپزخانه": "4×3 متر - پنجره شمال + سینک"},
                    {"نشیمن": "6×3 متر - پنجره شمال"},
                    {"اتاق خواب 1": "4×3 متر - پنجره جنوب"}
                ]
            })

with tab2:
    st.header("طراحی فضا")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        room = st.selectbox("فضا", ["آشپزخانه", "نشیمن", "اتاق خواب 1"])
        style = st.selectbox("سبک", ["مدرن", "مینیمال", "لوکس"])
        if st.button("✨ تولید طراحی", type="primary"):
            prompt = f"Photorealistic {style} {room}, 4x3m apartment, exact floorplan geometry, entry view from door, high quality interior design"
            
            # HF Free Image Gen
            with st.spinner("در حال تولید..."):
                response = requests.post(
                    "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0",
                    headers={"Authorization": "Bearer YOUR_HF_TOKEN"},
                    json={"inputs": prompt}
                )
                image = Image.open(io.BytesIO(response.content))
            
            st.image(image, caption=f"{room} - {style}")
            st.text_area("پرامپت استفاده شده", prompt, height=100)
            
            st.subheader("📊 جدول متریال")
            st.json({
                "کف": "کاشی {style} - 12 مترمربع",
                "دیوار": "رنگ مات - 25 مترمربع",
                "کابینت": "چوب بلوط - 3 متر"
            })
