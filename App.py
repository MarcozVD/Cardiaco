import streamlit as st
import numpy as np
import joblib
from pathlib import Path

st.set_page_config(page_title="Predicor de Problemas Cardíacos", layout="centered")

st.title("predicor de problemas cardicos")
st.subheader("elaborado ™ de marca registrada unab 2025")

st.markdown("---")

# Rutas esperadas para los archivos subidos por el usuario en el entorno
SCALER_PATH = Path("/mnt/data/scaler.jb")
MODEL_PATH = Path("/mnt/data/svc_model.jb")

# Sliders: edad (25-80, por defecto 55, step 1), colesterol (120-600, por defecto 242, step 2)
edad = st.slider("Edad", min_value=25, max_value=80, value=55, step=1)
colesterol = st.slider("Colesterol", min_value=120, max_value=600, value=242, step=2)

st.write("\n")

# Cargar scaler y modelo con manejo de errores
@st.cache_resource
def cargar_scaler(path: str):
    try:
        return joblib.load(path)
    except Exception as e:
        st.error(f"No se pudo cargar el scaler desde {path}: {e}")
        return None

@st.cache_resource
def cargar_modelo(path: str):
    try:
        return joblib.load(path)
    except Exception as e:
        st.error(f"No se pudo cargar el modelo desde {path}: {e}")
        return None

scaler = cargar_scaler(SCALER_PATH)
modelo = cargar_modelo(MODEL_PATH)

if modelo is None or scaler is None:
    st.warning("Asegúrate de que los archivos 'scaler.jb' y 'svc_model.jb' existan en /mnt/data/ y vuelve a ejecutar la app.")
else:
    # Preprocesar: aplicar la misma transformación MinMaxScaler usada en entrenamiento
    X_raw = np.array([[edad, colesterol]], dtype=float)
    try:
        X_scaled = scaler.transform(X_raw)
    except Exception as e:
        st.error(f"Error al escalar las variables: {e}")
        X_scaled = None

    if X_scaled is not None:
        # Predecir
        try:
            pred = modelo.predict(X_scaled)
            # Asegurarse que pred sea 0 o 1
            etiqueta = int(pred[0])
        except Exception as e:
            st.error(f"Error al predecir con el modelo: {e}")
            etiqueta = None

        if etiqueta is not None:
            if etiqueta == 0:
                st.success("Predicción: 0 — no sufrirá problemas cardíacos (según el modelo)")
                st.image("https://tse4.mm.bing.net/th/id/OIP.KabMgpPNpdP4pxUtND3TGQHaFj?rs=1&pid=ImgDetMain&o=7&rm=3", caption="No sufrirá", use_column_width=True)
            elif etiqueta == 1:
                st.error("Predicción: 1 — sufrirá problemas cardíacos (según el modelo)")
                st.image("https://ichef.bbci.co.uk/news/640/amz/worldservice/live/assets/images/2011/06/09/110609010302_heart_attack_304x171_spl.jpg", caption="Sufriría", use_column_width=True)
            else:
                st.warning(f"La predicción devolvió un valor inesperado: {etiqueta}")

st.markdown("---")
st.caption("Nota: Este predictor usa un modelo entrenado sólo con dos características (edad, colesterol). No sustituye evaluación médica profesional.")
