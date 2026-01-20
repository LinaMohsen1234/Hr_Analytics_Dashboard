# import streamlit as st
# import pandas as pd
# import sqlite3
# import plotly.express as px

# # --------------------------------------------------
# # Page Configuration
# # --------------------------------------------------
# st.set_page_config(
#     page_title="HR Analytics | Solutions by STC",
#     layout="wide"
# )

# # --------------------------------------------------
# # STC Corporate Styling + Sidebar Styling
# # --------------------------------------------------
# # st.markdown("""
# # <style>
# # body {
# #     background-color: #F4F6F8;
# # }

# # /* KPI Cards */
# # .kpi-card {
# #     background-color: #FFFFFF;
# #     padding: 28px;
# #     border-radius: 18px;
# #     border-left: 6px solid #16D19C;
# #     box-shadow: 0 10px 24px rgba(0,0,0,0.08);
# # }
# # .kpi-title {
# #     color: #6B7280;
# #     font-size: 13px;
# #     text-transform: uppercase;
# #     letter-spacing: 0.04em;
# # }
# # .kpi-value {
# #     color: #5B0E8B;
# #     font-size: 40px;
# #     font-weight: 700;
# #     margin-top: 6px;
# # }

# # /* Section Titles */
# # .section-title {
# #     color: #1F2937;
# #     font-size: 22px;
# #     font-weight: 600;
# #     margin-top: 28px;
# # }

# # /* Sidebar */
# # section[data-testid="stSidebar"] {
# #     background: linear-gradient(180deg, #5B0E8B 0%, #3E0A5E 100%);
# # }
# # section[data-testid="stSidebar"] * {
# #     color: white !important;
# # }
# # </style>
# # """, unsafe_allow_html=True)

# st.markdown("""
# <style>

# /* ===== MAIN BACKGROUND ===== */
# .stApp {
#     background: linear-gradient(
#         135deg,
#         #F3E8FF 0%,
#         #F0FDF4 35%,
#         #ECFEFF 70%,
#         #FFFFFF 100%
#     );
# }

# /* ===== KPI CARDS ===== */
# .kpi-card {
#     background-color: #FFFFFF;
#     padding: 28px;
#     border-radius: 18px;
#     border-left: 6px solid #16D19C;
#     box-shadow: 0 12px 28px rgba(0,0,0,0.10);
# }
# .kpi-title {
#     color: #6B7280;
#     font-size: 13px;
#     text-transform: uppercase;
#     letter-spacing: 0.05em;
# }
# .kpi-value {
#     color: #5B0E8B;
#     font-size: 40px;
#     font-weight: 700;
#     margin-top: 6px;
# }

# /* ===== SECTION TITLES ===== */
# .section-title {
#     color: #1F2937;
#     font-size: 22px;
#     font-weight: 600;
#     margin-top: 32px;
# }

# /* ===== SIDEBAR ===== */
# section[data-testid="stSidebar"] {
#     background: linear-gradient(
#         180deg,
#         #5B0E8B 0%,
#         #4A0C70 50%,
#         #3E0A5E 100%
#     );
# }
# section[data-testid="stSidebar"] * {
#     color: white !important;
# }

# /* Sidebar divider */
# section[data-testid="stSidebar"] hr {
#     border-color: rgba(255,255,255,0.2);
# }

# </style>
# """, unsafe_allow_html=True)

# # --------------------------------------------------
# # Header
# # --------------------------------------------------
# st.markdown(
#     "<h1 style='color:#5B0E8B;'>HR Analytics Dashboard</h1>"
#     "<p style='color:#6B7280;'>Solutions by STC – Workforce Insights</p>",
#     unsafe_allow_html=True
# )

# # --------------------------------------------------
# # Load Data
# # --------------------------------------------------
# @st.cache_data
# def load_data():
#     conn = sqlite3.connect("hr.db")
#     df = pd.read_sql("SELECT * FROM employees", conn)
#     conn.close()
#     return df

# df = load_data()

# # --------------------------------------------------
# # Sidebar Filters
# # --------------------------------------------------
# st.sidebar.markdown("## Workforce Filters")
# st.sidebar.markdown("Explore employee insights by department")

