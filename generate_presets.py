import json

presets = [
    {
        "id": "preset-office-1",
        "name": "Paket Starcomp Office & Kasir Hemat",
        "target": "Administrasi Perkantoran, Kasir, Lab Sekolah, Browsing & Ketik",
        "badge": "Entry-Level / Office",
        "badgeColor": "emerald",
        "notes": "Paket hemat daya, performa kencang dengan APU Radeon Vega 8, SSD responsif, casing hemat tempat.",
        "items": [
            {"category": "Processor", "name": "AMD RYZEN 3 3200G (4 Core / 4 Thread up to 4.0GHz)", "qtt": 1, "price": 1150000},
            {"category": "Motherboard", "name": "ASROCK B450M HDV R4.0", "qtt": 1, "price": 890000},
            {"category": "RAM / Memory", "name": "KLEVV VALUE SERIES 8GB DDR4 3200MHz", "qtt": 1, "price": 320000},
            {"category": "Storage SSD", "name": "PNY CS900 256GB SATA III 2.5\"", "qtt": 1, "price": 325000},
            {"category": "Power Supply (PSU)", "name": "PCCOOLER KF450 450W", "qtt": 1, "price": 407000},
            {"category": "Casing PC", "name": "ENLIGHT EN-200 Slim Desktop + Stand", "qtt": 1, "price": 385000},
            {"category": "Monitor / Display", "name": "Lenovo L22e-40 Monitor 21.5\" FHD VA 75Hz", "qtt": 1, "price": 1070000},
            {"category": "Keyboard & Mouse", "name": "Logitech MK120 USB Keyboard & Mouse Combo", "qtt": 1, "price": 175000},
            {"category": "Jasa & Layanan", "name": "Jasa Perakitan, Cable Management & Instalasi Windows 11 + Office Standar", "qtt": 1, "price": 100000}
        ]
    },
    {
        "id": "preset-school-lab",
        "name": "Paket Lab Sekolah & Bisnis Intel Gen-12",
        "target": "Lab Komputer Sekolah / Kampus, BPR, Kantor Notaris, Kasir Supermarket",
        "badge": "School / Institutional",
        "badgeColor": "blue",
        "notes": "Durabilitas tinggi untuk pemakaian harian instansi, didukung processor Intel Core i3 12th Gen.",
        "items": [
            {"category": "Processor", "name": "Intel Core i3 12100 Box (4 Core / 8 Thread up to 4.3GHz)", "qtt": 1, "price": 1550000},
            {"category": "Motherboard", "name": "MSI PRO H610M-S D4", "qtt": 1, "price": 1100000},
            {"category": "RAM / Memory", "name": "HYNIX 8GB DDR4 3200MHz", "qtt": 1, "price": 350000},
            {"category": "Storage SSD", "name": "ADATA LEGEND 710 256GB M.2 NVMe PCIe Gen3x4", "qtt": 1, "price": 430000},
            {"category": "Power Supply (PSU)", "name": "PCCOOLER KF450 450W", "qtt": 1, "price": 410000},
            {"category": "Casing PC", "name": "FP MAX AirMesh G2 Black + Free 3 Fan", "qtt": 1, "price": 425000},
            {"category": "Monitor / Display", "name": "ViewSonic 22\" VA22E2-H Full HD", "qtt": 1, "price": 950000},
            {"category": "Keyboard & Mouse", "name": "Logitech MK120 USB Keyboard & Mouse Combo", "qtt": 1, "price": 175000},
            {"category": "Jasa & Layanan", "name": "Jasa Rakit Rapi, Optimalisasi BIOS & Instalasi Software Edukasi/Office", "qtt": 1, "price": 150000}
        ]
    },
    {
        "id": "preset-gaming-esport",
        "name": "Paket Starcomp Esport Gaming Champion (Ryzen 5 + RTX 3050)",
        "target": "Esport Gaming (Valorant, DOTA 2, CS2, GTA V, Roblox) & Editing Pelajar",
        "badge": "Popular Gaming",
        "badgeColor": "indigo",
        "notes": "Best-seller PC Gaming Starcomp. Stabil di 1080p Competitive High FPS, Ray Tracing & DLSS Ready.",
        "items": [
            {"category": "Processor", "name": "AMD RYZEN 5 5600 Box (6 Core / 12 Thread up to 4.4GHz)", "qtt": 1, "price": 1970000},
            {"category": "Motherboard", "name": "MSI B450M-A PRO MAX II", "qtt": 1, "price": 985000},
            {"category": "RAM / Memory", "name": "TEAM T-FORCE DELTA RGB 16GB Kit (2x8GB) DDR4 3600MHz Black", "qtt": 1, "price": 685000},
            {"category": "VGA / Graphic Card", "name": "MSI GeForce RTX 3050 VENTUS 2X 6G OC GDDR6", "qtt": 1, "price": 3150000},
            {"category": "Storage SSD", "name": "ADATA LEGEND 710 512GB M.2 NVMe PCIe", "qtt": 1, "price": 585000},
            {"category": "Power Supply (PSU)", "name": "MSI MAG A550BN 550W 80+ Bronze", "qtt": 1, "price": 715000},
            {"category": "Casing PC", "name": "VenomRX PRAVA Tempered Glass M-ATX Black + 3 Fan ARGB", "qtt": 1, "price": 420000},
            {"category": "CPU Cooler / Fan", "name": "Deepcool AG400 LED CPU Air Cooler", "qtt": 1, "price": 285000},
            {"category": "Jasa & Layanan", "name": "Jasa Perakitan Premium, Stress Test, Cable Management & Instalasi Windows 11 + Steam/Valorant", "qtt": 1, "price": 150000}
        ]
    },
    {
        "id": "preset-gaming-content",
        "name": "Paket Gaming AAA & Content Creator Pro (Core i5 + RTX 4060)",
        "target": "Gaming AAA (Black Myth: Wukong, Cyberpunk), Adobe Premiere, After Effects, AutoCAD",
        "badge": "Mid-High Pro",
        "badgeColor": "purple",
        "notes": "Performa kencang 1080p Ultra / 1440p dengan NVIDIA Ada Lovelace RTX 4060 & DLSS 3 Frame Generation.",
        "items": [
            {"category": "Processor", "name": "Intel Core i5 12400F Box (6 Core / 12 Thread up to 4.4GHz)", "qtt": 1, "price": 1820000},
            {"category": "Motherboard", "name": "ASROCK B760M HDV/M2 D4", "qtt": 1, "price": 1495000},
            {"category": "RAM / Memory", "name": "ADATA XPG SPECTRIX D50 32GB Kit (2x16GB) DDR4 3200MHz RGB", "qtt": 1, "price": 1150000},
            {"category": "VGA / Graphic Card", "name": "ZOTAC GAMING GeForce RTX 4060 Twin Edge OC 8GB GDDR6", "qtt": 1, "price": 5250000},
            {"category": "Storage SSD", "name": "ADATA XPG GAMMIX S70 BLADE 1TB M.2 NVMe PCIe Gen4x4 (7400MB/s)", "qtt": 1, "price": 1350000},
            {"category": "Power Supply (PSU)", "name": "MSI MAG A650BN 650W 80+ Bronze", "qtt": 1, "price": 875000},
            {"category": "Casing PC", "name": "DarkFlash DS900 Airflow Panoramic Tempered Glass Black", "qtt": 1, "price": 750000},
            {"category": "Liquid Cooler AIO", "name": "Deepcool LS520 SE 240mm ARGB Liquid Cooler", "qtt": 1, "price": 1190000},
            {"category": "Jasa & Layanan", "name": "Jasa Rakit Pro, BIOS Tuning, GPU Benchmark & OS Windows 11 Pro + Adobe Family Ready", "qtt": 1, "price": 200000}
        ]
    },
    {
        "id": "preset-workstation-cad",
        "name": "Paket Workstation Arsitektur, CAD & 3D Render (i9-14900KF + RTX A4000)",
        "target": "Konsultan Arsitek, Rendering Lumion, Blender, SolidWorks, 3ds Max, Video Studio",
        "badge": "Studio Workstation",
        "badgeColor": "amber",
        "notes": "Ditenagai GPU Quadro Workstation & Processor 24 Core untuk stabilitas komputasi berat 24/7.",
        "items": [
            {"category": "Processor", "name": "Intel Core i9-14900KF Box (24 Core / 32 Thread up to 6.0GHz)", "qtt": 1, "price": 9450000},
            {"category": "Motherboard", "name": "MSI MAG Z790 TOMAHAWK WIFI DDR5", "qtt": 1, "price": 5440000},
            {"category": "RAM / Memory", "name": "G.SKILL Trident Z5 RGB 64GB Kit (2x32GB) DDR5 6000MHz", "qtt": 1, "price": 3850000},
            {"category": "VGA / Graphic Card", "name": "Leadtek NVIDIA Quadro RTX A4000 16GB GDDR6 ECC", "qtt": 1, "price": 22000000},
            {"category": "Storage SSD", "name": "SAMSUNG 990 PRO 2TB M.2 NVMe PCIe 4.0", "qtt": 1, "price": 3619000},
            {"category": "Power Supply (PSU)", "name": "MSI MAG A850GL PCIE5 850W 80+ Gold Full Modular", "qtt": 1, "price": 1780000},
            {"category": "Casing PC", "name": "PCCOOLER C3 D510 ATX High Airflow Gaming Case", "qtt": 1, "price": 695000},
            {"category": "Liquid Cooler AIO", "name": "DeepCool MYSTIQUE 360 LCD ARGB 360mm AIO Cooler", "qtt": 1, "price": 2400000},
            {"category": "Jasa & Layanan", "name": "Jasa Rakit Workstation, Thermal Grizzly Kryonaut, Burning Test & Windows 11 Pro Workstation", "qtt": 1, "price": 250000}
        ]
    },
    {
        "id": "preset-flagship-rog",
        "name": "Paket Starcomp God-Tier ROG Enthusiast (Ryzen 9 9950X3D + RTX 5090 32GB)",
        "target": "Extreme Gaming 4K/8K, Local AI Machine Learning LLM, Unreal Engine 5 Dev",
        "badge": "Extreme God-Tier",
        "badgeColor": "rose",
        "notes": "Spesifikasi puncak industri komputer tahun 2026. Komponen serba ASUS ROG edisi terbatas.",
        "items": [
            {"category": "Processor", "name": "AMD CPU Ryzen 9 9950X3D (16 Core / 32 Thread Zen 5 3D V-Cache)", "qtt": 1, "price": 13765000},
            {"category": "Motherboard", "name": "ASUS ROG CROSSHAIR X870E HERO WiFi", "qtt": 1, "price": 13075000},
            {"category": "RAM / Memory", "name": "Kingston Fury Beast 64GB Kit (2x32GB) DDR5 6000MHz RGB", "qtt": 1, "price": 7850000},
            {"category": "VGA / Graphic Card", "name": "ASUS ROG Astral GeForce RTX 5090 32GB GDDR7 OC Edition", "qtt": 1, "price": 73235000},
            {"category": "Storage SSD", "name": "Samsung 990 EVO PLUS 2TB M.2 NVMe Gen5/Gen4", "qtt": 1, "price": 4750000},
            {"category": "Power Supply (PSU)", "name": "ASUS ROG Thor 1200W Platinum II OLED Display", "qtt": 1, "price": 7580000},
            {"category": "Casing PC", "name": "ASUS ROG Hyperion GR701 E-ATX Full Tower Case", "qtt": 1, "price": 7330000},
            {"category": "Liquid Cooler AIO", "name": "ASUS ROG RYUO IV SLC 360 ARGB Liquid Cooler", "qtt": 1, "price": 4860000},
            {"category": "Jasa & Layanan", "name": "VIP Custom Rig Assembly, Precision Tuning, Stress Testing & Setup Windows 11 Pro", "qtt": 1, "price": 350000}
        ]
    }
]

with open("/home/bengkel/AI/starcomp-pc-configurator/data/presets.json", "w") as f:
    json.dump(presets, f, indent=2)

print(f"Generated {len(presets)} presets successfully!")
