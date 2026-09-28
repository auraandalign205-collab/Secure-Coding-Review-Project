import os

# VULNERABILITY 1: Hardcoded sensitive credentials (API key leaked in source code)
API_SECRET_KEY = "XYZ123_SUPER_SECRET_TOKEN_LEAKED"

def process_user_input():
    print("=== Secure Coding Audit Target System ===")
    user_data = input("Enter a mathematical command to execute: ")
    
    # VULNERABILITY 2: Using the dangerous 'eval()' function which allows Remote Code Execution (RCE)
    # Attackers can inject system destruction commands here.
    result = eval(user_data)
    print(f"Result: {result}")

if __name__ == "__main__":
    process_user_input()
