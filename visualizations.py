import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
import os

# Crear la conexión a la base de datos
engine = create_engine('mysql+pymysql://root:8923167@localhost/my_data_warehouse')

# Configurar el estilo de los gráficos de seaborn
sns.set(style="whitegrid")

# Crear carpeta para guardar visualizaciones
output_dir = "visualizations_output"
os.makedirs(output_dir, exist_ok=True)

# Función para mostrar y guardar gráficos
def save_and_show(fig_name):
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, fig_name), dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()

# 1. Hires by Technology
query_technology = """
SELECT Technology, COUNT(*) AS Hires
FROM FactCandidates
JOIN DimensionTechnology ON FactCandidates.TechnologyID = DimensionTechnology.TechnologyID
WHERE Hired = 1
GROUP BY Technology;
"""
kpi_data_technology = pd.read_sql(query_technology, engine)

plt.figure(figsize=(12,6))
sns.barplot(
    x='Technology', 
    y='Hires', 
    data=kpi_data_technology, 
    order=kpi_data_technology.sort_values('Hires', ascending=False).Technology,
    palette='Blues_d'
)
plt.title('Hires by Technology', fontsize=16, weight='bold')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Technology', fontsize=12)
plt.ylabel('Number of Hires', fontsize=12)
save_and_show("hires_by_technology.png")

# 2. Hires by Year
query_year = """
SELECT ApplicationYear AS Year, COUNT(*) AS Hires
FROM FactCandidates
JOIN DimensionYear ON FactCandidates.YearID = DimensionYear.YearID
WHERE Hired = 1
GROUP BY ApplicationYear;
"""
kpi_data_year = pd.read_sql(query_year, engine)

plt.figure(figsize=(12,6))
sns.barplot(x='Year', y='Hires', data=kpi_data_year, palette='viridis')
plt.title('Hires by Year', fontsize=16, weight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Hires', fontsize=12)
save_and_show("hires_by_year.png")

# 3. Hires by Seniority
query_seniority = """
SELECT Seniority, COUNT(*) AS Hires
FROM FactCandidates
JOIN DimensionSeniority ON FactCandidates.SeniorityID = DimensionSeniority.SeniorityID
WHERE Hired = 1
GROUP BY Seniority;
"""
kpi_data_seniority = pd.read_sql(query_seniority, engine)

plt.figure(figsize=(12,6))
sns.barplot(
    x='Seniority', 
    y='Hires', 
    data=kpi_data_seniority, 
    order=kpi_data_seniority.sort_values('Hires', ascending=False).Seniority,
    palette='coolwarm'
)
plt.title('Hires by Seniority', fontsize=16, weight='bold')
plt.xlabel('Seniority Level', fontsize=12)
plt.ylabel('Number of Hires', fontsize=12)
save_and_show("hires_by_seniority.png")

# 4. Hires by Country
query_country = """
SELECT Country, COUNT(*) AS Hires
FROM FactCandidates
WHERE Hired = 1 AND Country IN ('United States of America', 'Brazil', 'Colombia', 'Ecuador')
GROUP BY Country;
"""
kpi_data_country = pd.read_sql(query_country, engine)

plt.figure(figsize=(12,6))
sns.barplot(x='Country', y='Hires', data=kpi_data_country, palette='Set2')
plt.title('Hires by Country (USA, Brazil, Colombia, Ecuador)', fontsize=16, weight='bold')
plt.xlabel('Country', fontsize=12)
plt.ylabel('Number of Hires', fontsize=12)
save_and_show("hires_by_country.png")

# 5. Hires by Experience Range
query_experience = """
SELECT 
    CASE 
        WHEN Yoe <= 2 THEN '0-2 years'
        WHEN Yoe BETWEEN 3 AND 5 THEN '3-5 years'
        WHEN Yoe BETWEEN 6 AND 10 THEN '6-10 years'
        ELSE '10+ years'
    END AS ExperienceRange, 
    COUNT(*) AS Hires
FROM FactCandidates
WHERE Hired = 1
GROUP BY ExperienceRange;
"""
kpi_data_experience = pd.read_sql(query_experience, engine)

plt.figure(figsize=(12,6))
sns.barplot(
    x='ExperienceRange', 
    y='Hires', 
    data=kpi_data_experience, 
    palette='rocket',
    order=['0-2 years', '3-5 years', '6-10 years', '10+ years']
)
plt.title('Hires by Experience Range', fontsize=16, weight='bold')
plt.xlabel('Experience Range', fontsize=12)
plt.ylabel('Number of Hires', fontsize=12)
save_and_show("hires_by_experience_range.png")

# 6. Average Scores (Code Challenge & Technical Interview)
query_avg_scores = """
SELECT 
    AVG(`Code Challenge Score`) AS AvgCodeChallengeScore,
    AVG(`Technical Interview Score`) AS AvgTechnicalInterviewScore
FROM FactCandidates;
"""
avg_scores = pd.read_sql(query_avg_scores, engine)

avg_scores_melted = avg_scores.melt(var_name="ScoreType", value_name="AverageScore")
plt.figure(figsize=(8,6))
sns.barplot(x='ScoreType', y='AverageScore', data=avg_scores_melted, palette='magma')
plt.title('Average Scores (Code Challenge & Technical Interview)', fontsize=16, weight='bold')
plt.xlabel('Score Type', fontsize=12)
plt.ylabel('Average Score', fontsize=12)
save_and_show("average_scores.png")
