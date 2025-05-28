import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Master 2 Grade Calculator",
    page_icon="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn2.iconfinder.com%2Fdata%2Ficons%2Fcurrency-32%2F55%2Fcurrency-18-4096.png&f=1&nofb=1&ipt=925920844e55526262ccb6bc80b9f2cecfa279d58f8d79f576f16b989b686d43",
    layout="wide"
)

# --- CSS Styling ---
st.markdown("""
    <style>
    /* General Styles */
    .main-title {
        font-size: 2.5rem;
        color: #FFCDAC; /* Defaulting to Finance title color */
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
        background-color: #ff812f; /* Orange */
        color: white;
    }
    .finance-section .subject-header {
        color: #FFCDAC; /* Light Orange/Peach */
    }
    .finance-section .s2-header-color, .finance-section .subject-header.s2-header-color {
        color: #E6BEA3; /* Darker Peach for S2 Finance */
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
        background-color: #848CCF; /* Purple */
        color: white;
    }
    .accounting-section .subject-header {
        color: #848CCF; /* Purple */
    }
    .accounting-section .s2-header-color, .accounting-section .subject-header.s2-header-color {
        color: #848CCF; /* Same Purple for S2 Accounting */
    }
    .accounting-corner-gif {
        position: fixed;
        top: 100px;
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

    /* Contrôle de gestion Section Styles */
    .cdg-section .stButton > button {
        width: 100%;
        background-color: #4FD1C5; /* Teal/Green */
        color: white;
    }
    .cdg-section .subject-header {
        color: #4FD1C5; /* Teal/Green */
    }
    .cdg-section .s2-header-color, .cdg-section .subject-header.s2-header-color {
        color: #4FD1C5; /* Same Teal/Green for S2 CDG */
    }
    
    /* Monie, Finance et Banque Section Styles */
    .mfb-section .stButton > button {
        width: 100%;
        background-color: #4A90E2; /* Blue */
        color: white;
    }
    .mfb-section .subject-header {
        color: #4A90E2; /* Blue */
    }
    .mfb-section .s2-header-color, .mfb-section .subject-header.s2-header-color {
        color: #4A90E2; /* Same Blue for S2 MFB */
    }

    /* Management Section Styles */
    .management-section .stButton > button {
        width: 100%;
        background-color: #38A169; /* Vibrant Green */
        color: white;
    }
    .management-section .subject-header {
        color: #38A169; /* Vibrant Green */
    }
    .management-section .s2-header-color, .management-section .subject-header.s2-header-color {
        color: #38A169; /* Same Vibrant Green for S2 Management */
    }
    /* No specific GIF for CDG, MFB, or Management for now to avoid clutter */

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
cdg_s1_subjects = {
    "Management des coûts": 3, "Marché des capitaux et évaluation des actifs financiers": 3,
    "Droit des sociétés": 1.5, "Techniques bancaires": 3, "Comptabilité financière approfondie": 3,
    "Analyse des processus d'affaires": 1.5, "Contrôle de gestion": 3, "Management des opérations": 3,
    "Stratégie d'entreprise": 3, "Audit et systèmes de contrôle": 1.5,
    "Systèmes d'information de gestion": 3, "Management de la chaine de valeur": 1.5
}
cdg_s2_subjects = {
    "Comptabilité publique 1": 3, "Animation et contrôle budgétaire": 3, "Stage": 3,
    "Comptabilité des sociétés": 3, "Initiation à la méthodologie": 1.5, "Economie managériale": 3,
    "Analyse et conception des systèmes d'information": 3,
    "Diagnostic d'entreprise par l'approche de la qualité totale": 1.5, "Techniques de sondage": 3,
    "Mesures de performance": 1.5, "Tableau de bord": 1.5, "Droit pénal des affaires": 3
}
mfb_s1_subjects = {
    "Théorie financière": 3, "Séries temporelle": 3, "Technique bancaires": 3,
    "Macroéconomie profonde": 3, "Management des opérations": 3, "Economie des intermédiaires financiers": 3,
    "Stratégie d'entreprise": 3, "Marché des capitaux et évaluation des actifs financiers": 3,
    "Systèmes d'information de gestion": 3, "contrôle de gestion": 3
}
mfb_s2_subjects = {
    "Gestion de portefeuille": 3, "Droit pénal des affaires": 3, "Stage": 3,
    "Évaluation des projets d'investissement": 3, "Economie monétaire": 3,
    "Analyse et conception des systèmes d'information": 3, "modèles aléatoires": 3,
    "Economie managériale": 3, "droit des banques, assurance, boursier": 3,
    "finance islamique": 1.5, "Initiation méthodologie": 1.5
}

# Management Subjects
management_s1_subjects = {
    "Théorie de la décision et des jeux": 3,
    "Finances publiques": 1.5,
    "Culture d'entreprise": 1.5,
    "Gouvernance d'entreprise": 3,
    "Management public": 3,
    "Stratégie d'entreprise": 3,
    "Systèmes d'information de gestion": 3,
    "Organisation de l'entreprise": 3,
    "Management des ressources humaines": 3,
    "Management des opérations": 3,
    "contrôle de gestion": 3
}
management_s2_subjects = {
    "techniques de sondage": 3,
    "Animation et contrôle budgétaire": 3,
    "Tableaux de bord et de mesures de la performance": 3,
    "Stage": 3,
    "théories de la concurrence": 3,
    "Communication d'entreprise": 3,
    "Droit pénal des affaires": 3,
    "Management de changement": 3,
    "Comptabilité publique": 1.5,
    "Analyse et conception des systèmes d'information": 3,
    "Initiation à la méthodologie": 1.5
}

# --- Session State Initialization ---
all_subjects_config = {
    "FIN_S1": finance_s1_subjects, "FIN_S2": finance_s2_subjects,
    "ACC_S1": accounting_s1_subjects, "ACC_S2": accounting_s2_subjects,
    "CDG_S1": cdg_s1_subjects, "CDG_S2": cdg_s2_subjects,
    "MFB_S1": mfb_s1_subjects, "MFB_S2": mfb_s2_subjects,
    "MGT_S1": management_s1_subjects, "MGT_S2": management_s2_subjects # Added Management
}

for config_key_prefix, subjects_dict in all_subjects_config.items():
    for subject in subjects_dict:
        # Use replace to handle potential spaces or special chars in subject names for keys
        subject_key_part = subject.replace(" ", "_").replace("'", "").replace("é", "e").replace("è", "e").replace("à", "a").lower()
        exam_key = f"{config_key_prefix}_{subject_key_part}_exam"
        td_key = f"{config_key_prefix}_{subject_key_part}_TD"
        if exam_key not in st.session_state:
            st.session_state[exam_key] = None
        if td_key not in st.session_state:
            st.session_state[td_key] = None

# --- Calculation Function ---
def calculate_semester_average(semester_num_char, subjects_with_coef, session_state_key_prefix):
    subjects_data = {}
    valid_input = True
    
    for subject, coef in subjects_with_coef.items():
        subject_key_part = subject.replace(" ", "_").replace("'", "").replace("é", "e").replace("è", "e").replace("à", "a").lower()
        exam_key = f"{session_state_key_prefix}{subject_key_part}_exam"
        td_key = f"{session_state_key_prefix}{subject_key_part}_TD"
        try:
            exam_grade = st.session_state.get(exam_key)
            td_grade = st.session_state.get(td_key)
            
            exam_grade = float(exam_grade if exam_grade is not None and str(exam_grade).strip() != "" else 0.0)
            td_grade = float(td_grade if td_grade is not None and str(td_grade).strip() != "" else 0.0)

            if not (0 <= exam_grade <= 20 and 0 <= td_grade <= 20):
                st.error(f"Les notes pour '{subject}' doivent être entre 0 et 20.")
                valid_input = False
            
            subjects_data[subject] = {"exam": exam_grade, "td": td_grade, "coef": coef}

        except ValueError:
            st.error(f"Entrée invalide pour '{subject}'. Veuillez saisir uniquement des nombres.")
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
    
    color = "#FF0000" # Default Red (Fail)
    if semester_average >= 15: color = "#D89CF6"  # Purple
    elif semester_average >= 14: color = "#12CAD6"  # Teal
    elif semester_average >= 12: color = "#50D890"  # Green
    elif semester_average >= 10: color = "#FE9801"  # Orange
    
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
    title_semester_num = semester_id_str[-1]
    header_class = "subject-header"
    h2_additional_class = ""

    if is_s2_tab:
        h2_additional_class = "s2-header-color"
        header_class += " s2-header-color"
        st.markdown(f"<h2 style='text-align: center;' class='{h2_additional_class}'>Semestre {title_semester_num}</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 style='text-align: center;'>Semestre {title_semester_num}</h2>", unsafe_allow_html=True)

    session_state_key_prefix_for_subject = f"{spec_key_prefix}_{semester_id_str}_"

    for subject, coef in subjects_dict.items():
        st.markdown(f'<div class="{header_class}">{subject} (Coef: {coef})</div>', unsafe_allow_html=True)
        
        col_exam, col_td = st.columns(2)
        subject_key_part = subject.replace(" ", "_").replace("'", "").replace("é", "e").replace("è", "e").replace("à", "a").lower()
        exam_key_full = f"{session_state_key_prefix_for_subject}{subject_key_part}_exam"
        td_key_full = f"{session_state_key_prefix_for_subject}{subject_key_part}_TD"

        with col_exam:
            st.number_input("Note Examen", key=exam_key_full, min_value=0.0, max_value=20.0, value=st.session_state.get(exam_key_full), step=0.05, format="%.2f", help="Note de l'examen (0-20)")
        with col_td:
            st.number_input("Note TD", key=td_key_full, min_value=0.0, max_value=20.0, value=st.session_state.get(td_key_full), step=0.05, format="%.2f", help="Note de TD (0-20)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    button_key = f"calculate_avg_{spec_key_prefix}_{semester_id_str}"
    button_text = f"Calculer la Moyenne S{title_semester_num}"
    
    if spec_key_prefix == "FIN": # Finance button has specific centering
        _, col_btn, _ = st.columns([1, 1.5, 1])
        with col_btn:
            if st.button(button_text, key=button_key):
                calculate_semester_average(title_semester_num, subjects_dict, session_state_key_prefix_for_subject)
    else: # Other branches' buttons take full width within their column
        if st.button(button_text, key=button_key):
            calculate_semester_average(title_semester_num, subjects_dict, session_state_key_prefix_for_subject)

# --- Main Application Tabs ---
main_app_tabs = st.tabs(["Finance d'entreprise", "Comptabilité et finance", "Contrôle de gestion", "Monie, Finance et Banque", "Management"])

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

with main_app_tabs[2]: # Contrôle de gestion
    st.markdown('<div class="cdg-section">', unsafe_allow_html=True)
    
    _ , col_cdg_tabs_content, _ = st.columns([0.2, 2.6, 0.2])
    with col_cdg_tabs_content:
        cdg_semester_sub_tabs = st.tabs(["Semestre 1", "Semestre 2"])
        with cdg_semester_sub_tabs[0]:
            display_semester_subjects_ui(cdg_s1_subjects, "S1", "CDG", is_s2_tab=False)
        with cdg_semester_sub_tabs[1]:
            display_semester_subjects_ui(cdg_s2_subjects, "S2", "CDG", is_s2_tab=True)
    st.markdown('</div>', unsafe_allow_html=True)

with main_app_tabs[3]: # Monie, Finance et Banque
    st.markdown('<div class="mfb-section">', unsafe_allow_html=True)
    
    _ , col_mfb_tabs_content, _ = st.columns([0.2, 2.6, 0.2])
    with col_mfb_tabs_content:
        mfb_semester_sub_tabs = st.tabs(["Semestre 1", "Semestre 2"])
        with mfb_semester_sub_tabs[0]:
            display_semester_subjects_ui(mfb_s1_subjects, "S1", "MFB", is_s2_tab=False)
        with mfb_semester_sub_tabs[1]:
            display_semester_subjects_ui(mfb_s2_subjects, "S2", "MFB", is_s2_tab=True)
    st.markdown('</div>', unsafe_allow_html=True)

with main_app_tabs[4]: # Management
    st.markdown('<div class="management-section">', unsafe_allow_html=True)
    
    _ , col_management_tabs_content, _ = st.columns([0.2, 2.6, 0.2]) # Consistent layout for sub-tabs
    with col_management_tabs_content:
        management_semester_sub_tabs = st.tabs(["Semestre 1", "Semestre 2"])
        with management_semester_sub_tabs[0]:
            display_semester_subjects_ui(management_s1_subjects, "S1", "MGT", is_s2_tab=False)
        with management_semester_sub_tabs[1]:
            display_semester_subjects_ui(management_s2_subjects, "S2", "MGT", is_s2_tab=True)
    st.markdown('</div>', unsafe_allow_html=True)


# --- Footer ---
st.markdown("""
<div style="text-align: center; margin-top: 50px; padding: 20px; background-color: #0e1118; border-radius: 10px;">
    <p style="color: #dcdcdc; margin: 0;">© 2025 Master 2 Grade Calculator | Created by Sofiane Belkacem Nacer</p>
</div>
""", unsafe_allow_html=True)
