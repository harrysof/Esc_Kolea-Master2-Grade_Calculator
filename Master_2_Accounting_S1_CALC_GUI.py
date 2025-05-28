import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Master 2 Grade Calculator",
    page_icon="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn2.iconfinder.com%2Fdata%2Ficons%2Fcurrency-32%2F55%2Fcurrency-18-4096.png&f=1&nofb=1&ipt=925920844e55526262ccb6bc80b9f2cecfa279d58f8d79f576f16b989b686d43", # Using Finance icon
    layout="wide"
)

# --- CSS Styling ---
st.markdown("""
    <style>
    /* General Styles */
    .main-title {
        font-size: 2.5rem;
        color: #FFCDAC; /* Defaulting to Finance title color, can be made neutral */
        text-align: center;
        padding: 1.5rem 0;
        background: #0e1118;
        border-radius: 10px;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .result-box {
        padding: 1rem;
        border-radius: 5px;
        margin-top: 1rem;
        background-color: #0e1118;
        border: 1px solid #48BB78; /* Common green border */
    }
    
    /* Common subject header base style */
    .subject-header {
        font-size: 1.2rem;
        padding: 0.5rem 0;
        border-bottom: 2px solid #E2E8F0;
        margin-top: 1rem;
    }

    /* Finance d'entreprise Section Styles */
    .finance-section .stButton > button {
        width: 100%;
        background-color: #ff812f;
        color: white;
    }
    .finance-section .subject-header {
        color: #FFCDAC;
    }
    .finance-section .s2-header-color, .finance-section .subject-header.s2-header-color {
        color: #E6BEA3; /* S2 specific color for Finance */
    }
    .finance-corner-gif {
        position: fixed;
        top: 85px;
        right: 10px;
        z-index: 9999;
        width: 80px;
        height: 80px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        opacity: 0.8;
        transition: opacity 0.3s ease, transform 0.3s ease;
    }
    .finance-corner-gif:hover {
        opacity: 1;
        transform: scale(1.1);
    }

    /* Comptabilité et finance Section Styles */
    .accounting-section .stButton > button {
        width: 100%;
        background-color: #848CCF;
        color: white;
    }
    .accounting-section .subject-header {
        color: #848CCF;
    }
    .accounting-section .s2-header-color, .accounting-section .subject-header.s2-header-color {
        color: #848CCF; /* S2 specific color for Accounting (same as its primary) */
    }
    .accounting-corner-gif {
        position: fixed;
        top: 100px; /* Different top position for accounting GIF */
        right: 10px;
        z-index: 9999;
        width: 80px;
        height: 80px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        opacity: 0.8;
        transition: opacity 0.3s ease, transform 0.3s ease;
    }
    .accounting-corner-gif:hover {
        opacity: 1;
        transform: scale(1.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- Main Title ---
st.markdown("""
    <div class="main-title">
        Master 2<br>Grade Calculator<br>
        <span style="font-size: 1.2rem; color: #dcdcdc;">By Sofiane Belkacem Nacer</span>
    </div>
    """, unsafe_allow_html=True)

# --- GIFs HTML ---
finance_gif_html = """
    <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fbestanimations.com%2FAnimals%2FMammals%2FCats%2Fcats%2Fcute-kitty-animated-gif-61.gif&f=1&nofb=1&ipt=9b9f49feca4c1a8d04b816cebb11048d1cba7254539b845380dd510c43cb5d4e" class="finance-corner-gif" alt="Finance GIF">
"""
accounting_gif_html = """
    <img src="https://media3.giphy.com/media/njON3jEmTYHEfRbfsk/200w.gif?cid=6c09b95286r0q4sdyv82fj0t6vx4gmmec7lipefp8jihytoe&ep=v1_stickers_search&rid=200w.gif&ct=s" class="accounting-corner-gif" alt="Accounting GIF">
"""

# --- Subject Definitions ---
finance_s1_subjects = {
    "Théorie de la Décision et des Jeux": 3, "Stratégie d'Entreprise": 3, "Théorie Financière": 3,
    "Marchés des Capitaux": 3, "Comptabilité Approfondie": 3, "PMO": 3, "Séries Temporelles": 3,
    "Systèmes d'Information": 3, "Contrôle de Gestion": 3, "Technique Bancaires": 3
}
finance_s2_subjects = {
    "Économie de l'information": 1.5, "Stage": 3, "Droit pénal des affaires": 3, "Économie managériale": 3,
    "Initiation à la méthodologie": 1.5, "Économie monétaire": 3, "Gestion de portefeuille": 3,
    "Évaluation des projets d'investissement": 3, "Analyse et conception de systèmes d'information": 3,
    "Convexité et optimisation": 3, "Modèles stochastiques": 3
}
accounting_s1_subjects = {
    "Marche Des Capitaux": 3, "Comptabilite Approfondie": 3, "Management Des Couts": 3,
    "Control De Gestion": 3, "Technique Bancaire": 3, "PMO": 3, "Planification Financiere": 3,
    "Strategie D'entreprise": 3, "Systeme d'Information de Gestion": 3, "Droit": 1.5, "Finance Publique": 1.5
}
accounting_s2_subjects = {
    "Droit pénal des affaires": 3, "ACSI": 3, "Audit comptable et financier": 3, "Économie managériale": 3,
    "Animation et contrôle budgétaire": 3, "Comptabilité des sociétés": 3, "Comptabilité publique 1": 3,
    "Stage": 3, "Méthodologie": 1.5, "Finance d'entreprise approfondie": 3, "Comptabilité des instruments financiers": 1.5
}

# --- Session State Initialization ---
all_subjects_config = {
    "FIN_S1": finance_s1_subjects, "FIN_S2": finance_s2_subjects,
    "ACC_S1": accounting_s1_subjects, "ACC_S2": accounting_s2_subjects
}

for config_key_prefix, subjects_dict in all_subjects_config.items(): # Changed config_key to config_key_prefix for clarity
    for subject in subjects_dict:
        # Construct keys like "FIN_S1_SubjectName_exam" or "ACC_S2_SubjectName_TD"
        exam_key = f"{config_key_prefix}_{subject}_exam"
        td_key = f"{config_key_prefix}_{subject}_TD"
        if exam_key not in st.session_state:
            st.session_state[exam_key] = None
        if td_key not in st.session_state:
            st.session_state[td_key] = None

# --- Calculation Function ---
def calculate_semester_average(semester_num_char, subjects_with_coef, session_state_key_prefix):
    subjects_data = {}
    valid_input = True
    
    for subject, coef in subjects_with_coef.items():
        exam_key = f"{session_state_key_prefix}{subject}_exam" # Corrected to use full prefix
        td_key = f"{session_state_key_prefix}{subject}_TD"     # Corrected to use full prefix
        try:
            exam_grade = st.session_state.get(exam_key)
            td_grade = st.session_state.get(td_key)
            
            exam_grade = float(exam_grade if exam_grade is not None and str(exam_grade).strip() != "" else 0.0)
            td_grade = float(td_grade if td_grade is not None and str(td_grade).strip() != "" else 0.0)

            if not (0 <= exam_grade <= 20 and 0 <= td_grade <= 20):
                st.error(f"Les notes pour {subject} doivent être entre 0 et 20.")
                valid_input = False
            
            subjects_data[subject] = {"exam": exam_grade, "td": td_grade, "coef": coef}

        except ValueError:
            st.error(f"Entrée invalide pour {subject}. Veuillez saisir uniquement des nombres.")
            valid_input = False
            subjects_data[subject] = {"exam": 0.0, "td": 0.0, "coef": coef} 

    if not valid_input:
        return

    total_weighted_sum = 0
    total_credits = sum(subjects_with_coef.values())
    
    if total_credits == 0:
        st.error("Total des crédits est zéro. Impossible de calculer la moyenne.")
        return

    for subject, data in subjects_data.items():
        average = (data["exam"] * 0.67) + (data["td"] * 0.33)
        total_weighted_sum += average * data["coef"]

    semester_average = total_weighted_sum / total_credits if total_credits else 0
    formatted_avg = "{:.2f}".format(semester_average)
    formatted_total_weighted_sum = "{:.2f}".format(total_weighted_sum)
    
    color = "#FF0000"
    if semester_average >= 15: color = "#D89CF6"
    elif semester_average >= 14: color = "#12CAD6"
    elif semester_average >= 12: color = "#50D890"
    elif semester_average >= 10: color = "#FE9801"
    
    st.markdown(f"""
        <div class="result-box">
            <h3 style="color: #2F855A; margin: 0;">📊 Résultats</h3>
            <p style="font-size: 1.2rem; margin: 0.5rem 0;">
                Moyenne S{semester_num_char}: <strong style="color: {color}">{formatted_avg}</strong><br>
                Total pondéré: <strong style="color: {color};">{formatted_total_weighted_sum}</strong>
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- UI Function to Display Semester Subjects ---
def display_semester_subjects_ui(subjects_dict, semester_id_str, spec_key_prefix, is_s2_tab=False):
    # semester_id_str is "S1" or "S2"
    # spec_key_prefix is "FIN" or "ACC"
    
    title_semester_num = semester_id_str[-1] # "1" or "2"
    header_class = "subject-header"
    h2_additional_class = "" # Renamed variable

    if is_s2_tab:
        h2_additional_class = "s2-header-color" # This class is defined per-section in CSS
        header_class += " s2-header-color" # Appends to existing class string
        st.markdown(f"<h2 style='text-align: center;' class='{h2_additional_class}'>Semestre {title_semester_num}</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 style='text-align: center;'>Semestre {title_semester_num}</h2>", unsafe_allow_html=True)

    session_state_key_prefix_for_subject = f"{spec_key_prefix}_{semester_id_str}_" # e.g., "FIN_S1_"

    for subject, coef in subjects_dict.items():
        st.markdown(f'<div class="{header_class}">{subject} (Coef: {coef})</div>', unsafe_allow_html=True)
        
        col_exam, col_td = st.columns(2)
        # Full key for session state access and widget uniqueness
        exam_key_full = f"{session_state_key_prefix_for_subject}{subject}_exam"
        td_key_full = f"{session_state_key_prefix_for_subject}{subject}_TD"

        with col_exam:
            st.number_input("Note Examen", key=exam_key_full, min_value=0.0, max_value=20.0, value=st.session_state.get(exam_key_full), step=0.05, format="%.2f", help="Note de l'examen (0-20)")
        with col_td:
            st.number_input("Note TD", key=td_key_full, min_value=0.0, max_value=20.0, value=st.session_state.get(td_key_full), step=0.05, format="%.2f", help="Note de TD (0-20)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    button_key = f"calculate_avg_{spec_key_prefix}_{semester_id_str}"
    button_text = f"Calculer la Moyenne S{title_semester_num}"
    
    if spec_key_prefix == "FIN":
        _, col_btn, _ = st.columns([1, 1.5, 1])
        with col_btn:
            if st.button(button_text, key=button_key):
                calculate_semester_average(title_semester_num, subjects_dict, session_state_key_prefix_for_subject)
    else:
        if st.button(button_text, key=button_key):
            calculate_semester_average(title_semester_num, subjects_dict, session_state_key_prefix_for_subject)

# --- Main Application Tabs ---
main_app_tabs = st.tabs(["Finance d'entreprise", "Comptabilité et finance"])

with main_app_tabs[0]: # Finance d'entreprise
    st.markdown('<div class="finance-section">', unsafe_allow_html=True)
    st.markdown(finance_gif_html, unsafe_allow_html=True)
    
    _ , col_finance_tabs_content, _ = st.columns([0.2, 2.6, 0.2])
    with col_finance_tabs_content:
        finance_semester_sub_tabs = st.tabs(["Semestre 1", "Semestre 2"])
        with finance_semester_sub_tabs[0]:
            display_semester_subjects_ui(finance_s1_subjects, "S1", "FIN", is_s2_tab=False)
        with finance_semester_sub_tabs[1]:
            display_semester_subjects_ui(finance_s2_subjects, "S2", "FIN", is_s2_tab=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

with main_app_tabs[1]: # Comptabilité et finance
    st.markdown('<div class="accounting-section">', unsafe_allow_html=True)
    st.markdown(accounting_gif_html, unsafe_allow_html=True)

    _ , col_accounting_tabs_content, _ = st.columns([0.2, 2.6, 0.2])
    with col_accounting_tabs_content:
        accounting_semester_sub_tabs = st.tabs(["Semestre 1", "Semestre 2"])
        with accounting_semester_sub_tabs[0]:
            display_semester_subjects_ui(accounting_s1_subjects, "S1", "ACC", is_s2_tab=False)
        with accounting_semester_sub_tabs[1]:
            display_semester_subjects_ui(accounting_s2_subjects, "S2", "ACC", is_s2_tab=True)
            
    st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div style="text-align: center; margin-top: 50px; padding: 20px; background-color: #0e1118; border-radius: 10px;">
    <p style="color: #dcdcdc; margin: 0;">© 2025 Master 2 Grade Calculator | Created by Sofiane Belkacem Nacer</p>
</div>
""", unsafe_allow_html=True)
