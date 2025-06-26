Project Name: BTC Wallet Generator

Description:
This is a Python-based application to generate a Bitcoin (BTC) wallet locally. The wallet is stored securely on the local machine and can be used as a cold wallet.

Features:
- Create a new wallet with a custom name
- Generate a mnemonic phrase for backup and recovery
- Utilizes the `bitcoinlib` Python library
- Stores wallet data locally

File Structure:
- index.py          -> Main script to run the application
- requirements.txt  -> List of dependencies required
- venv/             -> (Excluded from Git) Local virtual environment

How to Run:
1. Clone the repository:
   git clone <REPO_URL>

2. Navigate into the project folder:
   cd project-folder-name

3. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate       # Linux/macOS
   venv\Scripts\activate          # Windows

4. Install the required packages:
   pip install -r requirements.txt

5. Run the application:
   python index.py

6. Enter a wallet name when prompted.

How to Exit the Virtual Environment:
- Type `deactivate` in the terminal.

Security Note:
- NEVER share your mnemonic phrase with anyone.
- Store the mnemonic securely in an offline location.
- This wallet is for educational/demo purposes. Do not use it to store large amounts of BTC without proper security audits.

Created by: Muhammad Rizki
