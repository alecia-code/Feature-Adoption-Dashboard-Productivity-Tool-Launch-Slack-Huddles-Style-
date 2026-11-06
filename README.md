# Feature Adoption Dashboard Productivity Tool Launch Slack Huddles Style 

**Portfolio case study | Synthetic data | Python, pandas, Streamlit, Plotly**

## Business question
Evaluate feature rollout, exposure-to-adoption funnel, prompt engagement, and retention.

## Analyst approach
1. Define the operational decision and measurable KPIs.
2. Segment the simulated records using dashboard controls.
3. Compare trends and flag exceptions for investigation.
4. Check metric definitions and filter consistency before presenting findings.

## Dashboard and metrics
The Streamlit app provides interactive filters, KPI summaries, and charts. Run it locally to explore how the selected segments change the results. The data is **synthetic**: findings are demonstrations of analytical methods, not observed customer outcomes.

## Quality assurance and interpretation
Prompt CTR uses clicks among exposed users over exposed users. Funnel stages are counts of event flags; ensure events are nested before interpreting as strict funnel conversion. Retention comparisons are observational, not causal.

**Validation checklist:** confirm the dataset loads; verify KPI numerators/denominators against pandas calculations; test each filter alone and combined; check zero-row and zero-denominator selections; confirm every chart responds to the same filtered dataset; review charts for misleading causal claims.

## Tools and reproduction
```bash
python -m pip install -r requirements.txt
streamlit run app.py
```
The CSV in this repository is simulated sample data. The original case-study document is retained as a supplemental artifact; this README documents the current analytical approach.

## What this demonstrates
Business problem framing, KPI design, data exploration, operational reporting, dashboard development, and analytical QA. This is an independent portfolio exercise, not a client engagement or production deployment.
