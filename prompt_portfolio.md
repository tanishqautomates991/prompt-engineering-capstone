# Prompt Portfolio: AI-Powered Business Automation & Decision Systems

**Course**: Project 6 -- Prompt Engineering Hands-On Course (Capstone)  
**Topic**: Topic 7 -- Capstone: AI-Powered Business Automation & Decision Systems  
**Author**: Tanishq Soni  
**GitHub Repository**: [tanishqautomates991/prompt-engineering-capstone](https://github.com/tanishqautomates991/prompt-engineering-capstone)  
**Document Type**: Mandatory Deliverable 1 of 7 (TR-001)  
**Version**: 1.0.0 (Production / Assessor-Audited)  

---

## 1. Portfolio Architecture & Design Philosophy

This Prompt Portfolio serves as the central prompt repository for the Tayana Academy Prompt Engineering Capstone. It addresses the enterprise procurement challenge of **Apex Cloud Services**, an enterprise migrating 150 active sales representatives from fragmented offline spreadsheets to a modern CRM platform.

The portfolio is architected around seven foundational and advanced prompt engineering frameworks covered throughout Lessons 1 to 6 and synthesized in the Capstone:

```
+---------------------------------------------------------------------------------------------+
|                                ENTERPRISE PROMPT ARCHITECTURE                               |
+-------------------------------+-----------------------------+-------------------------------+
|    STRATEGIC & EXECUTIVE      |   TACTICAL & OPERATIONAL    |    ADVANCED REASONING & META  |
+-------------------------------+-----------------------------+-------------------------------+
| * CO-STAR (Executive Briefs)  | * RGCCO (Scope & Spec)      | * Meta-Prompting (Agent Gen)  |
| * Decision Matrix MCDA Prompt | * CARE (Onboarding/SOPs)    | * Q-GoT (Multi-Branch Math)   |
| * Executive Presentation Deck | * ERA (Tactical Audits)     | * Tree of Thoughts (ToT Risk) |
+-------------------------------+-----------------------------+-------------------------------+
```

All prompt templates in this portfolio adhere to three engineering mandates:
1. **Zero Math Hallucination via Q-GoT**: Enforcing explicit arithmetic self-check verification steps before synthesizing business recommendations.
2. **Parameterized Reusability**: Using dynamic parameter variables (`{VARIABLE_NAME}`) to enable automated substitution across any enterprise procurement scenario.
3. **Traceable Prompt Engineering Lifecycle**: Demonstrating Meta-Prompting -> Generated System Prompt -> Downstream Evaluation Workflows.

---

## 2. Meta-Prompting: Autonomous CRM Research Agent Generation (REQ-003)

### 2.1 The Meta-Prompt Template
This meta-prompt directs ChatGPT to adopt the persona of an expert Prompt Engineer and construct a dedicated, constraint-enforced system prompt for specialized CRM research.

```markdown
# META-PROMPT: CRM RESEARCH PROMPT GENERATOR

Act as an expert Prompt Engineer. I need to write a system prompt that turns ChatGPT into a specialized B2B CRM Pricing and Feature Researcher.

The generated prompt must:
- Focus on comparing Salesforce Enterprise, HubSpot Sales Hub, and Zoho CRM.
- Set constraints to request only verified licensing models.
- Enforce a structured Markdown list output.

Write the system prompt inside a single markdown code block. Do not write anything else.
```

### 2.2 Traceability Flow
```
+----------------------------------------------------------------------------------------+
| 1. Meta-Prompt (Instructs ChatGPT as Expert Prompt Engineer)                           |
|    |-- Defines scope: Salesforce Enterprise vs HubSpot Sales Hub vs Zoho CRM           |
|    |-- Imposes constraints: verified licensing tiers, markdown structured list         |
+----------------------------------------------------------------------------------------+
| 2. Generated Specialized System Prompt (Section 2.3 below)                             |
|    |-- Configures ChatGPT as specialized B2B CRM Pricing and Feature Researcher        |
|    |-- Sets strict boundaries on data collection & cost drivers                        |
+----------------------------------------------------------------------------------------+
| 3. Downstream CRM Evaluation Workflow                                                  |
|    |-- Feeds verified pricing into CO-STAR Q-GoT vendor evaluation (Section 3)         |
|    |-- Informs Weighted Decision Matrix criteria (Section 4)                           |
|    |-- Backs B2B Business Proposal and 6-Slide Executive Deck                          |
+----------------------------------------------------------------------------------------+
```

### 2.3 The Generated Specialized System Prompt
*The resulting system prompt generated from the Meta-Prompt:*

```markdown
# SYSTEM PROMPT: SPECIALIZED B2B CRM PRICING AND FEATURE RESEARCHER

You are an expert B2B CRM Pricing and Feature Researcher specializing in mid-market and enterprise CRM software procurement. Your role is to provide rigorous, verified, and objective research comparing three specific platforms: Salesforce Enterprise, HubSpot Sales Hub Enterprise, and Zoho CRM Enterprise.

## CORE OBJECTIVES:
1. Analyze baseline licensing models and mandatory implementation fees based strictly on verified enterprise pricing:
   - Salesforce: $150 / user / month + $25,000 one-time setup fee
   - HubSpot: $90 / user / month + $10,000 one-time setup fee
   - Zoho: $40 / user / month + $5,000 one-time setup fee
2. Evaluate features across four key business domains:
   - Core sales pipeline governance and custom object architecture
   - Legacy spreadsheet data migration capabilities
   - Setup complexity and deployment timeline requirements
   - Sales representative usability and adoption ramp-up speed
3. Identify hidden licensing dependencies (e.g., storage tiers, API throughput limits, premier support fees).

## CONSTRAINTS & OPERATING BOUNDARIES:
- Request and report only verified enterprise licensing models.
- Do not fabricate promotional discounts, unverified tiers, or speculative features.
- If data points are unknown or variable, state the exact variables required to calculate them.

## OUTPUT FORMAT:
Deliver all analysis in a structured Markdown format containing:
1. A Markdown comparative table listing Base Price, Setup Fee, 1-Year Baseline, 3-Year Baseline, and Target Profile.
2. A bulleted Markdown list detailing Architectural Strengths, Critical Weaknesses, and Migration Risks for each vendor.
```

---

## 3. Master CO-STAR + Q-GoT Vendor Evaluation Prompt (REQ-001, REQ-002, CON-001)

This is the primary decision-support template executing Quantitative Graph of Thoughts (Q-GoT) arithmetic verification to compute 1-Year and 3-Year Total Cost of Ownership (TCO) across Salesforce, HubSpot, and Zoho.

### 3.1 Production Prompt 

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

### 3.2 Parameterized Master Template
```markdown
# CONTEXT:
{ENTERPRISE_NAME} is migrating {USER_COUNT} sales reps to a CRM. We are evaluating:
- {VENDOR_1_NAME} (${VENDOR_1_RATE}/user/month + ${VENDOR_1_SETUP} setup fee)
- {VENDOR_2_NAME} (${VENDOR_2_RATE}/user/month + ${VENDOR_2_SETUP} setup fee)
- {VENDOR_3_NAME} (${VENDOR_3_RATE}/user/month + ${VENDOR_3_SETUP} setup fee)

# OBJECTIVE:
Run a Quantitative Graph of Thoughts (Q-GoT) evaluation to calculate the 1-year ({TIMEFRAME_1_MONTHS} months) and 3-year ({TIMEFRAME_2_MONTHS} months) Total Cost of Ownership (TCO) for each vendor.

# SYSTEM CONTROLS & LOGIC STEPS:
1. Calculate 1-Year TCO for all vendors using: (User Count * Cost/mo * 12) + Setup Fee
2. Calculate 3-Year TCO for all vendors using: (User Count * Cost/mo * 36) + Setup Fee
3. Self-Check Math Check: Print the arithmetic step-by-step to confirm calculation values.
4. Perform Non-Linear Thought Verification:
   - Check Node: Verify 3-Year Subscription == 3 * 1-Year Subscription
   - Delta Node: Calculate Cost Differentials between lowest, median, and highest cost options.

# STYLE: {CONSULTING_STYLE}
# TONE: {EXECUTIVE_TONE}
# AUDIENCE: {TARGET_AUDIENCE}
# RESPONSE: Write a structured markdown analysis detailing calculations and recommend the most cost-effective option.
```

---

## 4. Weighted Cost-Benefit Decision Matrix Prompt (TR-002)

Generates the multi-criteria decision matrix with verified weight summation (1.00 / 100%) and per-cell arithmetic.

```markdown
Act as a Financial Analyst. Create a markdown table comparing Salesforce, HubSpot, and Zoho.

Use these criteria and weights (weights must sum to 100%):
- TCO Cost Model (30% weight)
- Customization & Scale (20% weight)
- Setup Speed (25% weight)
- User Adoption Ease (25% weight)

For each vendor, assign a raw score from 1 (poor) to 10 (excellent), calculate the weighted scores, and sum them. Show the math steps.

Verification Rules:
1. Confirm weights sum to exactly 1.0 (0.30 + 0.20 + 0.25 + 0.25 = 1.00).
2. Explicitly show the formula: Weighted Score = Raw Score * Weight for every cell.
3. Provide a clear scoring rationale for each rating.
4. State the objective mathematical ranking, while noting the operational context.
```

---

## 5. Phased Gantt Roadmap & Risk Registry Prompts (REQ-004)

### 5.1 Phased Implementation Roadmap Prompt
```markdown
Act as a Project Manager. The board selected HubSpot CRM as the optimal solution.
Create a phased 6-month implementation roadmap.
Represent the timeline as a markdown text Gantt chart showing:
- Phase 1: Planning & Data Cleanup (Month 1)
- Phase 2: System Configuration & Pilot (Months 2-3)
- Phase 3: Full Migration & Staff Training (Months 4-5)
- Phase 4: Post-Launch Optimization (Month 6)

Format the Gantt visualization using ASCII or markdown progress blocks.
Encapsulate the ASCII Gantt chart inside raw markdown code blocks (using three backticks ```) to prevent markdown rendering errors.
```

### 5.2 Implementation Risk Registry Prompt
```markdown
For the HubSpot CRM migration, identify 3 implementation risks. Format as a table:
| Risk Event | Probability (Low/Med/High) | Impact (Low/Med/High) | Mitigation |

