CREATE TABLE DimensionTechnology (
    TechnologyID INT PRIMARY KEY,
    Technology VARCHAR(255)
);

CREATE TABLE DimensionYear (
    YearID INT PRIMARY KEY,
    ApplicationYear INT
);

CREATE TABLE DimensionSeniority (
    SeniorityID INT PRIMARY KEY,
    Seniority VARCHAR(255)
);

CREATE TABLE FactCandidates (
    HireID INT AUTO_INCREMENT PRIMARY KEY,
    CandidateID INT,
    TechnologyID INT,
    YearID INT,
    SeniorityID INT,
    CodeChallengeScore INT,
    TechnicalInterviewScore INT,
    Hired BOOLEAN,
    YOE INT,
    FOREIGN KEY (TechnologyID) REFERENCES DimensionTechnology(TechnologyID),
    FOREIGN KEY (YearID) REFERENCES DimensionYear(YearID),
    FOREIGN KEY (SeniorityID) REFERENCES DimensionSeniority(SeniorityID)
);
