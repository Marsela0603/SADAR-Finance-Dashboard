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
    border-right: 2px solid rgba(100,171,136,.15);
    backdrop-filter: blur(10px);
}}

[data-testid="stSidebar"] * {{
    color: white !important;
}}

.logo-container {{
    display:flex;
    align-items:center;
    gap:14px;
    margin-bottom:20px;
    padding:10px 0;
}}

.logo-text {{
    font-size:24px;
    font-weight:800;
    color:white;
    letter-spacing: -0.5px;
}}

.logo-sub {{
    font-size:12px;
    color:#A8D5DB;
    margin-top:-5px;
    font-weight: 500;
}}

.hero {{
    background: linear-gradient(135deg, {C_PRIMARY} 0%, {C_ACCENT} 100%);
    border-radius:28px;
    padding:50px 40px;
    position:relative;
    overflow:hidden;
    margin-bottom:35px;
    animation: fadeIn 0.8s ease;
    box-shadow: 0 20px 60px rgba(12, 57, 84, 0.15), 0 0 40px rgba(0, 84, 166, 0.08);
    border: 1px solid rgba(255,255,255,.1);
}}

.hero::before {{
    content:'';
    position:absolute;
    width:400px;
    height:400px;
    background:radial-gradient(circle, rgba(255,255,255,.12) 0%, rgba(255,255,255,0) 70%);
    border-radius:50%;
    right:-100px;
    top:-100px;
    box-shadow: 
        inset 0 0 60px rgba(255,255,255,.08),
        0 0 80px rgba(100,171,136,.1);
}}

.hero::after {{
    content:'';
    position:absolute;
    width:300px;
    height:300px;
    background:radial-gradient(circle, rgba(100,171,136,.1) 0%, rgba(100,171,136,0) 70%);
    border-radius:50%;
    left:-50px;
    bottom:-50px;
    box-shadow: 
        inset 0 0 50px rgba(100,171,136,.12),
        0 0 60px rgba(255,255,255,.05);
}}

/* Dekorasi lingkaran tambahan */
.hero::before {{
    filter: blur(1px);
}}

.hero::after {{
    filter: blur(0.5px);
}}

.hero h1 {{
    color:white;
    font-size:42px;
    font-weight:800;
    margin-bottom:15px;
    position: relative;
    z-index: 1;
    letter-spacing: -1px;
    text-shadow: 0 2px 8px rgba(0,0,0,.1);
}}

.hero p {{
    color:#E5F2F8;
    font-size:15px;
    max-width:700px;
    line-height:1.9;
    position: relative;
    z-index: 1;
    font-weight: 400;
}}

/* Dekorasi circle elements */
.hero {{
    box-shadow: 
        0 20px 60px rgba(12, 57, 84, 0.15), 
        0 0 40px rgba(0, 84, 166, 0.08),
        inset 0 0 100px rgba(255,255,255,.03),
        inset 100px 100px 200px rgba(100,171,136,.05),
        inset -100px -100px 200px rgba(0,0,0,.05);
}}

.hero-decoration {{
    position: absolute;
    border-radius: 50%;
    opacity: 0.6;
}}

.hero-circle-1 {{
    width: 200px;
    height: 200px;
    top: -50px;
    right: 50px;
    background: radial-gradient(circle at 30% 30%, rgba(255,255,255,.15) 0%, transparent 70%);
    border: 2px solid rgba(255,255,255,.1);
    box-shadow: 0 0 40px rgba(255,255,255,.08);
    animation: floatCircle1 6s ease-in-out infinite;
}}

.hero-circle-2 {{
    width: 150px;
    height: 150px;
    bottom: -30px;
    left: 100px;
    background: radial-gradient(circle at 40% 40%, rgba(100,171,136,.12) 0%, transparent 70%);
    border: 1.5px solid rgba(100,171,136,.15);
    box-shadow: 0 0 30px rgba(100,171,136,.06);
    animation: floatCircle2 7s ease-in-out infinite;
}}

