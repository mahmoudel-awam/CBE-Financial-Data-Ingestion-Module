CREATE DATABASE FinGuard_DB;

CREATE TABLE Dim_ExchangeRates (
    Currency_Code VARCHAR(10) PRIMARY KEY, -- (USD, EUR, EGP) ???? ?? ??????? ???????
    Currency_Name VARCHAR(50) NOT NULL,
    Buy_Rate DECIMAL(18, 4),
    Sell_Rate DECIMAL(18, 4),
    Spread DECIMAL(18, 4),
    Extraction_Date TIMESTAMP
);

CREATE TABLE Fact_Transactions (
    Transaction_ID_SK VARCHAR(50) PRIMARY KEY,
    Customer_ID INT,
    Amount_Original DECIMAL(18, 2),
    Currency_Code_BK VARCHAR(10), 
    Amount_EGP DECIMAL(18, 2),
    Transaction_Date TIMESTAMP,
    
    CONSTRAINT FK_Currency FOREIGN KEY (Currency_Code_BK) 
    REFERENCES Dim_ExchangeRates(Currency_Code)
);
