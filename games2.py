import random

def main():
#mula permainan batu kertas gunting
#papar pilihan sama ada batu, kertas atau gunting
    print(".")
    print("PERMAINAN BATU KERTAS GUNTING")
    print("**************************************************")
    print("Pilih satu antara 3. BATU ATAU KERTAS ATAU GUNTING")
    print("**************************************************")
    
#set kan nilai untuk pilihan secara random
    pilihan = [ "BATU", "KERTAS", "GUNTING" ]
    
#sistem buat pilihan secara random
    x =random.choice(pilihan)
#print(x)
#arahan untuk pengguna input pilihan
    guess = str(input("MASUKKAN PILIHAN ANDA : "))
    print()
    
#jika pilihan pengguna dan sistem sama
    if guess == x:
        print(f"PILIHAN YANG SAMA")
    
#jika pilihan pengguna dan sistem berlainan

    elif guess == "BATU" and  x == "GUNTING" :
        print("KEPUTUSAN: ")
        print("BATU VS GUNTING. ANDA KALAH")
            
    elif guess == "BATU" and x == "KERTAS" :
        print("KEPUTUSAN: ")
        print("BATU VS KERTAS. ANDA MENANG")
            
    elif guess == "GUNTING" and x == "BATU" :
        print("KEPUTUSAN: ")
        print("GUNTING VS BATU. ANDA MENANG")
            
    elif guess == "GUNTING" and x == "KERTAS" :
        print("KEPUTUSAN: ")
        print("GUNTING VS KERTAS. ANDA KALAH")
            
    elif guess == "KERTAS" and x == "BATU" :
        print("KEPUTUSAN: ")
        print("KERTAS VS BATU. ANDA MENANG")
            
    elif guess == "KERTAS" and x == "GUNTING" :
        print("KEPUTUSAN: ")
        print("KERTAS VS GUNTING. ANDA KALAH")

#jika pengguna input pilihan yang salah 
    else:
        print("Masukkan pilihan yang betul berdasarkan arahan")
            
                
main()