# AI Business Analytics Agent Course

A 90-minute one-on-one advanced Python analytics course project.

## Course theme

**Build an AI-Powered Business Analytics Agent Workflow**

The student learns how to combine:

- Python
- Pandas
- Data cleaning
- Business metrics
- Logistic regression
- AI prompt workflows
- Visualization planning
- Alert/email drafting

## Core principle

> AI is not the source of truth. The data pipeline is.

AI is used for planning, checking assumptions, interpreting verified outputs, and drafting communication. Python is used to calculate all numbers.

## Repo structure

```text
.
├── index.html
├── styles.css
├── script.js
├── README.md
├── requirements.txt
├── prompts.md
├── data/
│   └── raw/
│       ├── customers.csv
│       ├── orders.csv
│       ├── order_items.csv
│       ├── payments.csv
│       ├── reviews.csv
│       └── activity.csv
├── scripts/
│   ├── generate_synthetic_data.py
│   └── download_olist_kaggle.py
├── src/
│   └── agent_workflow.py
└── notebooks/
    └── 01_agent_workflow_starter.py
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
# .venv\Scripts\activate  # Windows

pip install -r requirements.txt
python scripts/generate_synthetic_data.py
python src/agent_workflow.py
```

Outputs will be written to:

```text
outputs/
├── monthly_metrics.csv
├── channel_metrics.csv
├── order_fact.csv
├── table_summary.json
├── quality_report.json
├── alert_payload.json
└── alert_email.txt
```

## Use as a website

This is a static website. Open:

```text
index.html
```

Or deploy it through GitHub Pages.

## Upload to GitHub

```bash
git init
git add .
git commit -m "Add AI business analytics agent course"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-business-analytics-agent-course.git
git push -u origin main
```

Then enable GitHub Pages:

1. Go to the repo on GitHub.
2. Settings → Pages.
3. Source: Deploy from a branch.
4. Branch: `main`.
5. Folder: `/root`.
6. Save.

The site will become available at:

```text
https://YOUR_USERNAME.github.io/ai-business-analytics-agent-course/
```

## Data strategy

This repo includes **synthetic ecommerce data** that can be safely uploaded to GitHub and used immediately in class.

For a more realistic second version, you can optionally download the Olist Brazilian E-Commerce Public Dataset from Kaggle using:

```bash
pip install kaggle
python scripts/download_olist_kaggle.py
```

Check Kaggle's dataset license before redistributing the full raw dataset.

## 90-minute lesson flow

| Time | Module |
|---:|---|
| 0–10 min | Business question + metric contract |
| 10–20 min | Read data + schema inspection |
| 20–32 min | Data quality agent |
| 32–50 min | Metric tools + feature engineering |
| 50–68 min | Statistical modeling agent |
| 68–80 min | Insight + visualization agent |
| 80–90 min | Alert/email agent |

## Statistical modeling section

Recommended model:

```text
low_review ~ delivery_days_clean + payment_value + freight_value
```

This uses logistic regression to explain whether longer delivery delay is associated with higher low-review risk after controlling for order value and freight value.

Students learn:

- Target variable design
- Logistic regression
- Coefficients
- Odds ratios
- p-values
- Control variables
- Why association is not causality

## Agent workflow

| Agent | Responsibility |
|---|---|
| Data Reader Agent | Inspect schema, row counts, dtypes, joins |
| Data Quality Agent | Detect missing values, duplicates, invalid dates |
| Metric Agent | Calculate verified business metrics |
| Statistical Modeling Agent | Run interpretable model and explain uncertainty |
| Insight Agent | Convert verified outputs into business interpretation |
| Alert Agent | Detect threshold breaches and draft email |

## Teaching note

For a one-on-one student, this should be taught as pair programming:

1. Let the student inspect schema.
2. Let the student define metric denominators.
3. Let the student write one function.
4. You demonstrate the modeling section.
5. Let the student critique the AI-generated insight.
