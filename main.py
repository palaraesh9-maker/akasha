import streamlit as st
import swisseph as swe
import datetime

st.set_page_config(page_title="Aakashadeeptam", page_icon="✨", layout="centered")

st.title("✨ ആകാശദീപം (Aakashadeeptam)")
st.subheader("വേദ ജ്യോതിഷ വെബ്‌സൈറ്റിലേക്ക് സ്വാഗതം")

st.write("നിങ്ങളുടെ ജാതക കണക്കൂട്ടലുകളും ഗ്രഹസ്ഥിതികളും ഇവിടെ പരിശോധിക്കാവുന്നതാണ്.")

# യൂസർ ഇൻപുട്ട് എടുക്കുന്ന ഭാഗം
name = st.text_input("നിങ്ങളുടെ പേര് നൽകുക:")
birth_date = st.date_input("ജനന തീയതി:", datetime.date(2000, 1, 1))

if st.button("ജാതകം പരിശോധിക്കുക"):
    if name:
        st.success(f"നമസ്കാരം {name}! ജ്യോതിഷ കണക്കൂട്ടലുകൾ തയ്യാറാക്കിക്കൊണ്ടിരിക്കുന്നു...")
        
        # Swiss Ephemeris ടെസ്റ്റ് കണക്കുകൂട്ടൽ
        julday = swe.julday(birth_date.year, birth_date.month, birth_date.day, 12.0)
        st.info(f"ജ്യോതിഷ ജൂലിയൻ ഡേ കണക്ക് വിജയകരമായി ലഭിച്ചു: {julday}")
    else:
        st.warning("ദയവായി ആദ്യം പേര് നൽകുക.")
