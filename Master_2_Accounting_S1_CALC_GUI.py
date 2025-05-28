import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Grade Calculator",
    page_icon="https://cdn-icons-png.flaticon.com/512/2909/2909988.png",
    layout="wide",
    initial_sidebar_state="expanded" # Keep sidebar open by default on desktop
)

# --- CSS Styling ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

    :root {
        --font-family: 'Poppins', sans-serif;
        
        --finance-color: #FF8C00;        /* DarkOrange */
        --accounting-color: #6A5ACD;     /* SlateBlue */
        --cdg-color: #20B2AA;            /* LightSeaGreen */
        --mfb-color: #4682B4;            /* SteelBlue */
        --management-color: #32CD32;     /* LimeGreen */
        --marketing-color: #FF69B4;       /* HotPink */

        --text-light: #F0F0F0;
        --text-medium: #C0C0C0;
        --bg-main: #121218; 
        --bg-content: #1E1E2A; 
        --bg-accent: #2C2C3E;  
        --border-color: #3A3A5A;
        --shadow-color: rgba(0, 0, 0, 0.25);
        --glow-color-primary: #ffffff; /* For the main glow */
        --glow-color-secondary: #d89cf6; /* Accent glow color - from your example */
    }

    body {
        font-family: var(--font-family);
        background-color: var(--bg-main);
        color: var(--text-light);
        line-height: 1.6;
    }

    /* Main Title Styling - Glowing Text Effect */
    .title-area-container {
        text-align: center;
        margin-top: 2rem;
        margin-bottom: 2.5rem;
    }
    .interactive-main-title {
        font-size: 3rem; /* Increased size */
        font-weight: 700;
        color: var(--glow-color-primary); /* Base color for the text */
        text-shadow: 
            0 0 6px var(--glow-color-primary),   /* Innermost, brightest glow */
            0 0 12px var(--glow-color-secondary), /* Middle accent glow */
            0 0 20px var(--glow-color-secondary); /* Outer, softer accent glow */
        text-align: center;
        margin-bottom: 0.4rem;
        letter-spacing: 1.5px; /* Slightly more spacing */
        font-family: var(--font-family);
        display: inline-block; /* Helps with text-shadow rendering in some cases */
    }

    /* Credit Subtitle - Subtle Pulse Effect */
    @keyframes pulseTextColor {
        0% { color: var(--text-medium); opacity: 0.8; }
        50% { color: var(--text-light); opacity: 1; }
        100% { color: var(--text-medium); opacity: 0.8; }
    }
    .credit-subtitle {
        font-size: 1rem;
        font-weight: 400;
        margin-top: 0.3rem;
        display: inline-block;
        animation: pulseTextColor 4s ease-in-out infinite;
    }
    
    /* Sidebar Styling for Branch Selection */
    [data-testid="stSidebar"] {
        background-color: var(--bg-content);
        padding: 1.5rem 1rem;
        border-right: 1px solid var(--border-color); /* Add a subtle border */
    }
    .sidebar-header { /* Custom header for the selectbox */
        color: var(--text-light) !important;
        font-weight: 600 !important;
        font-size: 1.2rem !important; /* More prominent */
        margin-bottom: 1rem !important;
        text-align: left;
        padding-left: 0.2rem;
    }
    [data-testid="stSidebar"] .stSelectbox > label { /* Hide default label */
        display: none;
    }
    [data-testid="stSidebar"] div[data-baseweb="select"] > div { 
        background-color: var(--bg-accent) !important;
        border: 1px solid var(--border-color) !important;
        border-radius: 8px !important; /* More rounded */
        color: var(--text-light) !important;
        font-size: 1rem;
    }
    [data-testid="stSidebar"] div[data-baseweb="select"] svg { 
        fill: var(--text-light) !important;
    }

    /* SEMESTER Tab Styling */
    .semester-tabs-container .stTabs [data-baseweb="tab-list"] {
        background-color: var(--bg-accent);
        padding: 0.4rem;
        border-radius: 8px;
        display: flex;
        justify-content: center;
        margin-top: 1rem; 
        margin-bottom: 1.5rem; /* Increased margin */
    }
    .semester-tabs-container .stTabs [role="tab"] {
        font-family: var(--font-family);
        font-size: 1rem;
        font-weight: 500;
        color: var(--text-medium);
        background-color: transparent;
        border: none;
        padding: 0.7rem 1.3rem;
        margin: 0 0.3rem;
        border-radius: 6px;
        transition: background-color 0.3s ease, color 0.3s ease;
    }
    .semester-tabs-container .stTabs [role="tab"]:hover {
        color: var(--text-light);
        background-color: #3e3e5a; 
    }
    .finance-active-sem-tabs .stTabs [role="tab"][aria-selected="true"] { background-color: var(--finance-color); color: white !important; }
    .accounting-active-sem-tabs .stTabs [role="tab"][aria-selected="true"] { background-color: var(--accounting-color); color: white !important; }
    .cdg-active-sem-tabs .stTabs [role="tab"][aria-selected="true"] { background-color: var(--cdg-color); color: white !important; }
    .mfb-active-sem-tabs .stTabs [role="tab"][aria-selected="true"] { background-color: var(--mfb-color); color: white !important; }
    .management-active-sem-tabs .stTabs [role="tab"][aria-selected="true"] { background-color: var(--management-color); color: white !important; }
    .marketing-active-sem-tabs .stTabs [role="tab"][aria-selected="true"] { background-color: var(--marketing-color); color: white !important; }


    /* Subject Header */
    .subject-header {
        font-size: 1.15rem; 
        font-weight: 500;
        padding: 0.8rem 0 0.6rem 0;
        border-bottom: 1px solid; 
        margin-top: 1.8rem; 
        margin-bottom: 1.2rem;
    }
    
    div[data-testid="stNumberInput"] input {
        border-radius: 6px;
        border: 1px solid var(--border-color);
        background-color: var(--bg-accent);
        color: var(--text-light);
        padding: 0.5rem 0.75rem;
    }
    div[data-testid="stNumberInput"] label {
        font-weight: 400;
        color: var(--text-medium);
        margin-bottom: 0.3rem;
        display: block;
    }

    /* Button Styling */
    .stButton > button {
        width: 100%; 
        color: white !important;
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        font-size: 1.05rem;
        font-weight: 500;
        border: none;
        cursor: pointer;
        transition: background-color 0.2s ease, transform 0.15s ease, box-shadow 0.2s ease;
        box-shadow: 0 3px 6px var(--shadow-color);
        margin-top: 1.5rem;
    }
    .stButton > button:hover {
        opacity: 0.9;
        box-shadow: 0 5px 10px var(--shadow-color);
        transform: translateY(-2px);
    }
    .stButton > button:active {
        transform: translateY(0px);
        box-shadow: 0 2px 4px var(--shadow-color);
    }

    /* Result Box Styling */
    .modern-result-box-container { 
        display: flex;
        justify-content: center;
        width: 100%;
        margin-top: 2.8rem;
        margin-bottom: 2rem;
    }
    .modern-result-box {
        padding: 1.8rem 2.2rem;
        border-radius: 12px;
        background-color: var(--bg-content);
        border: 1px solid var(--border-color);
        width: auto; 
        min-width: 340px; 
        max-width: 480px; 
        text-align: center; 
        box-shadow: 0 6px 18px var(--shadow-color);
    }
    .modern-result-box .result-header {
        color: var(--text-light);
        font-size: 1.4rem;
        margin-bottom: 1.2rem;
        font-weight: 500;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 0.8rem;
    }
    .modern-result-box .result-text {
        font-size: 1.3rem; 
        color: var(--text-light);
        margin: 1rem 0 0 0;
    }
    .modern-result-box .result-text strong {
        font-weight: 600; 
    }

    /* Semester Title */
    .semester-title {
        text-align: center;
        font-size: 1.8rem; 
        font-weight: 600; 
        margin-top: 1.5rem; 
        margin-bottom: 2rem;
    }
    
    /* Footer Styling */
    .modern-footer {
        text-align: center;
        margin-top: 5rem; 
        padding: 2rem;
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
    <div class="title-area-container">
        <h1 class="interactive-main-title">Master 2<br>Grade Calculator</h1>
        <p class="credit-subtitle">By Sofiane Belkacem Nacer</p>
    </div>
    """, unsafe_allow_html=True)


BRANCH_COLORS = {
    "FIN": "var(--finance-color)", "ACC": "var(--accounting-color)", "CDG": "var(--cdg-color)",
    "MFB": "var(--mfb-color)", "MGT": "var(--management-color)", "MKT": "var(--marketing-color)",
}
BRANCH_ACTIVE_SEM_TAB_CLASSES = {
    "FIN": "finance-active-sem-tabs", "ACC": "accounting-active-sem-tabs", "CDG": "cdg-active-sem-tabs",
    "MFB": "mfb-active-sem-tabs", "MGT": "management-active-sem-tabs", "MKT": "marketing-active-sem-tabs",
}

# --- Subject Definitions (Capitalized) ---
def capitalize_module_name(name): # Function from previous step, unchanged
    words = []
    for word_idx, word in enumerate(name.split(' ')):
        if word.lower() in ["de", "la", "des", "et", "à", "l", "d"] and word_idx > 0:
             if words and words[-1][-1] != "'": 
                words.append(word.lower())
             else: 
                words.append(word)
        elif "'" in word: 
            parts = word.split("'")
            words.append(parts[0].lower() + "'" + parts[1].capitalize())
        else:
            words.append(word.capitalize())
    return " ".join(words)

finance_s1_subjects = {capitalize_module_name(k): v for k, v in {
    "Théorie de la Décision et des Jeux": 3, "Stratégie d'Entreprise": 3, "Théorie Financière": 3,
    "Marchés des Capitaux": 3, "Comptabilité Approfondie": 3, "PMO": 3, "Séries Temporelles": 3,
    "Systèmes d'Information": 3, "Contrôle de Gestion": 3, "Technique Bancaires": 3
}.items()}
finance_s2_subjects = {capitalize_module_name(k): v for k, v in {
    "Économie de l'information": 1.5, "Stage": 3, "Droit pénal des affaires": 3, "Économie managériale": 3,
    "Initiation à la méthodologie": 1.5, "Économie monétaire": 3, "Gestion de portefeuille": 3,
    "Évaluation des projets d'investissement": 3, "Analyse et conception de systèmes d'information": 3,
    "Convexité et optimisation": 3, "Modèles stochastiques": 3
}.items()}
accounting_s1_subjects = {capitalize_module_name(k): v for k, v in {
    "Marche Des Capitaux": 3, "Comptabilite Approfondie": 3, "Management Des Couts": 3,
    "Control De Gestion": 3, "Technique Bancaire": 3, "PMO": 3, "Planification Financiere": 3,
    "Strategie D'entreprise": 3, "Systeme d'Information de Gestion": 3, "Droit": 1.5, "Finance Publique": 1.5
}.items()}
accounting_s2_subjects = {capitalize_module_name(k): v for k, v in {
    "Droit pénal des affaires": 3, "ACSI": 3, "Audit comptable et financier": 3, "Économie managériale": 3,
    "Animation et contrôle budgétaire": 3, "Comptabilité des sociétés": 3, "Comptabilité publique 1": 3,
    "Stage": 3, "Méthodologie": 1.5, "Finance d'entreprise approfondie": 3, "Comptabilité des instruments financiers": 1.5
}.items()}
cdg_s1_subjects = {capitalize_module_name(k): v for k, v in {
    "Management des coûts": 3, "Marché des capitaux et évaluation des actifs financiers": 3,
    "Droit des sociétés": 1.5, "Techniques bancaires": 3, "Comptabilité financière approfondie": 3,
    "Analyse des processus d'affaires": 1.5, "Contrôle de gestion": 3, "Management des opérations": 3,
    "Stratégie d'entreprise": 3, "Audit et systèmes de contrôle": 1.5,
    "Systèmes d'information de gestion": 3, "Management de la chaine de valeur": 1.5
}.items()}
cdg_s2_subjects = {capitalize_module_name(k): v for k, v in {
    "Comptabilité publique 1": 3, "Animation et contrôle budgétaire": 3, "Stage": 3,
    "Comptabilité des sociétés": 3, "Initiation à la méthodologie": 1.5, "Economie managériale": 3,
    "Analyse et conception des systèmes d'information": 3,
    "Diagnostic d'entreprise par l'approche de la qualité totale": 1.5, "Techniques de sondage": 3,
    "Mesures de performance": 1.5, "Tableau de bord": 1.5, "Droit pénal des affaires": 3
}.items()}
mfb_s1_subjects = {capitalize_module_name(k): v for k, v in {
    "Théorie financière": 3, "Séries temporelle": 3, "Technique bancaires": 3,
    "Macroéconomie profonde": 3, "Management des opérations": 3, "Economie des intermédiaires financiers": 3,
    "Stratégie d'entreprise": 3, "Marché des capitaux et évaluation des actifs financiers": 3,
    "Systèmes d'information de gestion": 3, "contrôle de gestion": 3
}.items()}
mfb_s2_subjects = {capitalize_module_name(k): v for k, v in {
    "Gestion de portefeuille": 3, "Droit pénal des affaires": 3, "Stage": 3,
    "Évaluation des projets d'investissement": 3, "Economie monétaire": 3,
    "Analyse et conception des systèmes d'information": 3, "modèles aléatoires": 3,
    "Economie managériale": 3, "droit des banques, assurance, boursier": 3,
    "finance islamique": 1.5, "Initiation méthodologie": 1.5
}.items()}
management_s1_subjects = {capitalize_module_name(k): v for k, v in {
    "Théorie de la décision et des jeux": 3, "Finances publiques": 1.5, "Culture d'entreprise": 1.5,
    "Gouvernance d'entreprise": 3, "Management public": 3, "Stratégie d'entreprise": 3,
    "Systèmes d'information de gestion": 3, "Organisation de l'entreprise": 3,
    "Management des ressources humaines": 3, "Management des opérations": 3, "contrôle de gestion": 3
}.items()}
management_s2_subjects = {capitalize_module_name(k): v for k, v in {
    "techniques de sondage": 3, "Animation et contrôle budgétaire": 3,
    "Tableaux de bord et de mesures de la performance": 3, "Stage": 3, "théories de la concurrence": 3,
    "Communication d'entreprise": 3, "Droit pénal des affaires": 3, "Management de changement": 3,
    "Comptabilité publique": 1.5, "Analyse et conception des systèmes d'information": 3,
    "Initiation à la méthodologie": 1.5
}.items()}
marketing_s1_subjects = {capitalize_module_name(k): v for k, v in {
    "Marketing des services": 3, "Contrôle de gestion": 3, "Stratégie d'entreprise": 3,
    "Management des opérations": 3, "Système d'informations de gestion": 3,
    "Gestion des systèmes de la distribution": 3, "Marketing stratégique": 3,
    "Etudes et recherches marketing 1": 3, "Comportement du consommateur": 3,
    "Politique de communication": 3
}.items()}
marketing_s2_subjects = {capitalize_module_name(k): v for k, v in {
    "Introduction à l'e-commerce": 1.5, "Etudes et recherches marketing 2": 3,
    "Economie managériale": 3, "Initiation à la méthodologie": 1.5, "Techniques publicitaires": 3,
    "Droit pénal des affaires": 3, "techniques de sondage": 3, "Stage": 3,
    "Analyse et conception de systèmes d'information": 3, "Marketing international": 3,
    "Marketing produit et gestion de la marque": 3
}.items()}

# --- Session State Initialization ---
all_subjects_config = {
    "FIN_S1": finance_s1_subjects, "FIN_S2": finance_s2_subjects,
    "ACC_S1": accounting_s1_subjects, "ACC_S2": accounting_s2_subjects,
    "CDG_S1": cdg_s1_subjects, "CDG_S2": cdg_s2_subjects,
    "MFB_S1": mfb_s1_subjects, "MFB_S2": mfb_s2_subjects,
    "MGT_S1": management_s1_subjects, "MGT_S2": management_s2_subjects,
    "MKT_S1": marketing_s1_subjects, "MKT_S2": marketing_s2_subjects
}

def normalize_key_part(text): # Function from previous step, unchanged
    text_lower = text.lower()
    return text_lower.replace(" ", "_").replace("'", "").replace("-", "_").replace("é", "e").replace("è", "e").replace("ê", "e").replace("à", "a").replace("ç", "c").replace("ô", "o").replace("û", "u")

for config_key_prefix, subjects_dict in all_subjects_config.items():
    for subject_display_name in subjects_dict: 
        subject_key_part = normalize_key_part(subject_display_name) 
        exam_key = f"{config_key_prefix}_{subject_key_part}_exam"
        td_key = f"{config_key_prefix}_{subject_key_part}_TD"
        if exam_key not in st.session_state: st.session_state[exam_key] = None
        if td_key not in st.session_state: st.session_state[td_key] = None

# --- Calculation Function (unchanged from previous step) ---
def calculate_semester_average(semester_num_char, subjects_with_coef, session_state_key_prefix):
    subjects_data = {}
    valid_input = True
    for subject_display_name, coef in subjects_with_coef.items():
        subject_key_part = normalize_key_part(subject_display_name)
        exam_key = f"{session_state_key_prefix}{subject_key_part}_exam"
        td_key = f"{session_state_key_prefix}{subject_key_part}_TD"
        try:
            exam_grade = st.session_state.get(exam_key)
            td_grade = st.session_state.get(td_key)
            exam_grade = float(exam_grade if exam_grade is not None and str(exam_grade).strip() != "" else 0.0)
            td_grade = float(td_grade if td_grade is not None and str(td_grade).strip() != "" else 0.0)
            if not (0 <= exam_grade <= 20 and 0 <= td_grade <= 20):
                st.error(f"Les notes pour '{subject_display_name}' doivent être entre 0 et 20.")
                valid_input = False
            subjects_data[subject_display_name] = {"exam": exam_grade, "td": td_grade, "coef": coef}
        except ValueError:
            st.error(f"Entrée invalide pour '{subject_display_name}'. Veuillez saisir uniquement des nombres.")
            valid_input = False
            subjects_data[subject_display_name] = {"exam": 0.0, "td": 0.0, "coef": coef} 
    if not valid_input: return
    total_weighted_sum = 0
    total_credits = sum(subjects_with_coef.values())
    if total_credits == 0:
        st.error("Total des crédits est zéro. Impossible de calculer la moyenne.")
        return
    for subject_name_loop, data in subjects_data.items():
        average = (data["exam"] * 0.67) + (data["td"] * 0.33)
        total_weighted_sum += average * data["coef"]
    semester_average = total_weighted_sum / total_credits if total_credits else 0
    formatted_avg = "{:.2f}".format(semester_average)
    avg_color_hex = "#FF0000" 
    if semester_average >= 15: avg_color_hex = "#D89CF6"  
    elif semester_average >= 14: avg_color_hex = "#12CAD6"  
    elif semester_average >= 12: avg_color_hex = "#50D890"  
    elif semester_average >= 10: avg_color_hex = "#FE9801"  
    st.markdown(f"""
        <div class="modern-result-box-container">
            <div class="modern-result-box">
                <h3 class="result-header">Résultats</h3>
                <p class="result-text"> Moyenne S{semester_num_char}: <strong style="color: {avg_color_hex}">{formatted_avg}</strong></p>
            </div>
        </div>""", unsafe_allow_html=True)

# --- UI Function to Display Semester Subjects ---
def display_semester_subjects_ui(subjects_dict, semester_id_str, spec_key_prefix):
    title_semester_num = semester_id_str[-1]
    branch_color_var = BRANCH_COLORS.get(spec_key_prefix, "var(--text-light)")
    
    st.markdown(f"<h2 class='semester-title' style='color: {branch_color_var};'>{semester_id_str.replace('S', 'Semestre ')}</h2>", unsafe_allow_html=True)
    session_state_key_prefix_for_widgets = f"{spec_key_prefix}_{semester_id_str}_"
    
    for subject_display_name, coef in subjects_dict.items():
        border_color_css = f"color: {branch_color_var}; border-bottom-color: {branch_color_var.replace(')', ', 0.4)').replace('var(', 'rgba(') if 'var(' in branch_color_var else f'{branch_color_var}66'};"
        st.markdown(f'<div class="subject-header" style="{border_color_css}">{subject_display_name} (Coef: {coef})</div>', unsafe_allow_html=True)
        col_exam, col_td = st.columns(2)
        subject_key_part = normalize_key_part(subject_display_name)
        exam_key_full = f"{session_state_key_prefix_for_widgets}{subject_key_part}_exam"
        td_key_full = f"{session_state_key_prefix_for_widgets}{subject_key_part}_TD"
        with col_exam:
            st.number_input("Note Examen", key=exam_key_full, min_value=0.0, max_value=20.0, value=st.session_state.get(exam_key_full), step=0.05, format="%.2f")
        with col_td:
            st.number_input("Note TD", key=td_key_full, min_value=0.0, max_value=20.0, value=st.session_state.get(td_key_full), step=0.05, format="%.2f")
    st.markdown("<br>", unsafe_allow_html=True) 
    
    _, btn_col, _ = st.columns([0.8, 1.4, 0.8]) # Adjusted button column width slightly for centering
    with btn_col:
        # Apply dynamic button color
        button_style_html = f"""
            <style>
                #{st.session_state.get(f'button_container_id_{spec_key_prefix}_{semester_id_str}', 'none')} .stButton > button {{
                    background-color: {branch_color_var} !important;
                }}
            </style>
        """
        # To make this specific style injection work for each button uniquely, we need a unique ID for its container
        # Streamlit doesn't allow setting IDs on st.button directly. We can wrap it in a container.
        # However, a simpler approach might be to just let the general button styling apply if dynamic color
        # per button becomes too complex with this structure.
        # For now, this injected style might apply too broadly or not specifically enough.
        # A better way is to add a class to the button's PARENT container if possible, or use more specific CSS.
        # Let's try with a more general approach: if the dynamic styling via parent class on semester-tabs-container
        # is sufficient, or live with one button color if not.
        # For this iteration, the CSS for buttons per section is removed, relying on a general style or later dynamic class.
        # The below st.markdown(button_style_html) is commented out as it's hard to target specific buttons.
        # st.markdown(button_style_html, unsafe_allow_html=True)


        button_key = f"calculate_avg_{spec_key_prefix}_{semester_id_str}"
        button_text = f"Calculer Moyenne S{title_semester_num}"

        # General button style with specific color applied via a parent class on the section
        # We need to add a class to the button's container or the main section div.
        # For simplicity, let's define button colors directly in main CSS based on parent branch section.
        # Re-add section specific button styles in main CSS:
        # e.g., .finance-content .stButton > button { background-color: var(--finance-color); }

        if st.button(button_text, key=button_key):
            calculate_semester_average(title_semester_num, subjects_dict, session_state_key_prefix_for_widgets)


# --- Branch Configuration Data ---
branch_display_names = [
    "Finance d'entreprise", "Comptabilité et finance", "Contrôle de gestion", 
    "Monie, Finance et Banque", "Management", "Marketing"
]
branch_data_map = {
    "Finance d'entreprise": {"key_prefix": "FIN", "s1": finance_s1_subjects, "s2": finance_s2_subjects, "css_class_prefix": "finance"},
    "Comptabilité et finance": {"key_prefix": "ACC", "s1": accounting_s1_subjects, "s2": accounting_s2_subjects, "css_class_prefix": "accounting"},
    "Contrôle de gestion": {"key_prefix": "CDG", "s1": cdg_s1_subjects, "s2": cdg_s2_subjects, "css_class_prefix": "cdg"},
    "Monie, Finance et Banque": {"key_prefix": "MFB", "s1": mfb_s1_subjects, "s2": mfb_s2_subjects, "css_class_prefix": "mfb"},
    "Management": {"key_prefix": "MGT", "s1": management_s1_subjects, "s2": management_s2_subjects, "css_class_prefix": "management"},
    "Marketing": {"key_prefix": "MKT", "s1": marketing_s1_subjects, "s2": marketing_s2_subjects, "css_class_prefix": "marketing"},
}

# --- Sidebar for Branch Selection ---
with st.sidebar:
    # Use st.markdown for a styled header instead of the default selectbox label
    st.markdown("<p class='sidebar-header'>Choisir la Spécialité</p>", unsafe_allow_html=True)
    selected_branch_name = st.selectbox(
        label=".", # Dummy label, actual label is the markdown above
        options=branch_display_names,
        index=0, 
        label_visibility="collapsed" 
    )

# --- Main Content Area ---
if selected_branch_name:
    branch_config = branch_data_map[selected_branch_name]
    selected_branch_key_prefix = branch_config["key_prefix"]
    # This class will be used by CSS to style semester tabs and buttons for the selected branch
    dynamic_content_class = f"{branch_config['css_class_prefix']}-active-sem-tabs" 

    col_padding1, col_content_area, col_padding2 = st.columns([0.15, 2.7, 0.15])
    with col_content_area:
        # Apply the dynamic class to this container for styling child elements
        st.markdown(f'<div class="semester-tabs-container {dynamic_content_class}">', unsafe_allow_html=True)
        
        # Add section-specific button styling here, applied to the whole content area
        # This ensures buttons within this section get the right color.
        st.markdown(f"""
            <style>
                .{dynamic_content_class} .stButton > button {{
                    background-color: {BRANCH_COLORS[selected_branch_key_prefix]} !important;
                }}
            </style>
        """, unsafe_allow_html=True)

        semester_sub_tabs = st.tabs([f"Semestre {s}" for s in [1,2]])
        with semester_sub_tabs[0]:
            display_semester_subjects_ui(branch_config["s1"], "S1", selected_branch_key_prefix)
        with semester_sub_tabs[1]:
            display_semester_subjects_ui(branch_config["s2"], "S2", selected_branch_key_prefix)
        st.markdown('</div>', unsafe_allow_html=True) # Close semester-tabs-container

# --- Footer ---
st.markdown("""
<div class="modern-footer">
    <p>© 2025 Grade Calculator | Created by Sofiane Belkacem Nacer</p>
</div>
""", unsafe_allow_html=True)
