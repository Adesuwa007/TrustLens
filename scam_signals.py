# scam_signals.py

SCAM_SIGNALS = [
    {
        "name": "Upfront fees",
        "keywords": [
            "registration fee", "joining fee", "processing fee",
            "pay to apply", "security deposit", "training fee",
            "payment required", "pay", "fee"
        ],
        "reason": "Legitimate employers do not ask candidates to pay upfront fees.",
        "weight": 5
    },
    {
        "name": "No interview",
        "keywords": [
            "no interview", "no screening", "direct selection",
            "instant hiring", "immediate joining"
        ],
        "reason": "Most legitimate roles involve interviews or screening steps.",
        "weight": 4
    },
    {
        "name": "Urgent language",
        "keywords": [
            "urgent", "apply now", "limited slots",
            "hiring immediately", "last chance"
        ],
        "reason": "Scams often use urgency to pressure applicants.",
        "weight": 3
    },
    {
        "name": "Unrealistic salary",
        "keywords": [
            "earn 100000", "100,000", "guaranteed income",
            "easy money", "high pay", "huge salary"
        ],
        "reason": "Unrealistically high pay for minimal work is a common scam indicator.",
        "weight": 5
    },
    {
        "name": "Vague job details",
        "keywords": [
            "work from home", "online job",
            "simple work", "no experience required"
        ],
        "reason": "Scam postings often lack clear role responsibilities.",
        "weight": 2
    },
    {
        "name": "Suspicious contact method",
        "keywords": [
            "gmail.com", "telegram", "whatsapp",
            "contact directly", "dm us"
        ],
        "reason": "Professional employers usually use official company domains.",
        "weight": 4
    }
]