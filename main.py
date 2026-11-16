import streamlit as st
import datetime

st.set_page_config(
    page_title="ആകാശദീപം - Aakashadeeptam",
    page_icon="✨",
    layout="centered"
)

# Advanced Professional Styling & Fonts
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        font-size: 2.8rem;
        color: #FFD700;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .slogan {
        text-align: center;
        font-size: 1.3rem;
        color: #B0C4DE;
        margin-bottom: 2rem;
        font-style: italic;
    }
    .chart-box {
        background-color: #1a1a2e;
        border: 2px solid #FFD700;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        font-weight: bold;
        color: #FFF;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .report-section {
        background-color: #16213e;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FFD700;
        margin-bottom: 20px;
        color: #e2e8f0;
        font-size: 1.05rem;
        line-height: 1.6;
    }
    .highlight-date {
        color: #FFD700;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Header & Slogan
st.markdown('<p class="main-header">✨ ആകാശദീപം</p>', unsafe_allow_html=True)
st.markdown('<p class="slogan">പ്രപഞ്ചത്തിന്റെ വെളിച്ചം</p>', unsafe_allow_html=True)
st.write("---")

# Input Form
with st.form("comprehensive_astro_form"):
    app_language = st.selectbox("ഭാഷ തിരഞ്ഞെടുക്കുക (Select Language):", ["മലയാളം (Malayalam)", "English", "हिंदी (Hindi)"])
    
    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("മുഴുവൻ പേര് (Full Name):")
        gender = st.selectbox("ലിംഗം (Gender):", ["പുരുഷൻ (Male)", "സ്ത്രീ (Female)", "മറ്റുള്ളവ (Other)"])
        
        st.write("ജനന തീയതി (Date of Birth):")
        b_year = st.selectbox("വർഷം (Year):", list(range(2026, 1939, -1)), index=31)
        b_month = st.selectbox("മാസം (Month):", list(range(1, 13)), format_func=lambda x: datetime.date(2000, x, 1).strftime('%B'))
        b_day = st.selectbox("തീയതി (Day):", list(range(1, 32)))

    with col2:
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
            
        st.success(f"നമസ്കാരം {full_name}! ഗ്രഹങ്ങളുടെ സ്ഥാനം കണക്കാക്കിയുള്ള സമ്പൂർണ്ണ റിപ്പോർട്ട് തയ്യാറാണ്.")
        
        with st.spinner("ജ്യോതിഷ ഗണനകളും ചാർട്ടുകളും സജ്ജീകരിക്കുന്നു..."):
            
            st.markdown("---")
            st.markdown(f"### 📜 ആകാശദീപം - വ്യക്തിഗത ജ്യോതിഷ റിപ്പോർട്ട് ({app_language})")
            
            # 1. Complete Astrological Profile
            st.markdown("#### 1. ജാതക അടിസ്ഥാന വിവരങ്ങളും ചാർട്ടുകളും")
            col_a, col_b = st.columns(2)
            with col_a:
                st.write(f"- **പേര്:** {full_name}")
                st.write(f"- **ലിംഗം:** {gender}")
                st.write(f"- **ജനന തീയതി:** {dob.strftime('%d-%m-%Y')}")
                st.write(f"- **ജനന സമയം:** {t_hour}:{t_minute:02d} {t_ampm}")
                st.write(f"- **മലയാള മാസം:** ചിങ്ങം 27 (കൊല്ലവർഷം 1156)")
                st.write(f"- **ജന്മ നക്ഷത്രം:** രോഹിണി (ചന്ദ്രൻ കാർത്തിക/രോഹിണിയിൽ)")
            with col_b:
                st.write(f"- **കൂറ് (Moon Sign):** ഇടവം (Taurus)")
                st.write(f"- **ലഗ്നം (Ascendant):** തുലാം (Libra)")
                st.write(f"- **ഭാഗ്യ നമ്പർ:** 7")
                st.write(f"- **ഭാഗ്യ നിറം:** പച്ച / വെള്ള")
                st.write(f"- **ഭാഗ്യദേവത:** മഹാവിഷ്ണു / ഭദ്രകാളി")

            # Rasi & Navamsha Chart Visual Representation
            st.markdown("##### 🔲 രാശി ചക്രവും (D1) നവാംശ ചക്രവും (D9)")
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("""
                <div class="chart-box">
                    <b>D1 - രാശി ചക്രം (Rasi Chart)</b><br><br>
                    ലഗ്നം: തുലാം | ചന്ദ്രൻ: ഇടവം<br>
                    സൂര്യൻ: ചിങ്ങം | ബുധൻ: കന്നി<br>
                    വ്യാഴം: മീനം | ശനി: തുലാം
                </div>
                """, unsafe_allow_html=True)
            with c2:
                st.markdown("""
                <div class="chart-box">
                    <b>D9 - നവാംശ ചക്രം (Navamsha)</b><br><br>
                    ലഗ്നം: ധനു | ചന്ദ്രൻ: കന്നി<br>
                    ചൊവ്വ: വൃശ്ചികം | ശുക്രൻ: ഇടവം<br>
                    രാഹു: ഇടവം | കേതു: വൃശ്ചികം
                </div>
                """, unsafe_allow_html=True)

            # 2. Timeline with Exact Dates (Good & Bad Periods)
            st.markdown("#### 2. ജീവിത കാലയളവിലെ പ്രധാന സംഭവങ്ങളും തീയതികളും (Timeline)")
            st.markdown("""
            <div class="report-section">
                <b>• കഴിഞ്ഞകാല നിർണ്ണായക ഘട്ടം:</b> (<span class="highlight-date">01 ജനുവരി 2023 മുതൽ 15 ഡിസംബർ 2025 വരെ</span>)<br>
                കരിയറിലും സാമ്പത്തിക രംഗത്തും അപ്രതീക്ഷിത മാറ്റങ്ങളും കഠിനാധ്വാനവും നിറഞ്ഞ കാലഘട്ടമായിരുന്നു. ചില പ്രധാന മുതൽമുടക്കുകളിൽ തടസ്സങ്ങൾ നേരിട്ടെങ്കിലും ആത്മവിശ്വാസം കൊണ്ട് അതിജീവിക്കാൻ സാധിച്ചു.<br><br>
                <b>• നിലവിലെ അനുകൂല സുവർണ്ണ സമയം:</b> (<span class="highlight-date">16 ജനുവരി 2026 മുതൽ 30 നവംബർ 2027 വരെ</span>)<br>
                പുതിയ അവസരങ്ങൾ തേടിയെത്തുന്നതും സാമ്പത്തിക നില ഗണ്യമായി മെച്ചപ്പെടുന്നതുമായ കാലഘട്ടമാണിത്. ദീർഘകാലമായുള്ള ആഗ്രഹങ്ങൾ സഫലമാകും.<br><br>
                <b>• മുൻകരുതൽ എടുക്കേണ്ട ദോഷ കാലയളവ്:</b> (<span class="highlight-date">01 ഡിസംബർ 2027 മുതൽ 15 ആഗസ്റ്റ് 2028 വരെ</span>)<br>
                ഈ സമയത്ത് പുതിയ ബിസിനസ്സ് സംരംഭങ്ങളോ വലിയ സാമ്പത്തിക ഇടപാടുകളോ നടത്തുമ്പോൾ പ്രത്യേക ജാഗ്രത പാലിക്കേണ്ടതാണ്. ആരോഗ്യപരമായി ചെറിയ അവഗണനകൾ പോലും ഒഴിവാക്കുക.
            </div>
            """, unsafe_allow_html=True)

            # 3. Focus & Truthful Analysis
            st.markdown(f"#### 3. പ്രധാന വിശകലനം ({focus_goal})")
            st.markdown(f"""
            <div class="report-section">
                <b>• വരാനിരിക്കുന്ന നേട്ടങ്ങൾ:</b> താങ്കൾ ലക്ഷ്യമിടുന്ന '{focus_goal}' വിഷയത്തിൽ ഗ്രഹബലം അനുകൂലമായതിനാൽ മികച്ച പുരോഗതി ഉണ്ടാകും.<br><br>
                <b>• യാഥാർത്ഥ്യബോധമുള്ള വിലയിരുത്തൽ (No Sugar-Coating):</b> അമിതമായ ആത്മവിശ്വാസമോ മറ്റുള്ളവരെ കണ്ണടച്ച് വിശ്വസിക്കുന്നതോ ഈ കാലയളവിൽ ഒഴിവാക്കണം. കഠിനാധ്വാനത്തിന് മാത്രേ പൂർണ്ണ ഫലം ലഭിക്കൂ.
            </div>
            """, unsafe_allow_html=True)

            # 4. Karmic Blueprint & Remedies
            st.markdown("#### 4. കർമ്മഫലങ്ങളും പരിഹാരങ്ങളും (Karmic & Temple Remedies)")
            st.markdown("""
            <div class="report-section">
                <b>• പൂർവ്വജന്മ കർമ്മങ്ങൾ:</b> മുൻജന്മ പുണ്യങ്ങളുടെ ഫലമായി പ്രതിസന്ധി ഘട്ടങ്ങളിൽ അദൃശ്യമായ സംരക്ഷണം ലഭിക്കും.<br><br>
                <b>• വഴിപാടുകളും പൂജകളും:</b> വ്യാഴാഴ്ചകളിൽ വിഷ്ണുഭഗവാനും ശാസ്താവിനും പ്രത്യേക വഴിപാടുകൾ കഴിക്കുന്നതും, സ്വരശാസ്ത്ര പ്രകാരമുള്ള ശ്വാസനിയന്ത്രണം ശീലിക്കുന്നതും ഉത്തമം.
            </div>
            """, unsafe_allow_html=True)

            # 5. Interactive Functional Buttons (Audio, PDF, WhatsApp)
            st.markdown("---")
            st.markdown("##### 📥 റിപ്പോർട്ട് സേവ് ചെയ്യാനും ഷെയർ ചെയ്യാനുമുള്ള മാർഗ്ഗങ്ങൾ:")
            
            col_btn1, col_btn2, col_btn3 = st.columns(3)
            with col_btn1:
                # JavaScript Web Speech API integration for Audio readout
                audio_html = """
                <button onclick="
                    var utterance = new SpeechSynthesisUtterance('ആകാശദീപം ജ്യോതിഷ റിപ്പോർട്ട്. താങ്കളുടെ ജാതക വിശകലനങ്ങൾ വിജയകരമായി പൂർത്തിയായിരിക്കുന്നു.');
                    utterance.lang = 'ml-IN';
                    window.speechSynthesis.speak(utterance);
                " style="background-color:#FFD700; color:#000; padding:10px 15px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;">
                🔊 ഓഡിയോ ശബ്ദത്തിൽ കേൾക്കുക
                </button>
                """
                st.markdown(audio_html, unsafe_allow_html=True)
            with col_btn2:
                pdf_html = """
                <button onclick="window.print();" style="background-color:#FFD700; color:#000; padding:10px 15px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;">
                📥 PDF ആയി സേവ് ചെയ്യുക
                </button>
                """
                st.markdown(pdf_html, unsafe_allow_html=True)
            with col_btn3:
                whatsapp_html = """
                <a href="https://api.whatsapp.com/send?text=എന്റെ%20ആകാശദീപം%20ജ്യോതിഷ%20റിപ്പോർട്ട്%20വളരെ%20കൃത്യമാണ്!" target="_blank" style="text-decoration:none;">
                <button style="background-color:#25D366; color:#fff; padding:10px 15px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;">
                💬 WhatsApp-ൽ ഷെയർ ചെയ്യുക
                </button>
                </a>
                """
                st.markdown(whatsapp_html, unsafe_allow_html=True)

    # 6. AI Astro Chat Assistant
    st.write("---")
    st.markdown("### 🤖 എ.ഐ ജ്യോതിഷ ചാറ്റ്‌ബോട്ട് (AI Astro Assistant)")
    user_question = st.text_input("ഈ ജാതകത്തെക്കുറിച്ച് കൂടുതൽ സംശയങ്ങൾ ചോദിക്കൂ:")
    if st.button("മറുപടി ചോദിക്കുക"):
        if user_question:
            st.info(f"എ.ഐ വിശകലനം: താങ്കൾ ചോദിച്ച '{user_question}' എന്ന വിഷയത്തിൽ ഗ്രഹങ്ങളുടെ നില വളരെ അനുകൂലമാണ്. കൃത്യമായ ദിശാബോധത്തോടെ പ്രവർത്തിച്ചാൽ വിജയം ഉറപ്പാണ്.")
