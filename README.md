# Topic 7 Capstone: AI-Powered Business Automation & Decision Systems

**Course**: Project 6 -- Prompt Engineering Hands-On Course (Capstone)  
**Author / Learner**: Tanishq Soni  
**GitHub Account**: [tanishqautomates991](https://github.com/tanishqautomates991)  
**Repository Name**: `prompt-engineering-capstone`  
**Video Demonstration**: [Loom Walkthrough Video]
**Assessment Status**: Complete, Verified & Assessor-Ready  

---

## 1. Executive Project Overview

This repository contains the official capstone deliverables for the **Tayana Academy Prompt Engineering Hands-On Course (Topic 7 Capstone)**. The project constructs an autonomous, AI-driven business decision automation and procurement system evaluating Customer Relationship Management (CRM) platforms for an enterprise case study: **Apex Cloud Services**.

### The Enterprise Case Study: Apex Cloud Services
- **Organization Scale**: 150 active commercial sales representatives.
- **Current Operational Baseline**: Client data, customer interactions, and pipeline velocity tracked across decentralized, offline spreadsheets resulting in high data fragmentation, pipeline blindness, and +/- 30% revenue forecasting variance.
- **Strategic Objective**: Construct a virtual decision agent using advanced prompt engineering frameworks to evaluate three candidate platforms (**Salesforce Enterprise**, **HubSpot Sales Hub Enterprise**, and **Zoho CRM Enterprise**), execute mathematically verified Total Cost of Ownership (TCO) models, build a multi-criteria decision matrix, design a 6-month phased rollout roadmap, and deliver executive C-suite presentation assets.

---

## 2. Official Repository Structure (TR-001)

The repository strictly contains the seven required assessment deliverables in accordance with Technical Requirement **TR-001**:

```
prompt-engineering-capstone/
|-- README.md                  # Primary project documentation, case study, and Loom video link
|-- prompt_portfolio.md        # Prompt templates with parameter variables across all 7 frameworks
|-- decision_matrix.md         # Multi-criteria decision matrix (weights sum to 1.00) with verified math
|-- business_proposal.md       # McKinsey-grade B2B proposal for Apex Cloud Services CEO & Board
|-- implementation_plan.md     # 6-month phased roadmap with ASCII Gantt chart & risk registry
|-- executive_presentation.md  # Exactly 6 slides separated by standard markdown '---' horizontal rules
`-- lessons_learned_report.md  # Post-mortem on hallucination prevention, context drift, & framework alignment
```

---

## 3. Advanced Prompt Engineering Frameworks Applied

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

## 4. Key Quantitative Findings & Verified Calculations

### 4.1 Total Cost of Ownership (TCO) Comparison (150 Sales Reps)
All figures calculated and verified via **Quantitative Graph of Thoughts (Q-GoT)** using the official pricing parameters:  
$$\text{TCO} = (\text{User Count} \times \text{Monthly Cost} \times \text{Months}) + \text{Setup Fee}$$

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
  *Sum Verification*: $0.30 + 0.20 + 0.25 + 0.25 = 1.00$ (100% exact).
- **Objective Mathematical Outcome**:
  - **1st Place (Winner)**: **HubSpot Sales Hub Enterprise** -- Score: **8.625 / 10.00**
  - **2nd Place**: Zoho CRM Enterprise -- Score: **7.700 / 10.00**
  - **3rd Place**: Salesforce Enterprise -- Score: **5.450 / 10.00**
- **Governance Alignment**: The Board of Directors formally approved the implementation of **HubSpot Sales Hub Enterprise**, fully aligning with the objective mathematical outcome.

---

## 5. Loom Video Walkthrough Flow (4 to 6 Minutes)

The assessment mandates a **4-to-6 minute Loom video walkthrough** demonstrating the capstone system:

```
+----------------------------------------------------------------------------------------------------+
|                                    LOOM TIMELINE PACING OVERVIEW                                   |
+-------------------+---------------------------------------------------------+----------------------+
| Timestamp         | Core Demonstration Focus                                | Linked Assessment Req|
+-------------------+---------------------------------------------------------+----------------------+
| 0:00 - 1:00 (60s) | Self-Introduction & Apex Cloud Services Case Study      | REQ-002, ASM-001     |
| 1:00 - 2:00 (60s) | Walkthrough of prompt_portfolio.md Library              | REQ-001, REQ-003     |
| 2:00 - 4:00 (120s)| LIVE Paste-and-Run of CO-STAR Q-GoT Prompt in ChatGPT   | REQ-008, CON-001     |
| 4:00 - 5:15 (75s) | Executive Presentation Deck (---) & Lessons Learned     | REQ-005, REQ-006     |
| 5:15 - 6:00 (45s) | Phased Gantt Roadmap, Decision Matrix & GitHub Wrap-up  | REQ-004, REQ-007     |
+-------------------+---------------------------------------------------------+----------------------+
```

### The Exact Prompt to Paste Live in ChatGPT during Step 3:
```markdown
# CONTEXT:
Apex Cloud Services is migrating 150 sales reps to a CRM. We are evaluating Salesforce ($150/user/month + $25,000 setup fee), HubSpot ($90/user/month + $10,000 setup fee), and Zoho ($40/user/month + $5,000 setup fee).

# OBJECTIVE:
Run a Quantitative Graph of Thoughts (Q-GoT) evaluation to calculate the 1-year and 3-year Total Cost of Ownership (TCO) for each vendor.

# SYSTEM CONTROLS & LOGIC STEPS:
1. Calculate 1-Year TCO for Salesforce, HubSpot, and Zoho (User Count * Cost/mo * 12 + Setup Fee).
2. Calculate 3-Year TCO for each (User Count * Cost/mo * 36 + Setup Fee).
3. Self-Check Math Check: Print the arithmetic step-by-step to confirm calculation values.

# STYLE: McKinsey Strategy Consultant.
# TONE: Objective, analytical, finance-first.
# AUDIENCE: CEO and Board of Directors.
# RESPONSE: Write a structured markdown analysis detailing calculations and recommend the most cost-effective option.
```

---

## 6. Notes for LMS Assessment Submission

*Copy and paste the following text into the Description field in the LMS portal upon submission:*

> **Assessment Submission Notes**:
> - **Candidate Name**: Tanishq Soni
> - **Repository**: `prompt-engineering-capstone`
> - **Loom URL**: Set to "Anyone with the link can view".
> - **Q-GoT Arithmetic Auditing**: Standard LLMs exhibited arithmetic hallucination when computing 3-year TCO in unconstrained zero-shot modes. This was solved by enforcing Quantitative Graph of Thoughts (Q-GoT), requiring the model to display intermediate monthly burn, annual recurring subscriptions, and a secondary self-check equation (3 * 1-Year Sub = 3-Year Sub).
> - **Multi-Criteria Weighting**: Verified that decision matrix weights sum to exactly 1.00 (0.30 + 0.20 + 0.25 + 0.25). HubSpot ranked #1 (8.625) due to superior usability (25%) and rapid setup (25%), aligning with the board's implementation mandate.
> - **Context Drift Mitigation**: Solved attention degradation across multi-phase prompts by adopting clean session threads and modular prompt chaining.
