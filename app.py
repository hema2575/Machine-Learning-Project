# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 17:13:39 2021

@author: Mason
"""

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
from config import password

# NEW SHIT


Base = automap_base()

engine = create_engine("postgresql://postgres:" + password + "@localhost/diseaseML")

Base.prepare(engine, reflect = True)

Cancer = Base.classes.breast_cancer
CancerF = Base.classes.breast_cancer_full
Heart = Base.classes.heart_failure

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return (
        "Links to Data:<br/>"
        "/breast_cancer</br>"
        "/breast_cancer_full</br>"
        "/heart_failure<br/>"
        )

@app.route("/breast_cancer")
def cancerData():
    session = Session(engine)
    
    results = session.query(Cancer.sample_code_number, Cancer.clump_thickness, Cancer.uniformity_of_cell_size, 
                            Cancer.uniformity_of_cell_shape, Cancer.marginal_adhesion, 
                            Cancer.single_epithelial_cell_size, Cancer.bare_nuclei, Cancer.bland_chromatin, Cancer.normal_nucleoli, 
                            Cancer.mitoses, Cancer.status).all()
    
    session.close()
    
    data = []
    for sample_code_number, clump_thickness, uniformity_of_cell_size, uniformity_of_cell_shape, marginal_adhesion, single_epithelial_cell_size, bare_nuclei, bland_chromatin, normal_nucleoli, mitoses, status in results:
        data_dict = {}
        data_dict["sample_code_number"] = sample_code_number
        data_dict["clump_thickness"] = clump_thickness
        data_dict["uniformity_of_cell_size"] = uniformity_of_cell_size
        data_dict["uniformity_of_cell_shape"] = uniformity_of_cell_shape
        data_dict["marginal_adhesion"] = marginal_adhesion
        data_dict["single_epithelial_cell_size"] = single_epithelial_cell_size
        data_dict["bland_chromatin"] = bland_chromatin
        data_dict["normal_nucleoli"] = normal_nucleoli
        data_dict["mitoses"] = mitoses
        data_dict["status"] = status
        data.append(data_dict)
    
    return jsonify(data)

@app.route("/breast_cancer_full")
def cancerDataF():
    session = Session(engine)
    
    results = session.query(CancerF.patient_id, CancerF.diagnosis, CancerF.radius_mean, CancerF.texture_mean, CancerF.perimeter_mean, 
                            CancerF.area_mean, CancerF.smoothness_mean, CancerF.compactness_mean, CancerF.concavity_mean, 
                            CancerF.concave_points_mean, CancerF.symmetry_mean, CancerF.fractal_dimension_mean, CancerF.texture_se, 
                            CancerF.radius_se, CancerF.perimeter_se, CancerF.area_se, CancerF.smoothness_se, CancerF.compactness_se, 
                            CancerF.concavity_se, CancerF.concave_points_se, CancerF.symmetry_se, CancerF.fractal_dimension_se, 
                            CancerF.radius_worst, CancerF.texture_worst, CancerF.perimeter_worst, CancerF.area_worst, CancerF.smoothness_worst, 
                            CancerF.compactness_worst, CancerF.concavity_worst, CancerF.concave_points_worst, CancerF.symmetry_worst, 
                            CancerF.fractal_dimension_worst).all()
    
    session.close()
    
    data = []
    for patient_id, diagnosis, radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, texture_se, radius_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst in results:
        data_dict = {}
        data_dict["patient_id"] = patient_id
        data_dict["diagnosis"] = diagnosis
        data_dict["radius_mean"] = radius_mean
        data_dict["texture_mean"] = texture_mean
        data_dict["perimeter_mean"] = perimeter_mean
        data_dict["area_mean"] = area_mean
        data_dict["smoothness_mean"] = smoothness_mean
        data_dict["compactness_mean"] = compactness_mean
        data_dict["concavity_mean"] = concavity_mean
        data_dict["concave_points_mean"] = concave_points_mean
        data_dict["symmetry_mean"] = symmetry_mean
        data_dict["fractal_dimension_mean"] = fractal_dimension_mean
        data_dict["texture_se"] = texture_se
        data_dict["radius_se"] = radius_se
        data_dict["perimeter_se"] = perimeter_se
        data_dict["area_se"] = area_se
        data_dict["smoothness_se"] = smoothness_se
        data_dict["compactness_se"] = compactness_se
        data_dict["concavity_se"] = concavity_se
        data_dict["concave_points_se"] = concave_points_se
        data_dict["symmetry_se"] = symmetry_se
        data_dict["fractal_dimension_se"] = fractal_dimension_se
        data_dict["radius_worst"] = radius_worst
        data_dict["texture_worst"] = texture_worst
        data_dict["perimeter_worst"] = perimeter_worst
        data_dict["area_worst"] = area_worst
        data_dict["smoothness_worst"] = smoothness_worst
        data_dict["compactness_worst"] = compactness_worst
        data_dict["concavity_worst"] = concavity_worst
        data_dict["concave_points_worst"] = concave_points_worst
        data_dict["symmetry_worst"] = symmetry_worst
        data_dict["fractal_dimension_worst"] = fractal_dimension_worst
        data.append(data_dict)
    
    return jsonify(data)

@app.route("/heart_failure")
def heartData():
    session = Session(engine)
    
    results = session.query(Heart.age, Heart.anaemia, Heart.creatinine_phosphokinase, Heart.diabetes, Heart.ejection_fraction, 
                            Heart.high_blood_pressure, Heart.platelets, Heart.serum_creatinine, Heart.serum_sodium, Heart.sex,
                            Heart.smoking, Heart.time, Heart.DEATH_EVENT).all()
    
    session.close()
    
    data = []
    for age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time, DEATH_EVENT in results:
        data_dict = {}
        data_dict["age"] = age
        data_dict["anaemia"] = anaemia
        data_dict["creatinine_phosphokinase"] = creatinine_phosphokinase
        data_dict["diabetes"] = diabetes
        data_dict["ejection_fraction"] = ejection_fraction
        data_dict["high_blood_pressure"] = high_blood_pressure
        data_dict["platelets"] = platelets
        data_dict["serum_creatinine"] = serum_creatinine
        data_dict["serum_sodium"] = serum_sodium
        data_dict["sex"] = sex
        data_dict["smoking"] = smoking
        data_dict["time"] = time
        data_dict["DEATH_EVENT"] = DEATH_EVENT
        data.append(data_dict)
    
    return render_template('index.html', data = data)

# NEW SHIT
    
    
    """
    class heartTable(Table):
        name = Col('Name')
        description = Col('Description')
        
    class cancerRecord():
        def __init__(self, name, description):
            self.name = name
            self.description - description
    
    heart_records = session.query.Heart.all()
    table = heartTable(heart_records)
    return table.__html__()
    """
    
if __name__ == '__main__':
    app.run