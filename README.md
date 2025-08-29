# WorkShopETL

Este proyecto implementa un flujo completo de **ETL (Extract, Transform, Load)** para simular un proceso de reclutamiento, transformarlo en un **modelo dimensional (DDM)** en un Data Warehouse, y generar **KPIs con visualizaciones**.

---

## 🗂 Justificación del Modelo de Datos Dimensional (DDM)

Se utilizó un **modelo estrella (Star Schema)**, donde:

- **Tabla de Hechos → FactHiring**
  Contiene el evento del proceso de contratación, con las métricas clave.
- **Tablas de Dimensiones** describen los contextos de análisis (candidato, tecnología, año, seniority y país).

### 🔹 FactHiring
- HireID (PK)  
- CandidateID (FK)  
- TechnologyID (FK)  
- YearID (FK)  
- SeniorityID (FK)  
- CountryID (FK)  
- CodeChallengeScore  
- TechnicalInterviewScore  
- YOE (Years of Experience)  
- Hired (booleano)

### 🔹 Dimensiones
- **DimCandidate** → datos descriptivos del candidato (nombre, email).  
- **DimTechnology** → tecnologías aplicadas.  
- **DimYear** → año de aplicación.  
- **DimSeniority** → nivel de experiencia (Junior, Senior, etc.).  
- **DimCountry** → país del candidato.  

👉 Esto permite analizar desde múltiples perspectivas las métricas del proceso de selección.

---

## 📊 KPIs y Visualizaciones

### 1. Hires by Technology
Cantidad de contrataciones por tecnología.
![Hires by Technology](visualizations_output/hires_by_technology.png)

---

### 2. Hires by Year
Número de contrataciones por año de aplicación.
![Hires by Year](visualizations_output/hires_by_year.png)

---

### 3. Hires by Seniority
Número de contrataciones por nivel de seniority.
![Hires by Seniority](visualizations_output/hires_by_seniority.png)

---

### 4. Hires by Country
Contrataciones en países seleccionados.
![Hires by Country](visualizations_output/hires_by_country.png)

---

### 5. Hires by Experience Range
Contrataciones agrupadas por rangos de años de experiencia.
![Hires by Experience Range](visualizations_output/hires_by_experience_range.png)

---

### 6. Average Scores
Promedio de puntajes en el **Code Challenge** y la **Technical Interview**.  
👉 Cada barra incluye la etiqueta con el valor exacto.
![Average Scores](visualizations_output/average_scores.png)

---

### 7. Hire Rate (%) por Seniority
Proporción de candidatos contratados frente al total de postulados, por nivel de seniority.  
![Hire Rate by Seniority](visualizations_output/hire_rate_by_seniority.png)

---

### 8. Hires (volumen) + Hire Rate (%) por Seniority
Gráfico combinado que muestra:
- **Barras azules:** volumen de contrataciones (número absoluto).  
- **Línea roja:** Hire Rate (%) por seniority.  

Esto permite comparar **cantidad** y **eficiencia** en un solo gráfico.  
![Hire Volume and Rate by Seniority](visualizations_output/hire_volume_rate_by_seniority.png)

---

## 🛠 Tecnologías Utilizadas
- **Python** → ETL y generación de visualizaciones.  
- **Pandas & SQLAlchemy** → transformación y carga de datos.  
- **MySQL** → Data Warehouse.  
- **Matplotlib & Seaborn** → visualizaciones.  

---

## 📑 Reporte Consolidado
Todas las visualizaciones se encuentran también en un **PDF único**:  

📂 `visualizations_output/report.pdf`  

---

## 📌 Conclusiones
- El modelo dimensional permite analizar contrataciones desde múltiples perspectivas.  
- Los KPIs revelan diferencias entre volumen de contrataciones y tasas de éxito según tecnología, año, seniority y país.  
- El análisis combinado (volumen + Hire Rate) brinda una visión más profunda sobre **eficiencia del proceso de selección**.  