.hero-circle-3 {{
    width: 120px;
    height: 120px;
    bottom: 20px;
    right: 100px;
    background: radial-gradient(circle at 35% 35%, rgba(220,235,228,.1) 0%, transparent 70%);
    border: 1px solid rgba(220,235,228,.2);
    box-shadow: 0 0 25px rgba(220,235,228,.04);
    animation: floatCircle3 8s ease-in-out infinite;
}}

@keyframes floatCircle1 {{
    0%, 100% {{ transform: translateY(0px) scale(1); }}
    50% {{ transform: translateY(-15px) scale(1.05); }}
}}

@keyframes floatCircle2 {{
    0%, 100% {{ transform: translateX(0px) scale(1); }}
    50% {{ transform: translateX(10px) scale(0.95); }}
}}

@keyframes floatCircle3 {{
    0%, 100% {{ transform: translateY(0px) rotate(0deg) scale(1); }}
    50% {{ transform: translateY(-12px) rotate(180deg) scale(1.02); }}
}}

.metric-card {{
    background: linear-gradient(135deg, #FFFFFF 0%, #F9FBFD 100%);
    border:1.5px solid {C_BORDER};
    border-radius:24px;
    padding:28px;
    box-shadow: 0 8px 32px rgba(0,0,0,.06), 0 2px 8px rgba(0,0,0,.03);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    animation: floatUp 0.7s ease;
    position: relative;
    overflow: hidden;
}}

.metric-card::before {{
    content:'';
    position:absolute;
    top:0;
    left:0;
    right:0;
    height:4px;
    background: linear-gradient(90deg, {C_PRIMARY} 0%, {C_SECONDARY} 100%);
    transform: scaleX(0);
    transform-origin: left;
    animation: expandWidth 0.8s ease forwards;
}}

.metric-card:hover {{
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 20px 48px rgba(12, 57, 84, 0.12), 0 4px 16px rgba(0, 84, 166, 0.08);
    border-color: {C_SECONDARY};
}}

.metric-label {{
    color:{C_MUTED};
    font-size:12px;
    font-weight:700;
    text-transform:uppercase;
    letter-spacing: 0.8px;
}}

.metric-value {{
    font-size:20px;
    font-weight:800;
    background: linear-gradient(135deg, {C_PRIMARY} 0%, {C_SECONDARY} 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-top:14px;
    letter-spacing: -1px;
}}

.metric-sub {{
    color:{C_MUTED};
    font-size:13px;
    margin-top:8px;
    font-weight: 500;
}}

.section-title {{
    font-size:26px;
    font-weight:800;
    background: linear-gradient(135deg, {C_PRIMARY} 0%, {C_ACCENT} 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-top:30px;
    margin-bottom:24px;
    letter-spacing: -0.5px;
    position: relative;
    padding-bottom: 12px;
}}

.section-title::after {{
    content:'';
    position: absolute;
    bottom: 0;
    left: 0;
    height: 3px;
    width: 60px;
    background: linear-gradient(90deg, {C_SECONDARY} 0%, {C_ACCENT} 100%);
    border-radius: 2px;
}}

.card {{
    background: linear-gradient(135deg, #FFFFFF 0%, #F9FBFD 100%);
    border-radius:24px;
    padding:28px;
    border:1.5px solid {C_BORDER};
    box-shadow: 0 8px 32px rgba(0,0,0,.05), 0 2px 8px rgba(0,0,0,.02);
    margin-bottom:24px;
    transition: all 0.3s ease;
}}

.card:hover {{
    box-shadow: 0 16px 48px rgba(0,0,0,.08);
    transform: translateY(-2px);
}}

.insight-box {{
    background: linear-gradient(135deg, rgba(100,171,136,.08) 0%, rgba(0,84,166,.05) 100%);
    border-left:6px solid {C_SECONDARY};
    border-radius:20px;
    padding:22px 26px;
    margin-bottom:22px;
    animation: slideIn 0.6s ease;
    border: 1px solid rgba(100,171,136,.1);
    box-shadow: 0 4px 16px rgba(100,171,136,.08);
    position: relative;
    overflow: hidden;
}}

.insight-box::after {{
    content:'';
    position: absolute;
    right: -30px;
    top: -30px;
    width: 80px;
    height: 80px;
    background: radial-gradient(circle, rgba(255,255,255,.2) 0%, transparent 70%);
    border-radius: 50%;
}}

.insight-box b {{
    font-weight: 700;
    color: {C_PRIMARY};
}}

.stDataFrame {{
    border-radius:20px;
    overflow:hidden;
}}

.stPlotlyChart {{
    background: transparent;
}}

[data-testid="stMetricDelta"] {{
    color: {C_SUCCESS} !important;
}}

@keyframes fadeIn {{
    from {{
        opacity:0;
        transform:translateY(20px);
    }}
    to {{
        opacity:1;
        transform:translateY(0);
    }}
}}

@keyframes floatUp {{
    from {{
        opacity:0;
        transform:translateY(25px) scale(0.95);
    }}
    to {{
        opacity:1;
        transform:translateY(0) scale(1);
    }}
}}

@keyframes slideIn {{
    from {{
        opacity:0;
        transform:translateX(-20px);
    }}
    to {{
        opacity:1;
        transform:translateX(0);
    }}
}}

@keyframes expandWidth {{
    to {{
        transform: scaleX(1);
    }}
}}

/* Meningkatkan styling untuk selectbox dan input */
.stSelectbox, .stMultiSelect {{
    border-radius: 12px !important;
}}

.stSelectbox label, .stMultiSelect label {{
    font-weight: 700 !important;
    color: white !important;
}}

/* Separator styling */
hr {{
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent 0%, rgba(255,255,255,.2) 50%, transparent 100%);
    margin: 24px 0 !important;
}}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# PLOTLY STYLE
# ─────────────────────────────────────────────
PLOTLY_LAYOUT = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(250,251,253,.5)',
    font=dict(family='Poppins', color=C_TEXT, size=11),
    margin=dict(l=30, r=30, t=60, b=30),
    hoverlabel=dict(
        bgcolor="white",
        font_size=13,
        font_family="Poppins",
        bordercolor=C_PRIMARY
    ),
    hovermode='x unified'
)

# ─────────────────────────────────────────────
# LOAD DATA
# ─────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv("main_transactions_clean.csv")

    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    df['day_of_week'] = df['date'].dt.day_name()
    df['month'] = df['date'].dt.strftime('%Y-%m')
    df['day'] = df['date'].dt.day
    df['week'] = df['date'].dt.isocalendar().week
    df['is_weekend'] = df['day_of_week'].isin(['Saturday', 'Sunday'])

    def categorize_amount(x):
        if x < 50000:
            return 'Low'
        elif x < 200000:
            return 'Medium'
        else:
            return 'High'

    df['spending_level'] = df['amount'].apply(categorize_amount)

    df['log_amount'] = np.log1p(df['amount'])

    df = df.sort_values('date')

    df['rolling_7d_spending'] = df['amount'].rolling(window=7).sum()

    df['transaction_count'] = df.groupby('date')['amount'].transform('count')

    return df

df = load_data()

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("Logo-SADAR.png", width=200, use_container_width=True)

    st.markdown(f"<p style='text-align: center; color: white; font-size: 12px; margin-top: -10px;'>Smart Financial Analytics</p>", unsafe_allow_html=True)

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

# FILTER
dff = df[
    (df['month'].isin(selected_month)) &
    (df['category_primary'].isin(selected_category))
]

# ─────────────────────────────────────────────
# OVERVIEW
# ─────────────────────────────────────────────
if page == "🏠 Overview":

    st.markdown(f"""
    <div class="hero">
        <div class="hero-decoration hero-circle-1"></div>
        <div class="hero-decoration hero-circle-2"></div>
        <div class="hero-decoration hero-circle-3"></div>
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
            <div class="metric-sub">Total semua transaksi pada dataset</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Total Pengeluaran</div>
            <div class="metric-value">Rp {total_spending:,.0f}</div>
            <div class="metric-sub">Akumulasi spending</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Rata-rata Spending</div>
            <div class="metric-value">Rp {avg_spending:,.0f}</div>
            <div class="metric-sub">Per transaksi</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Kategori Dominan</div>
            <div class="metric-value" style="font-size:22px">{top_category}</div>
            <div class="metric-sub">Kategori paling sering</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Trend Pengeluaran Bulanan</div>", unsafe_allow_html=True)

    monthly = dff.groupby('month')['amount'].sum().reset_index()

    fig = px.area(
        monthly,
        x='month',
        y='amount',
        color_discrete_sequence=[C_ACCENT]
    )

    fig.update_traces(
        line=dict(width=4, color=C_ACCENT),
        fill='tozeroy',
        fillcolor=f'rgba(0, 84, 166, 0.15)',
        hovertemplate='<b>%{x}</b><br>Total: <b>Rp %{y:,.0f}</b><extra></extra>'
    )

    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor=f'rgba(0,0,0,.05)',
        showline=True,
        linewidth=1.5,
        linecolor=C_BORDER
    )

    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor=f'rgba(0,0,0,.05)',
        showline=True,
        linewidth=1.5,
        linecolor=C_BORDER
    )

    fig.update_layout(
        **PLOTLY_LAYOUT,
        height=450,
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

    colA, colB = st.columns(2)

    with colA:
        st.markdown("<div class='section-title'>Distribusi Kategori</div>", unsafe_allow_html=True)

        cat = dff.groupby('category_primary')['amount'].sum().reset_index()

        fig2 = px.pie(
            cat,
            values='amount',
            names='category_primary',
            hole=.65,
            color_discrete_sequence=COLOR_SEQ
        )

        fig2.update_traces(
            textposition='inside',
            textfont=dict(size=13, color='white', family='Poppins', weight='bold'),
            textinfo='label+percent',
            marker=dict(line=dict(color='white', width=2.5)),
            hovertemplate='<b>%{label}</b><br>Amount: <b>Rp %{value:,.0f}</b><br>Percentage: <b>%{percent}</b><extra></extra>'
        )

        fig2.update_layout(
            **PLOTLY_LAYOUT, 
            height=520,
            showlegend=False
        )

        st.plotly_chart(fig2, use_container_width=True)

    with colB:
        st.markdown("<div class='section-title'>Top Merchant</div>", unsafe_allow_html=True)

        top_merchant = dff['merchant'].value_counts().head(10).reset_index()
        top_merchant.columns = ['merchant', 'count']

        fig3 = px.bar(
            top_merchant,
            x='merchant',
            y='count',
            color='count',
            color_continuous_scale=[C_WARNING, C_PRIMARY]
        )

        fig3.update_traces(
            textposition='outside', 
            textfont=dict(size=13, color=C_PRIMARY, family='Poppins', weight='bold'),
            text=top_merchant['count'],
            marker=dict(line=dict(color='white', width=1.5)),
            hovertemplate='<b>%{x}</b><br>Transactions: <b>%{y}</b><extra></extra>'
        )
        
        fig3.update_xaxes(
            tickangle=-45,
            tickfont=dict(size=11, color=C_TEXT),
            showgrid=False,
            showline=True,
            linewidth=1.5,
            linecolor=C_BORDER
        )
        
        fig3.update_yaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor=f'rgba(0,0,0,.05)',
            showline=True,
            linewidth=1.5,
            linecolor=C_BORDER
        )
        
        fig3.update_layout(
            **PLOTLY_LAYOUT, 
            xaxis_tickangle=-45,
            height=520,
            showlegend=False
        )

        st.plotly_chart(fig3, use_container_width=True)

# ─────────────────────────────────────────────
# EDA & BUSINESS QUESTIONS
# ─────────────────────────────────────────────
elif page == "📊 EDA & Business Questions":

    st.markdown("<div class='section-title'>Business Questions Analysis</div>", unsafe_allow_html=True)

    # QUESTION 1
    st.markdown("""
    <div class='insight-box'>
    <b>1. Bagaimana distribusi pengeluaran user berdasarkan kategori dalam 3 bulan terakhir?</b>
    </div>
    """, unsafe_allow_html=True)

    last_3_months = dff[dff['date'] >= dff['date'].max() - pd.DateOffset(months=3)]

    category_spending = last_3_months.groupby('category_primary')['amount'].sum().reset_index()

    fig1 = px.bar(
        category_spending,
        x='category_primary',
        y='amount',
        color='amount',
        color_continuous_scale=['#DCEBE4', C_PRIMARY]
    )

    fig1.update_traces(
        marker=dict(line=dict(color='white', width=1.5)),
        hovertemplate='<b>%{x}</b><br>Total: <b>Rp %{y:,.0f}</b><extra></extra>'
    )
    
    fig1.update_xaxes(
        showgrid=False,
        showline=True,
        linewidth=1.5,
        linecolor=C_BORDER
    )
    
    fig1.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor=f'rgba(0,0,0,.05)'
    )

    fig1.update_layout(**PLOTLY_LAYOUT, height=450, showlegend=False)

    st.plotly_chart(fig1, use_container_width=True)

    # QUESTION 2
    st.markdown("""
    <div class='insight-box'>
    <b>2. Kategori apa yang mengalami peningkatan pengeluaran terbesar dari bulan ke bulan?</b>
    </div>
    """, unsafe_allow_html=True)

    monthly_category = dff.groupby(['month', 'category_primary'])['amount'].sum().reset_index()

    fig2 = px.line(
        monthly_category,
        x='month',
        y='amount',
        color='category_primary',
        markers=True,
        color_discrete_sequence=COLOR_SEQ
    )

    fig2.update_traces(
        line=dict(width=3.5),
        marker=dict(size=8, symbol='circle', line=dict(color='white', width=2)),
        hovertemplate='<b>%{x}</b><br><b>%{fullData.name}</b><br>Amount: <b>Rp %{y:,.0f}</b><extra></extra>'
    )
    
    fig2.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor=f'rgba(0,0,0,.05)',
        showline=True,
        linewidth=1.5,
        linecolor=C_BORDER
    )
    
    fig2.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor=f'rgba(0,0,0,.05)',
        showline=True,
        linewidth=1.5,
        linecolor=C_BORDER
    )

    fig2.update_layout(**PLOTLY_LAYOUT, height=450)

    st.plotly_chart(fig2, use_container_width=True)

    # QUESTION 3
    st.markdown("""
    <div class='insight-box'>
    <b>3. Pada hari apa transaksi paling sering terjadi?</b>
    </div>
    """, unsafe_allow_html=True)

    day_freq = dff['day_of_week'].value_counts().reset_index()
    day_freq.columns = ['day', 'count']

    fig3 = px.bar(
        day_freq,
        x='day',
        y='count',
        color='count',
        color_continuous_scale=['#DCEBE4', C_SECONDARY]
    )

    fig3.update_traces(
        marker=dict(line=dict(color='white', width=1.5)),
        hovertemplate='<b>%{x}</b><br>Frequency: <b>%{y}</b><extra></extra>'
    )
    
    fig3.update_xaxes(
        showgrid=False,
        showline=True,
        linewidth=1.5,
        linecolor=C_BORDER
    )
    
    fig3.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor=f'rgba(0,0,0,.05)'
    )

    fig3.update_layout(**PLOTLY_LAYOUT, height=450, showlegend=False)

    st.plotly_chart(fig3, use_container_width=True)

    # QUESTION 4
    st.markdown("""
    <div class='insight-box'>
    <b>4. Berapa rata-rata pengeluaran harian user dan bagaimana perubahannya dari waktu ke waktu?</b>
    </div>
    """, unsafe_allow_html=True)

    daily_spending = dff.groupby('date')['amount'].mean().reset_index()

    fig4 = px.line(
        daily_spending,
        x='date',
        y='amount',
        color_discrete_sequence=[C_SUCCESS]
    )

    fig4.update_traces(
        line=dict(width=3),
        marker=dict(size=5),
        fill='tozeroy',
        fillcolor=f'rgba(46, 204, 113, 0.1)',
        hovertemplate='<b>%{x|%d %B %Y}</b><br>Avg: <b>Rp %{y:,.0f}</b><extra></extra>'
    )
    
    fig4.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor=f'rgba(0,0,0,.05)',
        showline=True,
        linewidth=1.5,
        linecolor=C_BORDER
    )
    
    fig4.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor=f'rgba(0,0,0,.05)',
        showline=True,
        linewidth=1.5,
        linecolor=C_BORDER
    )

    fig4.update_layout(**PLOTLY_LAYOUT, height=450, showlegend=False)

    st.plotly_chart(fig4, use_container_width=True)

    # QUESTION 5
    st.markdown("""
    <div class='insight-box'>
    <b>5. Kapan waktu paling berisiko user mengalami lonjakan pengeluaran?</b>
    </div>
    """, unsafe_allow_html=True)

    dff['spike'] = dff['amount'] > dff['amount'].quantile(0.9)

    spike_by_day = dff.groupby('day_of_week')['spike'].sum().reset_index()

    fig5 = px.bar(
        spike_by_day,
        x='day_of_week',
        y='spike',
        color='spike',
        color_continuous_scale=['#FFD6D6', C_ERROR]
    )

    fig5.update_traces(
        marker=dict(line=dict(color='white', width=1.5)),
        hovertemplate='<b>%{x}</b><br>High Spending: <b>%{y}</b><extra></extra>'
    )
    
    fig5.update_xaxes(
        showgrid=False,
        showline=True,
        linewidth=1.5,
        linecolor=C_BORDER
    )
    
    fig5.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor=f'rgba(0,0,0,.05)'
    )

    fig5.update_layout(**PLOTLY_LAYOUT, height=450, showlegend=False)

    st.plotly_chart(fig5, use_container_width=True)

    # QUESTION 6
    st.markdown("""
    <div class='insight-box'>
    <b>6. Apakah terdapat perbedaan rata-rata pengeluaran berdasarkan metode pembayaran?</b>
    </div>
    """, unsafe_allow_html=True)

    payment_avg = dff.groupby('payment_method')['amount'].mean().reset_index()

    fig6 = px.bar(
        payment_avg,
        x='payment_method',
        y='amount',
        color='amount',
        color_continuous_scale=['#DCEBE4', C_ACCENT]
    )

    fig6.update_traces(
        marker=dict(line=dict(color='white', width=1.5)),
        hovertemplate='<b>%{x}</b><br>Average: <b>Rp %{y:,.0f}</b><extra></extra>'
    )
    
    fig6.update_xaxes(
        showgrid=False,
        showline=True,
        linewidth=1.5,
        linecolor=C_BORDER
    )
    
    fig6.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor=f'rgba(0,0,0,.05)'
    )

    fig6.update_layout(**PLOTLY_LAYOUT, height=450, showlegend=False)

    st.plotly_chart(fig6, use_container_width=True)

# ─────────────────────────────────────────────
# FINANCIAL BEHAVIOR
# ─────────────────────────────────────────────
elif page == "📈 Financial Behavior":

    st.markdown("<div class='section-title'>Financial Behavior Analysis</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        weekend_spending = dff.groupby('is_weekend')['amount'].mean().reset_index()

        fig = px.bar(
            weekend_spending,
            x='is_weekend',
            y='amount',
            color='amount',
            color_continuous_scale=['#DCEBE4', C_PRIMARY],
            title="Weekday vs Weekend Spending"
        )

        fig.update_traces(
            marker=dict(line=dict(color='white', width=1.5)),
            hovertemplate='<b>%{x}</b><br>Average: <b>Rp %{y:,.0f}</b><extra></extra>'
        )
        
        fig.update_xaxes(showgrid=False, showline=True, linewidth=1.5, linecolor=C_BORDER)
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor=f'rgba(0,0,0,.05)')

        fig.update_layout(**PLOTLY_LAYOUT, height=420, showlegend=False)

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        day_spending = dff.groupby('day_of_week')['amount'].mean().reset_index()

        fig2 = px.bar(
            day_spending,
            x='day_of_week',
            y='amount',
            color='amount',
            color_continuous_scale=['#DCEBE4', C_SECONDARY],
            title="Average Spending per Day"
        )

        fig2.update_traces(
            marker=dict(line=dict(color='white', width=1.5)),
            hovertemplate='<b>%{x}</b><br>Average: <b>Rp %{y:,.0f}</b><extra></extra>'
        )
        
        fig2.update_xaxes(showgrid=False, showline=True, linewidth=1.5, linecolor=C_BORDER)
        fig2.update_yaxes(showgrid=True, gridwidth=1, gridcolor=f'rgba(0,0,0,.05)')

        fig2.update_layout(**PLOTLY_LAYOUT, height=420, showlegend=False)

        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("<div class='section-title'>Rolling Spending Trend</div>", unsafe_allow_html=True)

    fig3 = px.line(
        dff,
        x='date',
        y='rolling_7d_spending',
        color_discrete_sequence=[C_ACCENT]
    )

    fig3.update_traces(
        line=dict(width=3.5),
        fill='tozeroy',
        fillcolor=f'rgba(0, 84, 166, 0.12)',
        hovertemplate='<b>%{x|%d %B %Y}</b><br>7-Day Total: <b>Rp %{y:,.0f}</b><extra></extra>'
    )
    
    fig3.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor=f'rgba(0,0,0,.05)',
        showline=True,
        linewidth=1.5,
        linecolor=C_BORDER
    )
    
    fig3.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor=f'rgba(0,0,0,.05)',
        showline=True,
        linewidth=1.5,
        linecolor=C_BORDER
    )

    fig3.update_layout(**PLOTLY_LAYOUT, height=450, showlegend=False)

    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("<div class='section-title'>Spending Level Distribution</div>", unsafe_allow_html=True)

    level = dff['spending_level'].value_counts().reset_index()
    level.columns = ['level', 'count']

    fig4 = px.pie(
        level,
        values='count',
        names='level',
        hole=.65,
        color_discrete_sequence=COLOR_SEQ
    )

    fig4.update_traces(
        marker=dict(line=dict(color='white', width=2.5)),
        textfont=dict(size=13, color='white', family='Poppins', weight='bold'),
        textposition='inside',
        textinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>Count: <b>%{value}</b><br>Percentage: <b>%{percent}</b><extra></extra>'
    )

    fig4.update_layout(**PLOTLY_LAYOUT, height=480, showlegend=False)

    st.plotly_chart(fig4, use_container_width=True)

# ─────────────────────────────────────────────
# INTERACTIVE
# ─────────────────────────────────────────────
elif page == "🔍 Interactive Exploration":

    st.markdown("<div class='section-title'>Interactive Data Exploration</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        x_axis = st.selectbox(
            "Pilih Sumbu X",
            [
                'category_primary',
                'payment_method',
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

    grouped = dff.groupby(x_axis)['amount'].agg(agg).reset_index()

    if chart_type == "Bar":

        fig = px.bar(
            grouped,
            x=x_axis,
            y='amount',
            color='amount',
            color_continuous_scale=['#DCEBE4', C_PRIMARY]
        )
        
        fig.update_traces(
            marker=dict(line=dict(color='white', width=1.5)),
            hovertemplate='<b>%{x}</b><br>Value: <b>Rp %{y:,.0f}</b><extra></extra>'
        )
        
        fig.update_xaxes(showgrid=False, showline=True, linewidth=1.5, linecolor=C_BORDER)
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor=f'rgba(0,0,0,.05)')

    elif chart_type == "Pie":

        fig = px.pie(
            grouped,
            values='amount',
            names=x_axis,
            hole=.65,
            color_discrete_sequence=COLOR_SEQ
        )
        
        fig.update_traces(
            marker=dict(line=dict(color='white', width=2.5)),
            textfont=dict(size=12, color='white', family='Poppins', weight='bold'),
            textposition='inside',
            textinfo='label+percent',
            hovertemplate='<b>%{label}</b><br>Amount: <b>Rp %{value:,.0f}</b><br>Percentage: <b>%{percent}</b><extra></extra>'
        )

    else:

        fig = px.line(
            grouped,
            x=x_axis,
            y='amount',
            markers=True,
            color_discrete_sequence=[C_ACCENT]
        )
        
        fig.update_traces(
            line=dict(width=3.5),
            marker=dict(size=8, symbol='circle', line=dict(color='white', width=2)),
            hovertemplate='<b>%{x}</b><br>Value: <b>Rp %{y:,.0f}</b><extra></extra>'
        )
        
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor=f'rgba(0,0,0,.05)', showline=True, linewidth=1.5, linecolor=C_BORDER)
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor=f'rgba(0,0,0,.05)', showline=True, linewidth=1.5, linecolor=C_BORDER)

    fig.update_layout(**PLOTLY_LAYOUT, height=480, showlegend=False)

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("<div class='section-title'>Raw Dataset</div>", unsafe_allow_html=True)

    st.dataframe(
        dff.reset_index(drop=True),
        use_container_width=True,
        height=500
    )

# ─────────────────────────────────────────────
# DATASET
# ─────────────────────────────────────────────
elif page == "📋 Dataset Information":

    st.markdown("<div class='section-title'>Dataset Information</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f"""
        <div class='card'>
            <h3 style='color:{C_PRIMARY}'>Dataset Summary</h3>
            <p style='color:{C_PRIMARY}'><b>Total Rows :</b> {len(df):,}</p>
            <p style='color:{C_PRIMARY}'><b>Total Columns :</b> {len(df.columns)}</p>
            <p style='color:{C_PRIMARY}'><b>Date Range :</b> {df['date'].min().date()} sampai {df['date'].max().date()}</p>
            <p style='color:{C_PRIMARY}'><b>Total Category :</b> {df['category_primary'].nunique()}</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class='card'>
            <h3 style='color:{C_PRIMARY}'>Project Information</h3>
            <p style='color:{C_PRIMARY}'><b>Project :</b> SADAR Finance</p>
            <p style='color:{C_PRIMARY}'><b>Tools :</b> Python, Streamlit, Plotly, Pandas</p>
            <p style='color:{C_PRIMARY}'><b>Focus :</b> Financial Analytics & Spending Behavior</p>
            <p style='color:{C_PRIMARY}'><b>Dataset :</b> main_transactions_clean.csv</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Data Dictionary</div>", unsafe_allow_html=True)

    dd = pd.DataFrame({
        "Column": df.columns,
        "Data Type": df.dtypes.astype(str)
    })

    st.dataframe(
        dd,
        use_container_width=True,
        hide_index=True
    )