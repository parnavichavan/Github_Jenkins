Jenkins ETL Pipeline Demo
This project demonstrates a simple ETL (Extract–Transform–Load) pipeline using Python and Jenkins.
The pipeline extracts sample data, transforms it, and loads it into a SQLite database—all automated through a Jenkins Pipeline.

📌 Pipeline Flow
Extract → Transform → Load

🛠️ Technologies Used

Python
Jenkins Pipeline
GitHub
Pandas
SQLite


📁 Project Structure
jenkins-etl-demo/
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── data/
│   (generated during pipeline execution)
│
├── requirements.txt
└── Jenkinsfile


🔄 ETL Steps
Step 1 – Extract

Generates sample user data.
Saves the data to:
data/input.csv

Step 2 – Transform

Reads input.csv and adds a new column:
age_after_10_years = age + 10
Outputs the transformed file:
data/transformed.csv

Step 3 – Load

Reads transformed.csv
Loads data into a SQLite database:
data/users.db
Creates a table named users


⚙️ Jenkins Pipeline
The Jenkinsfile automates the full ETL workflow with these stages:

Install Dependencies
Extract Data
Transform Data
Load Data

These steps are executed automatically when the pipeline runs.

🚀 How to Run the Project

Push the project code to a GitHub repository.
Open Jenkins → Create New Item.
Choose Pipeline as the job type.
Set Pipeline script from SCM.
Select Git as the SCM option.
Add your GitHub repository URL.
Set the script path to:
Jenkinsfile
Save → Click Build Now.


✅ Outcome
After a successful run, Jenkins will generate:

data/input.csv
data/transformed.csv
data/users.db
