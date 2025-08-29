-- =====================
-- Dimensiones
-- =====================

CREATE TABLE DimCandidate (
    CandidateID INT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Email VARCHAR(255)
);

CREATE TABLE DimTechnology (
    TechnologyID INT PRIMARY KEY,
    Technology VARCHAR(255)
);

CREATE TABLE DimYear (
    YearID INT PRIMARY KEY,
    ApplicationYear INT
);

CREATE TABLE DimSeniority (
    SeniorityID INT PRIMARY KEY,
    Seniority VARCHAR(255)
);

CREATE TABLE DimCountry (
    CountryID INT PRIMARY KEY,
    Country VARCHAR(255)
);

-- =====================
-- Tabla de hechos
-- =====================
CREATE TABLE FactHiring (
    HireID INT AUTO_INCREMENT PRIMARY KEY,
    CandidateID INT,
    TechnologyID INT,
    YearID INT,
    SeniorityID INT,
    CountryID INT,
    CodeChallengeScore INT,
    TechnicalInterviewScore INT,
    Hired BOOLEAN,

    FOREIGN KEY (CandidateID) REFERENCES DimCandidate(CandidateID),
    FOREIGN KEY (TechnologyID) REFERENCES DimTechnology(TechnologyID),
    FOREIGN KEY (YearID) REFERENCES DimYear(YearID),
    FOREIGN KEY (SeniorityID) REFERENCES DimSeniority(SeniorityID),
    FOREIGN KEY (CountryID) REFERENCES DimCountry(CountryID)
);
