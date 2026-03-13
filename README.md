Plant Disease Detector 🌱🩺
Introduction

The Plant Disease Detector is an AI-powered web application built using Python and Django.
It allows users to upload images of plant leaves and automatically detects disease presence, health score, and quality metrics of the plant.
This system provides a quick and accurate assessment of plant health, helping farmers, gardeners, and researchers monitor crop conditions effectively.

Key Features
Upload plant leaf images for analysis/
Detect diseases and health conditions using AI models/
View health score vs disease severity/
User-friendly web interface built with Django/
Modular and extensible for additional plant types and models/

Technologies Used
Programming Language/
Python

Backend Framework
Django 4.2.27/
AI / Machine Learning/
TensorFlow 2.13.0/
NumPy 1.22–1.25

Frontend
HTML / CSS/
Django Crispy Forms + Bootstrap 5

Libraries
django-crispy-forms==2.2.0/
crispy-bootstrap5==0.7/
django-allauth==0.59.0/
Pillow==10.0.0/
tensorflow==2.13.0/
numpy>=1.22,<1.25/

Plant Disease Detector/
│
├── ai_model/                # Trained AI model files
├── plant_detector/          # Django project settings
├── detector/                # Disease detection logic
├── media/                   # Uploaded leaf images and results
├── templates/               # HTML templates
├── static/                  # CSS / JS files
├── manage.py                # Django management script
└── README.md



