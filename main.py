import streamlit as st
import datetime

st.set_page_config(page_title="Aakashadeeptam", page_icon="✨", layout="centered")

st.title("✨ ആകാശദീപം (Aakashadeeptam)")
st.subheader("വേദ ജ്യോതിഷ വെബ്‌സൈറ്റിലേക്ക് സ്വാഗതം")

st.write("നിങ്ങളുടെ ജാതക കണക്കൂട്ടലുകളും വിവരങ്ങളും ഇവിടെ പരിശോധിക്കാവുന്നതാണ്.")

# യൂസർ ഇൻപുട്ട് എടുക്കുന്ന ഭാഗം
name = st.text_input("നിങ്ങളുടെ പേര് നൽകുക:")
birth_date = st.date_input("ജനന തീയതി:", datetime.date(2000, 1, 1))

if st.button("ജാതകം പരിശോധിക്കുക"):
    if name:
        st.success(f"നമസ്കാരം {name}! താങ്കളുടെ ജാതക വിവരങ്ങൾ വിജയകരമായി രേഖപ്പെടുത്തിയിരിക്കുന്നു.")
        st.info(f"ജനന തീയതി: {birth_date}")
    else:
        st.warning("ദയവായി ആദ്യം പേര് നൽകുക.")
