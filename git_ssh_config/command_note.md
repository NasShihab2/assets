# -------------------------
# 1️⃣ Generate SSH key for FIRST GitHub account
# -------------------------
# Replace your_email@example.com with first account email
ssh-keygen -t ed25519 -C "your_email@example.com" -f C:\Users\Admin\.ssh\id_ed25519
# Press Enter for file location if default, optional passphrase

# -------------------------
# 2️⃣ Add first public key to GitHub
# -------------------------
notepad C:\Users\Admin\.ssh\id_ed25519.pub
# Copy the entire line (ssh-ed25519 ... email) to GitHub → Settings → SSH and GPG keys → New SSH key → Add key

# -------------------------
# 3️⃣ Generate SSH key for SECOND GitHub account
# -------------------------
# Replace second_email@example.com with second account email
ssh-keygen -t ed25519 -C "second_email@example.com" -f C:\Users\Admin\.ssh\id_ed25519_second
# Press Enter for file location if default, optional passphrase

# -------------------------
# 4️⃣ Add second public key to SECOND GitHub account
# -------------------------
notepad C:\Users\Admin\.ssh\id_ed25519_second.pub
# Copy the entire line and paste it into second GitHub account → Settings → SSH and GPG keys → New SSH key → Add key

# -------------------------
# 5️⃣ Configure SSH for multiple accounts
# -------------------------
notepad C:\Users\Admin\.ssh\config

# Add the following:

# First GitHub account
Host github.com-first
    HostName github.com
    User git
    IdentityFile C:\Users\Admin\.ssh\id_ed25519

# Second GitHub account
Host github.com-second
    HostName github.com
    User git
    IdentityFile C:\Users\Admin\.ssh\id_ed25519_second

# -------------------------
# 6️⃣ Test connections
# -------------------------
ssh -T git@github.com-first
ssh -T git@github.com-second

# Expected: "Hi username! You've successfully authenticated..."

# -------------------------
# 7️⃣ Clone repo for FIRST account
# -------------------------
git clone git@github.com-first:username/repo.git

# -------------------------
# 8️⃣ Clone repo for SECOND account
# -------------------------
git clone git@github.com-second:username/repo.git

# -------------------------
# 9️⃣ Switch an existing repo to the correct account
# -------------------------
cd path\to\repo
git remote -v
git remote set-url origin git@github.com-first:username/repo.git
# or for second account
git remote set-url origin git@github.com-second:username/repo.git

# -------------------------
# 🔟 Push / Pull from GUI or terminal
# -------------------------
git push
git pull

# -------------------------
# 1️⃣1️⃣ Optional: Force all future HTTPS clones to SSH automatically
# -------------------------
git config --global url."git@github.com:".insteadOf "https://github.com/"
