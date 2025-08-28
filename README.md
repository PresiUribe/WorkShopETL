# WorkShopETL

This project is a **data engineering exercise** simulating a complete **ETL (Extract, Transform, Load)** process. The objective is to extract candidate data from a CSV file, transform it into a **dimensional data model (DDM)**, load it into a **Data Warehouse (DW)**, and generate reports with **KPIs** and visualizations.

---

## Table of Contents
1. [Dimensional Data Model (DDM) Justification](#dimensional-data-model-ddm-justification)
2. [ETL Process Flow](#etl-process-flow)
3. [KPIs and Visualizations](#kpis-and-visualizations)
4. [Technologies Used](#technologies-used)
5. [How to Run the Project](#how-to-run-the-project)
6. [Gitignore Recommendations](#gitignore-recommendations)

---

## Dimensional Data Model (DDM) Justification

### Star Schema Model
The data is structured using a **star schema**, a widely used design pattern for **Data Warehouses**. A star schema consists of a **central fact table** surrounded by **dimension tables**, allowing efficient analysis across multiple perspectives.

### Dimension Tables

- **Technology Dimension (`DimensionTechnology`)**: Contains information about technologies used by candidates. Includes a **unique identifier (`TechnologyID`)** and **technology name**. Allows analysis of hires by technology.

- **Year Dimension (`DimensionYear`)**: Contains the **application year** of each candidate (`ApplicationYear`) with a **unique identifier (`YearID`)**. Facilitates analysis of hires by year.

- **Seniority Dimension (`DimensionSeniority`)**: Stores the **seniority levels** of candidates (e.g., Junior, Senior) and assigns a **unique identifier (`SeniorityID`)**. Enables analysis of hires by experience level.

### Fact Table

The **fact table** is **`FactCandidates`**, containing **metrics related to the candidate selection process**. It includes:

- **`CandidateID`**: Unique identifier for each candidate
- **`TechnologyID`**: Links to `DimensionTechnology`
- **`YearID`**: Links to `DimensionYear`
- **`SeniorityID`**: Links to `DimensionSeniority`
- **`CodeChallengeScore`**: Candidate's coding challenge score
- **`TechnicalInterviewScore`**: Candidate's technical interview score
- **`Hired`**: Boolean indicating if the candidate was hired

#### Why `FactCandidates` is the Fact Table
`FactCandidates` is central because it stores the **key metrics** used for KPIs such as hire rate, hires by technology, hires by year, etc., making it the core of the star schema.

---

## ETL Process Flow

### Extraction (Extract)
- Load the CSV containing candidate data into a **Pandas DataFrame**
- Initial transformation: calculate the **`Hired`** column based on candidate scores

### Transformation (Transform)
- Apply business rules to determine if a candidate was hired (**both scores ≥ 7**)
- Create dimension tables: `DimensionTechnology`, `DimensionYear`, `DimensionSeniority` with unique identifiers
- Prepare the fact table, `FactCandidates`, with key metrics

### Load (Load)
- Load the transformed data into a **MySQL Data Warehouse** using **SQLAlchemy** and **pymysql**
- Dimension tables are loaded first, followed by the fact table

---

## KPIs and Visualizations

The following KPIs are visualized:

- **Hires by Technology**
- **Hires by Year**
- **Hires by Seniority**
- **Hires by Country** (USA, Brazil, Colombia, Ecuador)
- **Hires by Experience Range**
- **Hire Rate (%)**
- **Average Scores** (Code Challenge & Technical Interview)

Visualizations are created using **Seaborn** and **Matplotlib**.

---

## Technologies Used

- **Python** – Data processing and visualization
- **Pandas** – Data manipulation
- **SQLAlchemy & pymysql** – MySQL Data Warehouse connection
- **Seaborn & Matplotlib** – KPI visualizations

