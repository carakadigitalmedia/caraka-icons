# Caraka Icons Super

Library ikon WebP + CSS untuk GitHub Pages dengan generator otomatis, katalog responsif, pencarian, filter kategori, pengurutan, dan tombol salin class.

## Fitur
- Auto-generate CSS dan `icons.json` dari file `.webp`.
- Katalog otomatis: tidak perlu edit HTML saat menambah ikon.
- Pencarian nama, class, slug, kategori, kata kunci.
- Filter kategori berbasis subfolder `icons/`.
- Urut nama A–Z, Z–A, atau kategori.
- Validasi benturan class dan pesan error yang jelas.
- Nama file diubah menjadi slug konsisten.
- UI responsif, aksesibilitas keyboard, reduced-motion, dan fallback salin.
- Tidak memakai framework JS atau build bundler.

## Instalasi ke repository yang sudah ada
1. Unduh ZIP dan ekstrak.
2. Upload/replace isi paket ke root repository `carakadigitalmedia/caraka-icons`.
3. Jangan menghapus gambar ikon yang sudah Anda miliki; gabungkan semua file dari `icons/`.
4. Pastikan `.github/workflows/generate-icons.yml` dan `scripts/generate_icons.py` terunggah.
5. GitHub → Settings → Actions → General → Workflow permissions → pilih **Read and write permissions** → Save.
6. Pastikan Settings → Pages tetap `Deploy from a branch`, branch `main`, folder `/(root)`.
7. Commit file. Buka Actions → **Build Caraka Icons** dan tunggu status hijau. Jalankan **Run workflow** jika diperlukan.
8. Buka https://carakadigitalmedia.github.io/caraka-icons/

## Menambah ikon
Upload WebP ke folder `icons/`, lalu commit ke branch `main`.
- `icons/tkk-memasak.webp` → `ci ci-tkk-memasak`, kategori `Umum`.
- `icons/tkk/siaga.webp` → `ci ci-siaga`, kategori `Tkk`.
Nama class berasal dari nama file tanpa ekstensi. Nama file harus unik setelah normalisasi; jika bentrok, generator gagal dan log Actions menjelaskan file yang perlu diganti.

## Pemakaian CI3
Tambahkan di `<head>` template utama:
```html
<link rel="stylesheet" href="https://carakadigitalmedia.github.io/caraka-icons/caraka-icons.css">
```
Gunakan di view:
```html
<i class="ci ci-tkk-berkemah" aria-hidden="true"></i>
<i class="ci ci-tkk-memasak ci-lg" aria-hidden="true"></i>
```

Ukuran: `ci-xs`, `ci-sm`, `ci-lg`, `ci-xl`, `ci-2x`, `ci-3x`.

## Cara kerja
GitHub Actions menjalankan generator Python saat file di `icons/` atau generator berubah. File hasil `caraka-icons.css` dan `icons.json` di-commit otomatis. GitHub Pages kemudian menerbitkan hasil tersebut.

## Catatan
- Jangan edit `caraka-icons.css` dan `icons.json` secara manual; file tersebut dibuat otomatis.
- GitHub Pages tidak menjalankan PHP; generator berjalan di GitHub Actions.
- Jika Actions gagal, buka log workflow dan periksa permissions, duplikasi nama class, atau file gambar yang tidak valid.
