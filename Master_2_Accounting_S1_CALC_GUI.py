import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Master 2 Grade Calculator",
    page_icon="https://cdn-icons-png.flaticon.com/512/2909/2909988.png", # A more generic calculator/education icon
    layout="wide"
)

# --- CSS Styling ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    :root {
        --font-family: 'Poppins', sans-serif;
        
        --finance-color: #FF8C00;        /* DarkOrange */
        --accounting-color: #6A5ACD;     /* SlateBlue */
        --cdg-color: #20B2AA;            /* LightSeaGreen */
        --mfb-color: #4682B4;            /* SteelBlue */
        --management-color: #32CD32;     /* LimeGreen */
        --marketing-color: #FF69B4;       /* HotPink */

        --text-light: #EAEAEA;
        --text-medium: #B0B0B0;
        --text-dark: #333333;
        --bg-main: #10101A; /* Darker main background */
        --bg-content: #1C1C2B; /* Slightly lighter for content cards */
        --bg-accent: #2A2A3D;  /* For interactive elements or highlights */
        --border-color: #383854;
        --shadow-color: rgba(0, 0, 0, 0.2);
    }

    body {
        font-family: var(--font-family);
        background-color: var(--bg-main);
        color: var(--text-light);
    }

    /* Main Title Styling */
    .modern-title-container {
        text-align: center;
        margin-bottom: 2.5rem; /* Reduced margin */
        padding: 2rem 1rem; /* Adjusted padding */
        background: linear-gradient(145deg, var(--bg-accent) 0%, var(--bg-content) 100%);
        border-radius: 12px;
        box-shadow: 0 6px 12px var(--shadow-color);
    }
    .modern-main-title {
        font-size: 2.6rem; 
        font-weight: 600; 
        color: var(--text-light);
        margin-bottom: 0.4rem;
        letter-spacing: 0.5px;
    }
    .modern-subtitle {
        font-size: 1rem;
        color: var(--text-medium);
        font-style: italic;
        font-weight: 300;
    }
    
    /* General Section Styling */
    .branch-section-content { /* Wrapper for centering semester tabs and inputs */
        padding-top: 1rem;
    }

    /* Tab Styling - General for Semester Tabs */
    .stTabs { /* Targeting Streamlit's tab component */
        border-radius: 8px;
        overflow: hidden; /* Helps with border-radius on children */
    }
    .stTabs [data-baseweb="tab-list"] {
        background-color: var(--bg-accent); /* Background for the tab bar */
        padding: 0.3rem; /* Small padding around tab buttons */
        border-radius: 8px; /* Rounded tab bar */
        display: flex;
        justify-content: center; /* Center tab buttons */
    }
    .stTabs [role="tab"] {
        font-family: var(--font-family);
        font-size: 1rem; /* Slightly smaller for semester tabs */
        font-weight: 500;
        color: var(--text-medium);
        background-color: transparent; /* Make inactive tabs blend */
        border: none; /* Remove default borders */
        padding: 0.6rem 1.2rem; /* Adjusted padding */
        margin: 0 0.2rem; /* Spacing between tabs */
        border-radius: 6px; /* Rounded individual tabs */
        transition: background-color 0.3s ease, color 0.3s ease;
    }
    .stTabs [role="tab"]:hover {
        color: var(--text-light);
        background-color: #3c3c54; /* Slightly lighter accent for hover */
    }

    /* Branch-specific active semester tab styling */
    .finance-section .stTabs [role="tab"][aria-selected="true"] { background-color: var(--finance-color); color: white !important; }
    .accounting-section .stTabs [role="tab"][aria-selected="true"] { background-color: var(--accounting-color); color: white !important; }
    .cdg-section .stTabs [role="tab"][aria-selected="true"] { background-color: var(--cdg-color); color: white !important; }
    .mfb-section .stTabs [role="tab"][aria-selected="true"] { background-color: var(--mfb-color); color: white !important; }
    .management-section .stTabs [role="tab"][aria-selected="true"] { background-color: var(--management-color); color: white !important; }
    .marketing-section .stTabs [role="tab"][aria-selected="true"] { background-color: var(--marketing-color); color: white !important; }

    /* Subject Header (within each branch) */
    .subject-header {
        font-size: 1.1rem; /* Slightly smaller */
        font-weight: 500;
        padding: 0.8rem 0 0.6rem 0; /* Adjusted padding */
        border-bottom: 1px solid var(--border-color);
        margin-top: 1.5rem; /* Increased top margin */
        margin-bottom: 1rem;
        /* Branch color is applied inline via Python */
    }
    
    /* Input fields (st.number_input) are harder to style deeply without breaking Streamlit themes. */
    /* We rely on Streamlit's base styling + branch color for headers and buttons. */
    div[data-testid="stNumberInput"] input {
        border-radius: 6px;
        border: 1px solid var(--border-color);
        background-color: var(--bg-accent);
        color: var(--text-light);
    }
    div[data-testid="stNumberInput"] label {
        font-weight: 400;
        color: var(--text-medium);
    }


    /* Button Styling */
    .stButton > button {
        width: 100%; 
        color: white !important; /* Ensure text is white */
        padding: 0.7rem 1.5rem;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: 500;
        border: none;
        cursor: pointer;
        transition: background-color 0.2s ease, transform 0.1s ease, box-shadow 0.2s ease;
        box-shadow: 0 2px 4px var(--shadow-color);
        margin-top: 1rem; /* Add some space above the button */
    }
    .stButton > button:hover {
        opacity: 0.9;
        box-shadow: 0 4px 8px var(--shadow-color);
        transform: translateY(-1px);
    }
    .stButton > button:active {
        transform: translateY(0px);
        box-shadow: 0 1px 2px var(--shadow-color);
    }
    /* Branch specific background-colors for buttons */
    .finance-section .stButton > button { background-color: var(--finance-color); }
    .accounting-section .stButton > button { background-color: var(--accounting-color); }
    .cdg-section .stButton > button { background-color: var(--cdg-color); }
    .mfb-section .stButton > button { background-color: var(--mfb-color); }
    .management-section .stButton > button { background-color: var(--management-color); }
    .marketing-section .stButton > button { background-color: var(--marketing-color); }

    /* Result Box Styling */
    .modern-result-box-container { 
        display: flex;
        justify-content: center;
        width: 100%;
        margin-top: 2.5rem;
        margin-bottom: 1.5rem;
    }
    .modern-result-box {
        padding: 1.5rem 2rem;
        border-radius: 10px;
        background-color: var(--bg-content);
        border: 1px solid var(--border-color);
        width: auto; 
        min-width: 320px; 
        max-width: 450px; 
        text-align: center; 
        box-shadow: 0 5px 15px var(--shadow-color);
    }
    .modern-result-box .result-header {
        color: var(--text-light);
        font-size: 1.3rem;
        margin-bottom: 1rem;
        font-weight: 500;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 0.75rem;
    }
    .modern-result-box .result-text {
        font-size: 1.25rem; 
        color: var(--text-light);
        margin: 0.8rem 0 0 0;
    }
    .modern-result-box .result-text strong {
        font-weight: 600; 
    }

    /* Semester Title (S1/S2) within each tab content */
    .semester-title {
        text-align: center;
        font-size: 1.6rem;
        font-weight: 500;
        margin-top: 1rem; /* Space after semester tabs */
        margin-bottom: 1.5rem;
        /* Branch color applied inline via Python */
    }
    
    /* Corner GIF Styles - Kept if still desired */
    .corner-gif {
        position: fixed;
        z-index: 9999;
        width: 70px; /* Slightly smaller */
        height: 70px;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        opacity: 0.7;
        transition: opacity 0.3s ease, transform 0.3s ease;
    }
    .finance-corner-gif { top: 75px; right: 15px; }
    .accounting-corner-gif { top: 155px; right: 15px; } /* Adjusted to not overlap */
    .corner-gif:hover {
        opacity: 1;
        transform: scale(1.05);
    }

    /* Footer Styling */
    .modern-footer {
        text-align: center;
        margin-top: 4rem;
        padding: 1.5rem;
        background-color: var(--bg-content); 
        border-top: 1px solid var(--border-color);
    }
    .modern-footer p {
        color: var(--text-medium);
        margin: 0;
        font-size: 0.9rem;
        font-weight: 300;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Main Title ---
st.markdown("""
    <div class="modern-title-container">
        <h1 class="modern-main-title">Master 2 Grade Calculator</h1>
        <p class="modern-subtitle">By Sofiane Belkacem Nacer</p>
    </div>
    """, unsafe_allow_html=True)

# --- GIFs HTML (optional, can be removed if not desired) ---
finance_gif_html = """
    <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fbestanimations.com%2FAnimals%2FMammals%2FCats%2Fcats%2Fcute-kitty-animated-gif-61.gif&f=1&nofb=1&ipt=9b9f49feca4c1a8d04b816cebb11048d1cba7254539b845380dd510c43cb5d4e" class="corner-gif finance-corner-gif" alt="Finance GIF">
"""
accounting_gif_html = """
    <img src="https://media3.giphy.com/media/njON3jEmTYHEfRbfsk/200w.gif?cid=6c09b95286r0q4sdyv82fj0t6vx4gmmec7lipefp8jihytoe&ep=v1_stickers_search&rid=200w.gif&ct=s" class="corner-gif accounting-corner-gif" alt="Accounting GIF">
"""

# Branch colors mapping (used in Python for dynamic styling)
BRANCH_COLORS = {
    "FIN": "var(--finance-color)",
    "ACC": "var(--accounting-color)",
    "CDG": "var(--cdg-color)",
    "MFB": "var(--mfb-color)",
    "MGT": "var(--management-color)",
    "MKT": "var(--marketing-color)",
}

# --- Subject Definitions (remain the same) ---
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
management_s1_subjects = {
    "Théorie de la décision et des jeux": 3, "Finances publiques": 1.5, "Culture d'entreprise": 1.5,
    "Gouvernance d'entreprise": 3, "Management public": 3, "Stratégie d'entreprise": 3,
    "Systèmes d'information de gestion": 3, "Organisation de l'entreprise": 3,
    "Management des ressources humaines": 3, "Management des opérations": 3, "contrôle de gestion": 3
}
management_s2_subjects = {
    "techniques de sondage": 3, "Animation et contrôle budgétaire": 3,
    "Tableaux de bord et de mesures de la performance": 3, "Stage": 3, "théories de la concurrence": 3,
    "Communication d'entreprise": 3, "Droit pénal des affaires": 3, "Management de changement": 3,
    "Comptabilité publique": 1.5, "Analyse et conception des systèmes d'information": 3,
    "Initiation à la méthodologie": 1.5
}
marketing_s1_subjects = {
    "Marketing des services": 3, "Contrôle de gestion": 3, "Stratégie d'entreprise": 3,
    "Management des opérations": 3, "Système d'informations de gestion": 3,
    "Gestion des systèmes de la distribution": 3, "Marketing stratégique": 3,
    "Etudes et recherches marketing 1": 3, "Comportement du consommateur": 3,
    "Politique de communication": 3
}
marketing_s2_subjects = {
    "Introduction à l'e-commerce": 1.5, "Etudes et recherches marketing 2": 3,
    "Economie managériale": 3, "Initiation à la méthodologie": 1.5, "Techniques publicitaires": 3,
    "Droit pénal des affaires": 3, "techniques de sondage": 3, "Stage": 3,
    "Analyse et conception de systèmes d'information": 3, "Marketing international": 3,
    "Marketing produit et gestion de la marque": 3
}

# --- Session State Initialization ---
all_subjects_config = {
    "FIN_S1": finance_s1_subjects, "FIN_S2": finance_s2_subjects,
    "ACC_S1": accounting_s1_subjects, "ACC_S2": accounting_s2_subjects,
    "CDG_S1": cdg_s1_subjects, "CDG_S2": cdg_s2_subjects,
    "MFB_S1": mfb_s1_subjects, "MFB_S2": mfb_s2_subjects,
    "MGT_S1": management_s1_subjects, "MGT_S2": management_s2_subjects,
    "MKT_S1": marketing_s1_subjects, "MKT_S2": marketing_s2_subjects
}

def normalize_key_part(text):
    return text.replace(" ", "_").replace("'", "").replace("-", "_").replace("é", "e").replace("è", "e").replace("ê", "e").replace("à", "a").replace("ç", "c").replace("ô", "o").replace("û", "u").lower()

for config_key_prefix, subjects_dict in all_subjects_config.items():
    for subject in subjects_dict:
        subject_key_part = normalize_key_part(subject)
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
        subject_key_part = normalize_key_part(subject)
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

    for subject_name, data in subjects_data.items():
        average = (data["exam"] * 0.67) + (data["td"] * 0.33)
        total_weighted_sum += average * data["coef"]

    semester_average = total_weighted_sum / total_credits if total_credits else 0
    formatted_avg = "{:.2f}".format(semester_average)
    
    # Determine color based on average score (same logic as before)
    avg_color_hex = "#FF0000"  # Default Red
    if semester_average >= 15: avg_color_hex = "#D89CF6"  # Purple
    elif semester_average >= 14: avg_color_hex = "#12CAD6"  # Teal
    elif semester_average >= 12: avg_color_hex = "#50D890"  # Green
    elif semester_average >= 10: avg_color_hex = "#FE9801"  # Orange
    
    # Use the new modern result box structure
    st.markdown(f"""
        <div class="modern-result-box-container">
            <div class="modern-result-box">
                <h3 class="result-header">Résultats</h3>
                <p class="result-text">
                    Moyenne S{semester_num_char}: <strong style="color: {avg_color_hex}">{formatted_avg}</strong>
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- UI Function to Display Semester Subjects ---
def display_semester_subjects_ui(subjects_dict, semester_id_str, spec_key_prefix):
    title_semester_num = semester_id_str[-1]
    branch_color = BRANCH_COLORS.get(spec_key_prefix, "var(--text-light)") # Fallback color

    # Display Semester Title (S1/S2)
    st.markdown(f"<h2 class='semester-title' style='color: {branch_color};'>Semestre {title_semester_num}</h2>", unsafe_allow_html=True)

    session_state_key_prefix_for_subject_widgets = f"{spec_key_prefix}_{semester_id_str}_"

    for subject, coef in subjects_dict.items():
        # Apply branch color to subject header dynamically
        st.markdown(f'<div class="subject-header" style="color: {branch_color}; border-bottom-color: {branch_color}40;">{subject} (Coef: {coef})</div>', unsafe_allow_html=True)
        
        col_exam, col_td = st.columns(2)
        subject_key_part = normalize_key_part(subject)
        exam_key_full = f"{session_state_key_prefix_for_subject_widgets}{subject_key_part}_exam"
        td_key_full = f"{session_state_key_prefix_for_subject_widgets}{subject_key_part}_TD"

        with col_exam:
            st.number_input("Note Examen", key=exam_key_full, min_value=0.0, max_value=20.0, value=st.session_state.get(exam_key_full), step=0.05, format="%.2f", help="Note de l'examen (0-20)")
        with col_td:
            st.number_input("Note TD", key=td_key_full, min_value=0.0, max_value=20.0, value=st.session_state.get(td_key_full), step=0.05, format="%.2f", help="Note de TD (0-20)")
    
    st.markdown("<br>", unsafe_allow_html=True) # Spacer
    
    # Centering the button using columns, within the already centered content column
    _, btn_col, _ = st.columns([1, 1.5, 1]) 
    with btn_col:
        button_key = f"calculate_avg_{spec_key_prefix}_{semester_id_str}"
        button_text = f"Calculer Moyenne S{title_semester_num}"
        if st.button(button_text, key=button_key):
            calculate_semester_average(title_semester_num, subjects_dict, session_state_key_prefix_for_subject_widgets)

# --- Main Application Tabs ---
main_app_tabs_names = [
    "Finance d'entreprise", 
    "Comptabilité et finance", 
    "Contrôle de gestion", 
    "Monie, Finance et Banque", 
    "Management",
    "Marketing"
]
main_app_tabs = st.tabs(main_app_tabs_names)

# Branch configurations
branch_configs = [
    {"name": "Finance d'entreprise", "key_prefix": "FIN", "s1": finance_s1_subjects, "s2": finance_s2_subjects, "gif": finance_gif_html, "section_class": "finance-section"},
    {"name": "Comptabilité et finance", "key_prefix": "ACC", "s1": accounting_s1_subjects, "s2": accounting_s2_subjects, "gif": accounting_gif_html, "section_class": "accounting-section"},
    {"name": "Contrôle de gestion", "key_prefix": "CDG", "s1": cdg_s1_subjects, "s2": cdg_s2_subjects, "gif": None, "section_class": "cdg-section"},
    {"name": "Monie, Finance et Banque", "key_prefix": "MFB", "s1": mfb_s1_subjects, "s2": mfb_s2_subjects, "gif": None, "section_class": "mfb-section"},
    {"name": "Management", "key_prefix": "MGT", "s1": management_s1_subjects, "s2": management_s2_subjects, "gif": None, "section_class": "management-section"},
    {"name": "Marketing", "key_prefix": "MKT", "s1": marketing_s1_subjects, "s2": marketing_s2_subjects, "gif": None, "section_class": "marketing-section"},
]

for i, tab in enumerate(main_app_tabs):
    with tab:
        branch_config = branch_configs[i]
        st.markdown(f'<div class="{branch_config["section_class"]}">', unsafe_allow_html=True)
        if branch_config["gif"]:
            st.markdown(branch_config["gif"], unsafe_allow_html=True)
        
        # Centering column for semester tabs and content
        # Adjust the ratios here if content feels too narrow or too wide
        # [padding_left, content_width, padding_right]
        col_padding1, col_content_area, col_padding2 = st.columns([0.3, 2.4, 0.3]) 

        with col_content_area:
            st.markdown('<div class="branch-section-content">', unsafe_allow_html=True) # Wrapper for top padding
            semester_sub_tabs = st.tabs(["Semestre 1", "Semestre 2"])
            with semester_sub_tabs[0]:
                display_semester_subjects_ui(branch_config["s1"], "S1", branch_config["key_prefix"])
            with semester_sub_tabs[1]:
                display_semester_subjects_ui(branch_config["s2"], "S2", branch_config["key_prefix"])
            st.markdown('</div>', unsafe_allow_html=True) # Close branch-section-content

        st.markdown('</div>', unsafe_allow_html=True) # Close section_class div

# --- Footer ---
st.markdown("""
<div class="modern-footer">
    <p>© 2025 Master 2 Grade Calculator | Created by Sofiane Belkacem Nacer</p>
</div>
""", unsafe_allow_html=True)