Include risks addressing:
1. Legacy spreadsheet data quality and duplicate records.
2. Sales representative adoption resistance and dual-system usage.
3. In-flight deal pipeline disruption during final cutover.
```

---

## 6. Executive Presentation Slide Deck Prompt (REQ-005, TR-003)

Generates an executive presentation deck formatted as exactly six slides separated by standard markdown horizontal dividers (`---`).

```markdown
Act as a Strategy Consultant. Prepare a 6-slide executive deck summarizing our CRM vendor selection.

Format: Use standard markdown slide format where slides are separated by exactly three dashes (---).
Include:
Slide 1: Title & Executive Overview
Slide 2: Client Problem & Current Metrics
Slide 3: Vendor Candidates (Salesforce, HubSpot, Zoho)
Slide 4: Cost-Benefit Analysis & TCO
Slide 5: Decision Matrix & Recommendation
Slide 6: Phased Roadmap & Immediate Next Steps

Style: Clean, board-ready executive bullet points, bold key figures, clear takeaway headlines.
```

---

## 7. Lessons Learned Post-Mortem Report Prompt (REQ-006, CON-002)

```markdown
Act as a Principal AI Systems Architect. Write a comprehensive Lessons Learned Post-Mortem Report on using Large Language Models for automated business decision systems.

