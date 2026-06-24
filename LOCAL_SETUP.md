# Local Development Setup

This guide explains how to run the Snowflake notebooks locally in Cursor/VS Code while keeping them fully compatible with Snowflake Notebooks UI.

## Quick Start

### 1. Install Dependencies

```bash
pip install snowflake-snowpark-python snowflake-ml-python cryptography pandas numpy matplotlib
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

### 2. Configure Credentials

#### Option A: Using config.json (Recommended)

1. Copy the template:
   ```bash
   cp config.json.template config.json
   ```

2. Edit `config.json` with your credentials:
   ```json
   {
     "account": "your_account.region",
     "user": "your_username",
     "password": "your_password",
     "role": "FINSERV_DEMO_ADMIN",
     "warehouse": "FINSERV_DEMO_WH",
     "database": "FINSERV_FRAUD_DEMO",
     "schema": "FINSERV_MODEL_REGISTRY"

#### Option B: Using Environment Variables

Set these environment variables:
```bash
export SNOWFLAKE_ACCOUNT="your_account.region"
export SNOWFLAKE_USER="your_username"
export SNOWFLAKE_PASSWORD="your_password"
export SNOWFLAKE_ROLE="FINSERV_DEMO_ADMIN"
export SNOWFLAKE_WAREHOUSE="FINSERV_DEMO_WH"
export SNOWFLAKE_DATABASE="FINSERV_FRAUD_DEMO"
export SNOWFLAKE_SCHEMA="FINSERV_MODEL_REGISTRY"
```

#### Option C: Using Key Pair Authentication

1. Generate a key pair (if you don't have one):
   ```bash
   openssl genrsa 2048 | openssl pkcs8 -topk8 -inform PEM -out snowflake_key.p8 -nocrypt
   openssl rsa -in snowflake_key.p8 -pubout -out snowflake_key.pub
   ```

2. Add public key to Snowflake:
   ```sql
   ALTER USER your_username SET RSA_PUBLIC_KEY='YOUR_PUBLIC_KEY_CONTENT';
   ```

3. Update `config.json`:
   ```json
   {
     "account": "your_account.region",
     "user": "your_username",
     "private_key_path": "/path/to/snowflake_key.p8",
     "role": "FINSERV_DEMO_ADMIN",
     "warehouse": "FINSERV_DEMO_WH",
     "database": "FINSERV_FRAUD_DEMO",
     "schema": "FINSERV_MODEL_REGISTRY"

Modify the connection cell in each notebook to support both environments:

**Before (Snowflake-only):**
```python
from snowflake.snowpark.context import get_active_session
session = get_active_session()
```

**After (Dual compatibility):**
```python
# Works in both Snowflake Notebooks and locally in Cursor
try:
    from snowflake.snowpark.context import get_active_session
    session = get_active_session()
    print("✅ Running in Snowflake Notebooks")
except:
    from snowflake_connection import get_local_session
    session = get_local_session()
    print("✅ Running locally in Cursor")
```

### 4. Run Notebooks

- **In Cursor/VS Code**: Just run the cells normally with the Jupyter extension
- **In Snowflake UI**: Upload and run as normal - the `try/except` will use `get_active_session()`

## File Structure

```
finserv_ml_demo/
├── snowflake_connection.py    # Local connection helper
├── config.json.template        # Template for credentials
├── config.json                 # Your credentials (gitignored!)
├── .gitignore                  # Prevents committing secrets
├── LOCAL_SETUP.md             # This file
├── requirements.txt            # Python dependencies
├── 01_env_setup.sql           # Run this in Snowflake first
├── 02_generate_and_load_data.ipynb
├── 03_finserv_ml_demo.ipynb
├── 04_model_monitoring.ipynb
└── 05_clean_up.ipynb
```

## How It Works

1. **Snowflake Notebooks UI**: 
   - Uses `get_active_session()` (built-in)
   - No credentials needed (you're already logged in)

2. **Local (Cursor/VS Code)**:
   - Uses `get_local_session()` from `snowflake_connection.py`
   - Reads credentials from `config.json` or environment variables
   - Creates a session programmatically

3. **Dual Compatibility**:
   - The `try/except` block tries Snowflake Notebooks first
   - Falls back to local connection if that fails
   - Same notebook works in both environments!

## Security Best Practices

✅ **DO:**
- Use `config.json` for local credentials
- Use key pair authentication when possible
- Keep `.gitignore` updated

❌ **DON'T:**
- Commit `config.json` to git
- Hard-code credentials in notebooks
- Share private keys

## Troubleshooting

### "Missing required Snowflake credentials"
- Check that `config.json` exists and has valid values
- Or set environment variables

### "get_active_session() not available"
- This is expected locally - the except block will handle it
- Make sure `snowflake_connection.py` is in the same directory

### "Authentication failed"
- Verify your account identifier format: `account.region` (e.g., `xy12345.us-east-1`)
- Check username and password are correct
- For key pair: ensure public key is set in Snowflake

### Notebooks still don't work locally
- Make sure you installed all dependencies: `pip install -r requirements.txt`
- Check that Jupyter extension is installed in Cursor
- Verify Python kernel is selected

## Benefits of This Approach

✨ **Single Source of Truth**: Same notebooks work everywhere
🔒 **Secure**: Credentials never in version control
🚀 **Flexible**: Use password or key pair auth
🎯 **No Conflicts**: Snowflake UI users don't need local setup
💻 **Local Development**: Full IDE features in Cursor

## Next Steps

Once set up, you can:
1. Run notebooks locally for faster iteration
2. Use Cursor's AI features while developing
3. Upload to Snowflake for production/demos
4. Switch between environments seamlessly

