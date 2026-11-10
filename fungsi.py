# =================================================
# 1. DESAIN PROGRAM: FUNGSI MODULAR
# =================================================

def ganjil_genap(n):
    return "Genap" if n % 2 == 0 else "Ganjil"

def prima(n):
    if n < 2: 
        return False
    i = 2
    while i * i <= n:
        if n % i == 0: 
            return False
        i += 1
    return True

def fpb(a, b):
    while b != 0: 
        a, b = b, a % b
    return a

def kpk(a, b):
    return abs(a * b) // fpb(a, b)

def desimal_ke_hex(n):
    if n == 0:
        return "0"
    digit = "0123456789ABCDEF"
    hasil = ""
    temp = n
    while temp > 0:
        hasil = digit[temp % 16] + hasil
        temp //= 16
    return hasil

# --- PROGRAM UTAMA ---
data = [3, 11, 12, 17, 24, 36, 101]

for n in data:
    print(f"\nBilangan : {n}")
    print(f"Status   : {ganjil_genap(n)}")
    print(f"Prima    : {'Ya' if prima(n) else 'Tidak'}")
    print(f"Hex      : {desimal_ke_hex(n)}")
  
# ===================================================
# 2. STRUKTUR PTOGRAM UTAMA
# ===================================================

data = [260306014, 3, 11, 2026, 9, 12, 2006]

print("=" * 50)
print("ANALISIS BILANGAN")
print("=" * 50)

for n in data:
    print(f"\nBilangan : {n}")
    print(f"Status   : {ganjil_genap(n)}")
    print(f"Prima    : {'Ya' if prima(n) else 'Tidak'}")
    print(f"Hex      : {desimal_ke_hex(n)}")

# FPB dan KPK keseluruhan
hasil_fpb = data[0]
hasil_kpk = data[0]

for x in data[1:]:
    hasil_fpb = fpb(hasil_fpb, x)
    hasil_kpk = kpk(hasil_kpk, x)

print(f"\nFPB semua bilangan : {hasil_fpb}")
print(f"KPK semua bilangan : {hasil_kpk}")
