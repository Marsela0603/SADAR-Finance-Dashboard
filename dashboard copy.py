import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="SADAR Finance Dashboard",
    page_icon="Logo-SADAR.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# COLOR PALETTE
# ─────────────────────────────────────────────
C_PRIMARY   = "#0C3954"
C_SECONDARY = "#64AB88"
C_ACCENT    = "#0054A6"
C_MINT      = "#DCEBE4"
C_BG        = "#748BB9"
C_BLUE      = "#7DB3F1"
C_BORDER    = "#CFCFCF"
C_SUCCESS   = "#2ECC71"
C_WARNING   = "#F5A524"
C_ERROR     = "#E5484D"
C_TEXT      = "#333333"
C_TEXT2     = "#F8F9FA"
C_INPUT     = "#F5F7F9"
C_MUTED     = "#8E8E93"

COLOR_SEQ = [
    C_PRIMARY,
    C_SECONDARY,
    C_ACCENT,
    C_BLUE,
    C_SUCCESS,
    C_WARNING
]

# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown(f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

@keyframes slideInLeft {{
    from {{
        opacity: 0;
        transform: translateX(-30px);
    }}
    to {{
        opacity: 1;
        transform: translateX(0);
    }}
}}

@keyframes pulse {{
    0% {{
        box-shadow: 0 0 0 0 rgba(12, 57, 84, 0.7);
    }}
    70% {{
        box-shadow: 0 0 0 15px rgba(12, 57, 84, 0);
    }}
    100% {{
        box-shadow: 0 0 0 0 rgba(12, 57, 84, 0);
    }}
}}

@keyframes bounce {{
    0%, 100% {{
        transform: translateY(0);
    }}
    50% {{
        transform: translateY(-10px);
    }}
}}

@keyframes glow {{
    0% {{
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
    }}
    50% {{
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.8);
    }}
    100% {{
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
    }}
}}

@keyframes float {{
    0%, 100% {{
        transform: translateY(0px) translateX(0px);
    }}
    50% {{
        transform: translateY(-20px) translateX(10px);
    }}
}}

html, body, [class*="css"] {{
    font-family: 'Poppins', sans-serif;
    background-color: {C_BG};
    color: {C_TEXT};
}}

.stApp {{
    background: linear-gradient(135deg, {C_BG} 0%, #E5E9F2 100%);
}}

.block-container {{
    padding-top: 1rem;
    padding-bottom: 2rem;
}}

[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, {C_PRIMARY} 0%, #061F2E 100%);
}}

[data-testid="stSidebar"] * {{
    color: white !important;
}}

.hero {{
    background: linear-gradient(135deg, {C_PRIMARY} 0%, {C_ACCENT} 100%);
    border-radius:28px;
    padding:50px 40px;
    margin-bottom:35px;
    animation: slideInLeft 0.8s ease-out;
    position: relative;
    overflow: hidden;
}}

.hero::before {{
    content: '';
    position: absolute;
    width: 200px;
    height: 200px;
    background: rgba(255, 255, 255, 0.08);
    border-radius: 50%;
    top: -50px;
    right: -50px;
    animation: float 6s ease-in-out infinite;
}}

.hero::after {{
    content: '';
    position: absolute;
    width: 150px;
    height: 150px;
    background: rgba(255, 255, 255, 0.06);
    border-radius: 50%;
    bottom: -30px;
    left: -30px;
    animation: float 8s ease-in-out infinite reverse;
}}

.hero h1 {{
    color:white;
    font-size:42px;
    font-weight:800;
    animation: glow 2.5s ease-in-out infinite;
    position: relative;
    z-index: 1;
}}

.hero p {{
    color:#E5F2F8;
    font-size:15px;
    line-height:1.9;
    position: relative;
    z-index: 1;
}}

.metric-card {{
    background: white;
    border-radius:24px;
    padding:28px;
    border:1px solid {C_BORDER};
    box-shadow: 0 8px 20px rgba(0,0,0,.05);
    transition: all 0.3s ease;
    animation: slideInLeft 0.6s ease-out;
}}

.metric-card:hover {{
    transform: translateY(-8px);
    box-shadow: 0 12px 30px rgba(12, 57, 84, 0.15);
}}

