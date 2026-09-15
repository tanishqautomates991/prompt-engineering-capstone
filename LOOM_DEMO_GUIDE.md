# Loom Demonstration Guide: Capstone Video Walkthrough

**Course**: Project 6 -- Prompt Engineering Hands-On Course (Topic 7 Capstone)  
**Learner / Presenter**: Tanishq Soni  
**Target Duration**: 4 to 6 Minutes (Strictly Enforced by Rubric)  
**Artifact Classification**: Supporting Demonstration Guide (QA / Presentation Tool)  

---

## 1. Pre-Recording Preparation Checklist

Before launching Loom, ensure the following tabs and windows are arranged on your desktop:

1. **Browser Tab 1 (ChatGPT)**:
   - Navigate to [https://chatgpt.com/](https://chatgpt.com/).
   - Start a **clean new chat session** (`New Chat`) to ensure 100% attention capacity and zero context drift.
   - Verify you are logged into your account.
2. **Browser Tab 2 (GitHub Repository)**:
   - Open your public repository: `https://github.com/tanishqautomates991/prompt-engineering-capstone`.
3. **Local Editor / Markdown Viewer (VS Code or IDE)**:
   - Open the `prompt-engineering-capstone` folder.
   - Have tabs ready for:
     - `prompt_portfolio.md`
     - `decision_matrix.md`
     - `business_proposal.md`
     - `implementation_plan.md`
     - `executive_presentation.md`
     - `lessons_learned_report.md`
     - `README.md`
4. **Loom Configuration**:
   - Screen: Full Desktop or Browser + Editor window.
   - Camera: Enabled (webcam bubble placed in the lower-left or lower-right corner).
   - Audio: Microphone tested and verified.

---

## 2. Second-by-Second Video Presentation Script

```
+----------------------------------------------------------------------------------------------------+
|                                    LOOM TIMELINE PACING OVERVIEW                                   |
+-------------------+---------------------------------------------------------+----------------------+
| Timestamp         | Core Demonstration Focus                                | Linked Assessment Req|
+-------------------+---------------------------------------------------------+----------------------+
| 0:00 - 1:00 (60s) | Introduction & Apex Cloud Services Case Study           | REQ-002, ASM-001     |
| 1:00 - 2:00 (60s) | Prompt Portfolio Walkthrough (CO-STAR, Meta, Q-GoT)     | REQ-001, REQ-003     |
| 2:00 - 4:00 (120s)| LIVE ChatGPT Run: CO-STAR Q-GoT Prompt & TCO Math Audit | REQ-008, CON-001     |
| 4:00 - 5:15 (75s) | Executive Slide Deck (---) & Lessons Learned Insights   | REQ-005, REQ-006     |
| 5:15 - 6:00 (45s) | Phased Gantt, Decision Matrix, GitHub Structure & Wrap  | REQ-004, REQ-007     |
+-------------------+---------------------------------------------------------+----------------------+
```

---

### Step 1: Self-Introduction & Enterprise Case Study (0:00 - 1:00)
- **What to Show**: Display `README.md` or `business_proposal.md` on screen.
- **Talking Points**:
  - *"Hello, my name is Tanishq Soni, and this is my capstone demonstration for the Tayana Academy Prompt Engineering Hands-On Course: AI-Powered Business Automation & Decision Systems."*
  - *"Our enterprise scenario centers on Apex Cloud Services, an organization with 150 active sales representatives currently tracking deal flow in disconnected offline spreadsheets."*
  - *"This legacy model causes data silos, high duplication, lack of leadership pipeline visibility, and revenue forecast variances exceeding 30%."*
  - *"Our goal was to engineer an autonomous decision system that evaluates three candidate CRM platforms--Salesforce Enterprise, HubSpot Sales Hub Enterprise, and Zoho CRM Enterprise--and produces board-grade recommendations backed by verified mathematical rigor."*
- **Assessment Requirement Satisfied**: Demonstrates context baseline, business problem, and scenario setup.

---

### Step 2: Prompt Portfolio & Framework Architecture (1:00 - 2:00)
- **What to Show**: Switch to `prompt_portfolio.md` in your editor.
- **Talking Points**:
  - *"In `prompt_portfolio.md`, we engineered a production-grade prompt library integrating seven prompt frameworks."*
  - *"First, we applied **Meta-Prompting** (Section 2), where we instructed ChatGPT to act as an expert Prompt Engineer to generate a specialized B2B CRM pricing and feature researcher prompt. Notice the clean traceability: Meta-Prompt -> Generated System Prompt -> CRM evaluation workflow."*
  - *"Second, we developed our Master **CO-STAR + Q-GoT** template (Section 3). CO-STAR provides 360-degree calibration--defining Context, Objective, McKinsey Consultant Style, Analytical Tone, Board of Directors Audience, and Structured Markdown Response."*
  - *"Crucially, to prevent LLM math hallucinations, we integrated **Quantitative Graph of Thoughts (Q-GoT)**, requiring non-linear calculation branches and explicit self-checking arithmetic."*
  - *(Briefly scroll through Section 8)*: *"We also provided complete production templates for RGCCO, CARE, ERA, and Tree of Thoughts."*
- **Assessment Requirement Satisfied**: REQ-001 (CO-STAR), REQ-003 (Meta-Prompting), TR-001.

---

### Step 3: LIVE ChatGPT Demonstration -- CO-STAR Q-GoT Prompt (2:00 - 4:00) [CRITICAL]
- **What to Show**: Switch to your browser with [ChatGPT](https://chatgpt.com/) open in a **fresh new chat**.
- **Action**: Copy the exact prompt below and paste it live into ChatGPT, then hit Send.

#### The Exact Prompt to Paste Live:
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

- **Talking Points as ChatGPT Generates Output**:
  - *"Now I am executing our CO-STAR Q-GoT vendor evaluation live in ChatGPT."*
  - *(Point your mouse at the generating numbers)*:
    - *"Notice how Q-GoT forces the model to print every intermediate calculation node rather than guessing a final number."*
    - *"For Salesforce: 150 reps times $150/mo equals $22,500/mo. For 12 months, that is $270,000, plus the $25,000 setup fee, giving exactly **$295,000** 1-year TCO. For 3 years, 36 months times $22,500 is $810,000 plus $25,000 setup fee, yielding exactly **$835,000**."*
    - *"For HubSpot: 150 reps times $90/mo is $13,500/mo. Times 12 months is $162,000 plus $10,000 setup fee, giving **$172,000** 1-year TCO. For 3 years, $13,500 times 36 is $486,000 plus $10,000, yielding **$496,000**."*
    - *"For Zoho: 150 reps times $40/mo is $6,000/mo. 1-year TCO is $72,000 plus $5,000 setup, giving **$77,000**. 3-year TCO is $216,000 plus $5,000 setup, giving **$221,000**."*
    - *(Highlight the self-check)*: *"And look at the Self-Check Math Check: the model verifies that 3-year subscription equals exactly three times the 1-year subscription ($486k = 3 * $162k). Zero arithmetic hallucination."*
- **Assessment Requirement Satisfied**: REQ-002 (Vendor Evaluation), REQ-008 (Live Loom Execution), CON-001 (Q-GoT Self-Check).

---

### Step 4: Executive Slide Presentation & Lessons Learned (4:00 - 5:15)
- **What to Show**: Switch back to editor, open `executive_presentation.md`, then `lessons_learned_report.md`.
- **Talking Points**:
  - *"Next, in `executive_presentation.md`, we created our executive board deck. As mandated by Technical Requirement TR-003 and REQ-005, the presentation is structured into exactly six slides separated by standard markdown horizontal rules (`---`)."*
  - *(Scroll through the slides)*: *"Slide 1 Title, Slide 2 Client Problem, Slide 3 Vendor Candidates, Slide 4 TCO Analysis, Slide 5 Decision Matrix, and Slide 6 Phased Roadmap."*
  - *(Switch to `lessons_learned_report.md`)*: *"In `lessons_learned_report.md`, we documented critical post-mortem insights across three areas:"*
    1. *"**Hallucination Prevention**: How unconstrained LLMs fail at tokenized arithmetic, and how Q-GoT and Generated Knowledge ground the model in verified facts."*
    2. *"**Context Window Wind-down**: Why long conversational threads degrade attention due to the 'Lost in the Middle' phenomenon, and how starting clean threads and using prompt chaining mitigates constraint drift."*
    3. *"**Framework Alignment**: Guidelines explaining when to select RGCCO, CARE, ERA, CO-STAR, or Tree of Thoughts based on cognitive task topology."*
- **Assessment Requirement Satisfied**: REQ-005, TR-003, REQ-006, CON-002.

---

### Step 5: Phased Gantt, Decision Matrix & GitHub Repository Wrap-up (5:15 - 6:00)
- **What to Show**: Briefly flash `implementation_plan.md`, `decision_matrix.md`, and switch to your browser showing the GitHub repository.
- **Talking Points**:
  - *"In `decision_matrix.md`, our Multi-Criteria Decision Analysis scores the vendors across four criteria with weights summing to exactly 1.00 (100%). HubSpot emerges as the mathematical winner with 8.625 out of 10, balancing cost, enterprise custom objects, rapid setup, and top-tier user adoption."*
  - *"In `implementation_plan.md`, we built the 6-month phased implementation roadmap for HubSpot across all four phases, complete with a clean ASCII Gantt chart and a 3-risk registry table."*
  - *(Show GitHub repository)*: *"All seven mandatory deliverables and supporting QA test scripts are pushed to our public GitHub repository: `tanishqautomates991/prompt-engineering-capstone`. Our automated Python test suite confirms 100% compliance across all rubrics."*
  - *"Thank you for your time and evaluation!"*
- **Assessment Requirement Satisfied**: REQ-004, REQ-007, TR-001, TR-002.

---

## 3. Contingency & Troubleshooting Guidelines

### What if ChatGPT makes a small math mistake during the live run?
- **Do not panic**: This actually provides an outstanding teaching moment demonstrating why prompt engineering is necessary!
- **On-Camera Recovery**: Say: *"Notice here that even with structured prompting, probabilistic token generation can occasionally introduce arithmetic variance. This is precisely why we enforce Q-GoT self-check equations and run our deterministic Python verification scripts in our pipeline to catch discrepancies before board submission."*

### Setting Loom Video Permissions:
- Immediately after recording, click **Share** on Loom.
- Under Link Settings, ensure it is set to **"Anyone with the link can view"**.
- Copy the public URL and paste it into `README.md` and your LMS submission form!