# departments = ["All"] + sorted(df["department"].unique())
# selected_department = st.sidebar.selectbox("Department", departments)

# if selected_department != "All":
#     df = df[df["department"] == selected_department]

# st.sidebar.markdown("---")
# st.sidebar.markdown(
#     "<small>HR Analytics Platform<br>Solutions by STC</small>",
#     unsafe_allow_html=True
# )

# # --------------------------------------------------
# # KPI Section
# # --------------------------------------------------
# st.markdown("<div class='section-title'>Executive Overview</div>", unsafe_allow_html=True)

# k1, k2, k3 = st.columns(3)

# with k1:
#     st.markdown(
#         f"""
#         <div class="kpi-card">
#             <div class="kpi-title">Total Employees</div>
#             <div class="kpi-value">{df.shape[0]}</div>
#         </div>
#         """, unsafe_allow_html=True
#     )

# with k2:
#     attrition = (df["attrition"] == "Yes").mean() * 100
#     st.markdown(
#         f"""
#         <div class="kpi-card">
#             <div class="kpi-title">Attrition Rate</div>
#             <div class="kpi-value">{attrition:.1f}%</div>
#         </div>
#         """, unsafe_allow_html=True
#     )

# with k3:
#     avg_income = df["monthlyincome"].mean()
#     st.markdown(
#         f"""
#         <div class="kpi-card">
#             <div class="kpi-title">Avg Monthly Income</div>
#             <div class="kpi-value">{avg_income:,.0f}</div>
#         </div>
#         """, unsafe_allow_html=True
#     )

# # --------------------------------------------------
# # Workforce Distribution
# # --------------------------------------------------
# st.markdown("<div class='section-title'>Workforce Distribution</div>", unsafe_allow_html=True)

# c1, c2 = st.columns(2)

# with c1:
#     dept_df = df["department"].value_counts().reset_index()
#     dept_df.columns = ["Department", "Employees"]

#     fig_dept = px.bar(
#         dept_df,
#         x="Employees",
#         y="Department",
#         orientation="h",
#         color_discrete_sequence=["#5B0E8B"]
#     )
#     fig_dept.update_layout(
#         height=360,
#         plot_bgcolor="white",
#         paper_bgcolor="white",
#         xaxis_title="Employees",
#         yaxis_title=""
#     )
#     st.plotly_chart(fig_dept, use_container_width=True)

# with c2:
#     attr_df = df["attrition"].value_counts().reset_index()
#     attr_df.columns = ["Attrition", "Count"]

#     fig_attr = px.pie(
#         attr_df,
#         names="Attrition",
#         values="Count",
#         hole=0.6,
#         color_discrete_sequence=["#16D19C", "#5B0E8B"]
#     )
#     fig_attr.update_traces(textinfo="percent+label")
#     fig_attr.update_layout(
#         height=360,
#         paper_bgcolor="white",
#         showlegend=False
#     )
#     st.plotly_chart(fig_attr, use_container_width=True)

# # --------------------------------------------------
# # Compensation Analysis
# # --------------------------------------------------
# st.markdown("<div class='section-title'>Compensation Analysis</div>", unsafe_allow_html=True)

# income_role = (
#     df.groupby("jobrole")["monthlyincome"]
#     .mean()
#     .reset_index()
#     .sort_values("monthlyincome", ascending=True)
# )

# fig_income = px.bar(
#     income_role,
#     x="monthlyincome",
#     y="jobrole",
#     orientation="h",
#     color_discrete_sequence=["#16D19C"]
# )

# fig_income.update_layout(
#     height=420,
#     plot_bgcolor="white",
#     paper_bgcolor="white",
#     xaxis_title="Monthly Income (SAR)",
#     yaxis_title=""
# )

# st.plotly_chart(fig_income, use_container_width=True)

# # --------------------------------------------------
# # HR Actions (REQUIRED)
# # --------------------------------------------------
# st.markdown("<div class='section-title'>HR Actions</div>", unsafe_allow_html=True)

# tab1, tab2 = st.tabs(["➕ Add Employee", "✏️ Update Income"])

