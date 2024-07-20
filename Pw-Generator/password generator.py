while True:
    import random

    print("=" * 30)
    print("PASSWORD GENERATOR!!")
    print("=" * 30)

    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercases_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "!@#$%^&*9()+=-_[]]}{<>,./?"
    
    print("=" * 30)
    print("Select password options:")
    upper = input("Tambahkan Huruf Besar? (yes/no): ").strip().lower() == "yes"
    lower = input("Tambahkan Huruf Kecil? (yes/no): ").strip().lower() == "yes"
    nums = input("Tambahkan Nomor? (yes/no): ").strip().lower() == "yes"
    syms = input("Tambahkan Symbols? (yes/no): ").strip().lower() == "yes"
    print("=" * 30)
    

    all_chars = ""
    if upper:
        all_chars += uppercase_letters
    if lower:
        all_chars += lowercases_letters
    if nums:
        all_chars += digits
    if syms:
        all_chars += symbols
    print("=" * 30)
    length = int(input("Masukkan Panjang Sandi Nya(1 - 49): "))
    amount = int(input("Berapa Sandi Yang Kamu Mau: "))
    print("=" * 30)
    seed = "Hideri"
    random.seed(seed)

    for x in range(amount):
        password = "".join(random.sample(all_chars, length))
        print(password)
    
    print("=" * 30)
    back =input("Ingin Membuat Lagi (yes/no) :").strip().lower()
    if back != 'yes':
        print ("TERIMA KASIH :3")
        break