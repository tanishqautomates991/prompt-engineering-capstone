# Topic 7 Capstone: AI-Powered Business Automation & Decision Systems

**Course**: Project 6 -- Prompt Engineering Hands-On Course (Capstone)  
**Author / Learner**: Tanishq Soni  
**GitHub Account**: [tanishqautomates991](https://github.com/tanishqautomates991)  
**Repository Name**: `prompt-engineering-capstone`  
**Video Demonstration**: [Loom Walkthrough Video](PASTE_YOUR_PUBLIC_LOOM_SHARE_URL_HERE) *(Replace with your 4-6 min public Loom video URL)*  
**Assessment Status**: Complete, Verified & Assessor-Ready  

---

## 1. Executive Project Overview

This repository represents the completed Capstone Assessment for the **Tayana Academy Prompt Engineering Hands-On Course**. The project constructs an autonomous, AI-driven business decision automation and procurement system evaluating Customer Relationship Management (CRM) platforms for an enterprise case study: **Apex Cloud Services**.

### The Enterprise Case Study: Apex Cloud Services
- **Organization Scale**: 150 active commercial sales representatives.
- **Current Operational Baseline**: Client data, customer interactions, and pipeline velocity tracked in decentralized, offline spreadsheets resulting in severe data fragmentation, pipeline blindness, and +/- 30% revenue forecasting variance.
- **Strategic Objective**: Construct a virtual decision agent using advanced prompt engineering frameworks to evaluate three candidate platforms (**Salesforce Enterprise**, **HubSpot Sales Hub Enterprise**, and **Zoho CRM Enterprise**), execute mathematically verified Total Cost of Ownership (TCO) models, build a multi-criteria decision matrix, design a 6-month phased rollout roadmap, and deliver executive C-suite presentation assets.

---

## 2. Advanced Prompt Engineering Frameworks Applied

This capstone integrates seven foundational and advanced prompt engineering architectures across strategic, tactical, and reasoning domains:

1. **CO-STAR Framework** (Context, Objective, Style, Tone, Audience, Response):
   - Powers the primary decision-support models and the B2B Business Proposal (`business_proposal.md`), formatting high-stakes communications for the CEO and Board of Directors.
2. **Meta-Prompting**:
   - Instructs ChatGPT to act as a Principal Prompt Engineer to autonomously construct a specialized, constraint-bounded B2B CRM pricing and feature researcher prompt.
3. **Quantitative Graph of Thoughts (Q-GoT)**:
   - Decomposes multi-variable licensing and setup calculations into modular computational nodes with cross-equation self-checking, eliminating large language model arithmetic hallucinations.
4. **Multi-Criteria Decision Analysis (MCDA)**:
   - Evaluates vendor candidates against four weighted business criteria summing to exactly 1.00 (100%), showing step-by-step arithmetic proofs.
5. **RGCCO Framework** (Role, Goal, Context, Constraints, Output):
   - Formulates strict data schema boundary rules for migrating legacy spreadsheet records.
6. **CARE Framework** (Context, Action, Result, Example):
   - Structures sales representative training modules and change-management workflows.
7. **ERA Framework** (Expectation, Role, Action) & **Tree of Thoughts (ToT)**:
   - Applied for rapid data sanity checks (ERA) and non-linear migration cutover scenario evaluation (ToT).

---

## 3. Official Repository Structure (TR-001)

The repository strictly implements the mandatory file structure specified in Technical Requirement **TR-001**, complemented by supporting QA and demonstration guides:

```
prompt-engineering-capstone/
??? README.md                      # [TR-001] Primary project documentation, architecture, & Loom link
??? prompt_portfolio.md            # [TR-001, REQ-001/003] Complete prompt library with parameters & 7 frameworks
??? decision_matrix.md             # [TR-001, TR-002] Multi-criteria matrix (weights sum to 1.00) & verified math
??? business_proposal.md           # [TR-001, US-001] Executive B2B proposal for Apex Cloud Services CEO & Board
??? implementation_plan.md         # [TR-001, REQ-004] 6-month phased roadmap, ASCII Gantt chart, & risk registry
??? executive_presentation.md      # [TR-001, REQ-005, TR-003] Exactly 6 slides separated by markdown '---'
??? lessons_learned_report.md      # [TR-001, REQ-006, CON-002] Post-mortem on hallucination, context drift, & frameworks
?
??? LOOM_DEMO_GUIDE.md             # [Supporting QA] 4-6 min step-by-step video script & prompt runbook
??? SUBMISSION_CHECKLIST.md        # [Supporting QA] Comprehensive 16-point compliance checklist & LMS text
??? verify_capstone.py             # [Supporting QA] Automated verification test suite validating all requirements
```

---

## 4. Key Quantitative Findings & Verified Calculations

### 4.1 Total Cost of Ownership (TCO) Comparison (150 Sales Reps)
All figures calculated and verified via **Quantitative Graph of Thoughts (Q-GoT)** using the official pricing parameters:  
Formula: TCO = (User Count * Monthly Cost * Months) + Setup Fee

```
+--------------------------+----------------------------+-------------+-------------+-----------------------+
| Vendor Platform          | Baseline Cost Structure    | 1-Year TCO  | 3-Year TCO  | 3-Yr Delta vs HubSpot |
+--------------------------+----------------------------+-------------+-------------+-----------------------+
| Salesforce Enterprise    | $150/user/mo + $25k setup  |  $295,000   |  $835,000   |   +$339,000 (+68.3%)  |
| HubSpot Sales Hub Ent.   | $90/user/mo + $10k setup   |  $172,000   |  $496,000   |      BASELINE ($0)    |
| Zoho CRM Enterprise      | $40/user/mo + $5k setup    |   $77,000   |  $221,000   |   -$275,000 (-55.4%)  |
+--------------------------+----------------------------+-------------+-------------+-----------------------+
```

### 4.2 Multi-Criteria Decision Matrix Summary (TR-002)
- **Weights**: TCO Cost Model (30%), Customization & Scale (20%), Setup Speed (25%), User Adoption Ease (25%).  
  *Sum Verification*: 0.30 + 0.20 + 0.25 + 0.25 = 1.00 (100% exact).
- **Objective Mathematical Outcome**:
  - **1st Place (Winner)**: **HubSpot Sales Hub Enterprise** -- Score: **8.625 / 10.00**
  - **2nd Place**: Zoho CRM Enterprise -- Score: **7.700 / 10.00**
  - **3rd Place**: Salesforce Enterprise -- Score: **5.450 / 10.00**
- **Governance Alignment**: The Board of Directors formally approved the implementation of **HubSpot Sales Hub Enterprise**, fully aligning with the objective mathematical outcome.

---

## 5. Automated Verification & Quality Assurance

This repository includes an automated verification script (`verify_capstone.py`) that empirically audits the entire deliverable suite against the official requirements:

### Running the Test Suite:
```bash
python verify_capstone.py
```

### Verification Coverage:
- [x] **TR-001**: Presence and non-emptiness of all 7 mandatory markdown files.
- [x] **TR-002**: Decision matrix weights sum to exactly 1.00 (100%) and arithmetic consistency.
- [x] **TR-003**: Executive presentation contains exactly 6 slides separated by standard `---` dividers.
- [x] **REQ-001**: CO-STAR prompt templates with explicit parameter variables.
- [x] **REQ-002**: Comprehensive vendor comparisons across cost, scale, and timelines.
- [x] **REQ-003**: Meta-prompting flow and generated CRM researcher system prompt.
- [x] **REQ-004**: 6-month phased roadmap, ASCII Gantt chart in code block, and 3-risk registry table.
- [x] **REQ-006 & CON-002**: Lessons learned coverage of hallucination prevention, context window wind-down, and framework alignment.
- [x] **Security**: Scan for exposed API keys, tokens, or credentials (0 secrets detected).

---

## 6. Loom Video Demonstration Guide

The assessment mandates a **4-to-6 minute Loom video walkthrough**. Comprehensive step-by-step instructions, prompt text to copy-paste live into ChatGPT, and timing breakdowns are provided in [`LOOM_DEMO_GUIDE.md`](./LOOM_DEMO_GUIDE.md).

### High-Level Pacing Overview:
- **0:00 - 1:00**: Self-introduction (Tanishq Soni) and Apex Cloud Services case study summary.
- **1:00 - 2:00**: Walkthrough of `prompt_portfolio.md` library (explaining CO-STAR, Q-GoT, and Meta-Prompting).
- **2:00 - 4:00**: Live ChatGPT execution of the CO-STAR Q-GoT prompt showing step-by-step 1-year and 3-year TCO calculations on screen.
- **4:00 - 5:30**: Demonstration of `executive_presentation.md` slide formatting (`---` dividers) and `lessons_learned_report.md` insights.
- **5:30 - 6:00**: Review of public GitHub repository structure and closing remarks.

---

## 7. Notes for LMS Assessment Submission

*The following notes can be pasted directly into the LMS Description field upon submission:*

> **Assessment Submission Notes**:
> - **Candidate Name**: Tanishq Soni
> - **Repository**: `prompt-engineering-capstone`
> - **Loom URL**: Set to "Anyone with the link can view".
> - **Q-GoT Arithmetic Auditing**: Standard LLMs exhibited arithmetic hallucination when computing 3-year TCO in unconstrained zero-shot modes. This was solved by enforcing Quantitative Graph of Thoughts (Q-GoT), requiring the model to display intermediate monthly burn, annual recurring subscriptions, and a secondary self-check equation (3 * 1-Year Sub = 3-Year Sub).
> - **Multi-Criteria Weighting**: Verified that decision matrix weights sum to exactly 1.00 (0.30 + 0.20 + 0.25 + 0.25). HubSpot ranked #1 (8.625) due to superior usability (25%) and rapid setup (25%), aligning with the board's implementation mandate.
> - **Context Drift Mitigation**: Solved attention degradation across multi-phase prompts by adopting clean session threads and modular prompt chaining.
