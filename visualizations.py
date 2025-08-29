import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from matplotlib.backends.backend_pdf import PdfPages
import os

# ===============================
# Conexión a la base de datos
# ===============================
engine = create_engine('mysql+pymysql://root:8923167@localhost/my_data_warehouse')

# ===============================
# Configuración general
# ===============================
sns.set(style="whitegrid")

# Carpeta para guardar visualizaciones
output_dir = "visualizations_output"
os.makedirs(output_dir, exist_ok=True)

# PDF consolidado
pdf_path = os.path.join(output_dir, "report.pdf")
pdf = PdfPages(pdf_path)

# Función para mostrar y guardar gráficos
def save_and_show(fig_name):
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, fig_name), dpi=300, bbox_inches='tight')  # PNG
    pdf.savefig()  # Guardar también en el PDF
    plt.close()

# Función para agregar etiquetas encima de las barras
def add_labels(ax, decimals=0, suffix=""):
    for p in ax.patches:
        value = p.get_height()
        ax.annotate(f"{value:.{decimals}f}{suffix}",
                    (p.get_x() + p.get_width() / 2., value),
                    ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# ===============================
# 1. Hires by Technology
# ===============================
query_technology = """
SELECT t.Technology, COUNT(*) AS Hires
FROM FactHiring f
JOIN DimTechnology t ON f.TechnologyID = t.TechnologyID
WHERE f.Hired = 1
GROUP BY t.Technology;
"""
kpi_data_technology = pd.read_sql(query_technology, engine)
plt.figure(figsize=(12,6))
ax = sns.barplot(x='Technology', y='Hires',
                 data=kpi_data_technology,
                 order=kpi_data_technology.sort_values('Hires', ascending=False).Technology,
                 palette='Blues_d')
plt.title('Hires by Technology', fontsize=16, weight='bold')
plt.xticks(rotation=45, ha='right')
add_labels(ax)
save_and_show("hires_by_technology.png")

# ===============================
# 2. Hires by Year
# ===============================
query_year = """
SELECT y.ApplicationYear AS Year, COUNT(*) AS Hires
FROM FactHiring f
JOIN DimYear y ON f.YearID = y.YearID
WHERE f.Hired = 1
GROUP BY y.ApplicationYear;
"""
kpi_data_year = pd.read_sql(query_year, engine)
plt.figure(figsize=(12,6))
ax = sns.barplot(x='Year', y='Hires', data=kpi_data_year, palette='viridis')
plt.title('Hires by Year', fontsize=16, weight='bold')
add_labels(ax)
save_and_show("hires_by_year.png")

# ===============================
# 3. Hires by Seniority
# ===============================
query_seniority = """
SELECT s.Seniority, COUNT(*) AS Hires
FROM FactHiring f
JOIN DimSeniority s ON f.SeniorityID = s.SeniorityID
WHERE f.Hired = 1
GROUP BY s.Seniority;
"""
kpi_data_seniority = pd.read_sql(query_seniority, engine)
plt.figure(figsize=(12,6))
ax = sns.barplot(x='Seniority', y='Hires',
                 data=kpi_data_seniority,
                 order=kpi_data_seniority.sort_values('Hires', ascending=False).Seniority,
                 palette='coolwarm')
plt.title('Hires by Seniority', fontsize=16, weight='bold')
add_labels(ax)
save_and_show("hires_by_seniority.png")

# ===============================
# 4. Hires by Country
# ===============================
query_country = """
SELECT c.Country, COUNT(*) AS Hires
FROM FactHiring f
JOIN DimCountry c ON f.CountryID = c.CountryID
WHERE f.Hired = 1 
  AND c.Country IN ('United States of America', 'Brazil', 'Colombia', 'Spain', 'Canada')
GROUP BY c.Country;
"""
kpi_data_country = pd.read_sql(query_country, engine)
plt.figure(figsize=(12,6))
ax = sns.barplot(
    x='Country',
    y='Hires',
    data=kpi_data_country,
    order=kpi_data_country.sort_values('Hires', ascending=False).Country,
    palette='Set2'
)
plt.title('Hires by Country (USA, Brazil, Colombia, Spain, Canada)', fontsize=16, weight='bold')
plt.xlabel('Country', fontsize=12)
plt.ylabel('Number of Hires', fontsize=12)
add_labels(ax)
save_and_show("hires_by_country.png")

# ===============================
# 5. Hires by Experience Range
# ===============================
query_experience = """
SELECT 
    CASE 
        WHEN f.YOE <= 2 THEN '0-2 years'
        WHEN f.YOE BETWEEN 3 AND 5 THEN '3-5 years'
        WHEN f.YOE BETWEEN 6 AND 10 THEN '6-10 years'
        ELSE '10+ years'
    END AS ExperienceRange, 
    COUNT(*) AS Hires
FROM FactHiring f
WHERE f.Hired = 1
GROUP BY ExperienceRange;
"""
kpi_data_experience = pd.read_sql(query_experience, engine)
plt.figure(figsize=(12,6))
ax = sns.barplot(x='ExperienceRange', y='Hires',
                 data=kpi_data_experience,
                 palette='rocket',
                 order=['0-2 years', '3-5 years', '6-10 years', '10+ years'])
plt.title('Hires by Experience Range', fontsize=16, weight='bold')
add_labels(ax)
save_and_show("hires_by_experience_range.png")

# ===============================
# 6. Average Scores
# ===============================
query_avg_scores = """
SELECT 
    AVG(f.CodeChallengeScore) AS AvgCodeChallengeScore,
    AVG(f.TechnicalInterviewScore) AS AvgTechnicalInterviewScore
FROM FactHiring f;
"""
avg_scores = pd.read_sql(query_avg_scores, engine)
avg_scores_melted = avg_scores.melt(var_name="ScoreType", value_name="AverageScore")
plt.figure(figsize=(8,6))
ax = sns.barplot(x='ScoreType', y='AverageScore', data=avg_scores_melted, palette='magma')
plt.title('Average Scores (Code Challenge & Technical Interview)', fontsize=16, weight='bold')
add_labels(ax, decimals=2)
save_and_show("average_scores.png")

# ===============================
# 7. Hire Rate (%) por Seniority
# ===============================
query_hire_rate_seniority = """
SELECT 
    s.Seniority,
    (SUM(CASE WHEN f.Hired = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS HireRate
FROM FactHiring f
JOIN DimSeniority s ON f.SeniorityID = s.SeniorityID
GROUP BY s.Seniority;
"""
hire_rate_seniority = pd.read_sql(query_hire_rate_seniority, engine)
hire_rate_seniority['Seniority'] = hire_rate_seniority['Seniority'].astype(str)

plt.figure(figsize=(10,6))
ax = sns.barplot(x='Seniority', y='HireRate',
                 data=hire_rate_seniority,
                 order=hire_rate_seniority.sort_values('HireRate', ascending=False).Seniority,
                 palette='crest')
plt.title('Hire Rate (%) por Seniority', fontsize=16, weight='bold')
plt.ylabel('Hire Rate (%)')
add_labels(ax, decimals=2, suffix="%")
save_and_show("hire_rate_by_seniority.png")

# ===============================
# 8. Hire Volume + Hire Rate por Seniority (gráfico combinado mejorado)
# ===============================
query_hire_volume_rate_seniority = """
SELECT 
    s.Seniority,
    COUNT(*) AS TotalCandidates,
    SUM(CASE WHEN f.Hired = 1 THEN 1 ELSE 0 END) AS Hires,
    (SUM(CASE WHEN f.Hired = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS HireRate
FROM FactHiring f
JOIN DimSeniority s ON f.SeniorityID = s.SeniorityID
GROUP BY s.Seniority;
"""
hire_volume_rate_seniority = pd.read_sql(query_hire_volume_rate_seniority, engine)
hire_volume_rate_seniority['Seniority'] = hire_volume_rate_seniority['Seniority'].astype(str)

fig, ax1 = plt.subplots(figsize=(10,6))

# Barras = número de hires
sns.barplot(x='Seniority', y='Hires', 
            data=hire_volume_rate_seniority, 
            color='skyblue', ax=ax1)

ax1.set_ylabel("Número de Hires", fontsize=12, color="blue")
ax1.set_xlabel("Seniority", fontsize=12)
ax1.tick_params(axis='y', labelcolor="blue")

# Etiquetas sobre las barras
for p in ax1.patches:
    ax1.annotate(f"{p.get_height():.0f}", 
                 (p.get_x() + p.get_width() / 2., p.get_height()), 
                 ha='center', va='bottom', fontsize=10, fontweight='bold', color='blue')

# Línea = Hire Rate %
ax2 = ax1.twinx()
ax2.plot(hire_volume_rate_seniority['Seniority'], 
         hire_volume_rate_seniority['HireRate'], 
         marker='o', color='red', linewidth=2, label="Hire Rate (%)")
ax2.set_ylabel("Hire Rate (%)", fontsize=12, color="red")
ax2.tick_params(axis='y', labelcolor="red")

plt.title("Hires (volumen) + Hire Rate (%) por Seniority", fontsize=16, weight='bold')
fig.tight_layout()
save_and_show("hire_volume_rate_by_seniority.png")


# ===============================
# Cerrar PDF consolidado
# ===============================
pdf.close()
print(f"=== Reporte generado en {pdf_path} ===")