.metric-label {{
    color:{C_MUTED};
    font-size:12px;
    font-weight:700;
    text-transform:uppercase;
}}

.metric-value {{
    font-size:18px;
    font-weight:800;
    color:{C_PRIMARY};
    margin-top:14px;
}}

.metric-sub {{
    color:{C_MUTED};
    font-size:13px;
    margin-top:8px;
}}

.section-title {{
    font-size:26px;
    font-weight:800;
    color:{C_PRIMARY};
    margin-top:30px;
    margin-bottom:24px;
    animation: slideInLeft 0.7s ease-out;
    position: relative;
    display: inline-block;
    padding-bottom: 10px;
}}

.section-title::after {{
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, {C_PRIMARY} 0%, {C_SECONDARY} 100%);
    border-radius: 2px;
    animation: slideInLeft 0.7s ease-out;
}}

.insight-box {{
    background: rgba(100,171,136,.08);
    border-left:6px solid {C_SECONDARY};
    border-radius:20px;
    padding:22px 26px;
    margin-bottom:22px;
    transition: all 0.3s ease;
    animation: slideInLeft 0.6s ease-out;
}}

.insight-box:hover {{
    background: rgba(100,171,136,.12);
    border-left-width: 8px;
}}

.card {{
    background:white;
    border-radius:24px;
    padding:28px;
    border:1px solid {C_BORDER};
    animation: slideInLeft 0.6s ease-out;
    transition: all 0.3s ease;
}}

.card:hover {{
    box-shadow: 0 10px 25px rgba(0,0,0,.08);
}}

</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# PLOTLY STYLE
# ─────────────────────────────────────────────
PLOTLY_LAYOUT = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(250,251,253,.5)',
    font=dict(
        family='Poppins',
        color=C_TEXT,
        size=11
    ),
    margin=dict(
        l=30,
        r=30,
        t=60,
        b=30
    )
)

# ─────────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────────
@st.cache_data
def load_data():

    df = pd.read_csv("main_transactions_clean.csv")

    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # FEATURE ENGINEERING
    df['day_of_week'] = df['date'].dt.day_name()
    df['month'] = df['date'].dt.strftime('%Y-%m')
    df['day'] = df['date'].dt.day
    df['week'] = df['date'].dt.isocalendar().week

    df['is_weekend'] = df['day_of_week'].isin(
        ['Saturday', 'Sunday']
    )

    # SPENDING LEVEL
    def categorize_amount(x):

        if x < 50000:
            return 'Low'

        elif x < 200000:
            return 'Medium'

        else:
            return 'High'

    df['spending_level'] = df['amount'].apply(
        categorize_amount
    )

    # LOG TRANSFORM
    df['log_amount'] = np.log1p(df['amount'])

    # SORT
    df = df.sort_values('date')

    # ROLLING SPENDING
    df['rolling_7d_spending'] = (
        df['amount']
        .rolling(window=7)
        .sum()
    )

    # TRANSACTION COUNT
    df['transaction_count'] = (
        df.groupby('date')['amount']
        .transform('count')
    )

    return df

df = load_data()

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:

    st.image(
        "Logo-SADAR.png",
        width=200
    )

    st.markdown(
        "<p style='text-align:center;'>Smart Financial Analytics</p>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Overview",
            "📊 EDA & Business Questions",
            "📈 Financial Behavior",
            "🔍 Interactive Exploration",
            "📋 Dataset Information"
        ]
    )

    st.markdown("---")

    selected_month = st.multiselect(
        "Pilih Bulan",
        sorted(df['month'].unique()),
        default=sorted(df['month'].unique())[-3:]
    )

    selected_category = st.multiselect(
        "Pilih Kategori",
        sorted(df['category_primary'].dropna().unique()),
        default=sorted(df['category_primary'].dropna().unique())
    )

    selected_payment_media = st.multiselect(
        "Pilih Payment Media",
        sorted(df['payment_media'].dropna().unique()),
        default=sorted(df['payment_media'].dropna().unique())
    )

