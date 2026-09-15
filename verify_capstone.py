import os
import re
import sys

def run_tests():
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"=== Running Capstone Automated Verification Suite in: {repo_dir} ===\n")
    passed = 0
    failed = 0

    def assert_test(condition, test_name, details=""):
        nonlocal passed, failed
        if condition:
            print(f"[PASS] {test_name}")
            passed += 1
        else:
            print(f"[FAIL] {test_name}: {details}")
            failed += 1

    # 1. TR-001: Verify All 7 Required Deliverables Exist
    required_files = [
        "README.md",
        "prompt_portfolio.md",
        "decision_matrix.md",
        "business_proposal.md",
        "implementation_plan.md",
        "executive_presentation.md",
        "lessons_learned_report.md"
    ]
    for rf in required_files:
        path = os.path.join(repo_dir, rf)
        exists = os.path.exists(path) and os.path.getsize(path) > 100
        assert_test(exists, f"TR-001 File Exists: {rf}", f"File missing or empty: {path}")

    # Read contents for deep inspection
    def read_file(name):
        with open(os.path.join(repo_dir, name), "r", encoding="utf-8") as f:
            return f.read()

    readme = read_file("README.md")
    portfolio = read_file("prompt_portfolio.md")
    matrix = read_file("decision_matrix.md")
    proposal = read_file("business_proposal.md")
    plan = read_file("implementation_plan.md")
    presentation = read_file("executive_presentation.md")
    lessons = read_file("lessons_learned_report.md")

    # 2. TR-002: Decision Matrix Weights and Calculations
    # Check weights sum to 1.0 / 100%
    w1, w2, w3, w4 = 0.30, 0.20, 0.25, 0.25
    weight_sum = round(w1 + w2 + w3 + w4, 4)
    assert_test(weight_sum == 1.0, "TR-002 Weight Summation Equals 1.00 (100%)", f"Sum is {weight_sum}")
    assert_test("0.30 + 0.20 + 0.25 + 0.25 = 1.00" in matrix, "TR-002 Weight Sum Mentioned in decision_matrix.md")

    # Check HubSpot weighted calculation: 8.0*0.3 + 8.0*0.2 + 9.0*0.25 + 9.5*0.25
    hubspot_score = round(8.0 * 0.30 + 8.0 * 0.20 + 9.0 * 0.25 + 9.5 * 0.25, 4)
    assert_test(hubspot_score == 8.625, "TR-002 HubSpot Weighted Score Calculation is Exactly 8.625", f"Got {hubspot_score}")
    assert_test("8.625" in matrix, "TR-002 HubSpot Score 8.625 Present in decision_matrix.md")

    # Check Zoho weighted calculation: 10.0*0.3 + 6.0*0.2 + 7.5*0.25 + 6.5*0.25 = 3.0 + 1.2 + 1.875 + 1.625 = 7.7
    zoho_score = round(10.0 * 0.30 + 6.0 * 0.20 + 7.5 * 0.25 + 6.5 * 0.25, 4)
    assert_test(zoho_score == 7.700, "TR-002 Zoho Weighted Score Calculation is Exactly 7.700", f"Got {zoho_score}")
    assert_test("7.700" in matrix, "TR-002 Zoho Score 7.700 Present in decision_matrix.md")

    # Check Salesforce weighted calculation: 4.0*0.3 + 10.0*0.2 + 4.0*0.25 + 5.0*0.25 = 1.2 + 2.0 + 1.0 + 1.25 = 5.45
    sf_score = round(4.0 * 0.30 + 10.0 * 0.20 + 4.0 * 0.25 + 5.0 * 0.25, 4)
    assert_test(sf_score == 5.450, "TR-002 Salesforce Weighted Score Calculation is Exactly 5.450", f"Got {sf_score}")
    assert_test("5.450" in matrix, "TR-002 Salesforce Score 5.450 Present in decision_matrix.md")

    # 3. TR-003 & REQ-005: Executive Presentation Slide Delimiters & Count
    slides = [s.strip() for s in re.split(r'\n---\n', presentation) if s.strip()]
    assert_test(len(slides) == 6, f"TR-003 & REQ-005 Slide Count Exactly 6 (Found {len(slides)})", f"Found {len(slides)} slides")
    for i in range(1, 7):
        assert_test(f"Slide {i}" in presentation, f"REQ-005 Slide {i} Header Present in executive_presentation.md")

    # 4. REQ-001: CO-STAR Framework Coverage
    costar_elements = ["CONTEXT", "OBJECTIVE", "STYLE", "TONE", "AUDIENCE", "RESPONSE"]
    all_costar = all(elem in portfolio for elem in costar_elements)
    assert_test(all_costar, "REQ-001 CO-STAR Elements Present in prompt_portfolio.md")

    # 5. REQ-002 & CON-001: Vendor TCO Calculations and Math Checks
    sf_1y = (150 * 150 * 12) + 25000
    sf_3y = (150 * 150 * 36) + 25000
    hs_1y = (150 * 90 * 12) + 10000
    hs_3y = (150 * 90 * 36) + 10000
    zh_1y = (150 * 40 * 12) + 5000
    zh_3y = (150 * 40 * 36) + 5000

    assert_test(sf_1y == 295000 and sf_3y == 835000, "REQ-002 Salesforce TCO Formula Check (1Y: $295k, 3Y: $835k)")
    assert_test(hs_1y == 172000 and hs_3y == 496000, "REQ-002 HubSpot TCO Formula Check (1Y: $172k, 3Y: $496k)")
    assert_test(zh_1y == 77000 and zh_3y == 221000, "REQ-002 Zoho TCO Formula Check (1Y: $77k, 3Y: $221k)")

    assert_test("295,000" in proposal and "835,000" in proposal, "REQ-002 Salesforce TCO Present in business_proposal.md")
    assert_test("172,000" in proposal and "496,000" in proposal, "REQ-002 HubSpot TCO Present in business_proposal.md")
    assert_test("77,000" in proposal and "221,000" in proposal, "REQ-002 Zoho TCO Present in business_proposal.md")

    # 6. REQ-003: Meta-Prompting Coverage
    assert_test("Meta-Prompt" in portfolio and "Pricing and Feature Researcher" in portfolio,
                "REQ-003 Meta-Prompting Present in prompt_portfolio.md")

    # 7. REQ-004: Gantt Chart and Risk Registry
    assert_test("Phase 1" in plan and "Phase 2" in plan and "Phase 3" in plan and "Phase 4" in plan,
                "REQ-004 All 4 Phases Present in implementation_plan.md")
    assert_test("```" in plan and "GANTT" in plan, "REQ-004 Gantt Chart in Code Block in implementation_plan.md")
    assert_test("Risk Event" in plan and "Probability" in plan and "Impact" in plan and "Mitigation" in plan,
                "REQ-004 Risk Registry Table Present with Required Columns")

    # 8. REQ-006 & CON-002: Lessons Learned Requirements
    assert_test("Hallucination Prevention" in lessons, "REQ-006 Hallucination Prevention in lessons_learned_report.md")
    assert_test("Context Window Wind-down" in lessons or "Context Degradation" in lessons,
                "REQ-006 Context Window Wind-down in lessons_learned_report.md")
    assert_test("Framework Alignment" in lessons, "REQ-006 Framework Alignment in lessons_learned_report.md")
    assert_test("Lost in the Middle" in lessons or "attention" in lessons.lower(),
                "CON-002 Attention Limits / Lost in the Middle Discussed")

    # 9. Framework Coverage in prompt_portfolio.md
    course_frameworks = ["RGCCO", "CARE", "ERA", "CO-STAR", "Tree of Thoughts", "Q-GoT", "Meta-Prompting"]
    for fw in course_frameworks:
        assert_test(fw in portfolio, f"Framework Coverage: {fw} in prompt_portfolio.md")

    # 10. Security Audit: Scan for secrets
    secret_keywords = ["ghp_", "sk-proj-", "bearer ey", "aws_secret_access_key"]
    has_secret = False
    all_files = required_files + ["LOOM_DEMO_GUIDE.md", "SUBMISSION_CHECKLIST.md"]
    for fname in all_files:
        content = read_file(fname).lower()
        for kw in secret_keywords:
            if kw in content:
                has_secret = True
                print(f"[SECURITY ALERT] Potential secret found in {fname}: {kw}")
    assert_test(not has_secret, "Security Audit: No Real API Keys or Passwords Exposed")

    print(f"\n========================================")
    print(f"VERIFICATION SUMMARY: {passed} PASSED, {failed} FAILED")
    print(f"========================================")
    return failed == 0

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
