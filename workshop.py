import pandas as pd
from sqlalchemy import create_engine



# Cargar el archivo CSV con el separador ;
df = pd.read_csv('candidates.csv', sep=';')
df['Hired'] = (df['Code Challenge Score'] >= 7) & (df['Technical Interview Score'] >= 7)

# Crear las dimensiones
# Dimensión Tecnología (DimTechnology)
df['TechnologyID'] = df['Technology'].astype('category').cat.codes
dim_technology = df[['Technology', 'TechnologyID']].drop_duplicates()

# Dimensión Año (DimYear)
df['ApplicationYear'] = pd.to_datetime(df['Application Date']).dt.year
df['YearID'] = df['ApplicationYear'].astype('category').cat.codes
dim_year = df[['ApplicationYear', 'YearID']].drop_duplicates()

# Dimensión Senioridad (DimSeniority)
df['SeniorityID'] = df['Seniority'].astype('category').cat.codes
dim_seniority = df[['Seniority', 'SeniorityID']].drop_duplicates()

# Crear la tabla de hechos (FactCandidates) e incluir la columna Yoe
fact_candidates = df[['First Name', 'Last Name', 'Email', 'Country', 'TechnologyID', 'YearID', 'SeniorityID', 'Code Challenge Score', 'Technical Interview Score', 'Hired', 'YOE']]

# Crear la conexión a la base de datos
engine = create_engine('mysql+pymysql://root:8923167@localhost/my_data_warehouse')

# Cargar las dimensiones en el Data Warehouse
dim_technology.to_sql('DimensionTechnology', engine, if_exists='replace', index=False)
dim_year.to_sql('DimensionYear', engine, if_exists='replace', index=False)
dim_seniority.to_sql('DimensionSeniority', engine, if_exists='replace', index=False)

# Cargar la tabla de hechos en el Data Warehouse
fact_candidates.to_sql('FactCandidates', engine, if_exists='replace', index=False)

