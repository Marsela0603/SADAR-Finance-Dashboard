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
    page_icon="Logo_SADAR.png",
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
C_BG        = "#667BA5"
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
    background-color: {C_BG};
    background-image: 
        linear-gradient(90deg, transparent 24%, rgba(100, 171, 136, 0.05) 25%, rgba(100, 171, 136, 0.05) 26%, transparent 27%, transparent 74%, rgba(100, 171, 136, 0.05) 75%, rgba(100, 171, 136, 0.05) 76%, transparent 77%, transparent),
        linear-gradient(90deg, transparent 24%, rgba(12, 57, 84, 0.08) 25%, rgba(12, 57, 84, 0.08) 26%, transparent 27%, transparent 74%, rgba(12, 57, 84, 0.08) 75%, rgba(12, 57, 84, 0.08) 76%, transparent 77%, transparent),
        linear-gradient(135deg, {C_BG} 0%, #A8C5E0 50%, #E5E9F2 100%);
    background-size: 50px 100%, 40px 80%, 100% 100%;
    background-position: 0 0, 10px 20px, 0 0;
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
    margin-top:50px;
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
    margin-top:50px;
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
        "<p>Smart Financial Analytics</p>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "🏠 Overview",
            "📊 Interactive Business Questions",
            "📈 Financial Behavior",
            "🔍 Exploratory Data Analysis",
            "📋 Dataset Information",
            "👥 Teams"
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
        height=450,
        xaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        yaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
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
            height=500,
            legend=dict(font=dict(color=C_PRIMARY))
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
            height=500,
            xaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
            yaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
            coloraxis_colorbar=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY))
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
            "#6FC39F",
            C_PRIMARY
        ]
    )

    fig4.update_layout(
        **PLOTLY_LAYOUT,
        height=450,
        xaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        yaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        coloraxis_colorbar=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY))
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# ─────────────────────────────────────────────
# INTERACTIVE BUSINESS QUESTIONS
# ─────────────────────────────────────────────
elif page == "📊 Interactive Business Questions":

    st.markdown(
        "<div class='section-title'>Interactive Business Questions</div>",
        unsafe_allow_html=True
    )

    # QUESTION 1: DISTRIBUSI PENGELUARAN (3 BULAN TERAKHIR)
    st.markdown(f"""
    <div class='insight-box'>
    <b style='color:{C_PRIMARY}'>1. Bagaimana distribusi pengeluaran user berdasarkan kategori dalam 3 bulan terakhir?</b>
    </div>
    """, unsafe_allow_html=True)

    last_3_months = dff[dff['date'] >= dff['date'].max() - pd.DateOffset(months=3)]
    category_spending = last_3_months.groupby('category_primary')['amount'].sum().sort_values()

    fig1 = px.bar(
        x=category_spending.values,
        y=category_spending.index,
        orientation='h',
        color=category_spending.values,
        color_continuous_scale=[C_SECONDARY, C_ACCENT]
    )

    fig1.update_layout(
        **PLOTLY_LAYOUT,
        height=450,
        xaxis_title="Total Pengeluaran",
        yaxis_title="Kategori",
        xaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        yaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        coloraxis_colorbar=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY))
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # QUESTION 2: KATEGORI PALING MENINGKAT
    st.markdown(f"""
    <div class='insight-box'>
    <b style='color:{C_PRIMARY}'>2. Kategori apa yang mengalami peningkatan pengeluaran terbesar dari bulan ke bulan?</b>
    </div>
    """, unsafe_allow_html=True)

    monthly_category = (
        dff.groupby(['month', 'category_primary'])['amount']
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
        height=450,
        xaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        yaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        legend=dict(
            title=dict(text='category_primary', font=dict(color=C_PRIMARY)),
            font=dict(color=C_PRIMARY)
        )
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # QUESTION 3: HARI PALING SERING TRANSAKSI
    st.markdown(f"""
    <div class='insight-box'>
    <b style='color:{C_PRIMARY}'>3. Pada hari apa transaksi paling sering terjadi?</b>
    </div>
    """, unsafe_allow_html=True)

    day_freq = (
        dff['day_of_week']
        .value_counts()
        .reset_index()
    )

    day_freq.columns = ['day_of_week', 'count']

    fig3 = px.bar(
        day_freq,
        x='day_of_week',
        y='count',
        color='count',
        color_continuous_scale=[C_BLUE, C_ACCENT]
    )

    fig3.update_layout(
        **PLOTLY_LAYOUT,
        height=450,
        xaxis_title="Hari",
        yaxis_title="Jumlah Transaksi",
        xaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        yaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        coloraxis_colorbar=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY))
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    # QUESTION 4: RATA-RATA PENGELUARAN HARIAN
    st.markdown(f"""
    <div class='insight-box'>
    <b style='color:{C_PRIMARY}'>4. Berapa rata-rata pengeluaran harian user dan bagaimana perubahannya dari waktu ke waktu?</b>
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
        height=450,
        xaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        yaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    # QUESTION 5: WAKTU PALING BERISIKO LONJAKAN PENGELUARAN
    st.markdown(f"""
    <div class='insight-box'>
    <b style='color:{C_PRIMARY}'>5. Kapan waktu paling berisiko user mengalami lonjakan pengeluaran?</b>
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
        color='spike',
        color_continuous_scale=[C_WARNING, C_ERROR]
    )

    fig5.update_layout(
        **PLOTLY_LAYOUT,
        height=450,
        xaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        yaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        coloraxis_colorbar=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY))
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

    # QUESTION 6: METODE PEMBAYARAN vs SPENDING
    st.markdown(f"""
    <div class='insight-box'>
    <b style='color:{C_PRIMARY}'>6. Apakah terdapat perbedaan rata-rata pengeluaran berdasarkan metode pembayaran?</b>
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
        color='amount',
        color_continuous_scale=[C_SUCCESS, C_ACCENT]
    )

    fig6.update_layout(
        **PLOTLY_LAYOUT,
        height=450,
        xaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        yaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        coloraxis_colorbar=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY))
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
            height=420,
            title_font=dict(color=C_PRIMARY),
            xaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
            yaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
            coloraxis_colorbar=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY))
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
            height=420,
            title_font=dict(color=C_PRIMARY),
            xaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
            yaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
            coloraxis_colorbar=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY))
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
        height=450,
        xaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        yaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY))
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
        height=480,
        legend=dict(font=dict(color=C_PRIMARY))
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

# ─────────────────────────────────────────────
# Exploratory Data Analysis
# ─────────────────────────────────────────────
elif page == "🔍 Exploratory Data Analysis":

    st.markdown(
        "<div class='section-title'>Exploratory Data Analysis</div>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(f"<p style='color:{C_PRIMARY}; font-weight: 600;'>Pilih Sumbu X</p>", unsafe_allow_html=True)
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
            ],
            label_visibility="collapsed"
        )

    with col2:

        st.markdown(f"<p style='color:{C_PRIMARY}; font-weight: 600;'>Pilih Aggregation</p>", unsafe_allow_html=True)
        agg = st.selectbox(
            "Pilih Aggregation",
            ['sum', 'mean', 'count'],
            label_visibility="collapsed"
        )

    with col3:

        st.markdown(f"<p style='color:{C_PRIMARY}; font-weight: 600;'>Pilih Chart</p>", unsafe_allow_html=True)
        chart_type = st.selectbox(
            "Pilih Chart",
            ['Bar', 'Pie', 'Line'],
            label_visibility="collapsed"
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
        height=500,
        xaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        yaxis=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY)),
        coloraxis_colorbar=dict(tickfont=dict(color=C_PRIMARY), title_font=dict(color=C_PRIMARY))
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

    data_dict = {
        "No": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        "Nama Kolom": [
            "transaction_id", "user_id", "date", "merchant", "amount",
            "category_detail", "category_primary", "payment_method", "payment_media", "day_of_week",
            "month", "is_weekend", "day", "week", "time_of_day",
            "spending_level", "log_amount", "rolling_7d_spending", "transaction_count", "spike"
        ],
        "Tipe Data": [
            "string", "string", "datetime", "string", "float",
            "string", "string", "string", "string", "string",
            "integer", "boolean", "integer", "integer", "string",
            "string", "float", "float", "integer", "boolean"
        ],
        "Deskripsi": [
            "ID unik untuk setiap transaksi pengguna",
            "ID unik yang merepresentasikan masing-masing pengguna",
            "Tanggal dan waktu terjadinya transaksi",
            "Nama merchant atau penyedia layanan tempat transaksi dilakukan",
            "Nominal pengeluaran pada setiap transaksi",
            "Kategori detail transaksi yang lebih spesifik seperti groceries, entertainment, transport, dan utilities",
            "Kategori utama transaksi yang terdiri dari Needs, Wants, dan Investment",
            "Metode pembayaran yang digunakan pengguna seperti cash, transfer, debit, credit card, atau QRIS",
            "Media atau platform pembayaran yang digunakan seperti DANA, OVO, GoPay, ShopeePay, atau bank tertentu",
            "Hari dalam satu minggu saat transaksi dilakukan",
            "Bulan terjadinya transaksi dalam format numerik (1–12)",
            "Menunjukkan apakah transaksi terjadi pada akhir pekan (Sabtu/Minggu)",
            "Tanggal dalam satu bulan berdasarkan waktu transaksi",
            "Minggu ke dalam satu tahun berdasarkan kalender ISO",
            "Kategori waktu transaksi berdasarkan jam, yaitu Pagi, Siang, Sore, dan Malam",
            "Kategori tingkat pengeluaran berdasarkan nominal transaksi (low, medium, high)",
            "Hasil transformasi logaritmik dari nilai amount untuk membantu menstabilkan distribusi data",
            "Total akumulasi pengeluaran dari 7 transaksi terakhir sebagai indikator tren pengeluaran pengguna",
            "Jumlah transaksi yang terjadi pada periode waktu tertentu",
            "Indikator lonjakan pengeluaran, bernilai true jika transaksi termasuk kategori pengeluaran tinggi atau outlier"
        ]
    }

    dd = pd.DataFrame(data_dict)

    st.dataframe(
        dd,
        use_container_width=True,
        hide_index=True,
        height=600
    )

    st.markdown(f"""
    <div class='insight-box'>
    <b style='color:{C_PRIMARY}; font-size:16px;'>Penjelasan Tambahan:</b><br>
    <p style='color:{C_PRIMARY}; font-size:14px; line-height:1.8;'>
    Beberapa fitur tambahan dihasilkan melalui proses <b>feature engineering</b> untuk mendukung analisis perilaku keuangan dan pengembangan model prediksi, di antaranya:
    </p>
    <ul style='color:{C_PRIMARY}; font-size:14px; line-height:2;'>
        <li><b>spending_level</b> digunakan untuk mengelompokkan transaksi berdasarkan tingkat pengeluaran pengguna.</li>
        <li><b>rolling_7d_spending</b> digunakan untuk mengidentifikasi tren pengeluaran dalam periode terbaru.</li>
        <li><b>spike</b> digunakan sebagai indikator awal untuk mendeteksi potensi lonjakan pengeluaran (overspending).</li>
        <li><b>time_of_day</b> digunakan untuk menganalisis pola transaksi berdasarkan waktu aktivitas pengguna.</li>
        <li><b>log_amount</b> digunakan untuk membantu meningkatkan stabilitas distribusi data dan performa model machine learning.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# TEAMS
# ─────────────────────────────────────────────
elif page == "👥 Teams":

        st.markdown(
                "<div class='section-title'>Teams</div>",
                unsafe_allow_html=True
        )

        teams_html = f"""
        <div class='card' style='margin-bottom: 100px;'>
            <div style='margin-bottom: 24px;'>
                <h3 style='color:{C_PRIMARY}; font-size:18px; font-weight:700; margin:0 0 5px 0;'>Tentang Proyek</h3>
                <p style='color:{C_PRIMARY}; font-size:14px; line-height:1.8; margin:0;'>
                SADAR Finance Dashboard dikembangkan oleh tim CC26-PSU124 sebagai bagian dari Capstone Project Coding Camp 2026. Proyek ini merupakan hasil kolaborasi lintas peran yang menggabungkan kemampuan Data Science, AI Engineering, dan Fullstack Development untuk menciptakan solusi analitik keuangan yang informatif, interaktif, dan berdampak.
                </p>
            </div>
            <hr style='border:1px solid #f0f0f0; margin:20px 0;'>
            <table style='width:100%; border-collapse:collapse;'>
                <thead>
                 <tr style='background:{C_PRIMARY}; color:white;'>
                     <th style='padding:12px 8px; text-align:left;'>Nama Lengkap</th>
                     <th style='padding:12px 8px; text-align:left;'>ID Cohort</th>
                     <th style='padding:12px 8px; text-align:left;'>Learning Path</th>
                     <th style='padding:12px 8px; text-align:left;'>Link Linkedin</th>
                     <th style='padding:12px 8px; text-align:left;'>Link Github</th>
                 </tr>
                </thead>
                <tbody>
                 <tr style='border-bottom:1px solid #f0f0f0;'>
                     <td style='padding:12px 8px; color:{C_PRIMARY}; font-weight:600;'>Diah Ayu Puspasari</td>
                     <td style='padding:12px 8px; color:{C_PRIMARY};'>CDCC156D6X1244</td>
                     <td style='padding:12px 8px; color:{C_PRIMARY};'>Data Scientist</td>
                     <td style='padding:12px 8px;'><a style='color:{C_PRIMARY}; font-weight:500;' href='https://www.linkedin.com/in/diahaps/' target='_blank'>Linkedin</a></td>
                     <td style='padding:12px 8px;'><a style='color:{C_PRIMARY}; font-weight:500;' href='https://github.com/Diahayuups' target='_blank'>Github</a></td>
                 </tr>
                 <tr style='border-bottom:1px solid #f0f0f0;'>
                     <td style='padding:12px 8px; color:{C_PRIMARY}; font-weight:600;'>Marsela</td>
                     <td style='padding:12px 8px; color:{C_PRIMARY};'>CDCC156D6X0281</td>
                     <td style='padding:12px 8px; color:{C_PRIMARY};'>Data Scientist</td>
                     <td style='padding:12px 8px;'><a style='color:{C_PRIMARY}; font-weight:500;' href='https://www.linkedin.com/in/marsela-marsela-30a763248/' target='_blank'>Linkedin</a></td>
                     <td style='padding:12px 8px;'><a style='color:{C_PRIMARY}; font-weight:500;' href='https://github.com/Marsela0603' target='_blank'>Github</a></td>
                 </tr>
                 <tr style='border-bottom:1px solid #f0f0f0;'>
                     <td style='padding:12px 8px; color:{C_PRIMARY}; font-weight:600;'>Farrel Al Faqih Ekatama</td>
                     <td style='padding:12px 8px; color:{C_PRIMARY};'>CACC295D6Y0695</td>
                     <td style='padding:12px 8px; color:{C_PRIMARY};'>AI Engineer</td>
                     <td style='padding:12px 8px;'><a style='color:{C_PRIMARY}; font-weight:500;' href='https://www.linkedin.com/in/farrel-al-faqih-ekatama-339980217/' target='_blank'>Linkedin</a></td>
                     <td style='padding:12px 8px;'><a style='color:{C_PRIMARY}; font-weight:500;' href='https://github.com/farrelalfaqih' target='_blank'>Github</a></td>
                 </tr>
                 <tr style='border-bottom:1px solid #f0f0f0;'>
                     <td style='padding:12px 8px; color:{C_PRIMARY}; font-weight:600;'>Dzaky Jaisy Al-Qorney</td>
                     <td style='padding:12px 8px; color:{C_PRIMARY};'>CACC349D6Y1657</td>
                     <td style='padding:12px 8px; color:{C_PRIMARY};'>AI Engineer</td>
                     <td style='padding:12px 8px;'><a style='color:{C_PRIMARY}; font-weight:500;' href='https://www.linkedin.com/in/dzaky-jaisy-al-qorney-002889327?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app' target='_blank'>Linkedin</a></td>
                     <td style='padding:12px 8px;'><a style='color:{C_PRIMARY}; font-weight:500;' href='https://github.com/iMiNerVaa' target='_blank'>Github</a></td>
                 </tr>
                 <tr style='border-bottom:1px solid #f0f0f0;'>
                     <td style='padding:12px 8px; color:{C_PRIMARY}; font-weight:600;'>Fhazar Raffiful Aqyla</td>
                     <td style='padding:12px 8px; color:{C_PRIMARY};'>CFCC882D6Y0583</td>
                     <td style='padding:12px 8px; color:{C_PRIMARY};'>Fullstack Developer</td>
                     <td style='padding:12px 8px;'><a style='color:{C_PRIMARY}; font-weight:500;' href='https://www.linkedin.com/in/fhazaraqyla/' target='_blank'>Linkedin/</a></td>
                     <td style='padding:12px 8px;'><a style='color:{C_PRIMARY}; font-weight:500;' href='https://github.com/Fhazar-Aqyla' target='_blank'>Github</a></td>
                 </tr>
                 <tr>
                     <td style='padding:12px 8px; color:{C_PRIMARY}; font-weight:600;'>Muhammad Habib Rafi</td>
                     <td style='padding:12px 8px; color:{C_PRIMARY};'>CFCC220D6Y1309</td>
                     <td style='padding:12px 8px; color:{C_PRIMARY};'>Fullstack Developer</td>
                     <td style='padding:12px 8px;'><a style='color:{C_PRIMARY}; font-weight:500;' href='https://www.linkedin.com/in/mhmdhabibrafi' target='_blank'>Linkedin</a></td>
                     <td style='padding:12px 8px;'><a style='color:{C_PRIMARY}; font-weight:500;' href='https://github.com/mhmdhabibrafi' target='_blank'>Github</a></td>
                 </tr>
                </tbody>
            </table>
        </div>
        """

        st.markdown(teams_html, unsafe_allow_html=True)

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────

st.markdown(
    f"""
    <div id='footer' style='position:fixed; left:0; right:0; bottom:0; background-color: {C_PRIMARY}; color: white; font-size: 13px; padding: 12px 0; margin: 0; border-radius: 0; z-index: 9999;'>
        <div style='display:flex; justify-content:center; align-items:center; width:100%;'>
            <p style='margin: 0; font-weight: 600;'>Sadar Finance - Coding Camp 2026 - CC26-PSU124</p>
        </div>
    </div>
    <script>
        // Monitor sidebar visibility and adjust footer position
        const footer = document.getElementById('footer');
        const sidebar = document.querySelector('[data-testid="stSidebar"]');
        
        function updateFooterPosition() {{
            if (sidebar && sidebar.offsetParent !== null) {{
                // Sidebar is visible
                const sidebarWidth = sidebar.offsetWidth;
                footer.style.left = sidebarWidth + 'px';
            }} else {{
                // Sidebar is hidden
                footer.style.left = '0px';
            }}
        }}
        
        // Initial call
        updateFooterPosition();
        
        // Monitor changes with MutationObserver
        const observer = new MutationObserver(updateFooterPosition);
        const config = {{ attributes: true, subtree: true, attributeFilter: ['style'] }};
        if (sidebar) observer.observe(sidebar, config);
        
        // Also update on window resize
        window.addEventListener('resize', updateFooterPosition);
    </script>
    """,
    unsafe_allow_html=True
)