# with tab1:
#     with st.form("add_employee_form"):
#         employeenumber = st.number_input("Employee Number", min_value=1)
#         age = st.number_input("Age", min_value=18, max_value=65)
#         department = st.text_input("Department")
#         jobrole = st.text_input("Job Role")
#         monthlyincome = st.number_input("Monthly Income (SAR)", min_value=0)
#         performancerating = st.selectbox("Performance Rating", [1, 2, 3, 4])

#         submit_add = st.form_submit_button("Add Employee")

#         if submit_add:
#             conn = sqlite3.connect("hr.db")
#             cursor = conn.cursor()
#             cursor.execute("""
#                 INSERT INTO employees (
#                     employeenumber, age, department, jobrole,
#                     monthlyincome, performancerating
#                 )
#                 VALUES (?, ?, ?, ?, ?, ?)
#             """, (
#                 employeenumber, age, department, jobrole,
#                 monthlyincome, performancerating
#             ))
#             conn.commit()
#             conn.close()
#             st.success("Employee added successfully.")

# with tab2:
#     with st.form("update_income_form"):
#         emp_id = st.number_input("Employee Number", min_value=1)
#         new_income = st.number_input("New Monthly Income (SAR)", min_value=0)

#         submit_update = st.form_submit_button("Update Income")

#         if submit_update:
#             conn = sqlite3.connect("hr.db")
#             cursor = conn.cursor()
#             cursor.execute("""
#                 UPDATE employees
#                 SET monthlyincome = ?
#                 WHERE employeenumber = ?
#             """, (new_income, emp_id))
#             conn.commit()
#             conn.close()
#             st.success("Employee income updated successfully.")
            
# # --------------------------------------------------
# # Performance Rating Distribution
# # --------------------------------------------------
# st.markdown("<div class='section-title'>Performance Distribution</div>", unsafe_allow_html=True)

# perf_df = df["performancerating"].value_counts().sort_index().reset_index()
# perf_df.columns = ["Performance Rating", "Employees"]

# fig_perf = px.bar(
#     perf_df,
#     x="Performance Rating",
#     y="Employees",
#     color_discrete_sequence=["#5B0E8B"]
# )

# fig_perf.update_layout(
#     height=360,
#     plot_bgcolor="white",
#     paper_bgcolor="white",
#     xaxis_title="Performance Rating",
#     yaxis_title="Number of Employees"
# )

# st.plotly_chart(fig_perf, use_container_width=True)



# # --------------------------------------------------
# # Attrition Rate by Department
# # --------------------------------------------------
# st.markdown("<div class='section-title'>Attrition Risk by Department</div>", unsafe_allow_html=True)

# attr_dept = (
#     df.assign(attr_flag=df["attrition"].apply(lambda x: 1 if x == "Yes" else 0))
#       .groupby("department")["attr_flag"]
#       .mean()
#       .reset_index()
# )

# fig_attr_dept = px.bar(
#     attr_dept,
#     x="department",
#     y="attr_flag",
#     color_discrete_sequence=["#16D19C"]
# )

# fig_attr_dept.update_layout(
#     height=360,
#     plot_bgcolor="white",
#     paper_bgcolor="white",
#     yaxis_title="Attrition Rate",
#     xaxis_title="Department"
# )

# fig_attr_dept.update_yaxes(tickformat=".0%")

# st.plotly_chart(fig_attr_dept, use_container_width=True)

# # --------------------------------------------------
# # Data Table
# # --------------------------------------------------
# with st.expander("View Employee Records"):
#     st.dataframe(df, use_container_width=True)



#==================================================
#==================================================
#===================================================
# import streamlit as st
# import pandas as pd
# import sqlite3
# import plotly.express as px

# # ==================================================
# # PAGE CONFIG
# # ==================================================
# st.set_page_config(
#     page_title="HR Analytics | Solutions by STC",
#     layout="wide",
# )

# # ==================================================
# # BRAND COLORS (STC STYLE)
# # ==================================================
# STC_PURPLE = "#6D28D9"
# STC_GREEN = "#10B981"
# STC_RED = "#EF4444"
# BG_LIGHT = "#F6F0FA"

# # ==================================================
# # GLOBAL STYLING
# # ==================================================
# st.markdown(f"""
# <style>