Include sections detailing:
1. Hallucination Prevention: Document how Generated Knowledge and step-by-step math audits prevented calculation errors.
2. Context Window Wind-down: Explain how model performance degrades as threads grow longer (loss of attention/forgetting constraints) and how to manage this (e.g. starting clean threads, using prompt chaining).
3. Framework Alignment: Guidelines on when to select RGCCO (creative/copy), CARE (interactive dialogues), ERA (quick queries), or CO-STAR (presentations/proposals).

Provide concrete examples from the CRM procurement capstone to ground each theoretical insight.
```

---

## 8. Complete Prompt Engineering Framework Reference Library

This section provides reusable, production-ready templates for all seven course frameworks, establishing their enterprise use case, parameter variables, expected output, and engineering rationale.

### 8.1 RGCCO Framework (Role, Goal, Context, Constraints, Output)
- **Framework Name**: RGCCO
- **Purpose**: System-level configuration, task boundary enforcement, and technical specifications.
- **Why Used**: Provides clear boundary fences and negative constraints, making it ideal for data migration specifications where schema violations cause pipeline failure.
- **Capstone Use Case**: Formulating the data sanitization and schema migration specification for Apex Cloud Services' legacy spreadsheets.
- **Parameter Variables**: `{SYSTEM_ROLE}`, `{PRIMARY_GOAL}`, `{OPERATIONAL_CONTEXT}`, `{NEGATIVE_CONSTRAINTS}`, `{OUTPUT_SCHEMA}`
- **Complete Template**:
  ```markdown
  # ROLE: {SYSTEM_ROLE}
  # GOAL: {PRIMARY_GOAL}
  # CONTEXT: {OPERATIONAL_CONTEXT}
  # CONSTRAINTS:
  - {NEGATIVE_CONSTRAINTS_LIST}
  - Do not infer missing column data without flagging.
  - Enforce ISO-8601 date formatting on all timestamp records.
  # OUTPUT:
  - Deliver output adhering to schema: {OUTPUT_SCHEMA}
  ```
- **Expected Output**: A structured data cleaning report and Python/Pandas transformation script.

---

### 8.2 CARE Framework (Context, Action, Result, Example)
- **Framework Name**: CARE
- **Purpose**: Interactive dialogues, employee onboarding, procedure creation, and role-playing.
- **Why Used**: Grounds behavioral expectations through explicit canonical examples, which is critical for change management when training sales reps.
- **Capstone Use Case**: Generating the HubSpot sales representative training module and objection handling guide for Phase 3 staff enablement.
- **Parameter Variables**: `{SALES_CONTEXT}`, `{REQUIRED_ACTION}`, `{TARGET_RESULT}`, `{CANONICAL_EXAMPLE}`
- **Complete Template**:
  ```markdown
  # CONTEXT:
  {SALES_CONTEXT} (Apex Cloud Services reps transitioning from manual spreadsheets to HubSpot deal pipelines).
  # ACTION:
  {REQUIRED_ACTION} (Execute standard deal-stage updating, call logging, and automated quote generation).
  # RESULT:
  {TARGET_RESULT} (100% pipeline visibility, zero untracked customer touchpoints, updated pipeline within 2 hours of deal motion).
  # EXAMPLE:
  {CANONICAL_EXAMPLE} (Show a properly formatted HubSpot deal record for an Enterprise Cloud Migration prospect).
  ```
- **Expected Output**: A step-by-step Standard Operating Procedure (SOP) with realistic before-and-after CRM records.

---

### 8.3 ERA Framework (Expectation, Role, Action)
- **Framework Name**: ERA
- **Purpose**: Rapid tactical queries, operational audits, and sanity checks.
- **Why Used**: Highly compressed structure with minimal token overhead, ideal for quick single-turn validation tasks.
- **Capstone Use Case**: Auditing spreadsheet CSV headers before running HubSpot data ingestion.
- **Parameter Variables**: `{AUDIT_EXPECTATION}`, `{SPECIALIZED_ROLE}`, `{AUDIT_ACTION}`
- **Complete Template**:
  ```markdown
  # EXPECTATION:
  {AUDIT_EXPECTATION} (Verify that all 25 spreadsheet column headers map 1:1 to HubSpot standard contact/deal properties).
  # ROLE:
  {SPECIALIZED_ROLE} (Act as Lead CRM Data Auditor).
  # ACTION:
  {AUDIT_ACTION} (Scan provided column list: identify missing mandatory fields, duplicate headers, and syntax inconsistencies).
  ```
- **Expected Output**: A concise validation table listing Pass/Fail status per field.

---

### 8.4 CO-STAR Framework (Context, Objective, Style, Tone, Audience, Response)
- **Framework Name**: CO-STAR
- **Purpose**: Executive decision support, strategic business proposals, board presentations.
- **Why Used**: Fully calibrates tone, audience perspective, and structural response constraints, preventing generic or informal LLM outputs in corporate governance contexts.
- **Capstone Use Case**: Primary driver for the B2B Business Proposal (`business_proposal.md`) and Master Vendor Evaluation.
- **Parameter Variables**: `{CONTEXT}`, `{OBJECTIVE}`, `{STYLE}`, `{TONE}`, `{AUDIENCE}`, `{RESPONSE}`
- **Complete Template**:
  ```markdown
  # CONTEXT: {ENTERPRISE_BACKGROUND_AND_PROBLEM}
  # OBJECTIVE: {EXPLICIT_DECISION_OR_ANALYSIS_GOAL}
  # STYLE: {PROFESSIONAL_PERSONA_E_G_MCKINSEY_CONSULTANT}
  # TONE: {COMMUNICATION_TONE_E_G_ANALYTICAL_FINANCE_FIRST}
  # AUDIENCE: {EXECUTIVE_DECISION_MAKERS_E_G_BOARD_OF_DIRECTORS}
  # RESPONSE: {PRECISE_MARKDOWN_STRUCTURE_AND_SECTIONS}
  ```
- **Expected Output**: A comprehensive, polished executive document aligned with enterprise C-suite standards.

---

### 8.5 Tree of Thoughts (ToT) Framework
- **Framework Name**: Tree of Thoughts (ToT)
- **Purpose**: Multi-path exploratory reasoning, scenario planning, and strategic risk evaluation.
- **Why Used**: Enables the model to generate multiple competing paths of action, evaluate each path against evaluation criteria, and prune unviable branches before arriving at a synthesis.
- **Capstone Use Case**: Exploring migration cutover strategies (Direct Big Bang vs Phased Cohorts vs Parallel Running) to identify the lowest-risk implementation path.
- **Parameter Variables**: `{DECISION_SCENARIO}`, `{PATH_A}`, `{PATH_B}`, `{PATH_C}`, `{EVALUATION_CRITERIA}`
- **Complete Template**:
  ```markdown
  # SCENARIO: {DECISION_SCENARIO}
  Explore three distinct architectural execution pathways:
  - Branch Alpha: {PATH_A} (e.g. Big-Bang Cutover over a single weekend)
  - Branch Beta: {PATH_B} (e.g. 3-Cohort Phased Migration by sales territory)
  - Branch Gamma: {PATH_C} (e.g. Dual-system Parallel Running for 60 days)

  For each branch:
  1. Project short-term operational disruption and long-term data integrity.
  2. Score resource overhead, rep confusion risk, and failure recovery cost.
  3. Formulate a branch viability verdict (Prune / Viable / Optimal).
  Synthesize the winning branch into an executive migration strategy.
  ```
- **Expected Output**: A branch-by-branch analysis showing rationale for pruning unviable pathways and selecting the 3-Cohort Phased Migration.

---

### 8.6 Quantitative Graph of Thoughts (Q-GoT) Framework
- **Framework Name**: Quantitative Graph of Thoughts (Q-GoT)
- **Purpose**: Complex multi-variable mathematical evaluation, financial modeling, and deterministic arithmetic verification.
- **Why Used**: Standard LLMs predict tokens probabilistically, making multi-step arithmetic highly error-prone (math hallucination). Q-GoT decomposes mathematical tasks into modular computational nodes, computes intermediate values sequentially, and executes self-check equations (e.g., verifying 3 * 1-Year = 3-Year) before presenting numbers.
- **Capstone Use Case**: Exact 1-Year and 3-Year Total Cost of Ownership (TCO) calculations across Salesforce, HubSpot, and Zoho.
- **Parameter Variables**: `{POPULATION}`, `{RATES}`, `{TIMEFRAMES}`, `{FORMULAS}`, `{VERIFICATION_NODES}`
- **Complete Template**:
  ```markdown
  # INPUT PARAMETERS:
  - Population: {POPULATION}
  - Rates: {RATES}
  - Timeframes: {TIMEFRAMES}

  # EXECUTION GRAPH:
  Node [A]: Compute Baseline Annual Subscriptions for each entity.
  Node [B]: Add mandatory initial capital expenditure / onboarding fees.
  Node [C]: Compute Multi-Year Projections.
  Node [D]: Verification Audit -- Execute cross-validation formulas:
            Check 1: Multi-Year Subscriptions == Base Annual * Multiplier.
            Check 2: Delta Matrix == Absolute difference between entity TCOs.
  Node [E]: Synthesize results into audited financial table.
  ```
- **Expected Output**: Deterministically verified financial tables with zero calculation discrepancies.

---

### 8.7 Meta-Prompting Framework
- **Framework Name**: Meta-Prompting
- **Purpose**: Dynamic generation of specialized, domain-tailored system prompts and autonomous prompt optimization.
- **Why Used**: High-level domain tasks require nuanced prompt constraints that manual authoring often overlooks. Meta-Prompting leverages the model's meta-cognitive understanding of prompt architecture to design optimal task prompts.
- **Capstone Use Case**: Autonomous creation of the B2B CRM Researcher system prompt (Section 2.1 & 2.2).
- **Parameter Variables**: `{TARGET_DOMAIN}`, `{TARGET_VENDORS}`, `{OUTPUT_CONSTRAINTS}`, `{FORMAT_RULES}`
- **Complete Template**:
  ```markdown
  Act as an expert Prompt Engineer.
  Write a high-performance system prompt that configures an AI into a specialized {TARGET_DOMAIN} assistant.
  The prompt must enforce:
  - Specific domain coverage: {TARGET_VENDORS}
  - Rigorous constraints: {OUTPUT_CONSTRAINTS}
  - Output standard: {FORMAT_RULES}
  Output the prompt inside a single markdown code block.
  ```
- **Expected Output**: A fully-formed system prompt ready to deploy in an agentic loop or OpenAI custom instructions.
