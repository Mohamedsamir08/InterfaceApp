import streamlit as st
import pandas as pd
import numpy as np

# Streamlit page configuration (must be first)
st.set_page_config(page_title="CRM Dashboard", layout="wide")

# Set a custom background image using CSS with a local path
st.markdown("""
    <style>
        body {
            background-image: url("Savola.png");
            background-size: cover;
            background-position: center center;
            background-attachment: fixed;
        }
    </style>
""", unsafe_allow_html=True)

# Sample customer data (you can replace this with your own database or API call)
def generate_data():
    segments = ['Health-Conscious', 'Price-Sensitive', 'Premium']
    cities = ['Cairo', 'Alexandria', 'Giza', 'Sharm El Sheikh', 'Luxor', 'Aswan', 'Port Said', 'Tanta', 'Mansoura']
    customer_data = pd.DataFrame({
        'Customer ID': range(1, 11),
        'Phone Number': ['01551919999', '01009677798', '01118682321', '01222185558', '01554321987', 
                         '01198765432', '01098765432', '01239876543', '01551687432', '01123344556'],
        'Customer Name': ['Mohamed Samir', 'Ahmed Ibrahim', 'Abdallah', 'DR/ Mohamed Adel Kamel', 'David Williams', 
                          'Emily Davis', 'Frank Miller', 'Grace Lee', 'Hannah Scott', 'Isaac Green'],
        'Email Address': ['Mohamed.Samir0893@gmail.com', 'Ahmed.Ibrahim@yahoo.com', 'Mohamed.Adel.Kamel@hotmail.com', 'charlie@outlook.com', 'david@aol.com',
                          'emily.davis@gmail.com', 'frank.miller@yahoo.com', 'gracelee@mail.com', 'hannah_scott@gmail.com', 'isaac.green@outlook.com'],
        'Age': [31, 33, 28, 45, 50, 29, 40, 25, 32, 38],
        'City': ['Cairo', 'Giza', 'Giza', 'Alexandria', 'Luxor', 'Aswan', 'Port Said', 'Alexandria', 'Mansoura', 'Cairo'],
        'Order Value': [250, 500, 800, 2000, 350, 450, 200, 600, 300, 700],
        'Segment': ['Price-Sensitive', 'Price-Sensitive', 'Price-Sensitive', 'Premium', 'Price-Sensitive', 
                    'Premium', 'Health-Conscious', 'Price-Sensitive', 'Premium', 'Health-Conscious'],
        'Purchase Frequency (Months)': [6, 3, 12, 1, 9, 12, 7, 5, 11, 8],
        'CLV (EGP)': [1500, 2400, 2000, 20000, 1200, 5000, 1500, 900, 4500, 3000]
    })
    return customer_data

# Initial customer data
customer_data = generate_data()

# Add custom CSS for better aesthetics
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            color: #4CAF50;
            font-weight: bold;
            text-align: center;
            margin-top: 50px;
        }
        .section {
            padding: 20px;
            border-radius: 10px;
            background-color: #f9f9f9;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }
        .card {
            display: flex;
            flex-direction: column;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 15px;
            margin-bottom: 15px;
        }
        .card h3 {
            color: #4CAF50;
        }
        .btn {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
            margin-top: 20px;
            transition: background-color 0.3s ease;
        }
        .btn:hover {
            background-color: #45a049;
        }
        .alert {
            font-size: 18px;
            color: #d9534f;
            background-color: #f2dede;
            padding: 15px;
            border-radius: 5px;
        }
        .info {
            font-size: 18px;
            color: #5bc0de;
            background-color: #d9edf7;
            padding: 15px;
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("CRM Dashboard")
page = st.sidebar.radio("Choose a report", ["Customer Information"])

# 1. Customer Information Query
if page == "Customer Information":
    st.markdown("<h1 class='title'>Customer Information</h1>", unsafe_allow_html=True)
    
    # Phone Number input
    phone_number = st.text_input("Enter Customer Phone Number:", value="", max_chars=11, placeholder="Enter a phone number (e.g., 01001112222)")
    
    if phone_number:
        customer_found = customer_data[customer_data['Phone Number'] == phone_number]
        
        if not customer_found.empty:
            st.markdown("<div class='section'>", unsafe_allow_html=True)
            st.write(f"### Customer Found:")
            st.write(f"**Name**: {customer_found.iloc[0]['Customer Name']}")
            st.write(f"**Email**: {customer_found.iloc[0]['Email Address']}")
            st.write(f"**Age**: {customer_found.iloc[0]['Age']}")
            st.write(f"**City**: {customer_found.iloc[0]['City']}")
            st.write(f"**Total Orders Value**: {customer_found.iloc[0]['Order Value']} EGP")
            st.write(f"**Segment**: {customer_found.iloc[0]['Segment']}")
            st.write(f"**Purchase Frequency (Months)**: {customer_found.iloc[0]['Purchase Frequency (Months)']}")
            st.write(f"**CLV (EGP)**: {customer_found.iloc[0]['CLV (EGP)']}")
            st.markdown("</div>", unsafe_allow_html=True)

            # Get customer segment and order value
            segment = customer_found.iloc[0]['Segment']
            order_value = customer_found.iloc[0]['Order Value']
            
            # Check if the customer is price-sensitive or premium and apply tailored offer
            if segment == 'Price-Sensitive' or segment == 'Premium':
                # Tailored offer message based on Order Value
                if order_value < 500:
                    offer_message = "Offer: Buy 1 Get 1 Free on selected items! Great for saving more. Offer valid for the next 7 days!"
                elif 500 <= order_value < 1000:
                    offer_message = "Offer: Get 10% off on your next order! Valid with a minimum spend of 500 EGP. Customer also avail of bundle discounts!"
                elif order_value > 1999:
                    offer_message = "Exclusive Offer: Enjoy 20% off + a FREE gift on your next order"
                else:
                    offer_message = "Exclusive Offer: Enjoy 10% off + a FREE gift on your next order"
                
                # Show the offer message to the Sales Representative
                st.markdown(f"<div class='info'>{offer_message}</div>", unsafe_allow_html=True)
            
        else:
            st.markdown("<div class='alert'>Customer not found. Please add the customer's details.</div>", unsafe_allow_html=True)
            
            # Fields for adding new customer data if phone number doesn't exist
            with st.form(key="add_customer_form"):
                name = st.text_input("Customer Name")
                email = st.text_input("Email Address")
                age = st.number_input("Age", min_value=18, max_value=100)
                city = st.selectbox("City", customer_data['City'].unique())
                order_value = st.number_input("Order Value (EGP)", min_value=0)

                submit_button = st.form_submit_button("Add Customer")
                
                if submit_button:
                    # Add the new customer to the dataset
                    new_customer = pd.DataFrame({
                        'Phone Number': [phone_number],
                        'Customer Name': [name],
                        'Email Address': [email],
                        'Age': [age],
                        'City': [city],
                        'Order Value': [order_value],
                        'Segment': ['Unknown'],  # Segment can be calculated based on criteria
                        'Purchase Frequency (Months)': [1],  # A default frequency until more data is gathered
                        'CLV (EGP)': [order_value * 12]  # Dummy CLV calculation
                    })
                    customer_data = pd.concat([customer_data, new_customer], ignore_index=True)
                    st.success(f"Customer {name} has been added successfully!")
                    
    else:
        st.info("Enter a phone number to retrieve customer data.")
