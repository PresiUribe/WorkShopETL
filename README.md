# WorkShopETL
This project is a data engineering exercise to simulate a complete ETL (Extract, Transform, Load) process. The objective is to extract data from a CSV file, transform it into a dimensional data model (DDM), load it into a Data Warehouse (DW), and generate reports with KPIs and visualizations.

Justification of the Dimensional Data Model (DDM)
Star Schema Model

The chosen model for data transformation and loading is a star schema, which is one of the most common techniques in Data Warehouse design. The star schema is characterized by having a centralized fact table, surrounded by dimension tables that describe different perspectives of the data.

Dimension Tables

Technology Dimension (DimensionTechnology): This table contains information about the technologies used by the candidates. It is represented by a unique technology identifier (TechnologyID) and a technology name. This dimension allows analyzing candidates according to the technologies in which they have experience or are applying for.

Year Dimension (DimensionYear): This table contains the year when the candidates applied. The column ApplicationYear is extracted from the application date (Application Date) and assigned a unique year identifier (YearID). This dimension facilitates the analysis of hires by year.

Seniority Dimension (DimensionSeniority): This table stores the candidates' seniority levels (e.g., junior, senior, etc.). The column Seniority is used to represent these levels and assign a unique identifier (SeniorityID), allowing the analysis of hires according to the candidates' experience level.

Fact Table

The chosen fact table is FactCandidates, which contains metrics related to the candidates in the selection process. This table includes the following columns:

CandidateID: Unique identifier for each candidate.

TechnologyID: Related to DimensionTechnology, identifies the technology associated with the candidate.

YearID: Related to DimensionYear, represents the year the candidate applied.

SeniorityID: Related to DimensionSeniority, identifies the candidate's seniority level.

CodeChallengeScore: The score obtained by the candidate in the coding challenge.

TechnicalInterviewScore: The score obtained by the candidate in the technical interview.

Hired: A boolean value indicating whether the candidate was hired or not.

Why this is the fact table

FactCandidates is suitable as the fact table because it contains the key metrics related to the selection process. It includes the candidates’ scores, their seniority level, the technology they specialize in, and whether they were hired. These metrics are used to calculate KPIs (such as hire rate, hires by technology, hires by year, etc.), making this table the central component of the data structure.

ETL Process Flow
Extraction (Extract):

The extraction process takes the CSV file containing candidate data and loads it into a Pandas DataFrame.

An initial transformation is performed to calculate the Hired column based on the candidates’ scores.

Transformation (Transform):

Business rules are applied to determine if a candidate was hired (both scores must be greater than or equal to 7).

Dimension tables are created: DimensionTechnology, DimensionYear, and DimensionSeniority, assigning unique identifiers for each technology, year, and seniority level.

Finally, the fact table, FactCandidates, is prepared with the key metrics.

Load (Load):

The transformed data is loaded into a Data Warehouse (DW) using SQLAlchemy and pymysql.

Dimension tables are loaded first, followed by the fact table.

KPIs and Visualizations

Several visualizations were generated for the most relevant KPIs:

Hires by Technology: Number of hires per technology.

Hires by Year: Number of hires per year.

Hires by Seniority: Number of hires by seniority level.

Hires by Country: Hires in specific countries (USA, Brazil, Colombia, Ecuador).

Hires by Experience Range: Number of hires by candidates' experience range.

Hire Rate: Percentage of candidates hired.

Average Scores: Average scores in the Code Challenge and Technical Interview.

Technologies Used

Python: For data processing and visualization creation.

SQLAlchemy and pymysql: For connecting to the Data Warehouse (MySQL).

Seaborn and Matplotlib: For creating KPI visualizations.

Si quieres, puedo hacer una versión aún más profesional para tu README de GitHub en inglés, lista para subir directamente, incluyendo secciones de instalación y ejecución.

¿Quieres que haga eso?

Tú dijiste:
si
ChatGPT Plus

Perfecto, aquí tienes una versión profesional lista para usar como README.md en inglés para tu proyecto ETL en GitHub:

WorkShopETL

This project is a data engineering exercise simulating a complete ETL (Extract, Transform, Load) process. The objective is to extract candidate data from a CSV file, transform it into a dimensional data model (DDM), load it into a Data Warehouse (DW), and generate reports with KPIs and visualizations.

Table of Contents

Dimensional Data Model (DDM) Justification

ETL Process Flow

KPIs and Visualizations

Technologies Used

How to Run the Project

Gitignore Recommendations

Dimensional Data Model (DDM) Justification
Star Schema Model

The data is structured using a star schema, a widely used design pattern for Data Warehouses. A star schema consists of a central fact table surrounded by dimension tables, allowing efficient analysis across multiple perspectives.

Dimension Tables

Technology Dimension (DimensionTechnology): Contains information about technologies used by candidates. Includes a unique identifier (TechnologyID) and technology name. Allows analysis of hires by technology.

Year Dimension (DimensionYear): Contains the application year of each candidate (ApplicationYear) with a unique identifier (YearID). Facilitates analysis of hires by year.

Seniority Dimension (DimensionSeniority): Stores the seniority levels of candidates (e.g., Junior, Senior) and assigns a unique identifier (SeniorityID). Enables analysis of hires by experience level.

Fact Table

The fact table is FactCandidates, containing metrics related to the candidate selection process. It includes:

CandidateID: Unique identifier for each candidate

TechnologyID: Links to DimensionTechnology

YearID: Links to DimensionYear

SeniorityID: Links to DimensionSeniority

CodeChallengeScore: Candidate's coding challenge score

TechnicalInterviewScore: Candidate's technical interview score

Hired: Boolean indicating if the candidate was hired

Why FactCandidates is the Fact Table

FactCandidates is central because it stores the key metrics used for KPIs such as hire rate, hires by technology, hires by year, etc., making it the core of the star schema.

ETL Process Flow

Extract: Load the CSV containing candidate data into a Pandas DataFrame.

An initial transformation is performed to calculate the Hired column based on candidate scores.

Transform:

Apply business rules to determine if a candidate was hired (both scores ≥ 7).

Create dimension tables: DimensionTechnology, DimensionYear, DimensionSeniority.

Prepare the fact table, FactCandidates, with the key metrics.

Load:

Load the transformed data into a MySQL Data Warehouse using SQLAlchemy and pymysql.

Dimension tables are loaded first, followed by the fact table.

KPIs and Visualizations

The following KPIs are visualized:

Hires by Technology

Hires by Year

Hires by Seniority

Hires by Country (USA, Brazil, Colombia, Ecuador)

Hires by Experience Range

Hire Rate (%)

Average Scores (Code Challenge & Technical Interview)

Visualizations are created with Seaborn and Matplotlib.

Technologies Used

Python – Data processing and visualization

Pandas – Data manipulation

SQLAlchemy & pymysql – MySQL Data Warehouse connection

Seaborn & Matplotlib – KPI visualizations