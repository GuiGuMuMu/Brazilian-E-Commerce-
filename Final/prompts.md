# AI Prompts for Each Workflow Step

Use these prompts at the exact moments shown in the class schedule.
Rule: Python calculates the number first. AI interprets it second.

---

## Step 1 — Planning the Analysis (0–10 min)

**Use before touching code.**

```
I'm analyzing Brazilian e-commerce data with these tables:
customers (customer_id, signup_date, state, acquisition_channel, customer_segment, age)
orders (order_id, customer_id, order_purchase_date, order_status, delivery_days, order_delivered_date)
order_items (order_id, order_item_id, product_category, price, freight_value)
payments (order_id, payment_type, payment_installments, payment_value)
reviews (order_id, review_score, review_date)
activity (customer_id, activity_date, session_count, email_opened)

The business question is: Revenue dropped last month. What are the five most important
diagnostic metrics I should compute first, and what denominator should I use for each?
List them as a table: metric | numerator | denominator | filter.
```

**Why:** Forces the student to see that metrics have definitions — you can't just run a sum.

---

## Step 2 — Data Quality Planning (before running quality agent)

**Use before running `data_quality_agent()`.**

```
Before I run my data quality checks, what are the five most common data quality problems
in e-commerce order datasets that would silently corrupt these specific metrics:
- Monthly revenue
- Average delivery time
- Low-review rate
- Customer acquisition channel split

For each problem, explain what the corrupted metric would look like versus the clean version.
```

**Why:** Gets the student to predict issues before seeing them — builds intuition.

---

## Step 3 — Interpreting the Quality Report (after running quality agent)

**Paste the quality_report output into this prompt.**

```
Here is my data quality report:
[PASTE quality_report dict here]

For each issue, confirm whether my proposed fix is correct and flag any risks
I haven't considered. Do not calculate any new numbers. Only interpret the
findings I have already verified in Python.
```

**Why:** Shows AI in the right role — interpreter, not calculator.

---

## Step 4 — Interpreting Cleaning Impact

**Paste the cleaning_impact output.**

```
My Python cleaning script produced these before-vs-after changes:
[PASTE cleaning_impact dict here]

In plain English, explain what each change means for how the business should
interpret the metrics. Flag any assumptions that need to be documented in
a stakeholder report.
```

---

## Step 5 — Metric Contract Review (after computing metrics)

**Paste monthly and channel metrics.**

```
Here are the verified monthly and channel metrics computed in Python:
[PASTE monthly_metrics tail]
[PASTE channel_metrics]

Summarize the three most important business observations. Do not invent numbers.
Only reference the rows and columns in the data I provided.
```

**Why:** This is the hallucination-prevention demo. Tell the student to check if
AI adds any numbers that aren't in the output. It often will.

---

## Step 6 — Interpreting the Logistic Regression (after fitting model)

**Paste the model_result dict.**

```
Here are the results of a logistic regression predicting low_review
(review score 1 or 2) from delivery_days_clean, payment_value, and freight_value:

[PASTE model_result dict]

Interpret the significant predictors using odds ratios. Explain what a business
manager should conclude — and what they should NOT conclude. Do not claim causality.
Use simple language.
```

**Why:** Students often conflate "associated with" and "causes." This prompt forces
the AI to model the correct framing.

---

## Step 7 — Visualization Planning (before generating charts)

```
I have these verified metrics:
- Monthly revenue with MoM % change
- Revenue and low-review rate by acquisition channel
- Distribution of delivery days broken out by review score (1–5)

For each dataset, suggest one chart type that would make the business insight
immediately clear to a non-technical audience. Justify the choice.
Do not suggest more than one chart per dataset.
```

---

## Step 8 — Alert Email Refinement (after generating draft)

**Paste the alert email draft.**

```
Here is a draft alert email generated from verified Python outputs:
[PASTE email_draft]

Improve the tone and clarity for a business audience without changing any numbers.
Add one recommendation sentence that a data team lead would include.
Do not invent data. Flag any part of the email that should be verified before sending.
```

---

## Anti-patterns to show the student

Run these prompts to demonstrate AI hallucination risks:

**Bad prompt (never do this):**
```
What was our revenue last month and which channel performed best?
```
→ AI will invent numbers. The student should see this fail.

**Good prompt:**
```
Based only on the following Python output [paste data], what was our revenue
last month and which channel had the highest revenue?
```
→ AI is constrained to verified data.

---

## When to NOT use AI

- Calculating any number (use Python)
- Deciding what the metric denominator should be (use business logic)
- Diagnosing data quality issues (use Python checks)
- Choosing statistical model parameters (use your judgment)
- Approving an alert email for actual stakeholders (human review required)
