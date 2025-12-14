# TrustLens 🔍

### Job & Internship Scam Risk Assessment Tool

TrustLens is a web based tool created to assist students and job applicants in spotting possible fraudulent or hazardous job and internship opportunities. It examines job listings to find signs of scams and dubious activity aiding users in making more secure and well-informed choices prior, to applying.

Lately employment frauds have grown increasingly advanced and more difficult to detect— for those applying for the first time. TrustLens seeks to lower this danger by highlighting scam alerts in a noticeable and comprehensible manner.

## Problem Statement

Despite the presence of authentic job platforms nowadays employment and internship frauds are increasingly widespread worldwide. Learners and those entering the workforce for the time frequently become the main victims due, to their potential lack of experience and career advice.

Fraudsters often contact targets via:
- Emails
- WhatsApp or Telegram messages
- Social media DMs
- Third-party recruiters or consultants
- Impersonated company representatives

The majority of these frauds happen *beyond employment platforms*, where safeguards, at the platform level are not enforced. Consequently individuals may suffer loss compromise their personal information or lose trust right at the beginning of their professional journeys.

## Solution Overview

*TrustLens* functions as a verification and awareness layer* rather, than serving as a job platform.

Users have the option to insert any job or internship description—no its source—, into TrustLens. The platform subsequently:
- Scans the content for common scam indicators
- Assigns a risk level (Low / Medium / High)
- Clearly explains why the content may be risky
- Generates a downloadable PDF risk assessment report

The objective is not simply to alert users but to assist them in comprehending why a job proposal could be risky.

## What Is the Benefit of TrustLens if Authentic Platforms Are Available?

Authentic platforms concentrate on providing and showcasing job openings. They generally do not:
- Analyze recruiter messages sent outside the platform
- Explain scam patterns to users
- Evaluate offers received via email or messaging apps

TrustLens is *platform-independent* indicating it works with content, from:
- Job portals
- Emails
- WhatsApp or Telegram messages
- Social media and recruiter DMs

Platforms host jobs. TrustLens verifies descriptions.

## Why Not Just Rely on Common Sense?

Numerous frauds are meticulously crafted to look authentic. They frequently take advantage of:
- Urgency (“apply immediately”, “limited slots”)
- Inexperience of first-time applicants
- Financial pressure or false promises

TrustLens transforms ** warning signs** into *clear clarifications* aiding users in identifying trends they might otherwise miss. Gradually this also enhances users’ insight and attentiveness.
TrustLens doesn’t substitute judgment. It *enhances* it.

## How TrustLens Works

TrustLens employs a rule-based detection framework* grounded in genuine scam patterns, such, as:
- Unrealistic salary or income promises
- Upfront or hidden fees
- Urgent or pressuring language
- Claims of no interview or verification
- Suspicious contact methods
- Vague or generic job descriptions

Every identified indicator adds to a weighted risk score* which decides the ultimate risk level presented to the user.

## Why Rule-Based Instead of AI / ML?

This is a deliberate design choice.

Rule-based detection offers:
- Full transparency
- Clear and explainable results
- No black-box decisions
- Lower risk of false confidence in safety-critical scenarios

In the context of scam detection grasping why an item is considered risky usually holds value than getting a vague label. The framework is created so that machine learning models may be incorporated later as an upgrade than, as a substitute.

## What Happens If Fraudsters Alter Their Language?

Although the language used in scams may change over time scam *behavioral patterns stay mostly stable*—including urgency demands, for payment, communication and absence of verification.
TrustLens emphasizes identifying these hidden patterns of depending solely on precise expressions. Fraud signals are kept in JSON files enabling quick updates without altering the main application code.


## Key Features

-  Detection of real-world scam indicators (200+ keywords)
-  Risk scoring (Low / Medium / High)
-  Clear, explainable detection results
-  Downloadable PDF risk assessment report
-  Lightweight, fast, and accessible
-  Platform-agnostic input


## Limitations & Known Flaws (Honest Disclosure)

TrustLens is an *advisory tool*, not a legal or authoritative system.

Recognized constraints encompass:
- It may miss highly sophisticated or novel scams (false negatives)
- It may flag poorly written but legitimate job postings (false positives)
- Analysis is limited to textual content and does not perform external verification

Hence the outcomes are shown as *risk evaluations*, than definitive conclusions.
Awareness is the first line of defense.


## Scalability & Future Scope

TrustLens may be. Scaled as:
- A public web application
- An API for job platforms
- A browser extension
- A campus-level safety and awareness tool

Intended upcoming improvements encompass:
- ML-assisted adaptive detection
- Community-driven scam indicator updates
- URL and company domain verification
- Multi-language support
