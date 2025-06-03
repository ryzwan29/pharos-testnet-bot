# 🚀 PHAROS-AUTO | Bot Airdrop Testnet by AirDropFamilyIDN
![image](https://github.com/user-attachments/assets/6e11bb69-7224-4e36-ba2c-9cd347fe3586)



Bot otomatis untuk menyelesaikan semua task Pharos Testnet — termasuk check-in, faucet, swap token, transfer antar wallet, hingga staking. Semua dilakukan langsung via transaksi di blockchain  TX

---

## 🔧 FITUR UTAMA

| Fitur              | Keterangan                                                             |
|--------------------|------------------------------------------------------------------------|
| 🔐 Login Otomatis   | Login via tanda tangan wallet (tanpa email/password)                  |
| 📅 Auto Check-in    | Check-in harian otomatis                                               |
| 💧 Auto Faucet      | Klaim token faucet testnet otomatis setiap wallet                      |
| 🔄 Auto Swap        | Swap token menggunakan smart contract (real transaction)              |
| 💸 Auto Transfer    | Kirim token ke wallet random                                           |
| 🪙 Auto Staking     | Stake token otomatis ke smart contract staking                         |
| 📊 Laporan Akun     | Menampilkan poin dan status wallet                                     |
| 💡 Multi Wallet     | Bisa jalankan banyak wallet sekaligus                                  |
| 🔗 TX Explorer Link | Tampilkan link TX langsung ke explorer (https://testnet.pharosscan.xyz) |

---

## 📂 STRUKTUR FILE

| File              | Deskripsi                                                               |
|-------------------|-------------------------------------------------------------------------|
| `bot.py`          | File utama bot, sudah all-in-one                                        |
| `.env`            | Konfigurasi setting (fitur aktif, jumlah TX, delay, dll)               |
| `privateKeys.txt` | List private key (1 wallet per baris)                                   |
| `abi.txt`         | ABI smart contract (token, router, staking)                             |

---

## 🛠️ INSTALL DENGAN SCRIPT
```
source <(curl -s https://raw.githubusercontent.com/ryzwan29/pharos-testnet-bot/main/quick-installation.sh)
```
Ganti `privateKeys.txt` dengan privatekey wallet masing-masing (Support multi wallet)

1. Untuk menjalankan bot TF, Swap, Add LP
```
python3 bot.py
```
2. Untuk menjalankan bot auto mint NFT
```
python3 MintNFT.py
```
# 🚀 PHAROS AUTO - Auto Mint NFT (Testnet) via Termux

Script Python untuk **otomatis mint NFT** di Pharos Testnet menggunakan **multi wallet** + **proxy support**.  
✅ Aman, tidak double mint  
✅ Cek saldo otomatis  
✅ Link explorer disediakan  
✅ Cocok untuk dijalankan di Termux (Android)

---

## 🛠️ Fitur

- 🚀 Auto Mint NFT di jaringan Pharos Testnet
- 🔁 Multi wallet + proxy rotasi otomatis
- 💰 Deteksi saldo sebelum kirim tx
- 💾 Simpan riwayat mint di `datanft.txt`
- 🔗 Link transaksi langsung ke PharosScan

---

## 📦 Modul Python yang Dibutuhkan

```bash
pip install web3 eth-account eth-utils requests

🧠 CATATAN
Semua transaksi menggunakan testnet, aman & tanpa biaya

Transaksi dilakukan langsung ke smart contract menggunakan Web3 

Script ini 100% open-source, dikembangkan bersama komunitas

👥 KOMUNITAS
💬 Diskusi, update, dan bantuan:
👉 Telegram: @AirDropFamilyIDN