# ─────────────────────────────────────────────
# FILTER
# ─────────────────────────────────────────────
dff = df[
    (df['month'].isin(selected_month)) &
    (df['category_primary'].isin(selected_category)) &
    (df['payment_media'].isin(selected_payment_media))
]

# ─────────────────────────────────────────────
# OVERVIEW
# ─────────────────────────────────────────────
if page == "🏠 Overview":

    st.markdown(f"""
    <div class="hero">
        <h1>SADAR Finance Dashboard</h1>
        <p>
        Dashboard analisis keuangan modern berbasis data transaksi untuk membantu memahami
        pola pengeluaran, perilaku finansial, dan potensi risiko overspending pengguna.
        </p>
    </div>
    """, unsafe_allow_html=True)

    total_transaction = len(df)
    total_spending = dff['amount'].sum()
    avg_spending = dff['amount'].mean()
    top_category = dff['category_primary'].mode()[0]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Transaksi</div>
            <div class="metric-value">{total_transaction:,}</div>
            <div class="metric-sub">Total Transaksi pada Dataset</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Spending</div>
            <div class="metric-value">Rp {total_spending:,.0f}</div>
            <div class="metric-sub">Total pengeluaran</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Average Spending</div>
            <div class="metric-value">Rp {avg_spending:,.0f}</div>
            <div class="metric-sub">Rata-rata transaksi</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Top Category</div>
            <div class="metric-value">{top_category}</div>
            <div class="metric-sub">Kategori dominan</div>
        </div>
        """, unsafe_allow_html=True)

    # MONTHLY TREND
    st.markdown(
        "<div class='section-title'>Trend Pengeluaran Bulanan</div>",
        unsafe_allow_html=True
    )

    monthly = dff.groupby('month')['amount'].sum().reset_index()

    fig = px.area(
        monthly,
        x='month',
        y='amount',
        color_discrete_sequence=[C_ACCENT]
    )

    fig.update_layout(
        **PLOTLY_LAYOUT,
        height=450
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # CATEGORY DISTRIBUTION
    colA, colB = st.columns(2)

    with colA:

        st.markdown(
            "<div class='section-title'>Distribusi Kategori</div>",
            unsafe_allow_html=True
        )

        cat = (
            dff.groupby('category_primary')['amount']
            .sum()
            .reset_index()
        )

        fig2 = px.pie(
            cat,
            values='amount',
            names='category_primary',
            hole=.65,
            color_discrete_sequence=COLOR_SEQ
        )

        fig2.update_layout(
            **PLOTLY_LAYOUT,
            height=500
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    with colB:

        st.markdown(
            "<div class='section-title'>Top Merchant</div>",
            unsafe_allow_html=True
        )

        top_merchant = (
            dff['merchant']
            .value_counts()
            .head(10)
            .reset_index()
        )

        top_merchant.columns = [
            'merchant',
            'count'
        ]

        fig3 = px.bar(
            top_merchant,
            x='merchant',
            y='count',
            color='count',
            color_continuous_scale=[
                C_WARNING,
                C_PRIMARY
            ]
        )

        fig3.update_layout(
            **PLOTLY_LAYOUT,
            height=500
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    # PAYMENT MEDIA ANALYSIS
    st.markdown(
        "<div class='section-title'>Payment Media Analysis</div>",
        unsafe_allow_html=True
    )

    payment_media_spending = (
        dff.groupby('payment_media')['amount']
        .sum()
        .reset_index()
    )

    fig4 = px.bar(
        payment_media_spending,
        x='payment_media',
        y='amount',
        color='amount',
        color_continuous_scale=[
            '#DCEBE4',
            C_PRIMARY
        ]
    )

    fig4.update_layout(
        **PLOTLY_LAYOUT,
        height=450
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# ─────────────────────────────────────────────
# EDA & BUSINESS QUESTIONS
# ─────────────────────────────────────────────
elif page == "📊 EDA & Business Questions":

    st.markdown(
        "<div class='section-title'>Business Questions Analysis</div>",
        unsafe_allow_html=True
    )

    # QUESTION 1
    st.markdown("""
    <div class='insight-box'>
    <b>1. Bagaimana distribusi pengeluaran user berdasarkan kategori?</b>
    </div>
    """, unsafe_allow_html=True)

    category_spending = (
        dff.groupby('category_primary')['amount']
        .sum()
        .reset_index()
    )

    fig1 = px.bar(
        category_spending,
        x='category_primary',
        y='amount',
        color='amount'
    )

    fig1.update_layout(
        **PLOTLY_LAYOUT,
        height=450
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # QUESTION 2
    st.markdown("""
    <div class='insight-box'>
    <b>2. Kategori apa yang mengalami peningkatan pengeluaran terbesar?</b>
    </div>
    """, unsafe_allow_html=True)

    monthly_category = (
        dff.groupby(
            ['month', 'category_primary']
        )['amount']
        .sum()
        .reset_index()
    )

    fig2 = px.line(
        monthly_category,
        x='month',
        y='amount',
        color='category_primary',
        markers=True,
        color_discrete_sequence=COLOR_SEQ
    )

    fig2.update_layout(
        **PLOTLY_LAYOUT,
        height=450
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # QUESTION 3
    st.markdown("""
    <div class='insight-box'>
    <b>3. Hari apa transaksi paling sering terjadi?</b>
    </div>
    """, unsafe_allow_html=True)

    day_freq = (
        dff['day_of_week']
        .value_counts()
        .reset_index()
    )

    day_freq.columns = ['day', 'count']

    fig3 = px.bar(
        day_freq,
        x='day',
        y='count',
        color='count'
    )

    fig3.update_layout(
        **PLOTLY_LAYOUT,
        height=450
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    # QUESTION 4
    st.markdown("""
    <div class='insight-box'>
    <b>4. Bagaimana perubahan rata-rata pengeluaran harian?</b>
    </div>
    """, unsafe_allow_html=True)

    daily_spending = (
        dff.groupby('date')['amount']
        .mean()
        .reset_index()
    )

    fig4 = px.line(
        daily_spending,
        x='date',
        y='amount',
        color_discrete_sequence=[C_SUCCESS]
    )

    fig4.update_layout(
        **PLOTLY_LAYOUT,
        height=450
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    # QUESTION 5
    st.markdown("""
    <div class='insight-box'>
    <b>5. Kapan terjadi lonjakan pengeluaran?</b>
    </div>
    """, unsafe_allow_html=True)

    dff['spike'] = (
        dff['amount']
        > dff['amount'].quantile(0.9)
    )

    spike_by_day = (
        dff.groupby('day_of_week')['spike']
        .sum()
        .reset_index()
    )

    fig5 = px.bar(
        spike_by_day,
        x='day_of_week',
        y='spike',
        color='spike'
    )

    fig5.update_layout(
        **PLOTLY_LAYOUT,
        height=450
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

    # QUESTION 6
    st.markdown("""
    <div class='insight-box'>
    <b>6. Apakah ada perbedaan pengeluaran berdasarkan metode pembayaran?</b>
    </div>
    """, unsafe_allow_html=True)

    payment_avg = (
        dff.groupby('payment_method')['amount']
        .mean()
        .reset_index()
    )

    fig6 = px.bar(
        payment_avg,
        x='payment_method',
        y='amount',
        color='amount'
    )

    fig6.update_layout(
        **PLOTLY_LAYOUT,
        height=450
    )

    st.plotly_chart(
        fig6,
        use_container_width=True
    )

# ─────────────────────────────────────────────
# FINANCIAL BEHAVIOR
# ─────────────────────────────────────────────
elif page == "📈 Financial Behavior":

    st.markdown(
        "<div class='section-title'>Financial Behavior Analysis</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        weekend_spending = (
            dff.groupby('is_weekend')['amount']
            .mean()
            .reset_index()
        )

        fig = px.bar(
            weekend_spending,
            x='is_weekend',
            y='amount',
            color='amount',
            title="Weekday vs Weekend Spending"
        )

        fig.update_layout(
            **PLOTLY_LAYOUT,
            height=420
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        day_spending = (
            dff.groupby('day_of_week')['amount']
            .mean()
            .reset_index()
        )

        fig2 = px.bar(
            day_spending,
            x='day_of_week',
            y='amount',
            color='amount',
            title="Average Spending per Day"
        )

        fig2.update_layout(
            **PLOTLY_LAYOUT,
            height=420
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    # ROLLING TREND
    st.markdown(
        "<div class='section-title'>Rolling Spending Trend</div>",
        unsafe_allow_html=True
    )

    fig3 = px.line(
        dff,
        x='date',
        y='rolling_7d_spending',
        color_discrete_sequence=[C_ACCENT]
    )

    fig3.update_layout(
        **PLOTLY_LAYOUT,
        height=450
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    # SPENDING LEVEL
    st.markdown(
        "<div class='section-title'>Spending Level Distribution</div>",
        unsafe_allow_html=True
    )

    level = (
        dff['spending_level']
        .value_counts()
        .reset_index()
    )

    level.columns = ['level', 'count']

    fig4 = px.pie(
        level,
        values='count',
        names='level',
        hole=.65,
        color_discrete_sequence=COLOR_SEQ
    )

    fig4.update_layout(
        **PLOTLY_LAYOUT,
        height=480
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# ─────────────────────────────────────────────
# INTERACTIVE EXPLORATION
# ─────────────────────────────────────────────
elif page == "🔍 Interactive Exploration":

    st.markdown(
        "<div class='section-title'>Interactive Data Exploration</div>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        x_axis = st.selectbox(
            "Pilih Sumbu X",
            [
                'category_primary',
                'category_detail',
                'payment_method',
                'payment_media',
                'merchant',
                'day_of_week',
                'month'
            ]
        )

    with col2:

        agg = st.selectbox(
            "Pilih Aggregation",
            ['sum', 'mean', 'count']
        )

    with col3:

        chart_type = st.selectbox(
            "Pilih Chart",
            ['Bar', 'Pie', 'Line']
        )

    grouped = (
        dff.groupby(x_axis)['amount']
        .agg(agg)
        .reset_index()
    )

    if chart_type == "Bar":

        fig = px.bar(
            grouped,
            x=x_axis,
            y='amount',
            color='amount'
        )

    elif chart_type == "Pie":

        fig = px.pie(
            grouped,
            values='amount',
            names=x_axis,
            hole=.65,
            color_discrete_sequence=COLOR_SEQ
        )

    else:

        fig = px.line(
            grouped,
            x=x_axis,
            y='amount',
            markers=True,
            color_discrete_sequence=[C_ACCENT]
        )

    fig.update_layout(
        **PLOTLY_LAYOUT,
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.markdown(
        "<div class='section-title'>Raw Dataset</div>",
        unsafe_allow_html=True
    )

    st.dataframe(
        dff.reset_index(drop=True),
        use_container_width=True,
        height=500
    )

# ─────────────────────────────────────────────
# DATASET INFORMATION
# ─────────────────────────────────────────────
elif page == "📋 Dataset Information":

    st.markdown(
        "<div class='section-title'>Dataset Information</div>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f"""
        <div class='card'>
            <h3 style='color:{C_PRIMARY}'>Dataset Summary</h3>
            <p style='color:{C_TEXT}'><b>Total Rows :</b> {len(df):,}</p>
            <p style='color:{C_TEXT}'><b>Total Columns :</b> {len(df.columns)}</p>
            <p style='color:{C_TEXT}'><b>Date Range :</b> {df['date'].min().date()} - {df['date'].max().date()}</p>
            <p style='color:{C_TEXT}'><b>Total Category :</b> {df['category_primary'].nunique()}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class='card'>
            <h3 style='color:{C_PRIMARY}'>Project Information</h3>
            <p style='color:{C_TEXT}'><b>Project :</b> SADAR Finance</p>
            <p style='color:{C_TEXT}'><b>Tools :</b> Python, Streamlit, Plotly, Pandas</p>
            <p style='color:{C_TEXT}'><b>Focus :</b> Financial Analytics & Spending Behavior</p>
            <p style='color:{C_TEXT}'><b>Dataset :</b> main_transactions_clean.csv</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        "<div class='section-title'>Data Dictionary</div>",
        unsafe_allow_html=True
    )

    dd = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(
        dd,
        use_container_width=True,
        hide_index=True
    )