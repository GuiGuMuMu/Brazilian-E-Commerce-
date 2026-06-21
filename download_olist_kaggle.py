* {
  box-sizing: border-box;
}

:root {
  --bg: #0b1020;
  --bg-2: #111a32;
  --card: rgba(255, 255, 255, 0.08);
  --text: #f5f7fb;
  --muted: #b9c2d0;
  --accent: #71e8c5;
  --accent-2: #8aa4ff;
  --border: rgba(255, 255, 255, 0.14);
}

body {
  margin: 0;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  background: radial-gradient(circle at top left, #21335f 0, var(--bg) 38%, #070a14 100%);
  color: var(--text);
  line-height: 1.6;
}

a {
  color: inherit;
}

.hero {
  min-height: 92vh;
  padding: 28px;
  display: flex;
  flex-direction: column;
}

nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1120px;
  width: 100%;
  margin: 0 auto;
}

.logo {
  font-weight: 800;
  letter-spacing: 0.03em;
}

nav a {
  color: var(--muted);
  text-decoration: none;
  border: 1px solid var(--border);
  padding: 8px 14px;
  border-radius: 999px;
}

.hero-content {
  max-width: 1120px;
  width: 100%;
  margin: auto;
  padding: 90px 0;
}

.eyebrow,
.section-label {
  color: var(--accent);
  text-transform: uppercase;
  font-size: 0.78rem;
  letter-spacing: 0.16em;
  font-weight: 800;
}

h1 {
  font-size: clamp(3rem, 8vw, 6.8rem);
  line-height: 0.95;
  max-width: 1000px;
  margin: 20px 0;
}

h2 {
  font-size: clamp(2rem, 4vw, 3.5rem);
  line-height: 1.05;
  margin: 12px 0 20px;
}

h3 {
  margin-top: 0;
}

.subtitle {
  color: var(--muted);
  font-size: 1.3rem;
  max-width: 760px;
}

.cta-row {
  display: flex;
  gap: 14px;
  margin-top: 32px;
  flex-wrap: wrap;
}

.button {
  text-decoration: none;
  padding: 14px 20px;
  border-radius: 14px;
  font-weight: 700;
}

.button.primary {
  background: var(--accent);
  color: #05121a;
}

.button.secondary {
  border: 1px solid var(--border);
  color: var(--text);
}

.section {
  max-width: 1120px;
  margin: 0 auto;
  padding: 88px 28px;
}

.outcome-grid,
.guardrail-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.card,
.step,
.code-card,
.data-table,
.schedule-list {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 24px;
  backdrop-filter: blur(14px);
}

.card p,
.step p,
.section p {
  color: var(--muted);
}

.pipeline {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.step span {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, var(--accent), var(--accent-2));
  color: #07101d;
  width: 36px;
  height: 36px;
  border-radius: 999px;
  font-weight: 900;
  margin-bottom: 18px;
}

.step strong {
  display: block;
  font-size: 1.15rem;
}

.split {
  display: grid;
  grid-template-columns: 0.95fr 1.05fr;
  gap: 42px;
  align-items: start;
}

.schedule-list,
.data-table {
  display: grid;
  gap: 14px;
}

.schedule-list div,
.data-table div {
  display: grid;
  grid-template-columns: 120px 1fr;
  gap: 18px;
  border-bottom: 1px solid var(--border);
  padding-bottom: 12px;
}

.schedule-list div:last-child,
.data-table div:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.schedule-list span,
.data-table span {
  color: var(--muted);
}

.code-card {
  overflow-x: auto;
}

pre {
  margin: 0;
  font-size: 1.1rem;
}

blockquote {
  font-size: clamp(1.8rem, 4vw, 3.4rem);
  line-height: 1.1;
  margin: 28px 0;
  color: var(--accent);
  font-weight: 900;
}

footer {
  text-align: center;
  color: var(--muted);
  padding: 42px 28px;
  border-top: 1px solid var(--border);
}

@media (max-width: 820px) {
  .outcome-grid,
  .guardrail-grid,
  .pipeline,
  .split {
    grid-template-columns: 1fr;
  }

  .schedule-list div,
  .data-table div {
    grid-template-columns: 1fr;
    gap: 4px;
  }

  nav {
    align-items: flex-start;
    gap: 12px;
  }
}