# /* App background */
# .stApp {{
#     background: linear-gradient(135deg, {BG_LIGHT} 0%, #FFFFFF 70%);
# }}

# /* Sidebar */
# section[data-testid="stSidebar"] {{
#     background: linear-gradient(180deg, #4B1D6B 0%, #3A1558 100%);
# }}
# section[data-testid="stSidebar"] * {{
#     color: white !important;
# }}

# /* Titles */
# .section-title {{
#     font-size: 22px;
#     font-weight: 600;
#     margin: 32px 0 12px 0;
#     color: #1F2937;
# }}

# /* KPI Cards */
# .kpi-card {{
#     background-color: white;
#     padding: 28px;
#     border-radius: 18px;
#     box-shadow: 0 12px 30px rgba(0,0,0,0.08);
#     border-left: 6px solid {STC_PURPLE};
# }}
# .kpi-title {{
#     font-size: 13px;
#     color: #6B7280;
#     text-transform: uppercase;
#     letter-spacing: 0.05em;
# }}
# .kpi-value {{
#     font-size: 40px;
#     font-weight: 700;
#     color: {STC_PURPLE};
# }}

# </style>
# """, unsafe_allow_html=True)

# # ==================================================
# # HEADER
# # ==================================================
# st.markdown(
#     f"""
#     <h1 style="color:{STC_PURPLE}; margin-bottom:0;">HR Analytics Dashboard</h1>
#     <p style="color:#6B7280; margin-top:4px;">Solutions by STC – Workforce Overview</p>
#     """,
#     unsafe_allow_html=True
# )

# # ==================================================
# # LOAD DATA
# # ==================================================
# @st.cache_data
# def load_data():
#     conn = sqlite3.connect("hr.db")
#     df = pd.read_sql("SELECT * FROM employees", conn)
#     conn.close()
#     return df

# df = load_data()

# # ==================================================
# # SIDEBAR
# # ==================================================
# st.sidebar.markdown("## HR Controls")
# st.sidebar.markdown("Solutions by STC")

# departments = ["All"] + sorted(df["department"].unique())
# selected_department = st.sidebar.selectbox("Department", departments)

# if selected_department != "All":
#     df = df[df["department"] == selected_department]

# # ==================================================
# # KPI SECTION
# # ==================================================
# st.markdown("<div class='section-title'>Executive Overview</div>", unsafe_allow_html=True)

# k1, k2, k3, k4 = st.columns(4)

# with k1:
#     st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-title">Employees</div>
#         <div class="kpi-value">{df.shape[0]}</div>
#     </div>
#     """, unsafe_allow_html=True)

# with k2:
#     attr_rate = (df["attrition"] == "Yes").mean() * 100
#     st.markdown(f"""
#     <div class="kpi-card" style="border-left-color:{STC_RED}">
#         <div class="kpi-title">Attrition Rate</div>
#         <div class="kpi-value" style="color:{STC_RED}">{attr_rate:.1f}%</div>
#     </div>
#     """, unsafe_allow_html=True)

# with k3:
#     avg_income = df["monthlyincome"].mean()
#     st.markdown(f"""
#     <div class="kpi-card" style="border-left-color:{STC_GREEN}">
#         <div class="kpi-title">Avg Income</div>
#         <div class="kpi-value" style="color:{STC_GREEN}">{avg_income:,.0f}</div>
#     </div>
#     """, unsafe_allow_html=True)

# with k4:
#     avg_perf = df["performancerating"].mean()
#     st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-title">Avg Performance</div>
#         <div class="kpi-value">{avg_perf:.2f}</div>
#     </div>
#     """, unsafe_allow_html=True)

# # ==================================================
# # CHART ROW 1
# # ==================================================
# st.markdown("<div class='section-title'>Workforce Distribution</div>", unsafe_allow_html=True)
# c1, c2 = st.columns(2)

# with c1:
#     dept_df = df["department"].value_counts().reset_index()
#     dept_df.columns = ["Department", "Employees"]

#     fig = px.bar(
#         dept_df,
#         x="Employees",
#         y="Department",
#         orientation="h",
#         color_discrete_sequence=[STC_PURPLE]
#     )
#     fig.update_layout(plot_bgcolor="white", paper_bgcolor="white")
#     st.plotly_chart(fig, use_container_width=True)

