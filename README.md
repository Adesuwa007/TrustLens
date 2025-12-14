## TrustLens 🔍

Job & Internship Scam Risk Assessment Tool

TrustLens is a web-based tool created to help students and job applicants identify potentially fraudulent or risky job and internship opportunities. It analyzes job descriptions to detect common scam indicators and suspicious behavior patterns, enabling users to make safer and more informed decisions before applying.

In recent years, employment scams have become increasingly sophisticated and harder to detect—especially for first-time applicants. TrustLens aims to reduce this risk by highlighting scam warning signs in a clear, visible, and easy-to-understand manner.

## Problem Statement

Despite the availability of legitimate job platforms today, job and internship scams continue to grow worldwide. Students and first-time job seekers are often the primary targets due to limited experience and lack of professional guidance.

Scammers commonly reach victims through:

-Emails

-WhatsApp or Telegram messages

-Social media DMs

-Third-party recruiters or consultants

-Impersonated company representatives

Most of these scams occur outside official job platforms, where platform-level safety mechanisms do not apply. As a result, individuals may lose money, have their personal data compromised, or lose confidence at the very beginning of their professional journeys.


## Solution Overview

TrustLens functions as a verification and awareness layer, rather than as a job platform. Users can paste any job or internship description, regardless of its source into TrustLens. The system then:

-Scans the content for common scam indicators

-Assigns a risk level (Low / Medium / High)

-Clearly explains why the content may be risky

-Generates a downloadable PDF risk assessment report

The goal is not only to alert users, but also to help them understand why a particular opportunity may be unsafe.


## Why Use TrustLens When Legitimate Platforms Exist?

Legitimate platforms primarily focus on hosting and displaying job listings. They typically do not:
-Analyze recruiter messages sent outside the platform

-Explain scam patterns to users

-Evaluate offers received through email or messaging apps


TrustLens is platform-agnostic, meaning it works with content from:

-Job portals

-Emails

-WhatsApp or Telegram messages

-Social media and recruiter DMs

Platforms host jobs. TrustLens verifies descriptions.

## Why Not Just Rely on Common Sense?

Many scams are carefully designed to appear genuine. They often exploit:

-Urgency (e.g., “apply immediately”, “limited slots”)

-The inexperience of first-time applicants

-Financial pressure or unrealistic promises

TrustLens transforms implicit warning signs into explicit explanations, helping users recognize patterns they might otherwise overlook. Over time, this also improves users’ own awareness and judgment. TrustLens does not replace judgment, it enhances it.

## How TrustLens Works

TrustLens uses a rule-based detection framework built on real-world scam patterns, including:

-Unrealistic salary or income promises

-Upfront or hidden fees

-Urgent or pressuring language

-Claims of no interview or verification

-Suspicious contact methods

-Vague or generic job descriptions


Each detected indicator contributes to a weighted risk score, which determines the final risk level presented to the user.


## Why Rule-Based Instead of AI / ML?

This is a deliberate design choice.

Rule-based detection provides:
-Full transparency

-Clear and explainable results

-No black-box decisions

-Lower risk of false confidence in safety-critical scenarios

In scam detection, understanding why something is considered risky is often more valuable than receiving an opaque classification. The system architecture is designed so that machine learning models can be added later as an enhancement rather than a replacement

What Happens If Scammers Change Their Language?

Although scam wording may evolve over time, behavioral patterns remain largely consistent, such as urgency, payment requests, unofficial communication, and lack of verification. TrustLens focuses on identifying these underlying patterns instead of relying solely on exact phrasing. Scam indicators are stored in external JSON files, allowing quick updates without modifying the core application logic.

## Key Features:
-Detection of real-world scam indicators (200+ keywords)

-Risk scoring (Low / Medium / High)

-Clear and explainable detection results

-Downloadable PDF risk assessment report

-Lightweight, fast, and accessible

-Platform-agnostic input


## Limitations & Known Flaws (Honest Disclosure)

TrustLens is an advisory tool, not a legal or authoritative system.

Known limitations include:

-It may miss highly sophisticated or novel scams (false negatives)

-It may flag poorly written but legitimate job postings (false positives)

-Analysis is limited to textual content and does not include external verification

Therefore, results are presented as risk assessments, not definitive conclusions.
Awareness is the first line of defense.


## Scalability & Future Scope

TrustLens can be scaled as:

-A public web application

-An API for job platforms

-A browser extension

-A campus-level safety and awareness tool

## Planned future enhancements include:

-ML-assisted adaptive detection

-Community-driven scam indicator updates

-URL and company domain verification

-Multi-language support

