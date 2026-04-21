Fraud Detection Data Pipeline (Data Engineering Project)

Overview

This project builds a complete **Data Engineering pipeline** for fraud detection using real-time exchange rates from the Central Bank of Egypt (CBE).
The pipeline extracts, transforms, and loads (ETL) currency data into a Data Warehouse, which can be used later for detecting suspicious financial transactions.

---

Project Objective

To design a scalable data pipeline that:

* Collects real-world financial data
* Stores it in a structured Data Warehouse
* Enables fraud detection analysis based on currency behavior

---

Tech Stack

* **Python**: Data extraction & transformation
  (Requests, BeautifulSoup, Pandas)
* **SQL Server**: Data Warehouse design
* **Git & GitHub**: Version control
* **CSV Storage**: Intermediate data layer

---

Data Pipeline Workflow

1. **Extract**

   * Scrape exchange rates from CBE website

2. **Transform**

   * Clean data
   * Calculate spread (Sell - Buy)
   * Add extraction timestamp

3. **Load**

   * Store data in CSV
   * Insert into Data Warehouse tables

---

Data Warehouse Design

Dimension Table: `Dim_ExchangeRates`

| Column          | Description                   |
| --------------- | ----------------------------- |
| Currency_Code   | Currency identifier           |
| Currency_Name   | Currency name                 |
| Buy_Rate        | Buying price                  |
| Sell_Rate       | Selling price                 |
| Spread          | Difference between sell & buy |
| Extraction_Date | Data timestamp                |

---

Fact Table: `Fact_Transactions`

| Column           | Description                 |
| ---------------- | --------------------------- |
| Transaction_ID   | Unique transaction ID       |
| Customer_ID      | Customer identifier         |
| Amount_Original  | Original transaction amount |
| Currency_Code    | Currency used               |
| Amount_EGP       | Converted amount            |
| Transaction_Date | Date of transaction         |

---

Data Model

![Data Warehouse](docs/architecture.png)

---

Fraud Detection Use Case

This pipeline supports fraud detection by:

* Detecting abnormal transaction values based on exchange rates
* Identifying unusual currency spreads
* Monitoring suspicious currency fluctuations
* Flagging inconsistent conversions

---

Project Structure

```
fraud-detection-data-pipeline/
│
├── data/                  # Sample data files
├── scripts/               # Python scraping script
├── sql/                   # Data warehouse SQL scripts
├── docs/                  # Architecture diagrams
├── README.md
├── requirements.txt
└── .gitignore
```

---

How to Run

### 1. Clone the repository

```
git clone https://github.com/your-username/fraud-detection-data-pipeline.git
cd fraud-detection-data-pipeline
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run scraper

```
python scripts/cbe_scraper.py
```

---

Sample Output

* CSV file with exchange rates
* Clean structured data ready for DW loading

---

Future Enhancements

* Automate pipeline using **Apache Airflow**
* Real-time streaming using **Apache Kafka**
* Build ML model for fraud detection
* Create dashboard using **Power BI / Tableau**

---

Author

Mahmoud Ramdan 
Aspiring Data Engineering 
