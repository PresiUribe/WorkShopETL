import pandas as pd
from sqlalchemy import create_engine

# =====================
# Cargar CSV
# =====================
df = pd.read_csv('candidates.csv', sep=';')

# Calcular columna Hired
df['Hired'] = (df['Code Challenge Score'] >= 7) & (df['Technical Interview Score'] >= 7)

# =====================
# DimCandidate
# =====================
df['CandidateID'] = range(1, len(df) + 1)  # genera ID único
dim_candidate = df[['CandidateID', 'First Name', 'Last Name', 'Email']].drop_duplicates()

# =====================
# DimTechnology
# =====================
df['TechnologyID'] = df['Technology'].astype('category').cat.codes + 1
dim_technology = df[['TechnologyID', 'Technology']].drop_duplicates()

# =====================
# DimYear
# =====================
df['ApplicationYear'] = pd.to_datetime(df['Application Date']).dt.year
df['YearID'] = df['ApplicationYear'].astype('category').cat.codes + 1
dim_year = df[['YearID', 'ApplicationYear']].drop_duplicates()

# =====================
# DimSeniority
# =====================
df['SeniorityID'] = df['Seniority'].astype('category').cat.codes + 1
dim_seniority = df[['SeniorityID', 'Seniority']].drop_duplicates()

# =====================
# DimCountry
# =====================
df['CountryID'] = df['Country'].astype('category').cat.codes + 1
dim_country = df[['CountryID', 'Country']].drop_duplicates()

# =====================
# FactHiring
# =====================
# FactHiring
fact_hiring = df[['CandidateID', 'TechnologyID', 'YearID', 'SeniorityID', 'CountryID',
                  'Code Challenge Score', 'Technical Interview Score', 'YOE','Hired']]

# Renombrar columnas para evitar espacios en MySQL
fact_hiring = fact_hiring.rename(columns={
    'Code Challenge Score': 'CodeChallengeScore',
    'Technical Interview Score': 'TechnicalInterviewScore'
})


# =====================
# Conexión DB
# =====================
engine = create_engine('mysql+pymysql://root:8923167@localhost/my_data_warehouse')

# Cargar dimensiones
dim_candidate.to_sql('DimCandidate', engine, if_exists='replace', index=False)
dim_technology.to_sql('DimTechnology', engine, if_exists='replace', index=False)
dim_year.to_sql('DimYear', engine, if_exists='replace', index=False)
dim_seniority.to_sql('DimSeniority', engine, if_exists='replace', index=False)
dim_country.to_sql('DimCountry', engine, if_exists='replace', index=False)

# Cargar fact table
fact_hiring.to_sql('FactHiring', engine, if_exists='replace', index=False)
