# WorkShopETL
Este proyecto es un ejercicio de ingeniería de datos para simular un proceso ETL (Extract, Transform, Load) completo. El objetivo es extraer datos de un archivo CSV, transformarlos en un modelo dimensional (DDM), cargarlos en un Data Warehouse (DW) y generar reportes con KPIs y visualizaciones.

Justificación del Modelo de Datos Dimensional (DDM)
Modelo Estrella (Star Schema)

El modelo elegido para la transformación y carga de los datos es un modelo estrella (Star Schema), que es una de las técnicas más comunes en el diseño de Data Warehouses. El modelo estrella se caracteriza por tener una tabla de hechos centralizada, rodeada de tablas de dimensiones que describen las diferentes perspectivas de los datos.

Tablas de Dimensiones

Dimensión Tecnología (DimensionTechnology): Esta tabla contiene información sobre las tecnologías utilizadas por los candidatos. Está representada por un identificador único de tecnología (TechnologyID) y un nombre de tecnología. Esta dimensión permite analizar los candidatos según las tecnologías en las que tienen experiencia o en las que se postulan.

Dimensión Año (DimensionYear): Esta tabla contiene el año de la aplicación de los candidatos. La columna ApplicationYear se extrae de la fecha de la solicitud (Application Date) y se asigna un identificador único de año (YearID). Esta dimensión facilita el análisis de los contratados por año.

Dimensión Senioridad (DimensionSeniority): Esta tabla almacena los niveles de senioridad de los candidatos (por ejemplo, junior, senior, etc.). La columna Seniority se usa para representar estos niveles y asignar un identificador único (SeniorityID), permitiendo analizar el número de contrataciones según el nivel de experiencia de los candidatos.

Tabla de Hechos

La tabla de hechos elegida es FactCandidates, que contiene las métricas relacionadas con los candidatos en el proceso de selección. Esta tabla incluye las siguientes columnas:

CandidateID: Identificador único de cada candidato.

TechnologyID: Relacionado con la DimensionTechnology, identifica la tecnología relacionada con el candidato.

YearID: Relacionado con la DimensionYear, representa el año en que el candidato aplicó.

SeniorityID: Relacionado con la DimensionSeniority, identifica el nivel de senioridad del candidato.

CodeChallengeScore: La puntuación obtenida por el candidato en el reto de codificación.

TechnicalInterviewScore: La puntuación obtenida por el candidato en la entrevista técnica.

Hired: Un valor booleano que indica si el candidato fue contratado o no.

¿Por qué esta es la tabla de hechos?

La tabla FactCandidates es adecuada para ser la tabla de hechos porque contiene las métricas clave relacionadas con el proceso de selección. En ella se encuentran las puntuaciones de los candidatos, su nivel de senioridad, la tecnología en la que se especializan, y si fueron contratados o no. Estas métricas se utilizan para calcular KPIs (como la tasa de contratación, contrataciones por tecnología, contrataciones por año, etc.), lo que convierte a esta tabla en el centro de la estructura de datos.

Flujo del Proceso ETL

Extracción (Extract):

El proceso de extracción toma el archivo CSV que contiene los datos de los candidatos y lo carga en un DataFrame de Pandas.

Se realiza una transformación inicial para calcular la columna Hired en función de las puntuaciones de los candidatos.

Transformación (Transform):

Se aplica la regla de negocio para determinar si un candidato fue contratado (ambas puntuaciones deben ser mayores o iguales a 7).

Se crean las tablas de dimensiones: DimensionTechnology, DimensionYear, y DimensionSeniority, donde se asignan identificadores únicos a cada tecnología, año y nivel de senioridad.

Finalmente, se prepara la tabla de hechos, FactCandidates, que contiene las métricas clave.

Carga (Load):

Los datos transformados se cargan en un Data Warehouse (DW) utilizando SQLAlchemy y pymysql.

Las tablas de dimensiones se cargan primero, seguidas de la tabla de hechos.

KPIs y Visualizaciones

Se generaron varias visualizaciones con los KPIs más relevantes:

Hires by Technology: Visualización del número de contrataciones por tecnología.

Hires by Year: Visualización del número de contrataciones por año.

Hires by Seniority: Visualización del número de contrataciones por nivel de senioridad.

Hires by Country: Visualización de contrataciones en países específicos (USA, Brasil, Colombia, Ecuador).

Hires by Experience Range: Visualización del número de contrataciones según el rango de experiencia de los candidatos.

Hire Rate: Porcentaje de contratación.

Average Scores: Promedio de puntuaciones en el "Code Challenge" y la "Technical Interview".

Tecnologías Utilizadas

Python: Para el procesamiento de datos y creación de visualizaciones.

SQLAlchemy y pymysql: Para la conexión con el Data Warehouse (MySQL).

Seaborn y Matplotlib: Para la creación de visualizaciones de KPIs.