# with c2:
#     attr_df = df["attrition"].value_counts().reset_index()
#     attr_df.columns = ["Attrition", "Count"]

#     fig = px.pie(
#         attr_df,
#         names="Attrition",
#         values="Count",
#         hole=0.6,
#         color_discrete_sequence=[STC_GREEN, STC_RED]
#     )
#     fig.update_layout(paper_bgcolor="white")
#     st.plotly_chart(fig, use_container_width=True)

# # ==================================================
# # CHART ROW 2
# # ==================================================
# st.markdown("<div class='section-title'>Compensation & Performance</div>", unsafe_allow_html=True)
# c3, c4 = st.columns(2)

# with c3:
#     income_role = df.groupby("jobrole")["monthlyincome"].mean().reset_index()
#     fig = px.bar(
#         income_role,
#         x="monthlyincome",
#         y="jobrole",
#         orientation="h",
#         color_discrete_sequence=[STC_GREEN]
#     )
#     fig.update_layout(plot_bgcolor="white", paper_bgcolor="white")
#     st.plotly_chart(fig, use_container_width=True)

# with c4:
#     perf_df = df["performancerating"].value_counts().sort_index().reset_index()
#     perf_df.columns = ["Rating", "Employees"]

#     fig = px.bar(
#         perf_df,
#         x="Rating",
#         y="Employees",
#         color_discrete_sequence=[STC_PURPLE]
#     )
#     fig.update_layout(plot_bgcolor="white", paper_bgcolor="white")
#     st.plotly_chart(fig, use_container_width=True)

# # ==================================================
# # HR ACTIONS
# # ==================================================
# st.markdown("<div class='section-title'>HR Actions</div>", unsafe_allow_html=True)
# tab1, tab2 = st.tabs(["➕ Add Employee", "✏️ Update Income"])

# with tab1:
#     with st.form("add_employee"):
#         emp_no = st.number_input("Employee Number", min_value=1)
#         dept = st.text_input("Department")
#         role = st.text_input("Job Role")
#         income = st.number_input("Monthly Income", min_value=0)
#         rating = st.selectbox("Performance Rating", [1, 2, 3, 4])

#         if st.form_submit_button("Add Employee"):
#             conn = sqlite3.connect("hr.db")
#             cur = conn.cursor()
#             cur.execute("""
#                 INSERT INTO employees (employeenumber, department, jobrole, monthlyincome, performancerating)
#                 VALUES (?, ?, ?, ?, ?)
#             """, (emp_no, dept, role, income, rating))
#             conn.commit()
#             conn.close()
#             st.success("Employee added successfully")

# with tab2:
#     with st.form("update_income"):
#         emp_no = st.number_input("Employee Number", min_value=1, key="upd")
#         new_income = st.number_input("New Monthly Income", min_value=0)

#         if st.form_submit_button("Update Income"):
#             conn = sqlite3.connect("hr.db")
#             cur = conn.cursor()
#             cur.execute("""
#                 UPDATE employees SET monthlyincome=? WHERE employeenumber=?
#             """, (new_income, emp_no))
#             conn.commit()
#             conn.close()
#             st.success("Income updated successfully")

# # ==================================================
# # DATA VIEW
# # ==================================================
# with st.expander("View Employee Records"):
#     st.dataframe(df, use_container_width=True)


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
# GLOBAL STYLING
# ==================================================
st.markdown(f"""
<style>

/* App background */
.stApp {{
    background: linear-gradient(135deg, {BG_LIGHT} 0%, #FFFFFF 70%);
}}

/* Sidebar */
section[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, #4B1D6B 0%, #3A1558 100%);
}}
section[data-testid="stSidebar"] * {{
    color: white !important;
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

.section-title {{
    font-size: 20px;
    font-weight: 600;
    margin: 16px 0 6px 0;
    color: #1F2937;
}}

</style>
""", unsafe_allow_html=True)

