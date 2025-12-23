# Rainbow Table Attack Demonstration

## Project Overview
This educational project demonstrates how rainbow table attacks work and how password salting provides effective defense against them. The demonstration shows both the vulnerability of unsalted password hashes and the protection offered by proper salting techniques.

## Team Members
- Engy Ashraf Samy (20236017)
- Hana Ayman Mohamed (20236116)
- Jana Tamer Mohamed (20236026)
- Rawan Hassan Mohamed (20236038)
- Logyn Hossam Eldeen (20236075)

## Demo Code
The main demonstration is in `RainbowTable_demo.py`. This Python script shows:
1. Creation of a rainbow table with common passwords
2. Simulation of a password cracking attack on unsalted hashes
3. Implementation of password salting as a defense
4. Demonstration of stronger hash functions

## How to Run the Demo
1. Ensure you have Python installed on your system
2. Download or clone this repository
3. Run the demo script:

## Expected Output
When you run the demo, you should see output similar to:
Creating Rainbow Table :
123456 -> e10adc3949ba59abbe56e057f20f883e
password -> 5f4dcc3b5aa765d61d8327deb882cf99
admin -> 21232f297a57a5a743894a0e4a801fc3
letmein -> 0d107d09f5bbe40cade3de5c71e9e9b7
qwerty -> d8578edf8458ce06fbc5bb76a58c5ca4
1234 -> 81dc9bdb52d04dc20036dbd8313ed055

Rainbow Table Size: 6 entries

 Simulating Stolen Hash (No Salt)=
Victim Password: admin
Stolen Hash (MD5): 21232f297a57a5a743894a0e4a801fc3

Attempting Crack (Rainbow Table Lookup) =
[SUCCESS] Password cracked: admin

 Adding Salt to Hashing =
Salt: S@1t#
Salted Input: S@1t#admin
Salted Hash: 43e272ac58f451c3f7103416db9afdde

 Trying to Crack Salted Hash :
[FAILED] Salted hash not found in rainbow table

Using SHA-256 with Salt =
Salted SHA-256 Hash: e3ab270a3798200ac464113b8c76880beec3139898349e98f2a64b3a4e7ac992



## Key Security Concepts Demonstrated

### 1. Rainbow Table Attack
- A rainbow table is a precomputed database of passwords and their hashes
- Attackers can quickly look up stolen hashes to recover passwords
- Effective against unsalted password databases

### 2. Password Salting Defense
- Salting involves adding random data to passwords before hashing
- Each user gets a unique salt, making each hash different
- Prevents rainbow table attacks because precomputed tables become useless

### 3. Hash Function Security
- MD5 is shown for demonstration but is cryptographically broken
- SHA-256 is more secure but still fast
- For production systems, slower hashing algorithms like bcrypt or Argon2 are recommended

## Learning Objectives
1. Understand how rainbow table attacks work
2. Learn why password salting is essential for security
3. Recognize the limitations of fast hash functions like MD5
4. Understand the importance of using modern, slow hash functions for password storage

## Files Included
- `RainbowTable_demo.py` - Main demonstration script
- `presentation.pdf` - Educational presentation slides
- `README.md` - This documentation file

## Ethical Considerations
This demonstration is for educational purposes only. Understanding how attacks work helps security professionals build better defenses. Never attempt to access systems or data without proper authorization.

## License
This project is for educational use. All materials are provided for learning purposes.