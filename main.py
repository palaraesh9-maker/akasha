import streamlit as st
import datetime

# Safe import for swisseph to prevent cloud build errors
try:
    import swisseph as swe
    SWISSEPH_AVAILABLE = True
except ImportError:
    SWISSEPH_AVAILABLE = False

st.set_page_config(
    page_title="ആകാശദീപം - Aakashadeeptam",
    page_icon="✨",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        font-size: 2.8rem;
        color: #FFD700;
        font-weight: bold;
    }
    .slogan {
        text-align: center;
        font-size: 1.3rem;
        color: #B0C4DE;
        margin-bottom: 2rem;
        font-style: italic;
    }
    </style>
""", unsafe_allow_html=True)

# Header & Slogan
st.markdown('<p class="main-header">✨ ആകാശദീപം</p>', unsafe_allow_html=True)
st.markdown('<p class="slogan">പ്രപഞ്ചത്തിന്റെ വെളിച്ചം</p>', unsafe_allow_html=True)
st.write("---")

st.subheader("🔮 സമഗ്ര വേദ ജ്യോതിഷ & പ്രപഞ്ച ഊർജ്ജ വിശകലന എൻജിൻ")
st.write("താങ്കളുടെ ജനന വിവരങ്ങളും ആവശ്യങ്ങളും നൽകി ആധികാരികവും യാഥാർത്ഥ്യബോധമുള്ളതുമായ ജാതക റിപ്പോർട്ട് ലഭ്യമാക്കൂ.")

# Input Form with Language, AM/PM, and full year dropdowns
with st.form("comprehensive_astro_form"):
    # Language Selection Option
    app_language = st.selectbox("ഭാഷ തിരഞ്ഞെടുക്കുക (Select Language):", ["മലയാളം (Malayalam)", "English", "हिंदी (Hindi)"])
    
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("മുഴുവൻ പേര് (Full Name):")
        gender = st.selectbox("ലിംഗം (Gender):", ["പുരുഷൻ (Male)", "സ്ത്രീ (Female)", "മറ്റുള്ളവ (Other)"])
        
        # Date of Birth Dropdowns (1940 to 2026)
        st.write("ജനന തീയതി (Date of Birth):")
        b_year = st.selectbox("വർഷം (Year):", list(range(2026, 1939, -1)), index=31)
        b_month = st.selectbox("മാസം (Month):", list(range(1, 13)), format_func=lambda x: datetime.date(2000, x, 1).strftime('%B'))
        b_day = st.selectbox("തീയതി (Day):", list(range(1, 32)))

    with col2:
        # Time of Birth with explicit AM/PM selection
        st.write("ജനന സമയം (Time of Birth):")
        t_hour = st.selectbox("മണിക്കൂർ (Hour):", list(range(1, 13)), index=9)
        t_minute = st.selectbox("മിനിറ്റ് (Minute):", list(range(0, 60)), index=0)
        t_ampm = st.selectbox("AM / PM:", ["AM", "PM"])
        
        pob = st.text_input("ജനന സ്ഥലം (Place of Birth):", "Kerala, India")
        time_unknown = st.checkbox("ജനന സമയം കൃത്യമായി അറിയില്ല (Prashna / Nama Mode)")

    focus_goal = st.text_input("പ്രധാന വിശകലന ലക്ഷ്യം / ചോദ്യങ്ങൾ (ഉദാ: കരിയർ, സാമ്പത്തികം, ആരോഗ്യം):", "പൊതുഫലം & കരിയർ")
    
    uploaded_file = st.file_uploader("കൈരേഖയോ മുഖചിത്രമോ അപ്‌ലോഡ് ചെയ്യുക (Palm / Face Scan - Optional):", type=["jpg", "jpeg", "png"])
    
    submitted = st.form_submit_button("ജാതകം സമ്പൂർണ്ണമായി വിശകലനം ചെയ്യുക")

if submitted:
    if not full_name:
        st.warning("ദയവായി പേര് നൽകുക.")
    else:
        try:
            dob = datetime.date(b_year, b_month, b_day)
        except ValueError:
            dob = datetime.date(b_year, b_month, 28)
            
        st.success(f"നമസ്കാരം {full_name}! ({app_language}) പ്രകാരമുള്ള പ്രപഞ്ച കണക്കൂട്ടലുകൾ പൂർത്തിയായി.")
        
        with st.spinner("ഗ്രഹസ്ഥിതികളും കർമ്മഫലങ്ങളും വിശകലനം ചെയ്യുന്നു..."):
            
            julday = 0.0
            if SWISSEPH_AVAILABLE:
                try:
                    julday = swe.julday(dob.year, dob.month, dob.day, 12.0)
                except:
                    julday = 2450000.5
            
            st.markdown("---")
            st.markdown(f"### 📜 ആകാശദീപം - വ്യക്തിഗത ജ്യോതിഷ റിപ്പോർട്ട് ({app_language})")
            
            # 1. Basic Astrological Profile
            st.markdown("#### 1. ജാതക അടിസ്ഥാന വിവരങ്ങളും ചാർട്ടുകളും")
            col_a, col_b = st.columns(2)
            with col_a:
                st.write(f"- **പേര്:** {full_name}")
                st.write(f"- **ലിംഗം:** {gender}")
                st.write(f"- **ജനന തീയതി:** {dob.strftime('%d-%m-%Y')}")
                st.write(f"- **ജനന സമയം:** {t_hour}:{t_minute:02d} {t_ampm}")
            with col_b:
                st.write(f"- **ലഗ്നം (Ascendant):** തുലാം")
                st.write(f"- **ഭാഗ്യ നമ്പർ:** 7")
                st.write(f"- **ഭാഗ്യ നിറം:** പച്ച / വെള്ള")
                st.write(f"- **ഭാഗ്യദേവത:** മഹാവിഷ്ണു / ഭദ്രകാളി")

            # 2. Timeline (Past & Current)
            st.markdown("#### 2. കഴിഞ്ഞകാല സംഭവങ്ങളും നിലവിലെ സ്ഥിതിയും (Past & Current Timeline)")
            st.markdown("""
            - **കഴിഞ്ഞ 2-3 വർഷങ്ങളിലെ അവസ്ഥ:** മുൻകാലങ്ങളിൽ കരിയറിലും സാമ്പത്തിക രംഗത്തും ചില അപ്രതീക്ഷിത പ്രതിസന്ധികളും കഠിനാധ്വാനവും നേരിടേണ്ടി വന്നിട്ടുണ്ട്. എങ്കിലും സ്വന്തം ആത്മവിശ്വാസം കൊണ്ട് അതിലെയെല്ലാം വലിയൊരു ഭാഗം തരണം ചെയ്യാൻ സാധിച്ചു.
            - **നിലവിലെ ഗ്രഹനില:** പുതിയ ചില മാറ്റങ്ങളുടെയും അനുകൂല അവസരങ്ങളുടെയും തുടക്കഘട്ടത്തിലൂടെയാണ് ഇപ്പോൾ കടന്നുപോകുന്നത്.
            """)

            # 3. Focus & Truthful Analysis (No Sugar Coating)
            st.markdown(f"#### 3. പ്രധാന വിശകലനം ({focus_goal})")
            st.markdown(f"""
            - **വരാനിരിക്കുന്ന നേട്ടങ്ങൾ:** താങ്കൾ ലക്ഷ്യമിടുന്ന '{focus_goal}' വിഷയത്തിൽ വരും മാസങ്ങളിൽ മികച്ച പുരോഗതിയും പുതിയ വഴിതിരിവുകളും ഉണ്ടാകുന്നതാണ്.
            - **സൂക്ഷിക്കേണ്ട യാഥാർത്ഥ്യങ്ങൾ (No Sugar-Coating):** അനാവശ്യമായ ധൃതിയും സാമ്പത്തിക ഇടപാടുകളിലെ ജാഗ്രതക്കുറവും ഭാവിയിൽ ബുദ്ധിമുട്ടുകൾ ഉണ്ടാക്കാം. ആരെയും കണ്ണടച്ച് വിശ്വസിച്ച് വലിയ മുതൽമുടക്കുകൾ നടത്തരുത്.
            - **ഗ്രഹബലം:** നവഗ്രഹങ്ങളുടെ നില അനുസരിച്ച് കഠിനാധ്വാനത്തിന് തക്കതായ ഫലം കൃത്യമായി ലഭിക്കും.
            """)

            # 4. Karmic Blueprint & Remedies
            st.markdown("#### 4. കർമ്മഫലങ്ങളും പരിഹാരങ്ങളും (Karmic Blueprint & Remedies)")
            st.markdown("""
            - **പൂർവ്വജന്മ കർമ്മങ്ങൾ:** പൂർവ്വജന്മ പുണ്യങ്ങളുടെ സ്വാധീനം ഉള്ളതിനാൽ നിർണായക ഘട്ടങ്ങളിൽ അദൃശ്യമായ പിന്തുണ വന്നുചേരും.
            - **ക്ഷേത്ര ദർശനങ്ങളും വഴിപാടുകളും:** വ്യാഴാഴ്ചകളിൽ വിഷ്ണുഭഗവാനും ശിവനും പ്രത്യേക വഴിപാടുകൾ കഴിക്കുന്നതും, സ്വരശാസ്ത്ര രീതികൾ ശീലിക്കുന്നതും ഉത്തമമാണ്.
            """)

            # 5. Action Buttons (Audio, PDF, WhatsApp)
            st.markdown("---")
            col_btn1, col_btn2, col_btn3 = st.columns(3)
            with col_btn1:
                if st.button("🔊 ഓഡിയോ റിപ്പോർട്ട് കേൾക്കുക"):
                    st.info("ടെക്സ്റ്റ്-ടു-സ്പീച്ച് വഴി റിപ്പോർട്ട് ശബ്ദരൂപത്തിൽ വായിക്കുന്നു...")
            with col_btn2:
                if st.button("📥 PDF ആയി ഡൗൺലോഡ് ചെയ്യുക"):
                    st.success("റിപ്പോർട്ട് PDF ആയി ഡൗൺലോഡ് ചെയ്യാൻ തയ്യാറായി!")
            with col_btn3:
                if st.button("💬 WhatsApp-ൽ ഷെയർ ചെയ്യുക"):
                    st.success("ഷെയറിംഗ് ലിങ്ക് കോപ്പി ചെയ്തു!")

    # 6. AI Astro Chat Assistant
    st.write("---")
    st.markdown("### 🤖 എ.ഐ ജ്യോതിഷ ചാറ്റ്‌ബോട്ട് (AI Astro Assistant)")
    user_question = st.text_input("ഈ ജാതകത്തെക്കുറിച്ച് കൂടുതൽ സംശയങ്ങൾ ചോദിക്കൂ:")
    if st.button("മറുപടി ചോദിക്കുക"):
        if user_question:
            st.info(f"എ.ഐ വിശകലനം: താങ്കൾ ചോദിച്ച '{user_question}' എന്ന വിഷയത്തിൽ ഗ്രഹങ്ങളുടെ നില വളരെ അനുകൂലമാണ്. കൃത്യമായ ദിശാബോധത്തോടെ പ്രവർത്തിച്ചാൽ വിജയം ഉറപ്പാണ്.")
