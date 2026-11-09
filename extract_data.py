import openpyxl
import json
import re
from collections import defaultdict

wb = openpyxl.load_workbook("/tmp/rakitan_test.xlsx", data_only=True)
sheet = wb["RAKITAN"]

CATEGORY_MAP = {
    "PROCE": "Processor",
    "PROC": "Processor",
    "PROCESSOR": "Processor",
    "MOBO": "Motherboard",
    "MOTHERBOARD": "Motherboard",
    "MB": "Motherboard",
    "RAM": "RAM / Memory",
    "MEMORY": "RAM / Memory",
    "VGA": "VGA / Graphic Card",
    "GPU": "VGA / Graphic Card",
    "SSD": "Storage SSD",
    "HDD": "Storage HDD",
    "HARDDISK": "Storage HDD",
    "PSU": "Power Supply (PSU)",
    "CASE": "Casing PC",
    "CASING": "Casing PC",
    "COOLER": "CPU Cooler / Fan",
    "HSF": "CPU Cooler / Fan",
    "FAN": "CPU Cooler / Fan",
    "AIO": "Liquid Cooler AIO",
    "LED": "Monitor / Display",
    "MONITOR": "Monitor / Display",
    "KEY": "Keyboard & Mouse",
    "MOUSE": "Keyboard & Mouse",
    "KEY+MOUSE": "Keyboard & Mouse",
    "KEY-MOUSE": "Keyboard & Mouse",
    "JASA+INSTAL": "Jasa & Layanan",
    "INSTALASI": "Jasa & Layanan",
    "RAKIT + INSTALL": "Jasa & Layanan",
    "JASA": "Jasa & Layanan"
}

items_by_cat = defaultdict(lambda: defaultdict(list))
raw_items = []

rows = list(sheet.iter_rows(values_only=True))

for r in rows:
    # Check left side (cols 0 to 4)
    for c_start in [0, 6]:
        cat_raw = r[c_start]
        item_raw = r[c_start + 1]
        qtt_raw = r[c_start + 2]
        price_raw = r[c_start + 3]
        
        if item_raw and str(item_raw).strip() != "" and str(item_raw).strip().upper() != "ITEM":
            item_name = str(item_raw).strip()
            cat_str = str(cat_raw).strip().upper() if cat_raw else ""
            
            # Skip noise
            if item_name.startswith("=") or item_name.upper() in ["TOTAL", "SUBTOTAL", "DP", "LUNAS", "DISC"]:
                continue
                
            # Categorize
            mapped_cat = CATEGORY_MAP.get(cat_str)
            if not mapped_cat:
                u_name = item_name.upper()
                if "RYZEN" in u_name or "INTEL CORE" in u_name or "ATHLON" in u_name:
                    mapped_cat = "Processor"
                elif "B450" in u_name or "B550" in u_name or "B760" in u_name or "H610" in u_name or "X870" in u_name or "Z790" in u_name:
                    mapped_cat = "Motherboard"
                elif "RTX" in u_name or "GTX" in u_name or "RADEON" in u_name or "RX " in u_name or "ARC B" in u_name:
                    mapped_cat = "VGA / Graphic Card"
                elif "NVME" in u_name or "SSD" in u_name:
                    mapped_cat = "Storage SSD"
                elif "D4" in u_name or "D5" in u_name or "DDR4" in u_name or "DDR5" in u_name or "KIT D" in u_name:
                    mapped_cat = "RAM / Memory"
                elif "WATT" in u_name or "PSU" in u_name or "80+" in u_name or "550W" in u_name or "650W" in u_name:
                    mapped_cat = "Power Supply (PSU)"
                elif "MONITOR" in u_name or "LED" in u_name or "INCH" in u_name or "FHD" in u_name or "IPS" in u_name:
                    mapped_cat = "Monitor / Display"
                elif "JASA" in u_name or "INSTALL" in u_name or "RAKIT" in u_name:
                    mapped_cat = "Jasa & Layanan"
                else:
                    mapped_cat = "Aksesoris & Lainnya"
                    
            try:
                price = float(str(price_raw).replace(",", "").strip())
                if price <= 0:
                    continue
            except:
                continue
                
            items_by_cat[mapped_cat][item_name].append(price)

# Clean and dedup
catalog = []
item_id = 1

for cat_name, items_dict in items_by_cat.items():
    for item_name, prices in items_dict.items():
        # Clean up item name
        clean_name = re.sub(r'\s+', ' ', item_name).strip()
        if len(clean_name) < 3 or len(clean_name) > 120:
            continue
            
        # Get most common or latest price
        avg_price = sorted(prices)[len(prices)//2]
        
        catalog.append({
            "id": f"SC-{item_id:04d}",
            "name": clean_name,
            "category": cat_name,
            "price": int(avg_price),
            "occurrences": len(prices)
        })
        item_id += 1

# Sort catalog by occurrences descending per category
catalog.sort(key=lambda x: (x["category"], -x["occurrences"]))

print(f"Total Unique Catalog Items Extracted: {len(catalog)}")

# Curate top items per category
curated_catalog = []
for cat in set(x["category"] for x in catalog):
    cat_items = [x for x in catalog if x["category"] == cat]
    # keep top 60 items per category or all if less
    curated_catalog.extend(cat_items[:60])

print(f"Curated Catalog Items: {len(curated_catalog)}")

# Save catalog.json
with open("/home/bengkel/AI/starcomp-pc-configurator/data/catalog.json", "w") as f:
    json.dump(curated_catalog, f, indent=2)

print("Saved catalog.json successfully!")
