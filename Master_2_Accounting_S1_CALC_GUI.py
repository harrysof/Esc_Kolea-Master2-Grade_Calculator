import streamlit as st
import pandas as pd

# Add custom CSS for print styling
st.markdown("""
<style>
@media print {
    .stApp {
        padding: 20px;
    }
    .css-1d391kg, .css-14xtw13 {
        display: none;
    }
    button[data-testid="baseButton-secondary"] {
        display: none;
    }
}

.print-table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}
.print-table th, .print-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}
.print-table th {
    background-color: #f8f9fa;
}
.results-section {
    margin: 20px 0;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

def create_results_table(subjects_data, semester_average, total):
    table_html = """
    <div class="results-container">
        <table class="print-table">
            <tr>
                <th>Subject</th>
                <th>Exam (67%)</th>
                <th>TD (33%)</th>
                <th>Weight</th>
                <th>Weighted Average</th>
            </tr>
    """
    
    for subject, grades in subjects_data.items():
        exam = grades["exam"]
        td = grades["td"]
        weight = 3 if subject in ["Marche Des Capitaux", "Comptabilite Approfondie", 
                                "Management Des Couts", "Control De Gestion", 
                                "Technique Bancaire", "PMO", "Planification Financiere",
                                "Strategie D'entreprise", 
                                "Systeme d'Information de Gestion"] else 1.5
        average = (exam * 0.67) + (td * 0.33)
        weighted_avg = average * weight
        
        table_html += f"""
        <tr>
            <td>{subject}</td>
            <td>{exam:.2f}</td>
            <td>{td:.2f}</td>
            <td>{weight}</td>
            <td>{weighted_avg:.2f}</td>
        </tr>
        """
    
    table_html += """
        </table>
        <div class="results-section">
            <h3>Final Results</h3>
            <p><strong>Total Points:</strong> {:.2f}</p>
            <p><strong>Semester Average:</strong> {:.2f}</p>
        </div>
    </div>
    """.format(total, semester_average)
    
    return table_html

def calculate_semester_average():
    subjects_data = {}
    for subject in subjects:
        exam_key = f"{subject}_exam"
        td_key = f"{subject}_TD"

        try:
            exam_grade = float(st.session_state.get(exam_key, 0.0) or 0.0)
            td_grade = float(st.session_state.get(td_key, 0.0) or 0.0)
            subjects_data[subject] = {"exam": exam_grade, "td": td_grade}

        except (ValueError, TypeError):
            st.error(f"Invalid input for {subject}. Please enter numbers only.")
            return None, None, None

    total = 0
    for subject, grades in subjects_data.items():
        average = (grades["exam"] * 0.67) + (grades["td"] * 0.33)
        weight = 3 if subject in ["Marche Des Capitaux", "Comptabilite Approfondie", 
                                "Management Des Couts", "Control De Gestion", 
                                "Technique Bancaire", "PMO", "Planification Financiere",
                                "Strategie D'entreprise", 
                                "Systeme d'Information de Gestion"] else 1.5
        total += average * weight

    semester_average = total / 30
    return subjects_data, semester_average, total

# Add print button JavaScript
print_button_html = """
<button onclick="window.print()" style="
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 4px;">
    Print Results
</button>
"""

# Streamlit app
st.title("Master 2 Accounting - S1 Grade Calculator ~ By Sofiane Belkacem Nacer")

subjects = [
    "Marche Des Capitaux", "Comptabilite Approfondie", "Management Des Couts",
    "Control De Gestion", "Technique Bancaire", "PMO", "Planification Financiere",
    "Strategie D'entreprise", "Systeme d'Information de Gestion", "Droit", "Finance Publique"
]

# Initialize session state
for subject in subjects:
    exam_key = f"{subject}_exam"
    td_key = f"{subject}_TD"
    if exam_key not in st.session_state:
        st.session_state[exam_key] = None
    if td_key not in st.session_state:
        st.session_state[td_key] = None

# Input fields
for subject in subjects:
    st.subheader(subject)
    col1, col2 = st.columns(2)
    with col1:
        st.number_input(
            "Exam",
            key=f"{subject}_exam",
            min_value=0.0,
            value=None,
            step=0.05,
            format="%.2f"
        )
    with col2:
        st.number_input(
            "TD",
            key=f"{subject}_TD",
            min_value=0.0,
            value=None,
            step=0.05,
            format="%.2f"
        )

if st.button("Calculate"):
    subjects_data, semester_average, total = calculate_semester_average()
    if subjects_data and semester_average and total:
        st.success(f"Semester Average: {semester_average:.2f}")
        st.success(f"Total: {total:.2f}")
        
        # Display results table
        results_table = create_results_table(subjects_data, semester_average, total)
        st.markdown(results_table, unsafe_allow_html=True)
        
        # Add print button
        st.markdown(print_button_html, unsafe_allow_html=True)
