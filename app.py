import streamlit as st
import PyPDF2
import re

st.set_page_config(page_title="AI Resume Scanner", page_icon="📄", layout="wide")
st.title("📄 AI Resume ATS Scanner")
st.markdown("### College Students Kosam - Built by YOU! 🚀")
st.write("---")

TECH_KEYWORDS = ["python", "sql", "machine learning", "aws", "pandas", "streamlit", "github", "data analysis", "aiml", "power bi", "excel", "java"]

uploaded = st.file_uploader("📤 Nee Resume PDF ikkada drop chey bro", type="pdf")

if uploaded:
    reader = PyPDF2.PdfReader(uploaded)
    full_text = ""
    for p in reader.pages:
        txt = p.extract_text()
        if txt:
            full_text += txt
    
    lower_text = full_text.lower()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("✅ Unna Skills")
        found = [k for k in TECH_KEYWORDS if k in lower_text]
        for f in found:
            st.success(f"✓ {f.upper()}")
        if not found:
            st.error("Emi dorakaledu bro, resume text ga ledu emo")
    
    with col2:
        st.subheader("❌ Add Cheyalsina Skills")
        missing = [k for k in TECH_KEYWORDS if k not in lower_text]
        for m in missing[:6]:
            st.warning(f"+ {m.upper()}")
    
    st.divider()
    score = int((len(found)/len(TECH_KEYWORDS))*100) if TECH_KEYWORDS else 0
    
    c1, c2, c3 = st.columns(3)
    c1.metric("ATS SCORE", f"{score}%")
    c2.metric("Skills Found", f"{len(found)}/{len(TECH_KEYWORDS)}")
    c3.metric("Words", f"{len(full_text.split())}")
    
    if score < 50:
        st.error("🔴 Bro Resume weak ga undi! Missing skills add chey, projects add chey!")
    elif score < 75:
        st.warning("🟡 Good! Kani inka 2-3 skills add cheste top ki vastav!")
    else:
        st.balloons()
        st.success("🟢 KING! FAANG level resume idi!")
        
    with st.expander("📝 Resume Full Text"):
        st.text(full_text[:3000])
else:
    st.info("👆 PDF upload cheste magic chupista!")
    st.markdown("**Tip:** Nee LeetLens project ni resume lo add chesava? Add chey, score perugutundi!")
