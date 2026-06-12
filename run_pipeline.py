"""
Master Pipeline Script
Bluestock Mutual Fund Analytics Project
Author: Gaurav Rajput
"""

import os

print("=" * 60)
print("Mutual Fund Analytics Pipeline")
print("=" * 60)

print("\nRunning Data Ingestion...")
os.system("python data_ingestion.py")

print("\nRunning Live NAV Fetch...")
os.system("python live_nav_fetch.py")

print("\nRunning Fund Recommender...")
os.system("python recommender.py")

print("\nPipeline Completed Successfully!")