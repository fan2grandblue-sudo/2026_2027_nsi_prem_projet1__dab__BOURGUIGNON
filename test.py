import time
import sys

print("Connexion en cours...")

for i in range(101):
    bar = "█" * (i // 5) + "░" * (20 - i // 5)
    sys.stdout.write(f"\r[{bar}] {i}%")
    sys.stdout.flush()
    time.sleep(0.03)

print("\n\n[✓] Login successful!")