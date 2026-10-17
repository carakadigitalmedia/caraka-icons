# Caraka Icons

Library ikon ringan berbasis **WebP + CSS**, siap di-host gratis menggunakan GitHub Pages.

## Isi paket

- `index.html` — katalog ikon dengan pencarian dan tombol salin class.
- `caraka-icons.css` — stylesheet library.
- `icons/tkk-berkemah.webp` — ikon pertama dari gambar yang diberikan.
- `examples/codeigniter3/` — contoh integrasi CodeIgniter 3.

## Deploy ke GitHub Pages

1. Buat repository baru bernama `caraka-icons` di https://github.com/new.
2. Pilih **Public** agar bisa dipakai melalui GitHub Pages gratis.
3. Unggah semua isi folder paket ini ke root repository, bukan folder `caraka-icons` di dalam repository.
4. Klik **Settings → Pages**.
5. Pada **Build and deployment**, pilih **Deploy from a branch**.
6. Pilih branch `main` dan folder `/(root)`, lalu klik **Save**.
7. Tunggu deployment selesai. URL umumnya:
   `https://USERNAME.github.io/caraka-icons/`
8. Uji halaman katalog dan stylesheet:
   `https://USERNAME.github.io/caraka-icons/caraka-icons.css`

Ganti `USERNAME` dengan username GitHub Anda. URL di atas merupakan pola alamat, bukan situs yang sudah diterbitkan.

## Pemakaian di HTML

```html
<link rel="stylesheet" href="https://USERNAME.github.io/caraka-icons/caraka-icons.css">

<i class="ci ci-tkk-berkemah" aria-label="TKK Berkemah"></i>
<i class="ci ci-tkk-berkemah ci-2x" aria-label="TKK Berkemah"></i>
```

Ikon mengikuti ukuran font elemen induk. Helper ukuran tersedia: `ci-xs`, `ci-sm`, `ci-lg`, `ci-xl`, `ci-2x`, `ci-3x`.

## Integrasi CodeIgniter 3

Contoh lengkap ada di `examples/codeigniter3/README.md`.

## Menambahkan ikon baru

1. Simpan aset WebP di folder `icons/`, gunakan nama file sederhana, huruf kecil, dan tanda hubung. Contoh: `tkk-memasak.webp`.
2. Tambahkan class CSS:

```css
.ci-tkk-memasak {
  background-image: url("./icons/tkk-memasak.webp");
}
```

3. Tambahkan kartu ikon baru ke `index.html`. Salin struktur kartu TKK Berkemah, lalu ubah nama, deskripsi, `data-search`, class ikon, dan nilai `data-copy`.
4. Commit perubahan ke repository. GitHub Pages akan menerbitkan versi terbaru.

## Catatan teknis

- Aset WebP tetap berupa gambar raster; warna di dalam gambar tidak dapat diubah dengan `color` CSS.
- Tidak ada JavaScript yang diperlukan untuk menampilkan ikon. JavaScript hanya dipakai pada katalog untuk pencarian dan menyalin class.
- Untuk aksesibilitas, ikon dekoratif sebaiknya diberi `aria-hidden="true"`; ikon bermakna dapat memakai `role="img"` dan label yang sesuai.
- Gunakan hanya gambar yang Anda miliki atau berhak gunakan.
