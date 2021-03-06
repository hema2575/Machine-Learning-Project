# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
import pandas
from config import password

engine = create_engine("postgresql://postgres:" + password + "@localhost/diseaseML")

cancer_df = pandas.read_csv("../data/BC_1_unique.csv", header = 0) # BC_1_unique has been cleaned of duplicate sample_code_number
cancer_df_full = pandas.read_csv("../data/wisconsin_diagnostic.csv", header = 0)
heart_df = pandas.read_csv("../data/heart_failure_clinical_records_dataset.csv", header = 0)

print(cancer_df)
print(cancer_df_full)
print(heart_df)

cancer_df.to_sql("breast_cancer", con = engine, if_exists = "replace", index = False)
engine.execute("ALTER TABLE breast_cancer ADD PRIMARY KEY (sample_code_number);")
print("breast_cancer table updated!")       

cancer_df_full.to_sql("breast_cancer_full", con = engine, if_exists = "replace")
engine.execute("ALTER TABLE breast_cancer_full ADD PRIMARY KEY (patient_id);")
print("breast_cancer_full table updated!")

heart_df.to_sql("heart_failure", con = engine, if_exists = "replace")
engine.execute("ALTER TABLE heart_failure ADD PRIMARY KEY (INDEX);")
print("heart_failure table updated!")