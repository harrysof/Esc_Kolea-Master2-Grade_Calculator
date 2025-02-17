import streamlit as st

st.markdown("""
    <style>
    /* Overall page styling */
    .main {
        padding: 2rem;
    }
    
    /* Title styling */
    .css-10trblm {
        color: #2e4057;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        padding: 20px;
        background: linear-gradient(to right, #4a90e2, #2e4057);
        color: white;
        border-radius: 10px;
    }
    
    /* Subject headers styling */
    .css-1outpf7 {
        color: #4a90e2;
        font-size: 22px;
        padding: 15px 0;
        margin-top: 20px;
        border-bottom: 2px solid #4a90e2;
    }
    
    /* Input fields styling */
    .stNumberInput input {
        border-radius: 8px;
        border: 2px solid #4a90e2;
        padding: 8px;
        transition: all 0.3s ease;
    }
    
    .stNumberInput input:focus {
        border-color: #2e4057;
        box-shadow: 0 0 5px rgba(74, 144, 226, 0.5);
    }
    
    /* Calculate button styling */
    .stButton button {
        background-color: #4a90e2;
        color: white;
        padding: 12px 30px;
        border-radius: 8px;
        border: none;
        width: 250px;
        margin: 30px auto;
        display: block;
        font-size: 18px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        background-color: #2e4057;
        transform: translateY(-2px);
    }
    
    /* Success message styling */
    .stSuccess {
        background-color: #28a745;
        padding: 20px;
        border-radius: 8px;
        color: white;
        text-align: center;
        margin: 15px 0;
        font-size: 18px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Error message styling */
    .stError {
        background-color: #dc3545;
        padding: 20px;
        border-radius: 8px;
        color: white;
        text-align: center;
        margin: 15px 0;
        font-size: 18px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Subject container styling */
    .subject-container {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

for subject in [
    "Marche Des Capitaux", "Comptabilite Approfondie", "Management Des Couts",
    "Control De Gestion", "Technique Bancaire", "PMO", "Planification Financiere",
    "Strategie D'entreprise", "Systeme d'Information de Gestion", "Droit", "Finance Publique"
]:
    exam_key = f"{subject}_exam"
    td_key = f"{subject}_TD"
    if exam_key not in st.session_state:
        st.session_state[exam_key] = None
    if td_key not in st.session_state:
        st.session_state[td_key] = None

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
            return

    total = 0
    for subject, grades in subjects_data.items():
        average = (grades["exam"] * 0.67) + (grades["td"] * 0.33)
        weight = 3 if subject in ["Marche Des Capitaux", "Comptabilite Approfondie", "Management Des Couts",
                                 "Control De Gestion", "Technique Bancaire", "PMO", "Planification Financiere",
                                 "Strategie D'entreprise", "Systeme d'Information de Gestion"] else 1.5
        total += average * weight

    semester_average = total / 30
    formatted_float = "{:.2f}".format(semester_average)
    better_total = "{:.2f}".format(total)

    st.success(f"Moyenne Semestrielle Estimée: {formatted_float}")
    st.success(f"Total: {better_total}")

# Streamlit app
st.title("Master 2 Accounting - S1 Grade Calculator ~ By Sofiane Belkacem Nacer")

subjects = [
    "Marche Des Capitaux", "Comptabilite Approfondie", "Management Des Couts",
    "Control De Gestion", "Technique Bancaire", "PMO", "Planification Financiere",
    "Strategie D'entreprise", "Systeme d'Information de Gestion", "Droit", "Finance Publique"
]


col1, col2 = st.columns(2)

for i, subject in enumerate(subjects):
    with col1 if i % 2 == 0 else col2:
        st.markdown(f"""
            <div class="subject-container">
                <h3>{subject}</h3>
            </div>
        """, unsafe_allow_html=True)
        
        st.number_input(
            "Exam",
            key=f"{subject}_exam",
            min_value=0.0,
            value=None,
            step=0.05,
            format="%.2f"
        )
        
        st.number_input(
            "TD",
            key=f"{subject}_TD",
            min_value=0.0,
            value=None,
            step=0.05,
            format="%.2f"
        )

if st.button("Calculate Average"):
    calculate_semester_average()

