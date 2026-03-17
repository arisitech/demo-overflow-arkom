import streamlit as st


# ── LOGO ─────────────────────────────────────────────────────────────────────
LOGO_B64 = "/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAJQApgMBIgACEQEDEQH/xAAcAAEAAgMBAQEAAAAAAAAAAAAABgcBBQgEAwL/xAA7EAABAwMCAwQHBgQHAAAAAAAAAQIDBAURBhIHEyExMmFxFDZBUXKBsiIzUmJzdDRCocIVFiRTgpGT/8QAGAEBAQEBAQAAAAAAAAAAAAAAAAMCAQT/xAAfEQEAAwEAAgMBAQAAAAAAAAAAAQIRAxIhIjFBMmH/2gAMAwEAAhEDEQA/ALxAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMKAyMnPPEqaVut7s1ssiIj29Ecv4Gl4aRVV0tZ1VcqtFD1/4IbtTxiJYrfZxtgq4Cmh1tHNNYZWU7HvfvZ0YiqveMx7lSsbON9kZIDoGmrYbvK6phnYxYFRFkaqJnKe8pisnm9MqESeX75/86/iUrHHbZEs9pjlOfbqXIyczf4PqDGfQLn/5SF1cLIKmm0hDHWxSxTJLIqtmRUd3vEzfnFY3WK3mZzEwBjKDKE1GQDGUAyDGUGUAyDGUMgAYyhkAAABhTJhQOduJnrxd/jZ9DS8tI+qln/ZQ/QhRvEz14u/xs+hpeWkfVSz/ALKH6EPR1/iqPP8AqX1uF7oKCfkVcqsfjOEY5enyQ9NDWQXCBJ6V+6NVVMq1U7PMjmprFXXG4pNTNYrEjRv2n46m203Qz2+2Np6lER6PcuGuymFU86dOnWes1mPTbHK1X/HT/rv+pTqk5Wq/46f9d/1Kejh+qdfx1NF9yz4UI1cLzcbjcprVplsO6mXbWV86K6OB34GtTvv8OxPab2snWltM1Q1MrFA56J5NyanQlMlPo+1vVE5tRTNqZlTtdJIm9y/9uUhCjyppm8KvNfrG6JL24ZDCkefh2KuPmfSnu1ys1bT0Wo+TNTVD+XTXKBmxqyL2MkZ12qvsXsXs6Lg0FVZOIMt6dcIb1SRs5m5lKkruUjM9Gq3b16e3tJjqG3tumna2jqGojpad3Vq91+MoqL4Kan/XIe2urqe30ctXWSNigharpHr2NRCnr7xcuU070s0EFLSp3ZJk3yO8V64Ty6nr4kXmortBadc5XIte1k0ydm7axFwvzXPyPrwWsdDUUlZd6mGOaojqORFvTdsRGtcqonsVd39ClK1rXyli1pm3jDSW3ixf4JkWrbSVsKLh7Nmx2PBU7F80Usut1S2o0HV6is3RzKd0kaTMX7Lk9ip7fkuFPbe9K2W+ywS3GhjkkhduRyJtV35XY7U8Dza9jjh0HeIoWNZGyjc1rGphEROxEQzNqWmMhqItWJ2UY4ca4vOo78+iuXovJbTOkTkxK1coqJ7195J+IV7rNP6akuFv5XPbLGxOa3c3CuwvTKFH6T1HPpe5urqanjne6JY1bIqoiIqouenkbjVHESu1LaHW2ot9NBG+Rr1fHI5VTauU7Ss8vnuek46fH39p/wAMNWXTU7ril05H+nSPZyY1b3s5z1X3E/Kj4E9+8+UP9xbhHrGXmIV5ztYAATbDCmQoHOvEz14u/wAbPoaXlpD1Vs/7KH6ENHfOG1mvd1qLjVT1rZqhUV6RyNRvRETp9nwJXbqOO32+mooVc6OnibExXrlVRqYTPj0K3vFqxEJ0rMWmXoBkElGDlar610/67/qU6pUgz+FWm3yvld6buc5XKvpC9qrn3FeV4rup9KzbMTRI2y0vLemWvj2qnvRUI5pCoSgi/wAtVi8urt7eXBu6c+nTpG9vvwmEVPYqeJJ2tRrEanYiYPDdrNQ3eFjK6Hc6Nd0UrHKySJfex6dWr5KSbxCKjQ2pZL098erq9ltfJu2pUScxrVXuomcfM/WprPHSpHbLZeL5Pd6zLYYXXOVyRt/mleme6mfmqohIl03W52t1Pekh/wBvdCq4925Y93zznxNhaLFQWjmOpI3LPL99UTPWSWX4nr1XyN+cs+KL8QdJvuGj6aktbFfPbdroY0Tq9qN2uanjjr5oVroXWc+k554n0y1FHO7MsW7a9j06ZTPTOEwqLj+nXoNW+JHr5ojT98mdPW0DUnd3pYXLG53mre35mqdIiPG30zak7sK8v3FusmdElkpG0zGOR0j6nD1f+XCLhE+efIll5us964W3GvqaGSjlmo3LynrnP5k8F7Uz1Pfa+HmmbZOk8Nv5sjV3NWokWTC+CL0JBcLfTXGgmoayPmU0zNj2ZxlPd0OWtTY8Yditveyo7hRbaK56llguNJBVRJSOcjJo0eiLub16+ZMeKWnrNbdIy1NvtNFTTpPE1JIoWtciK7r1RCW2TSFksdY6rtlJyZnMViu5jl6KucdV8D33m0UV7oXUVyh51O5yOVm5UyqLlOw1PXb+X45FPjisuBXfvPlF/cW4aew6ZtOn1mW00vIWbHM+0q5x2dvmbhDF7eVtbpXIwABhoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAf/2Q=="
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
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 16px;
    }
    .header-text { flex: 1; }
    .header-box h2 { color: white; margin: 0 0 4px 0; font-size: 22px; }
    .header-box p  { color: #aab4d4; margin: 0; font-size: 13px; }
    .header-logo {
        background: white;
        border-radius: 8px;
        padding: 8px 12px;
        display: flex;
        align-items: center;
        flex-shrink: 0;
    }
    .header-logo img { height: 40px; width: auto; display: block; }

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
st.markdown(f"""
<div class="header-box">
    <div class="header-text">
        <h2>🖥️ Demo Overflow — Kasus Kasir</h2>
        <p>Arsitektur dan Organisasi Komputer &nbsp;·&nbsp; STTI NIIT Jakarta</p>
    </div>
    <div class="header-logo">
        <img src="data:image/jpeg;base64,{LOGO_B64}" alt="ITech Logo">
    </div>
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
