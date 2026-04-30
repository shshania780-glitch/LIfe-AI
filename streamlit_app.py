import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

from app import predict_lifestyle_score

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Life AI Dashboard",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {background: linear-gradient(135deg,#F3F4F6,#E5E7EB);}
.stMetric {
    background:white;padding:20px;border-radius:12px;border-top:4px solid #10B981;
}
.header-card {
    background:linear-gradient(135deg,#10B981,#059669);
    color:white;padding:30px;border-radius:12px;margin-bottom:30px;
}
.score-card {
    background:linear-gradient(135deg,#F59E0B,#D97706);
    color:white;padding:30px;border-radius:12px;text-align:center;
}
.score-value {font-size:3em;font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# ---------------- SAMPLE DATA ----------------
sample_data = {
    'username': 'John Doe',
    'email': 'john@example.com',
    'total_entries': 12,
    'latest_score': 87,
    'avg_sleep': 7.5,
    'avg_exercise': 3.2,
    'entries': [
        {'date':'2026-04-29','sleep_hours':8.3,'exercise_hours':3.7,'diet_quality':'Excellent','lifestyle_score':100,'address':'New York'},
        {'date':'2026-04-28','sleep_hours':6.9,'exercise_hours':1.5,'diet_quality':'Good','lifestyle_score':70,'address':'New York'},
        {'date':'2026-04-27','sleep_hours':7.4,'exercise_hours':3.6,'diet_quality':'Excellent','lifestyle_score':100,'address':'New York'},
    ]
}

if 'records' not in st.session_state:
    st.session_state.records = sample_data['entries'].copy()

records = st.session_state.records

df = pd.DataFrame(records).copy()
if not df.empty:
    df['date'] = pd.to_datetime(df['date'])

records_count = len(records)
latest_record = df.sort_values('date', ascending=False).iloc[0] if not df.empty else None
latest_score = latest_record['lifestyle_score'] if latest_record is not None else 0
avg_sleep = df['sleep_hours'].mean() if not df.empty else 0
avg_exercise = df['exercise_hours'].mean() if not df.empty else 0

diet_options = ["Poor", "Fair", "Good", "Excellent"]

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎯 Life AI Dashboard")
page = st.sidebar.radio(
    "Navigation",
    ["📊 Dashboard", "📈 Analytics", "🧬 Predict", "⚙️ Settings", "ℹ️ About"]
)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header-card">
<h1>🎯 Welcome to Life AI Dashboard</h1>
<p>Track your lifestyle and get AI-powered insights</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# 📊 DASHBOARD PAGE
# ============================================================
if page == "📊 Dashboard":

    st.header("📊 Dashboard")

    col1,col2,col3,col4 = st.columns(4)
    col1.metric("Total Entries", records_count)
    col2.metric("Latest Score", f"{latest_score}/100")
    col3.metric("Avg Sleep", f"{avg_sleep:.1f}h")
    col4.metric("Avg Exercise", f"{avg_exercise:.1f}h")

    if df.empty:
        st.warning("No data available yet.")
        st.stop()

    latest = df.sort_values('date', ascending=False).iloc[0]

    col1,col2 = st.columns([2,1])

    with col1:
        st.subheader("Latest Lifestyle Assessment")
    
        # a.info(f"Sleep\n{latest['sleep_hours']}h")
        # b.info(f"Exercise\n{latest['exercise_hours']}h")
        # c.info(f"Diet\n{latest['diet_quality']}")
        # d.info(f"Location\n{latest['address']}")

    with col2:
        st.markdown(f"""
        <div class="score-card">
        <p>Score</p>
        <div class="score-value">{latest['lifestyle_score']}</div>
        <p>Out of 100</p>
        </div>
        """, unsafe_allow_html=True)

    # st.subheader("Recent History")
    # st.dataframe(
    #     df[['date','sleep_hours','exercise_hours','diet_quality','lifestyle_score']],
    #     use_container_width=True,
    #     hide_index=True
    # )

# ============================================================
# 📈 ANALYTICS PAGE
# ============================================================
elif page == "📈 Analytics":

    st.header("📈 Analytics")

    if df.empty:
        st.warning("No data to analyze.")
        st.stop()

    df['date'] = pd.to_datetime(df['date'])

    col1,col2 = st.columns(2)
    fig1 = px.line(df,x='date',y='sleep_hours',markers=True,title="Sleep Trend")
    col1.plotly_chart(fig1,use_container_width=True)

    fig2 = px.bar(df,x='date',y='exercise_hours',title="Exercise Trend")
    col2.plotly_chart(fig2,use_container_width=True)

    col3,col4 = st.columns(2)
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x=df['date'],y=df['lifestyle_score'],mode='lines+markers'))
    fig3.update_layout(title="Lifestyle Score Trend")
    col3.plotly_chart(fig3,use_container_width=True)

    diet_counts = df['diet_quality'].value_counts()
    fig4 = px.pie(values=diet_counts.values,names=diet_counts.index,title="Diet Distribution")
    col4.plotly_chart(fig4,use_container_width=True)

# ============================================================
# 🧬 PREDICT PAGE
# ============================================================
elif page == "🧬 Predict":
    st.header("🧬 Lifestyle Prediction")
    with st.form("prediction_form"):
        address = st.text_input("Address", value="New York")
        sleep_hours = st.number_input("Sleep Hours", min_value=0.0, max_value=24.0, value=7.5, step=0.1)
        exercise_hours = st.number_input("Exercise Hours", min_value=0.0, max_value=24.0, value=2.0, step=0.1)
        diet_quality = st.selectbox("Diet Quality", diet_options)
        submit = st.form_submit_button("Predict Lifestyle Score")

    if submit:
        try:
            score = predict_lifestyle_score(sleep_hours, exercise_hours, diet_quality)
            new_record = {
                'date': datetime.now().strftime('%Y-%m-%d'),
                'sleep_hours': sleep_hours,
                'exercise_hours': exercise_hours,
                'diet_quality': diet_quality,
                'lifestyle_score': score,
                'address': address
            }
            st.session_state.records.append(new_record)
            records = st.session_state.records
            df = pd.DataFrame(records).copy()
            df['date'] = pd.to_datetime(df['date'])
            latest_record = df.sort_values('date', ascending=False).iloc[0]

            st.success(f"Predicted lifestyle score: {score}/100")
            st.markdown(
                f"""
                <div class=\"score-card\">
                <p>Predicted Score</p>
                <div class=\"score-value\">{score}</div>
                <p>Based on your current lifestyle inputs</p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown("### Latest Assessment")
            st.write(
                f"Sleep: {latest_record['sleep_hours']}h  |  "
                f"Exercise: {latest_record['exercise_hours']}h  |  "
                f"Diet: {latest_record['diet_quality']}  |  "
                f"Score: {latest_record['lifestyle_score']}/100"
            )
        except Exception as e:
            st.error(f"Prediction failed: {e}")

# ============================================================
# ⚙️ SETTINGS PAGE
# ============================================================
elif page == "⚙️ Settings":

    st.header("Settings")

    col1,col2 = st.columns(2)
    col1.text_input("Username", value=sample_data['username'], disabled=True)
    col1.text_input("Email", value=sample_data['email'], disabled=True)

    if col2.button("Change Password"):
        st.info("Password change page coming soon")

    if st.button("Save Preferences"):
        st.success("Preferences saved!")

# ============================================================
# ℹ️ ABOUT PAGE
# ============================================================
else:
    st.header("About Life AI")
    st.write("Life AI is a smart lifestyle tracking app. Track sleep, exercise, diet and get AI score.")

st.markdown("---")
st.caption("© 2026 Life AI Dashboard")