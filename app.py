import streamlit as st
import pandas as pd

st.set_page_config(page_title="SMV Envíos", page_icon="🚀")

st.title("Sistema de Difusión - SMV Electronica")

st.write("Sube tu lista de clientes y la lista de precios actualizada.")

# Subida de archivo
archivo_clientes = st.file_uploader("Sube tu archivo CSV de clientes", type=['csv'])

if archivo_clientes is not None:
    df = pd.read_csv(archivo_clientes)
    st.dataframe(df.head())
    
    mensaje = st.text_area("Pega la lista de precios aquí:")
    
    if st.button("Iniciar Envío Automático"):
        st.warning("Próximamente: Conexión con WhatsApp en la nube...")
