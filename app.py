import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="HR Analytics | Solutions by STC",
    layout="wide"
)

# ==================================================
# BRAND COLORS
# ==================================================
STC_PURPLE = "#6D28D9"
STC_GREEN = "#10B981"
STC_RED = "#EF4444"
BG_LIGHT = "#F6F0FA"

# ==================================================
# GLOBAL STYLING  ✅ CLEAN & SAFE
# ==================================================
st.markdown(f"""
<style>

/* App background */
.stApp {{
    background: linear-gradient(135deg, {BG_LIGHT} 0%, #FFFFFF 70%);
}}

/* Sidebar background */
section[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #4B1D6B 0%, #3A1558 100%);
}}

/* Sidebar text */
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p {{
    color: white !important;
}}

/* Selectbox input (VISIBLE TEXT FIX) */
section[data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"] > div {{
    background-color: white !important;
    color: #1F2937 !important;
    border-radius: 8px;
}}

/* Dropdown options */
section[data-testid="stSidebar"] .stSelectbox span {{
    color: #1F2937 !important;
}}

/* KPI Cards */
.kpi-card {{
    background: white;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    border-left: 6px solid {STC_PURPLE};
}}

.kpi-title {{
    font-size: 12px;
    color: #6B7280;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}}

.kpi-value {{
    font-size: 34px;
    font-weight: 700;
    color: {STC_PURPLE};
}}

</style>
""", unsafe_allow_html=True)

# ==================================================
# LOAD DATA
# ==================================================
@st.cache_data
def load_data():
    conn = sqlite3.connect("hr.db")
    df = pd.read_sql("SELECT * FROM employees", conn)
    conn.close()
    return df

df = load_data()

# ==================================================
# SIDEBAR FILTER
# ==================================================
st.sidebar.markdown("### Filters")

departments = ["All Departments"] + sorted(df["department"].unique().tolist())

selected_department = st.sidebar.selectbox(
    "Department",
    departments,
    index=0
)

# Filtered dataframe (BEST PRACTICE)
if selected_department != "All Departments":
    df_filtered = df[df["department"] == selected_department]
else:
    df_filtered = df.copy()

# ==================================================
# HEADER (SHOW SELECTED DEPARTMENT)
# ==================================================
dept_label = "All Departments" if selected_department == "All Departments" else f"Department: {selected_department}"

st.markdown(
    f"""
    <h2 style="color:{STC_PURPLE}; margin-bottom:0;">
        HR Analytics Dashboard
    </h2>
    <p style="color:#6B7280; margin-top:4px;">
        Solutions by STC — Executive Workforce View
    </p>
    <p style="color:{STC_GREEN}; font-weight:600; margin-top:2px;">
        {dept_label}
    </p>
    """,
    unsafe_allow_html=True
)

# ==================================================
# KPI ROW
# ==================================================
k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Employees</div>
        <div class="kpi-value">{len(df_filtered)}</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    attr_rate = (df_filtered["attrition"] == "Yes").mean() * 100
    st.markdown(f"""
    <div class="kpi-card" style="border-left-color:{STC_RED}">
        <div class="kpi-title">Attrition Rate</div>
        <div class="kpi-value" style="color:{STC_RED}">
            {attr_rate:.1f}%
        </div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    avg_income = df_filtered["monthlyincome"].mean()
    st.markdown(f"""
    <div class="kpi-card" style="border-left-color:{STC_GREEN}">
        <div class="kpi-title">Avg Income</div>
        <div class="kpi-value" style="color:{STC_GREEN}">
            {avg_income:,.0f}
        </div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    avg_perf = df_filtered["performancerating"].mean()
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Avg Performance</div>
        <div class="kpi-value">{avg_perf:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# CHART ROW 1
# ==================================================
c1, c2 = st.columns(2)

attr_dept = (
    df_filtered.assign(attr_flag=(df_filtered["attrition"] == "Yes").astype(int))
    .groupby("department")["attr_flag"]
    .mean()
    .reset_index()
)

fig_attr = px.bar(
    attr_dept,
    x="attr_flag",
    y="department",
    orientation="h",
    text=attr_dept["attr_flag"].map(lambda x: f"{x:.0%}"),
    color_discrete_sequence=[STC_RED]
)
fig_attr.update_layout(
    title="Attrition Risk by Department",
    xaxis_tickformat=".0%",
    plot_bgcolor="white",
    paper_bgcolor="white",
    height=260
)

with c1:
    st.plotly_chart(fig_attr, use_container_width=True)

perf_dist = df_filtered["performancerating"].value_counts().reset_index()
perf_dist.columns = ["Rating", "Count"]

fig_perf = px.pie(
    perf_dist,
    names="Rating",
    values="Count",
    hole=0.65,
    color_discrete_sequence=[STC_GREEN, STC_PURPLE, "#CBD5E1"]
)
fig_perf.update_layout(
    title="Performance Distribution",
    annotations=[dict(text=f"{avg_perf:.2f}", x=0.5, y=0.5, font_size=24, showarrow=False)],
    paper_bgcolor="white",
    height=260
)

with c2:
    st.plotly_chart(fig_perf, use_container_width=True)

# ==================================================
# CHART ROW 2
# ==================================================
c3, c4 = st.columns(2)

fig_income = px.box(
    df_filtered,
    x="department",
    y="monthlyincome",
    color_discrete_sequence=[STC_GREEN]
)
fig_income.update_layout(
    title="Income Distribution by Department",
    plot_bgcolor="white",
    paper_bgcolor="white",
    height=260
)

with c3:
    st.plotly_chart(fig_income, use_container_width=True)

tenure = df_filtered.groupby("yearsatcompany").size().reset_index(name="Employees")

fig_tenure = px.line(
    tenure,
    x="yearsatcompany",
    y="Employees",
    markers=True,
    color_discrete_sequence=[STC_PURPLE]
)
fig_tenure.update_layout(
    title="Employee Tenure Trend",
    plot_bgcolor="white",
    paper_bgcolor="white",
    height=260
)

with c4:
    st.plotly_chart(fig_tenure, use_container_width=True)

# ==================================================
# HR ACTIONS
# ==================================================
with st.expander("HR Actions"):
    tab1, tab2 = st.tabs(["➕ Add Employee", "✏️ Update Income"])

    with tab1:
        with st.form("add_employee"):
            emp_no = st.number_input("Employee Number", min_value=1)
            dept = st.text_input("Department")
            role = st.text_input("Job Role")
            income = st.number_input("Monthly Income", min_value=0)
            rating = st.selectbox("Performance Rating", [1, 2, 3, 4])

            if st.form_submit_button("Add Employee"):
                conn = sqlite3.connect("hr.db")
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO employees
                    (employeenumber, department, jobrole, monthlyincome, performancerating)
                    VALUES (?, ?, ?, ?, ?)
                """, (emp_no, dept, role, income, rating))
                conn.commit()
                conn.close()
                st.success("Employee added successfully")

    with tab2:
        with st.form("update_income"):
            emp_no = st.number_input("Employee Number", min_value=1, key="upd")
            new_income = st.number_input("New Monthly Income", min_value=0)

            if st.form_submit_button("Update Income"):
                conn = sqlite3.connect("hr.db")
                cur = conn.cursor()
                cur.execute("""
                    UPDATE employees
                    SET monthlyincome = ?
                    WHERE employeenumber = ?
                """, (new_income, emp_no))
                conn.commit()
                conn.close()
                st.success("Income updated successfully")
