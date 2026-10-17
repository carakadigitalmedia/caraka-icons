# Integrasi Caraka Icons ke CodeIgniter 3

## Opsi A — pakai CDN GitHub Pages

Edit template utama, misalnya `application/views/templates/header.php`, dan tambahkan di bagian `<head>`:

```php
<link rel="stylesheet"
      href="https://USERNAME.github.io/caraka-icons/caraka-icons.css">
```

Ganti `USERNAME` dengan username GitHub Anda. Setelah itu, gunakan di view mana pun:

```html
<i class="ci ci-tkk-berkemah" aria-label="TKK Berkemah"></i>
<i class="ci ci-tkk-berkemah ci-lg" aria-label="TKK Berkemah"></i>
```

Contoh di tombol Bootstrap:

```html
<a href="#" class="btn btn-success">
  <i class="ci ci-tkk-berkemah" aria-hidden="true"></i>
  TKK Berkemah
</a>
```

## Opsi B — host lokal di aplikasi CI3

Salin `caraka-icons.css` dan folder `icons` ke:

```text
assets/caraka-icons/
├── caraka-icons.css
└── icons/
    └── tkk-berkemah.webp
```

Tambahkan di template:

```php
<link rel="stylesheet"
      href="<?= base_url('assets/caraka-icons/caraka-icons.css'); ?>">
```

Pastikan struktur relatif CSS tidak berubah: `icons/tkk-berkemah.webp` harus berada di dalam folder yang sama dengan CSS, di subfolder `icons`.

## Menggunakan ukuran berbeda

```html
<i class="ci ci-tkk-berkemah ci-sm"></i>
<i class="ci ci-tkk-berkemah"></i>
<i class="ci ci-tkk-berkemah ci-xl"></i>
<i class="ci ci-tkk-berkemah ci-3x"></i>
```

Ukuran mengikuti ukuran font CSS. Untuk ukuran khusus:

```html
<i class="ci ci-tkk-berkemah" style="font-size:42px"
   aria-label="TKK Berkemah"></i>
```
