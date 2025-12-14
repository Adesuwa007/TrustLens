from scam_signals import SCAM_SIGNALS
import streamlit as st
import re
from datetime import datetime
from fpdf import FPDF
import json

with open("scam_signals.json", "r") as f:
    SCAM_KEYWORDS = json.load(f)
def clean_text(text):
    return text.encode("latin-1", "ignore").decode("latin-1")

# Scam indicators

SCAM_KEYWORDS = {
    "Unrealistic compensation claims": [
        "high pay", "huge salary", "earn", "per day", "quick money"
    ],
    "Fees requested": [
        "registration fee", "processing fee", "payment required", "pay to apply"
    ],
    "Urgent or pressuring language": [
        "urgent hiring", "apply immediately", "limited slots", "act now"
    ],
    "Suspicious contact method": [
        "whatsapp", "telegram", "@gmail.com", "@yahoo.com", "@outlook.com"
    ],
    "Vague job details": [
        "no interview", "easy work", "work from home", "no experience required"
    ]
}


# Pattern detection


def detect_patterns(text):
    patterns = []

    if re.search(r"\$\s*\d{4,}|\d{5,}\s*dollars", text):
        patterns.append("Unusually high compensation mentioned")

    if re.search(r"per day|daily income", text):
        patterns.append("Daily pay promised for vague work")

    if re.search(r"@gmail\.com|@yahoo\.com|@outlook\.com", text):
        patterns.append("Uses personal email instead of company domain")

    if len(text.split()) < 30:
        patterns.append("Very short description with limited role details")

    return patterns


# Main analysis function

def analyze_posting(text):
    text_lower = text.lower()
    reasons = []

    for category, keywords in SCAM_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                reasons.append(category)
                break

    pattern_flags = detect_patterns(text_lower)
    reasons.extend(pattern_flags)

    unique_reasons = list(set(reasons))

    if len(unique_reasons) >= 4:
        risk = "HIGH"
    elif len(unique_reasons) >= 2:
        risk = "MEDIUM"
    elif len(unique_reasons) == 1:
        risk = "LOW"
    else:
        risk = "LOW"

    return risk, unique_reasons
# PDF GENERATION
def generate_pdf(job_text, risk, reasons):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(
        pdf.epw, 10,
        clean_text("TrustLens - Job Scam Risk Assessment Report")
    )

    # Timestamp
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(
        pdf.epw, 8,
        clean_text(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    )

    pdf.ln(5)

    # Risk Level
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, clean_text("Risk Level:"), ln=True)

    pdf.set_font("Arial", size=12)
    pdf.set_x(pdf.l_margin)
    pdf.cell(0, 10, clean_text(risk), ln=True)

    pdf.ln(5)

    # Detected Indicators
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, clean_text("Detected Indicators:"), ln=True)

    pdf.set_font("Arial", size=12)

    if reasons:
        for r in reasons:
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(
                pdf.epw, 8,
                clean_text("• " + r)
            )
            pdf.ln(1)
    else:
        pdf.set_x(pdf.l_margin)
        pdf.multi_cell(
            pdf.epw, 8,
            clean_text("No common scam indicators detected.")
        )

    pdf.ln(5)

    # Job Description
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, clean_text("Submitted Job Description:"), ln=True)

    pdf.set_font("Arial", size=11)
    pdf.set_x(pdf.l_margin)
    pdf.multi_cell(
        pdf.epw, 7,
        clean_text(job_text)
    )

    pdf.ln(5)

    # Disclaimer
    pdf.set_x(pdf.l_margin)
    pdf.set_font("Arial", "I", 10)
    pdf.multi_cell(
        pdf.epw, 7,
        clean_text(
            "Disclaimer: This report provides advisory guidance only and does not guarantee accuracy. "
            "Users should independently verify job opportunities."
        )
    )

    # ✅ Correct return type for Streamlit
    return bytes(pdf.output(dest="S"))


import re

def normalize_text_for_scan(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)   # remove punctuation
    text = re.sub(r"\s+", " ", text)       # normalize spaces
    return text
#ANALYSIS BASED ON WEIGHTED SCAM SIGNALS
def analyze_job_text(text):
    text = text.lower()
    score = 0
    reasons = []

    for category, data in SCAM_SIGNALS.items():
        for kw in data["keywords"]:
            if kw.lower() in text:
                score += data["weight"]
                reasons.append(
                    f"{category}: detected phrase '{kw}'"
                )
                break

    if score >= 12:
        risk = "HIGH"
    elif score >= 6:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return risk, reasons, score

# Streamlit UI

st.set_page_config(page_title="TrustLens", layout="centered")

st.title("🔍 TrustLens")
st.subheader("Helping students identify fake internships and job scams")

st.write(
    "Paste a job or internship description below. "
    "TrustLens highlights common scam indicators and explains potential risks."
)

job_text = st.text_area(
    "Job / Internship Description",
    placeholder="Paste the job or internship description here...",
    height=200
)

if st.button("Analyze"):
    if job_text.strip() == "":
        st.warning("Please paste a job or internship description.")
    else:
        # NEW analysis logic
        risk, reasons, score = analyze_job_text(job_text)

        st.markdown("### Risk Assessment")

        if risk == "HIGH":
            st.error(f"🚨 HIGH RISK (Score: {score})")
        elif risk == "MEDIUM":
            st.warning(f"⚠ MEDIUM RISK (Score: {score})")
        else:
            st.success(f"✅ LOW RISK (Score: {score})")

        st.markdown("### Detected Indicators")
        if reasons:
            for r in set(reasons):
                st.write(f"- {r}")
        else:
            st.write("No common scam indicators were detected.")

        st.caption(
            "Disclaimer: This tool provides advisory guidance only and does not guarantee accuracy."
        )

        # Generate PDF (already returns bytes)
        pdf_data = generate_pdf(job_text, risk, reasons)

        st.download_button(
            label="📄 Download Risk Assessment PDF",
            data=pdf_data,
            file_name="TrustLens_Risk_Report.pdf",
            mime="application/pdf"
        )