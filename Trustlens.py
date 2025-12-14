# TrustLens - Simple Scam Risk Analyzer
# Prototype for ideathon feasibility demonstration

SCAM_KEYWORDS = {
    "fee": ["registration fee", "processing fee", "payment required", "pay to apply"],
    "urgency": ["urgent hiring", "limited slots", "apply immediately"],
    "contact": ["whatsapp", "telegram", "personal email", "direct message"],
    "vagueness": ["no interview", "work from home", "easy money", "no experience required"]
}

def analyze_posting(text):
    text_lower = text.lower()
    reasons = []

    for category, keywords in SCAM_KEYWORDS.items():
        for keyword in keywords:
            if keyword in text_lower:
                reasons.append(f"Contains suspicious phrase: '{keyword}'")
                break

    if len(reasons) >= 3:
        risk = "HIGH"
    elif len(reasons) == 2:
        risk = "MEDIUM"
    elif len(reasons) == 1:
        risk = "LOW"
    else:
        risk = "LOW"

    return risk, reasons


def main():
    print("=== TrustLens: Job Scam Risk Analyzer (Prototype) ===\n")
    print("Paste the job or internship description below.")
    print("Press Enter twice when done.\n")

    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    job_text = " ".join(lines)

    if not job_text.strip():
        print("\nNo input provided.")
        return

    risk, reasons = analyze_posting(job_text)

    print("\n--- Analysis Result ---")
    print(f"Risk Level: {risk}")

    if reasons:
        print("\nReasons:")
        for r in reasons:
            print(f"- {r}")
    else:
        print("\nNo common scam indicators detected.")

    print("\nNote: This is an advisory-only prototype, not a definitive judgment.")


if __name__ == "__main__":
    main()