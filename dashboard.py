"""
Dashboard Interaktif untuk Quantum Readiness Scanner
Visualisasi hasil audit kesiapan quantum website kampus dan BUMN Indonesia
"""

import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
from datetime import datetime
import os

# Konfigurasi halaman
st.set_page_config(
    page_title="Quantum Readiness Scanner Dashboard",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .status-ready {
        color: #28a745;
        font-weight: bold;
    }
    .status-partial {
        color: #ffc107;
        font-weight: bold;
    }
    .status-not-ready {
        color: #dc3545;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


def load_scan_results(filename='scan_results.json'):
    """Memuat hasil scan dari file JSON"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        st.error(f"File {filename} tidak ditemukan. Silakan jalankan scanner terlebih dahulu.")
        return None
    except json.JSONDecodeError:
        st.error(f"Error membaca file {filename}. Format JSON tidak valid.")
        return None


def process_results_to_dataframe(results):
    """Mengubah hasil scan menjadi DataFrame"""
    processed_data = []
    
    for result in results:
        url = result.get('url', '')
        accessible = result.get('accessible', False)
        qr = result.get('quantum_readiness', {})
        ssl_info = result.get('ssl_info', {})
        
        row = {
            'URL': url,
            'Dapat Diakses': 'Ya' if accessible else 'Tidak',
            'Status': qr.get('status', 'Unknown'),
            'Score': qr.get('score', 0),
            'Persentase': qr.get('percentage', 0),
            'TLS Version': ssl_info.get('tls_version', 'N/A'),
            'Cipher Suite': ssl_info.get('cipher_suite', 'N/A'),
            'Key Size': str(ssl_info.get('key_size', 'N/A')),
            'Sertifikat Valid': 'Ya' if ssl_info.get('certificate_valid') else 'Tidak'
        }
        
        # Ekstrak kategori website
        if 'ac.id' in url or 'edu' in url:
            row['Kategori'] = 'Universitas'
        elif any(bumn in url.lower() for bumn in ['bumn', 'pertamina', 'pln', 'telkom', 'bri', 'bni', 'mandiri']):
            row['Kategori'] = 'BUMN'
        elif any(gov in url.lower() for gov in ['go.id', 'gov', 'kemenkeu', 'bpkp', 'bpk']):
            row['Kategori'] = 'Pemerintah'
        else:
            row['Kategori'] = 'Lainnya'
        
        processed_data.append(row)
    
    return pd.DataFrame(processed_data)


def create_summary_metrics(df):
    """Membuat metrik ringkasan"""
    total = len(df)
    accessible = len(df[df['Dapat Diakses'] == 'Ya'])
    quantum_ready = len(df[df['Status'] == 'Quantum-Ready'])
    partially_ready = len(df[df['Status'] == 'Partially Ready'])
    not_ready = len(df[df['Status'] == 'Not Ready'])
    avg_score = df['Score'].mean()
    
    return {
        'total': total,
        'accessible': accessible,
        'quantum_ready': quantum_ready,
        'partially_ready': partially_ready,
        'not_ready': not_ready,
        'avg_score': avg_score
    }


def create_status_distribution_chart(df):
    """Membuat chart distribusi status"""
    status_counts = df['Status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Jumlah']
    
    colors = {
        'Quantum-Ready': '#28a745',
        'Partially Ready': '#ffc107',
        'Not Ready': '#dc3545',
        'Inaccessible': '#6c757d',
        'Error': '#6c757d'
    }
    
    fig = px.pie(
        status_counts, 
        values='Jumlah', 
        names='Status',
        title='Distribusi Status Kesiapan Quantum',
        color='Status',
        color_discrete_map=colors
    )
    
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=400)
    
    return fig


def create_category_comparison_chart(df):
    """Membuat chart perbandingan antar kategori"""
    category_status = df.groupby(['Kategori', 'Status'], as_index=False).size()
    category_status.columns = ['Kategori', 'Status', 'Jumlah']
    
    fig = px.bar(
        category_status,
        x='Kategori',
        y='Jumlah',
        color='Status',
        title='Perbandingan Status Kesiapan Berdasarkan Kategori',
        barmode='group',
        color_discrete_map={
            'Quantum-Ready': '#28a745',
            'Partially Ready': '#ffc107',
            'Not Ready': '#dc3545',
            'Inaccessible': '#6c757d',
            'Error': '#6c757d'
        }
    )
    
    fig.update_layout(height=400, xaxis_title='Kategori', yaxis_title='Jumlah Website')
    
    return fig


def create_score_distribution_chart(df):
    """Membuat chart distribusi score"""
    accessible_df = df[df['Dapat Diakses'] == 'Ya']
    
    fig = px.histogram(
        accessible_df,
        x='Score',
        nbins=20,
        title='Distribusi Score Kesiapan Quantum',
        labels={'Score': 'Score (0-100)', 'count': 'Jumlah Website'},
        color_discrete_sequence=['#667eea']
    )
    
    fig.update_layout(height=400, showlegend=False)
    
    return fig


def create_tls_version_chart(df):
    """Membuat chart distribusi versi TLS"""
    tls_counts = df[df['TLS Version'] != 'N/A']['TLS Version'].value_counts().reset_index()
    tls_counts.columns = ['TLS Version', 'Jumlah']
    
    fig = px.bar(
        tls_counts,
        x='TLS Version',
        y='Jumlah',
        title='Distribusi Versi TLS yang Digunakan',
        color='Jumlah',
        color_continuous_scale='blues'
    )
    
    fig.update_layout(height=400, showlegend=False)
    
    return fig


def create_top_bottom_websites(df, top_n=10):
    """Membuat tabel top dan bottom websites"""
    accessible_df = df[df['Dapat Diakses'] == 'Ya'].copy()
    
    if len(accessible_df) == 0:
        return None, None
    
    # Sort by score
    sorted_df = accessible_df.sort_values('Score', ascending=False)
    
    top_websites = sorted_df.head(top_n)[['URL', 'Status', 'Score', 'TLS Version']]
    bottom_websites = sorted_df.tail(top_n)[['URL', 'Status', 'Score', 'TLS Version']]
    
    return top_websites, bottom_websites


def main():
    # Header
    st.markdown('<h1 class="main-header">🔐 Quantum Readiness Scanner Dashboard</h1>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/000000/security-lock.png", width=100)
        st.title("Menu Navigasi")
        
        page = st.radio(
            "Pilih Halaman:",
            ["📊 Overview", "📈 Analisis Detail", "📋 Data Lengkap", "ℹ️ Informasi"]
        )
        
        st.markdown("---")
        st.markdown("### Tentang Proyek")
        st.info("""
        **Quantum Readiness Scanner**
        
        Alat audit untuk mengecek kesiapan website kampus dan BUMN Indonesia terhadap ancaman quantum computing.
        
        Dikembangkan sebagai bagian dari Tugas Audit TI 2025.
        """)
    
    # Load data
    scan_data = load_scan_results()
    
    if scan_data is None:
        st.warning("⚠️ Belum ada data hasil scan. Jalankan `python quantum_scanner.py` terlebih dahulu.")
        return
    
    # Process data
    results = scan_data.get('results', [])
    metadata = scan_data.get('scan_metadata', {})
    df = process_results_to_dataframe(results)
    metrics = create_summary_metrics(df)
    
    # Tampilkan metadata scan
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Informasi Scan")
    st.sidebar.text(f"Waktu Scan: {metadata.get('scan_time', 'N/A')[:19]}")
    st.sidebar.text(f"Total Website: {metadata.get('total_scanned', 0)}")
    st.sidebar.text(f"Versi Scanner: {metadata.get('scanner_version', '1.0.0')}")
    
    # Page routing
    if page == "📊 Overview":
        show_overview_page(df, metrics)
    elif page == "📈 Analisis Detail":
        show_analysis_page(df, metrics)
    elif page == "📋 Data Lengkap":
        show_data_page(df)
    elif page == "ℹ️ Informasi":
        show_info_page()


def show_overview_page(df, metrics):
    """Halaman overview dengan metrik utama"""
    st.header("📊 Ringkasan Hasil Audit")
    
    # Metrik utama
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Website",
            value=metrics['total'],
            delta=f"{metrics['accessible']} dapat diakses"
        )
    
    with col2:
        st.metric(
            label="Quantum-Ready",
            value=metrics['quantum_ready'],
            delta=f"{round((metrics['quantum_ready']/metrics['accessible'])*100 if metrics['accessible'] > 0 else 0, 1)}%"
        )
    
    with col3:
        st.metric(
            label="Partially Ready",
            value=metrics['partially_ready'],
            delta=f"{round((metrics['partially_ready']/metrics['accessible'])*100 if metrics['accessible'] > 0 else 0, 1)}%"
        )
    
    with col4:
        st.metric(
            label="Rata-rata Score",
            value=f"{round(metrics['avg_score'], 1)}/100",
            delta="Score keseluruhan"
        )
    
    st.markdown("---")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_status_distribution_chart(df), use_container_width=True)
    
    with col2:
        st.plotly_chart(create_category_comparison_chart(df), use_container_width=True)
    
    # Key Findings
    st.markdown("---")
    st.header("🔍 Temuan Utama")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.success(f"""
        **✓ Capaian Positif:**
        - {metrics['quantum_ready']} website sudah quantum-ready
        - {len(df[df['TLS Version'] == 'TLSv1.3'])} website menggunakan TLS 1.3
        - {metrics['accessible']} dari {metrics['total']} website dapat diakses
        """)
    
    with col2:
        st.error(f"""
        **✗ Area Perbaikan:**
        - {metrics['not_ready']} website belum siap menghadapi quantum
        - {metrics['total'] - metrics['accessible']} website tidak dapat diakses
        - Diperlukan upgrade infrastruktur keamanan
        """)


def show_analysis_page(df, metrics):
    """Halaman analisis detail"""
    st.header("📈 Analisis Detail")
    
    # Score distribution
    st.plotly_chart(create_score_distribution_chart(df), use_container_width=True)
    
    st.markdown("---")
    
    # TLS Version distribution
    st.plotly_chart(create_tls_version_chart(df), use_container_width=True)
    
    st.markdown("---")
    
    # Top and Bottom websites
    st.header("🏆 Ranking Website")
    
    top_websites, bottom_websites = create_top_bottom_websites(df, top_n=10)
    
    if top_websites is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("✅ Top 10 Website Terbaik")
            st.dataframe(top_websites, use_container_width=True, hide_index=True)
        
        with col2:
            st.subheader("⚠️ 10 Website yang Perlu Perhatian")
            st.dataframe(bottom_websites, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Category breakdown
    st.header("📊 Breakdown Berdasarkan Kategori")
    
    category_summary = df.groupby('Kategori').agg({
        'Score': 'mean',
        'URL': 'count'
    }).round(2).reset_index()
    category_summary.columns = ['Kategori', 'Rata-rata Score', 'Jumlah Website']
    
    st.dataframe(category_summary, use_container_width=True, hide_index=True)


def show_data_page(df):
    """Halaman data lengkap"""
    st.header("📋 Data Lengkap Hasil Scan")
    
    # Filter options
    col1, col2, col3 = st.columns(3)
    
    with col1:
        status_filter = st.multiselect(
            "Filter Status:",
            options=df['Status'].unique(),
            default=df['Status'].unique()
        )
    
    with col2:
        category_filter = st.multiselect(
            "Filter Kategori:",
            options=df['Kategori'].unique(),
            default=df['Kategori'].unique()
        )
    
    with col3:
        accessible_filter = st.multiselect(
            "Filter Aksesibilitas:",
            options=['Ya', 'Tidak'],
            default=['Ya', 'Tidak']
        )
    
    # Apply filters
    filtered_df = df[
        (df['Status'].isin(status_filter)) &
        (df['Kategori'].isin(category_filter)) &
        (df['Dapat Diakses'].isin(accessible_filter))
    ]
    
    st.markdown(f"**Menampilkan {len(filtered_df)} dari {len(df)} website**")
    
    # Display data
    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Score": st.column_config.ProgressColumn(
                "Score",
                format="%d/100",
                min_value=0,
                max_value=100,
            ),
        }
    )
    
    # Download button
    csv = filtered_df.to_csv(index=False, encoding='utf-8-sig')
    st.download_button(
        label="📥 Download Data (CSV)",
        data=csv,
        file_name=f"quantum_scan_results_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )


def show_info_page():
    """Halaman informasi"""
    st.header("ℹ️ Informasi Proyek")
    
    st.markdown("""
    ## Quantum Readiness Scanner
    
    ### 🎯 Tujuan Proyek
    Proyek ini bertujuan untuk mengaudit kesiapan website kampus dan BUMN Indonesia dalam menghadapi 
    ancaman quantum computing yang diprediksi akan menjadi nyata dalam 5-10 tahun ke depan.
    
    ### 🔬 Metodologi
    Scanner ini melakukan evaluasi berdasarkan beberapa parameter:
    
    1. **Versi TLS/SSL** (30 poin)
       - TLS 1.3: Standar terbaru dan paling aman
       - TLS 1.2: Masih aman tapi disarankan upgrade
       - TLS 1.1 atau lebih lama: Tidak aman
    
    2. **Cipher Suite** (40 poin)
       - Quantum-safe ciphers (AES-256-GCM, ChaCha20-Poly1305)
       - Cipher yang rentan quantum (RSA, DH, ECDH, ECDSA)
    
    3. **Ukuran Key** (20 poin)
       - 3072+ bit: Sangat kuat
       - 2048 bit: Standar (perlu upgrade)
       - < 2048 bit: Lemah
    
    4. **Validitas Sertifikat** (10 poin)
       - Sertifikat valid dan terpercaya
    
    ### 📊 Interpretasi Hasil
    
    - **Quantum-Ready (80-100)**: Website sudah siap menghadapi ancaman quantum
    - **Partially Ready (50-79)**: Perlu beberapa upgrade untuk kesiapan penuh
    - **Not Ready (0-49)**: Sangat rentan, perlu upgrade segera
    
    ### 🛠️ Teknologi yang Digunakan
    
    - **Python**: Bahasa pemrograman utama
    - **Streamlit**: Framework dashboard interaktif
    - **Plotly**: Library visualisasi data
    - **SSL/TLS Libraries**: Untuk analisis keamanan
    
    ### 👨‍💻 Pengembang
    
    Proyek ini dikembangkan sebagai bagian dari Tugas Audit TI 2025 dengan fokus pada 
    keamanan siber dan kesiapan infrastruktur digital Indonesia menghadapi era quantum computing.
    
    ### 📚 Referensi
    
    1. NIST Post-Quantum Cryptography Standardization
    2. NSA Quantum-Safe Cryptography Guidelines
    3. BSSN - Panduan Keamanan Siber Indonesia
    
    ### 📞 Kontak & Kontribusi
    
    Proyek ini bersifat open-source. Kontribusi dan saran perbaikan sangat diterima 
    melalui GitHub repository.
    """)
    
    st.markdown("---")
    
    st.success("""
    💡 **Tips Penggunaan Dashboard:**
    - Gunakan menu navigasi di sidebar untuk berpindah halaman
    - Filter data di halaman "Data Lengkap" untuk analisis spesifik
    - Download hasil dalam format CSV untuk analisis lebih lanjut
    - Share link dashboard untuk kolaborasi dengan tim
    """)


if __name__ == "__main__":
    main()
