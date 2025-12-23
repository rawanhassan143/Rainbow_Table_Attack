import hashlib

#  Create a Simple Rainbow Table
print(" Creating Rainbow Table :")
common_passwords = ["123456", "password", "admin", "letmein", "qwerty", "1234"]
rainbow_table = {}

for pwd in common_passwords:
    hash_md5 = hashlib.md5(pwd.encode()).hexdigest()
    rainbow_table[hash_md5] = pwd
    print(f"{pwd} -> {hash_md5}")

print(f"\nRainbow Table Size: {len(rainbow_table)} entries")

# Simulate Stolen Hash (No Salt)
print("\n Simulating Stolen Hash (No Salt)=")
victim_password = "admin"
victim_hash = hashlib.md5(victim_password.encode()).hexdigest()
print(f"Victim Password: {victim_password}")
print(f"Stolen Hash (MD5): {victim_hash}")

#  Crack Password
print("\nAttempting Crack (Rainbow Table Lookup) =")
if victim_hash in rainbow_table:
    print(f"[SUCCESS] Password cracked: {rainbow_table[victim_hash]}")
else:
    print("[FAILED] Password not in rainbow table")

#  with Salt
print("\n Adding Salt to Hashing =")
salt = "S@1t#"
salted_password = salt + victim_password
salted_hash = hashlib.md5(salted_password.encode()).hexdigest()
print(f"Salt: {salt}")
print(f"Salted Input: {salted_password}")
print(f"Salted Hash: {salted_hash}")

# Attempt Crack with Salt
print("\n Trying to Crack Salted Hash :")
if salted_hash in rainbow_table:
    print(f"[SUCCESS] Cracked: {rainbow_table[salted_hash]}")
else:
    print("[FAILED] Salted hash not found in rainbow table")

#  Defense: Using a Stronger Hash
print("\nUsing SHA-256 with Salt =")
hash_sha256 = hashlib.sha256(salted_password.encode()).hexdigest()
print(f"Salted SHA-256 Hash: {hash_sha256}")
print("(Even slower hashing like bcrypt is recommended in production)")