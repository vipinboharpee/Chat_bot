import sqlite3
import re
import streamlit as st
from datetime import datetime

# Streamlit page configuration
st.set_page_config(page_title="Chat Assistant", layout="centered")

# Custom CSS for better UI
def set_custom_style():
    st.markdown(
        """
        <style>
            .stTextInput>div>div>input {
                font-size: 16px !important;
                padding: 10px !important;
                border-radius: 10px !important;
                border: 1px solid #ccc !important;
            }
            .stButton>button {
                background-color: #007BFF !important;
                color: white !important;
                font-size: 16px !important;
                padding: 10px 20px !important;
                border-radius: 10px !important;
                border: none !important;
            }
            .stButton>button:hover {
                background-color: #0056b3 !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

set_custom_style()

# Function to execute database queries
def execute_query(query, params=()):
    with sqlite3.connect("chat_assistant.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

# Extract department from query
def extract_department(query):
    match = re.search(r"in the (\w+) department", query, re.IGNORECASE)
    return match.group(1) if match else None

# Extract date from query
def extract_date(query):
    match = re.search(r"after (\d{4}-\d{2}-\d{2})", query)
    return match.group(1) if match else None

# Validate date format
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Function to process the query
def process_query(query):
    if not query:
        return "No query provided."

    if "Show me all employees in the" in query:
        department = extract_department(query)
        if not department:
            return "Please specify a valid department name."
        
        sql_query = "SELECT Name FROM Employees WHERE Department = ?"
        result = execute_query(sql_query, (department,))
        
        return f"**Employees in {department}:**\n- " + "\n- ".join([row[0] for row in result]) if result else f"No employees found in {department}."

    elif "Who is the manager of the" in query:
        department = extract_department(query)
        if not department:
            return "Please specify a valid department name."

        sql_query = "SELECT Manager FROM Departments WHERE Name = ?"
        result = execute_query(sql_query, (department,))
        
        return f"**The manager of {department} is:** {result[0][0]}" if result else "No department found with this name."

    elif "List all employees hired after" in query:
        date = extract_date(query)
        if not date or not is_valid_date(date):
            return "Invalid date format. Please use YYYY-MM-DD."

        sql_query = "SELECT Name FROM Employees WHERE Hire_Date > ?"
        result = execute_query(sql_query, (date,))
        
        return f"**Employees hired after {date}:**\n- " + "\n- ".join([row[0] for row in result]) if result else "No employees hired after this date."

    elif "Show the highest-paid employee" in query:
        sql_query = "SELECT Name, Salary, Department FROM Employees ORDER BY Salary DESC LIMIT 1"
        result = execute_query(sql_query)
        
        return f"💰 **The highest-paid employee is:** {result[0][0]} from {result[0][2]} with a salary of **${result[0][1]:,.2f}**." if result else "No employee data available."

    elif "What is the total salary expense for the" in query:
        department = extract_department(query)
        if not department:
            return "Please specify a valid department name."

        sql_query = "SELECT SUM(Salary) FROM Employees WHERE Department = ?"
        result = execute_query(sql_query, (department,))
        
        return f"💰 **Total salary expense for {department}:** **${result[0][0]:,.2f}**" if result and result[0][0] else f"No salary data found for {department} department."
    
    else:
        return "❌ Sorry, I couldn't understand the query. Please try again."

# Streamlit UI
st.markdown("# 🤖 Employee Chat Assistant")
st.markdown("### Ask me about employees, departments, managers, and salaries!")

# User input
query = st.text_input("🔍 Enter your query:", placeholder="e.g., Show me all employees in the HR department")

# Process query when the user enters text
if st.button("Get Answer"):
    if query:
        response = process_query(query)
        st.markdown(f"📢 **Response:**\n{response}")
    else:
        st.warning("Please enter a query!")


        