# ==================================================
# HEADER
# ==================================================
st.markdown(
    f"""
    <h2 style="color:{STC_PURPLE}; margin-bottom:0;">
        HR Analytics Dashboard
    </h2>
    <p style="color:#6B7280; margin-top:4px;">
        Solutions by STC — Executive Workforce View
    </p>
    """,
    unsafe_allow_html=True
)

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
departments = ["All"] + sorted(df["department"].unique())
selected_department = st.sidebar.selectbox("Department", departments)

if selected_department != "All":
    df = df[df["department"] == selected_department]

# ==================================================
# KPI ROW (ROW 1)
# ==================================================
k1, k2, k3, k4 = st.columns(4)

with k1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Employees</div>
        <div class="kpi-value">{len(df)}</div>
    </div>
    """, unsafe_allow_html=True)

with k2:
    attr_rate = (df["attrition"] == "Yes").mean() * 100
    st.markdown(f"""
    <div class="kpi-card" style="border-left-color:{STC_RED}">
        <div class="kpi-title">Attrition Rate</div>
        <div class="kpi-value" style="color:{STC_RED}">
            {attr_rate:.1f}%
        </div>
    </div>
    """, unsafe_allow_html=True)

with k3:
    avg_income = df["monthlyincome"].mean()
    st.markdown(f"""
    <div class="kpi-card" style="border-left-color:{STC_GREEN}">
        <div class="kpi-title">Avg Income</div>
        <div class="kpi-value" style="color:{STC_GREEN}">
            {avg_income:,.0f}
        </div>
    </div>
    """, unsafe_allow_html=True)

with k4:
    avg_perf = df["performancerating"].mean()
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Avg Performance</div>
        <div class="kpi-value">{avg_perf:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# CHART ROW 2 (NO SCROLL)
# ==================================================
c1, c2 = st.columns(2)

# Attrition Risk by Department (Executive Risk View)
attr_dept = (
    df.assign(attr_flag=(df["attrition"] == "Yes").astype(int))
      .groupby("department")["attr_flag"]
      .mean()
      .sort_values()
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
    height=260,
    xaxis_tickformat=".0%",
    title="Attrition Risk by Department",
    plot_bgcolor="white",
    paper_bgcolor="white"
)

with c1:
    st.plotly_chart(fig_attr, use_container_width=True)

# Performance Donut with Insight
perf_dist = df["performancerating"].value_counts().reset_index()
perf_dist.columns = ["Rating", "Count"]

fig_perf = px.pie(
    perf_dist,
    names="Rating",
    values="Count",
    hole=0.65,
    color_discrete_sequence=[STC_GREEN, STC_PURPLE, "#CBD5E1"]
)
fig_perf.update_layout(
    height=260,
    title="Performance Distribution",
    annotations=[dict(
        text=f"{avg_perf:.2f}",
        x=0.5, y=0.5,
        font_size=26,
        showarrow=False
    )],
    paper_bgcolor="white"
)

with c2:
    st.plotly_chart(fig_perf, use_container_width=True)

# ==================================================
# CHART ROW 3 (FINAL ROW)
# ==================================================
c3, c4 = st.columns(2)

# Income Distribution (Box Plot)
fig_income = px.box(
    df,
    x="department",
    y="monthlyincome",
    color_discrete_sequence=[STC_GREEN]
)
fig_income.update_layout(
    height=260,
    title="Income Distribution by Department",
    plot_bgcolor="white",
    paper_bgcolor="white"
)

with c3:
    st.plotly_chart(fig_income, use_container_width=True)

# Tenure Trend
tenure = (
    df.groupby("yearsatcompany")
      .size()
      .reset_index(name="Employees")
)

fig_tenure = px.line(
    tenure,
    x="yearsatcompany",
    y="Employees",
    markers=True,
    color_discrete_sequence=[STC_PURPLE]
)
fig_tenure.update_layout(
    height=260,
    title="Employee Tenure Trend",
    plot_bgcolor="white",
    paper_bgcolor="white"
)

with c4:
    st.plotly_chart(fig_tenure, use_container_width=True)

# ==================================================
# HR ACTIONS (COLLAPSED – DOES NOT BREAK ONE SCREEN)
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
                    SET monthlyincome=?
                    WHERE employeenumber=?
                """, (new_income, emp_no))
                conn.commit()
                conn.close()
                st.success("Income updated successfully")
