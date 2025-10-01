# Predicor de Problemas Cardíacos

Aplicación en **Streamlit** que predice si una persona sufrirá problemas cardíacos en función de su **edad** y **colesterol**, utilizando un modelo de **Support Vector Classifier (SVC)** previamente entrenado.

---

## 📌 Características
- Interfaz interactiva con **sliders** para:
  - Edad (25 a 80 años, valor por defecto: 55)
  - Colesterol (120 a 600 mg/dL, valor por defecto: 242)
- Normalización de datos con `MinMaxScaler`.
- Predicción con modelo **SVC** cargado desde `svc_model.jb`.
- Visualización de imágenes según el resultado:
  - **0** → No sufrirá problemas cardíacos ✅
  - **1** → Sí sufrirá problemas cardíacos ⚠️

---

## 📂 Archivos necesarios
- `app.py` → Código de la aplicación Streamlit.
- `requirements.txt` → Dependencias del proyecto.
- `scaler.jb` → Scaler entrenado con MinMaxScaler.
- `svc_model.jb` → Modelo entrenado (Support Vector Classifier).

---

## 🚀 Instalación y ejecución
1. Clonar o descargar este repositorio.
2. Crear un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Linux/Mac
   venv\Scripts\activate      # En Windows
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecutar la aplicación:
   ```bash
   streamlit run app.py
   ```

---

## 📸 Vista previa
- **Predicción 0:**
  ![No sufrirá](https://tse4.mm.bing.net/th/id/OIP.KabMgpPNpdP4pxUtND3TGQHaFj?rs=1&pid=ImgDetMain&o=7&rm=3)

- **Predicción 1:**
  ![Sí sufrirá](https://ichef.bbci.co.uk/news/640/amz/worldservice/live/assets/images/2011/06/09/110609010302_heart_attack_304x171_spl.jpg)

---

## ⚠️ Nota
Este proyecto es un **ejemplo educativo**. No reemplaza en ningún caso el diagnóstico médico profesional.
