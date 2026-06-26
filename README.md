# Finserv Fraud Demo - Payment Fraud Detection

**End-to-End Machine Learning Platform Demo**

This project demonstrates a complete ML workflow for payment transaction fraud detection using Snowflake's ML platform. The demo is designed for finserv prospects and showcases Snowflake as a unified ML platform - no separate infrastructure needed.

## Use Case

**Payment / Transaction Fraud Detection**

Detect fraudulent payment transactions before settlement by identifying:
- Unusual transaction amounts relative to a customer's spending baseline
- High transaction-to-average ratio (a strong fraud signal)
- Cross-border transactions inconsistent with normal behavior

The key finserv tension this demo addresses: **false negatives** (missed fraud = direct loss) vs **false positives** (blocked legitimate transactions = customer frustration and churn). A well-managed ML platform optimizes both.

## What This Demo Shows

- **Feature Store**: Centralized feature management eliminates duplicate engineering across fraud, AML, and credit risk models
- **Model Registry**: Version-controlled model lifecycle - V1 baseline vs V2 optimized, with full comparison
- **Real-time Inference**: Deploy models for immediate scoring
- **Model Monitoring**: Track model performance and detect data drift over time
- **Cortex Integration**: LLM-powered explanations for analyst case review

## Data

Three synthetic tables, 10,000 rows each:

| Table | Description |
|---|---|
| `TRANSACTIONS` | Payment transactions with amount, merchant, device, channel, fraud label |
| `CUSTOMERS` | Customer profiles with account tier and spending baseline |
| `MERCHANTS` | Merchant data with category and risk tier |

Fraud rate: ~4-8% (higher for e-commerce and travel merchants)

## Setup

### Prerequisites
- Snowflake account with ACCOUNTADMIN or equivalent
- Python 3.11+ with Jupyter support, OR Snowflake Notebooks
- RSA key pair for Snowflake authentication (auto-generated on first run)

### Quick Start

1. **Environment Setup** - Run in Snowflake:
   ```sql
   -- Execute 01_env_setup.sql
   -- Creates: FINSERV_FRAUD_DEMO database, RAW_DATA schema, ML schemas
   ```

2. **Python Environment** (local setup only):
   ```bash
   conda env create -f environment.yml
   conda activate app_environment
   ```

3. **Run notebooks in order:**
   - `02_generate_and_load_data.ipynb` - Generate and load synthetic data
   - `03_finserv_fraud_demo.ipynb` - Main ML demo
   - `04_model_monitoring.ipynb` - Model performance tracking
   - `05_clean_up.ipynb` - Reset demo environment

## Project Structure

| File | Purpose |
|---|---|
| `01_env_setup.sql` | Create Snowflake database, schemas, tables, roles |
| `02_generate_and_load_data.ipynb` | Generate 10k transactions and load to Snowflake |
| `03_finserv_fraud_demo.ipynb` | Main demo: Feature Store, Model Registry, Inference, Cortex |
| `04_model_monitoring.ipynb` | Model performance tracking and drift detection |
| `05_clean_up.ipynb` | Reset demo environment |
| `demo_script.md` | SE demo script with talking points and discovery questions |
| `snowflake_connection.py` | Snowflake connection handler (local development) |
| `config.json.template` | Connection config template |

## Snowflake Objects Created

- **Database**: `FINSERV_FRAUD_DEMO`
- **Warehouse**: `STANDARD_WH_01_XS` (XSmall, auto-suspend 150s)
- **Schemas**:
  - `RAW_DATA` - Source tables
  - `FINSERV_FEATURE_STORE` - Feature Store schema
  - `FINSERV_MODEL_REGISTRY` - Model Registry schema

## Demo Talking Points

See `demo_script.md` for a full SE demo script with discovery questions.

---

*This demo uses synthetic data. For production deployment, implement appropriate data governance, security controls, and compliance measures.*
