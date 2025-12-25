


import pandas as pd
import numpy as np

class FraudPreprocessor:
    """
    Main class to handle data cleaning and feature engineering 
    for the Athena Fraud Detection Engine.
    """
    
    def __init__(self):
        pass

    def categorize_device(self, device_info):
        """
        Simplifies the 'DeviceInfo' string into categories (Mobile, Desktop, Other).
        Example: 'Samsung SM-G9600' -> 'Mobile'
        """
        if pd.isna(device_info):
            return "Unknown"
        
        device_str = str(device_info).lower()
        
        if any(x in device_str for x in ['windows', 'mac', 'linux', 'desktop']):
            return "Desktop"
        elif any(x in device_str for x in ['ios', 'android', 'samsung', 'pixel', 'iphone']):
            return "Mobile"
        else:
            return "Other"

    def parse_email_domain(self, email):
        """
        Extracts the domain provider from email.
        Example: 'user@gmail.com' -> 'gmail'
        """
        if pd.isna(email):
            return "Missing"
        
        try:
            return email.split('@')[1].split('.')[0]
        except:
            return "Invalid"

    def run_pipeline(self, transaction_data):
        """
        Wrapper to run all cleaning steps on a single transaction dictionary.
        Returns a clean dictionary ready for the model.
        """
        # Create a copy to avoid editing original data
        clean_data = transaction_data.copy()
        
        # 1. Device Clean
        clean_data['DeviceType'] = self.categorize_device(clean_data.get('DeviceInfo'))
        
        # 2. Email Clean
        clean_data['EmailDomain'] = self.parse_email_domain(clean_data.get('P_emaildomain'))
        
        return clean_data
