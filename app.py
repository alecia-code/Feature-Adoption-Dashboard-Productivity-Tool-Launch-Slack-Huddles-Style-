import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("feature_adoption_rollout.csv", parse_dates=["signup_date", "feature_rollout_date"])

st.set_page_config(page_title="Feature Adoption Dashboard", layout="wide")
st.title("🚀 Feature Adoption Dashboard – Productivity Tool Launch")

# Sidebar filters
with st.sidebar:
    st.header("Filter Users")
    segment = st.multiselect("User Segment", df["user_segment"].unique())
    device = st.multiselect("Device Type", df["device_type"].unique())
    prompt = st.multiselect("In-App Prompt Shown", [0, 1])

filtered = df.copy()
if segment:
    filtered = filtered[filtered["user_segment"].isin(segment)]
if device:
    filtered = filtered[filtered["device_type"].isin(device)]
if len(prompt) > 0:
    filtered = filtered[filtered["in_app_prompt_shown"].isin(prompt)]

# KPI cards
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Users", f"{filtered.shape[0]:,}")
col2.metric("Adoption Rate", f"{filtered['feature_used'].mean()*100:.1f}%" if filtered.shape[0] > 0 else "0%")
col3.metric("Avg Days to Adoption", f"{filtered['days_to_adoption'].mean():.1f}" if filtered['days_to_adoption'].notnull().any() else "N/A")
col4.metric("7-Day Retention", f"{filtered['retention_7d'].mean()*100:.1f}%" if filtered.shape[0] > 0 else "0%")
col5.metric("Prompt CTR", f"{(filtered['feature_clicked'].sum() / filtered['in_app_prompt_shown'].sum())*100:.1f}%" if filtered['in_app_prompt_shown'].sum() > 0 else "N/A")

# Time-to-Adoption Curve
st.subheader("📈 Time-to-Adoption Curve")
adoption_curve = filtered[filtered["days_to_adoption"].notnull()]
curve_fig = px.histogram(adoption_curve, x="days_to_adoption", nbins=10,
                         title="Days to Adoption Distribution",
                         labels={"days_to_adoption": "Days to Adoption"})
st.plotly_chart(curve_fig, use_container_width=True)

# Funnel Progression
st.subheader("🔁 Feature Funnel: Login → Click → Use → Revisit")
funnel_data = {
    "Stage": ["Feature Exposed", "Clicked", "Used", "Revisited"],
    "Users": [
        filtered["feature_exposed"].sum(),
        filtered["feature_clicked"].sum(),
        filtered["feature_used"].sum(),
        filtered["feature_revisited"].sum()
    ]
}
funnel_df = pd.DataFrame(funnel_data)
funnel_fig = px.funnel(funnel_df, x="Users", y="Stage", title="User Progression Through Feature")
st.plotly_chart(funnel_fig, use_container_width=True)

# Retention Comparison
st.subheader("📊 Retention by Prompt Exposure")
ret_fig = px.bar(
    filtered.groupby("in_app_prompt_shown")[["retention_7d", "retention_14d"]].mean().reset_index().melt(id_vars="in_app_prompt_shown"),
    x="in_app_prompt_shown", y="value", color="variable", barmode="group",
    labels={"in_app_prompt_shown": "Prompt Shown", "value": "Retention Rate"},
    title="Retention Rate (7d/14d) by Prompt Exposure"
)
st.plotly_chart(ret_fig, use_container_width=True)

# Behavior Change
st.subheader("📉 Post-Feature Activity Change")
change_fig = px.histogram(
    filtered[filtered["post_feature_activity_change"].notnull()],
    x="post_feature_activity_change",
    nbins=30,
    title="Distribution of Activity Change After Feature Use",
    labels={"post_feature_activity_change": "Activity Change (%)"}
)
st.plotly_chart(change_fig, use_container_width=True)