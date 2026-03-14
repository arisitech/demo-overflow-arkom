import streamlit as st

# ── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Demo Overflow — Kasus Kasir",
    page_icon="🖥️",
    layout="centered"
)

# ── STYLE ─────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stApp { background-color: #f8f9fa; }

    .header-box {
        background: #1a1a2e;
        color: white;
        padding: 20px 28px;
        border-radius: 10px;
        margin-bottom: 24px;
    }
    .header-box h2 { color: white; margin: 0 0 4px 0; font-size: 22px; }
    .header-box p  { color: #aab4d4; margin: 0; font-size: 13px; }

    .barang-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 16px 20px;
        margin-bottom: 12px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }
    .barang-label {
        font-size: 13px;
        color: #888;
        margin-bottom: 2px;
    }
    .barang-nama {
        font-size: 17px;
        font-weight: 700;
        color: #1a1a2e;
        margin-bottom: 0;
    }

    .biner-row {
        font-family: 'Courier New', monospace;
        font-size: 15px;
        background: #f0f4ff;
        border-radius: 6px;
        padding: 10px 14px;
        margin: 8px 0;
        letter-spacing: 2px;
    }
    .bit-dibuang   { color: #cc0000; font-weight: bold; }
    .bit-tersimpan { color: #0055cc; font-weight: bold; }

    .result-ok {
        background: #e8f5e9;
        border-left: 4px solid #2e7d32;
        border-radius: 6px;
        padding: 10px 16px;
        color: #1b5e20;
        font-weight: 600;
        margin-top: 8px;
    }
    .result-error {
        background: #ffebee;
        border-left: 4px solid #c62828;
        border-radius: 8px;
        padding: 14px 18px;
        margin-top: 10px;
    }
    .result-error h4 { color: #b71c1c; margin: 0 0 6px 0; font-size: 15px; }
    .result-error p  { color: #7f0000; margin: 0; font-size: 14px; }

    .tabel-tipe th {
        background: #1a1a2e;
        color: white;
        padding: 8px 12px;
        text-align: left;
    }
    .tabel-tipe td { padding: 8px 12px; border-bottom: 1px solid #eee; }
    .tabel-tipe tr.too-small { background: #fff3f3; color: #c62828; }
    .tabel-tipe tr.ok-row    { background: #f0fff4; color: #1b5e20; }

    .footer {
        text-align: center;
        color: #aaa;
        font-size: 12px;
        margin-top: 40px;
        padding-top: 16px;
        border-top: 1px solid #ddd;
    }
</style>
""", unsafe_allow_html=True)

# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-box">
    <h2>🖥️ Demo Overflow — Kasus Kasir</h2>
    <p>Arsitektur dan Organisasi Komputer &nbsp;·&nbsp; STTI NIIT Jakarta &nbsp;·&nbsp; Arismunandar, M.T.I.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("**Sistem kasir menyimpan harga dalam tipe data `char` (8 bit, nilai 0–255). Masukkan harga untuk setiap barang dan lihat apa yang terjadi.**")
st.caption("💡 Coba masukkan nilai di atas 255 pada barang ketiga untuk melihat overflow.")

st.divider()

# ── FUNGSI UTAMA ──────────────────────────────────────────────────────────────
def proses_char(harga):
    overflow  = harga > 255
    hasil     = harga % 256
    biner_in  = bin(harga)[2:]
    return overflow, hasil, biner_in

def tampil_biner(biner_in, overflow):
    if overflow and len(biner_in) > 8:
        dibuang   = biner_in[:-8]
        tersimpan = biner_in[-8:].zfill(8)
        html = (f'<div class="biner-row">'
                f'<span class="bit-dibuang">{dibuang}</span>'
                f'<span class="bit-tersimpan">{tersimpan}</span>'
                f' &nbsp;<span style="color:#888;font-size:12px;">({len(biner_in)} bit — bit merah dibuang)</span>'
                f'</div>')
    else:
        tersimpan = biner_in.zfill(8)
        html = (f'<div class="biner-row">'
                f'<span class="bit-tersimpan">{tersimpan}</span>'
                f' &nbsp;<span style="color:#888;font-size:12px;">({len(biner_in)} bit)</span>'
                f'</div>')
    return html

# ── STATE ─────────────────────────────────────────────────────────────────────
barang_list = ["Pulpen", "Buku tulis", "Kopi sachet"]

if "langkah" not in st.session_state:
    st.session_state.langkah  = 0
if "riwayat" not in st.session_state:
    st.session_state.riwayat  = []
if "overflow_terjadi" not in st.session_state:
    st.session_state.overflow_terjadi = False

# ── TAMPILKAN RIWAYAT ─────────────────────────────────────────────────────────
for item in st.session_state.riwayat:
    with st.container():
        st.markdown(f"""
        <div class="barang-card">
            <div class="barang-label">Barang {item['no']}</div>
            <div class="barang-nama">{item['nama']}</div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Input:** `{item['harga']}`")
            st.markdown(f"**Tipe data:** `char` (8 bit, maks = 255)")
        with col2:
            st.markdown(f"**Biner:**")
            st.markdown(tampil_biner(item['biner'], item['overflow']),
                       unsafe_allow_html=True)

        if item['overflow']:
            st.markdown(f"""
            <div class="result-error">
                <h4>⚠ OVERFLOW!</h4>
                <p>Input <strong>{item['harga']}</strong> melebihi kapasitas char (maks 255).<br>
                Bit ke-{len(item['biner'])} dibuang → tersimpan sebagai <strong>{item['hasil']}</strong></p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-ok">
                ✓ Aman &nbsp;—&nbsp; Tersimpan sebagai {item['harga']}
            </div>
            """, unsafe_allow_html=True)

        st.divider()

# ── INPUT BERIKUTNYA ──────────────────────────────────────────────────────────
langkah = st.session_state.langkah

if not st.session_state.overflow_terjadi and langkah < len(barang_list):
    nama_barang = barang_list[langkah]

    st.markdown(f"### Barang {langkah + 1} dari {len(barang_list)}: **{nama_barang}**")

    with st.form(key=f"form_{langkah}"):
        harga = st.number_input(
            f"Masukkan harga untuk '{nama_barang}'",
            min_value=0, max_value=99999,
            step=1, value=0,
            help="Coba masukkan nilai di atas 255 untuk melihat overflow"
        )
        submit = st.form_submit_button("💾  Simpan ke Memori", use_container_width=True)

    if submit:
        overflow, hasil, biner_in = proses_char(harga)
        st.session_state.riwayat.append({
            "no"      : langkah + 1,
            "nama"    : nama_barang,
            "harga"   : harga,
            "hasil"   : hasil,
            "biner"   : biner_in,
            "overflow": overflow,
        })
        if overflow:
            st.session_state.overflow_terjadi = True
        else:
            st.session_state.langkah += 1
        st.rerun()

# ── KESIMPULAN SETELAH OVERFLOW ───────────────────────────────────────────────
if st.session_state.overflow_terjadi:
    st.error("🚨 **Program berhenti — data tidak bisa disimpan dengan benar.**")

    if st.button("🔄  Ulangi Demo", use_container_width=True):
        st.session_state.langkah          = 0
        st.session_state.riwayat          = []
        st.session_state.overflow_terjadi = False
        st.rerun()

# ── SELESAI TANPA OVERFLOW ────────────────────────────────────────────────────
elif langkah == len(barang_list):
    total = sum(i['hasil'] for i in st.session_state.riwayat)
    st.success(f"✅ Semua barang tersimpan dengan aman. Total: **{total}**")

    if st.button("🔄  Ulangi Demo", use_container_width=True):
        st.session_state.langkah          = 0
        st.session_state.riwayat          = []
        st.session_state.overflow_terjadi = False
        st.rerun()

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Arismunandar, M.T.I. &nbsp;·&nbsp; Arsitektur dan Organisasi Komputer &nbsp;·&nbsp; STTI NIIT Jakarta
</div>
""", unsafe_allow_html=True)
