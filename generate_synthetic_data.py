<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI Business Analytics Agent Workflow</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <header class="hero">
    <nav>
      <div class="logo">AI Analytics Agent</div>
      <a href="https://github.com/" target="_blank" rel="noreferrer">Deploy on GitHub</a>
    </nav>
    <section class="hero-content">
      <p class="eyebrow">90-minute 1:1 Python + Statistics + AI course</p>
      <h1>Build an AI-Powered Business Analytics Agent Workflow</h1>
      <p class="subtitle">
        Students learn how to combine Pandas, statistical modeling, visualization,
        and AI prompts into a controlled analyst workflow.
      </p>
      <div class="cta-row">
        <a class="button primary" href="#workflow">View Workflow</a>
        <a class="button secondary" href="#data">Dataset Plan</a>
      </div>
    </section>
  </header>

  <main>
    <section class="section" id="outcome">
      <div class="section-label">Course outcome</div>
      <h2>What the student will build</h2>
      <div class="outcome-grid">
        <div class="card">
          <h3>Business Problem</h3>
          <p>Revenue dropped this month. Is it traffic, conversion, retention, order value, customer experience, or data quality?</p>
        </div>
        <div class="card">
          <h3>Agent Workflow</h3>
          <p>Data Reader → Quality Agent → Metric Agent → Statistical Modeling Agent → Insight Agent → Alert Agent.</p>
        </div>
        <div class="card">
          <h3>Final Deliverable</h3>
          <p>A notebook and Python scripts that produce verified metrics, a model interpretation, a chart plan, and an email alert draft.</p>
        </div>
      </div>
    </section>

    <section class="section" id="workflow">
      <div class="section-label">Agent workflow</div>
      <h2>Pipeline architecture</h2>
      <div class="pipeline">
        <div class="step"><span>1</span><strong>Read Data</strong><p>Load raw CSVs and inspect schema.</p></div>
        <div class="step"><span>2</span><strong>Quality Agent</strong><p>Find missing values, duplicates, invalid dates, and risky assumptions.</p></div>
        <div class="step"><span>3</span><strong>Metric Agent</strong><p>Calculate revenue, AOV, repeat purchase, review score, delivery delay, and churn proxy.</p></div>
        <div class="step"><span>4</span><strong>Modeling Agent</strong><p>Use logistic regression to explain low-review risk with interpretable statistics.</p></div>
        <div class="step"><span>5</span><strong>Insight Agent</strong><p>Translate verified Python outputs into business language without hallucination.</p></div>
        <div class="step"><span>6</span><strong>Alert Agent</strong><p>Detect threshold breaches and draft an email alert.</p></div>
      </div>
    </section>

    <section class="section split" id="schedule">
      <div>
        <div class="section-label">90-minute plan</div>
        <h2>Class schedule</h2>
        <p>
          The course starts with a metric contract instead of raw code. This helps the student understand that AI analytics workflows must be grounded in definitions, denominators, and verified Python outputs.
        </p>
      </div>
      <div class="schedule-list">
        <div><strong>0–10 min</strong><span>Business question + metric contract</span></div>
        <div><strong>10–20 min</strong><span>Read data + schema inspection</span></div>
        <div><strong>20–32 min</strong><span>Data quality agent</span></div>
        <div><strong>32–50 min</strong><span>Metric tools + feature engineering</span></div>
        <div><strong>50–68 min</strong><span>Logistic regression modeling agent</span></div>
        <div><strong>68–80 min</strong><span>Insight + visualization agent</span></div>
        <div><strong>80–90 min</strong><span>Alert / email agent</span></div>
      </div>
    </section>

    <section class="section" id="model">
      <div class="section-label">Not-too-simple statistics</div>
      <h2>Statistical model: low-review risk</h2>
      <div class="code-card">
        <pre><code>low_review ~ delivery_days_clean + payment_value + freight_value</code></pre>
      </div>
      <p>
        The model uses logistic regression to test whether delivery delay is associated with low-review risk after controlling for payment value and freight value. Students learn coefficients, p-values, odds ratios, and why correlation does not imply causation.
      </p>
    </section>

    <section class="section split" id="data">
      <div>
        <div class="section-label">Data source</div>
        <h2>Teaching data strategy</h2>
        <p>
          This repo includes synthetic ecommerce CSVs so the student can start immediately without Kaggle setup. It also includes an optional Kaggle download script for the real Olist Brazilian Ecommerce dataset.
        </p>
      </div>
      <div class="data-table">
        <div><strong>customers.csv</strong><span>Customer profile, channel, state, segment, age</span></div>
        <div><strong>orders.csv</strong><span>Order dates, delivery dates, status, delivery days</span></div>
        <div><strong>order_items.csv</strong><span>Product category, item count, price, freight</span></div>
        <div><strong>payments.csv</strong><span>Payment type, installment count, payment value</span></div>
        <div><strong>reviews.csv</strong><span>Review score and review date</span></div>
        <div><strong>activity.csv</strong><span>Session count, email opened, activity date</span></div>
      </div>
    </section>

    <section class="section" id="guardrails">
      <div class="section-label">AI guardrails</div>
      <h2>Course principle</h2>
      <blockquote>
        AI is not the source of truth. The data pipeline is.
      </blockquote>
      <div class="guardrail-grid">
        <div class="card"><h3>AI can plan</h3><p>Ask AI to propose analysis steps and data quality checks.</p></div>
        <div class="card"><h3>Python must verify</h3><p>All numbers must come from Pandas, not from the LLM.</p></div>
        <div class="card"><h3>Humans decide</h3><p>The analyst reviews assumptions, caveats, and recommendations.</p></div>
      </div>
    </section>
  </main>

  <footer>
    <p>Built for a 90-minute one-on-one advanced Python analytics course.</p>
  </footer>

  <script src="script.js"></script>
</body>
</html>
