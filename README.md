Chat Assistant with SQLite
Overview
This is a simple yet powerful chat assistant that interacts with an SQLite database to answer user queries related to employees and departments. It is built using Streamlit and provides structured, real-time responses based on user input.

👨‍💻 Developed by: Vipin Boharpee

🚀 Features
✅ Accepts natural language queries
✅ Converts user input into SQL queries dynamically
✅ Fetches real-time data from an SQLite database
✅ Provides structured and interactive responses
✅ Implements error handling for incorrect inputs
✅ Modern Streamlit UI for a seamless experience

🗂 Database Schema
The assistant uses an SQLite database with the following tables:

Employees Table
ID	Name	Department	Salary	Hire_Date
1	Alice	Sales	50,000	2021-01-15
2	Bob	Engineering	70,000	2020-06-10
3	Charlie	Marketing	60,000	2022-03-20
Departments Table
ID	Name	Manager
1	Sales	Alice
2	Engineering	Bob
3	Marketing	Charlie
🛠 Supported Queries
The assistant supports various employee-related queries, including:

✅ "Show me all employees in the [department] department."
✅ "Who is the manager of the [department] department?"
✅ "List all employees hired after [date]."
✅ "What is the total salary expense for the [department] department?"

📦 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/vipinboharpee/Chat_bot.git
cd chat_assistant
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Streamlit Application
bash
Copy
Edit
streamlit run chat_assistant.py
🔒 Security Improvements
✔️ Uses parameterized queries to prevent SQL injection
✔️ Implements input validation to handle incorrect department names and invalid dates

🏗 Code Quality Improvements
🔹 Refactored chat_assistant.py to improve modularity
🔹 Improved error handling for unexpected inputs
🔹 Added comments and docstrings for better readability

🎨 User Experience Enhancements
🖥️ Provides clearer error messages
🎨 Uses a modern Streamlit UI for an enhanced chat experience
📊 Implements logging to track API usage and errors

🚀 Deployment
This project is deployed on Streamlit Cloud. You can access it at: 👉 https://chatbot-8viln4vplouqw6oeeegciv.streamlit.app/

📜 Known Limitations & Future Improvements
⚠️ Currently supports only a predefined set of queries
⚡ Can be extended with advanced NLP for better query understanding
🔒 Add authentication for secure access

🔥 Maintained by: Vipin Boharpee
