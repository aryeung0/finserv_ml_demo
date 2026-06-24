# Strava ML Demo - Fraud Detection
**End-to-End Machine Learning Platform Demo (2025)**

This project demonstrates a complete end-to-end machine learning workflow for fraud detection on Strava-like fitness data using Snowflake's ML platform. It showcases how to build, deploy, and monitor ML models entirely within Snowflake.

## 🏃‍♀️ What This Project Does

This demo showcases **Strava leaderboard fraud detection** using Snowflake's ML platform to demonstrate:
- **Feature Store**: Centralized feature management to eliminate duplicate engineering across teams
- **Model Registry**: Version-controlled model lifecycle management with V1 and V2 models
- **Real-time Inference**: Deploy fraud detection models for immediate business value
- **Model Monitoring**: Track model performance and detect data drift over time
- **Cortex Integration**: AI-powered analysis complementing traditional ML approaches

### Business Use Case
Detect potentially fraudulent athlete activities on leaderboards by identifying:
- Unrealistic pace improvements
- Impossible heart rate patterns
- Sudden dramatic performance boosts
- Suspicious activity patterns

## 📊 Data

The project works with three main datasets (10,000 rows each):
- **Activities**: Running, cycling, and other activity data with metrics like distance, pace, heart rate, and elevation
- **Challenges**: Sponsored challenge participation and completion data
- **Subscriptions**: User subscription plans and engagement data

## 🛠️ Setup

### Prerequisites
- Snowflake account with appropriate permissions (ACCOUNTADMIN or equivalent)
- Python 3.11+ environment with Jupyter notebook support
- RSA key pair for Snowflake authentication (auto-generated on first run)

### Quick Start
1. **Environment Setup**: Run the SQL setup script to create database, schemas, and tables:
   ```sql
   -- Execute 01_env_setup.sql in Snowflake
   -- This creates: STRAVA_DEMO_SAMPLE database, RAW_DATA schema, and all required tables
   ```

2. **Python Environment**: Set up Python environment:
   ```bash
   conda env create -f environment.yml
   conda activate app_environment
   ```

3. **Snowflake Connection**: Configure authentication:
   - RSA key pair authentication (recommended for local development)
   - Keys auto-generated in `~/.snowflake/` directory
   - Connection managed by `snowflake_connection.py`
   - Alternative: Use Snowflake Notebooks (no local setup required)

## 📁 Project Structure

### Setup & Configuration
- `01_env_setup.sql` - SQL script to create Snowflake database, schemas, tables, and roles
- `01_env_setup.ipynb` - Interactive notebook for environment setup verification
- `01_execute.ipynb` - Quick execution notebook for running setup scripts
- `snowflake_connection.py` - Snowflake connection handler with RSA key pair authentication
- `environment.yml` - Python dependencies (Snowpark, ML, visualization libraries)

### Demo Notebooks (Run in Order)
- `02_generate_and_load_data_snowflake.ipynb` - Generate realistic Strava data (10k rows) and load into Snowflake
- `03_strava_ml_demo.ipynb` - **Main ML Demo**: Feature engineering, model training (V1 & V2), registry, inference
- `04_model_monitoring.ipynb` - **NEW**: Model performance tracking, comparison, and monitoring framework
- `05_clean_up.ipynb` - Clean up demo environment (preserves infrastructure)

### Additional Files
- `setup_snowflake_auth.py` - Automated RSA key pair generation for authentication
- `demo_script_for_katy.md` - Presentation script and talking points
- `README.md` - This file

## 🚀 Usage

### Step-by-Step Workflow

1. **Environment Setup** (One-time)
   ```bash
   # Execute SQL setup in Snowflake
   snowsql -f 01_env_setup.sql
   
   # OR run the notebook
   jupyter notebook 01_env_setup.ipynb
   ```

2. **Generate and Load Data**
   ```bash
   # Creates 10,000 realistic Strava activities with fraud indicators
   jupyter notebook 02_generate_and_load_data_snowflake.ipynb
   ```

3. **ML Model Training & Deployment**
   ```bash
   # Feature Store, Model Registry, V1 & V2 models, Real-time inference
   jupyter notebook 03_strava_ml_demo.ipynb
   ```

4. **Model Monitoring** (New!)
   ```bash
   # Performance tracking, model comparison, monitoring framework
   jupyter notebook 04_model_monitoring.ipynb
   ```

5. **Clean Up** (Optional)
   ```bash
   # Resets demo environment while preserving infrastructure
   jupyter notebook 05_clean_up.ipynb
   ```

## 🔧 Technical Architecture

### Snowflake ML Platform Components
- **Feature Store**: Centralized feature management with versioning and lineage tracking
- **Model Registry**: Version-controlled storage for RandomForest fraud detection models (V1 & V2)
- **Snowpark Python**: Server-side execution for data processing and feature engineering
- **Cortex AI**: LLM-powered fraud analysis and churn prediction
- **ML Observability**: Model performance tracking and drift detection (framework ready)

### Technology Stack
- **Python**: 3.11+ (Anaconda packages for Snowflake compatibility)
- **ML Libraries**: snowflake-ml-python, scikit-learn, xgboost
- **Data Processing**: Snowpark DataFrames (server-side execution)
- **Visualization**: matplotlib, seaborn
- **Authentication**: RSA key pair (auto-generated)

### Data Architecture
- **Database**: `STRAVA_DEMO_SAMPLE` (single database for simplicity)
- **Schemas**:
  - `RAW_DATA` - Source data tables (Activities, Challenges, Subscriptions)
  - `STRAVA_FEATURE_STORE` - Feature definitions and feature views
  - `STRAVA_MODEL_REGISTRY` - Registered models and inference procedures
- **Warehouse**: `STRAVA_DEMO_WH` (Medium size, auto-suspend enabled)

## 📝 Key Features & Capabilities

### 1. Feature Engineering & Management
- ✅ Centralized Feature Store eliminates duplicate engineering
- ✅ Feature versioning and lineage tracking
- ✅ Reusable features across multiple models
- ✅ Consistent feature definitions for training and inference

### 2. ML Model Lifecycle
- ✅ **Model Training**: RandomForest classifier with hyperparameter tuning
- ✅ **Model Versioning**: V1 (baseline) and V2 (optimized) with full version history
- ✅ **Model Registry**: Centralized model storage with metadata and metrics
- ✅ **Real-time Inference**: Stored procedures for production deployment

### 3. Fraud Detection Capabilities
- ✅ Detects unrealistic pace patterns (>20 km/h running)
- ✅ Identifies impossible heart rate patterns (>200 bpm)
- ✅ Flags suspicious activity clusters
- ✅ Provides explainability through feature analysis

### 4. Model Monitoring (New!)
- ✅ Performance comparison between model versions
- ✅ Comprehensive metrics (Accuracy, Precision, Recall, F1)
- ✅ Confusion matrix analysis
- ✅ Inference pipeline with stored procedures
- ✅ Framework for drift detection and alerting

### 5. AI Integration
- ✅ Snowflake Cortex for fraud risk assessment
- ✅ LLM-powered analysis with Claude 3.5 Sonnet
- ✅ Churn prediction using AI
- ✅ Model vs. AI comparison analysis

## 🎯 Business Value

### Problem Solved
Strava's challenge: Managing 15+ fraud detection models with:
- ❌ Inconsistent feature engineering across teams
- ❌ No centralized model versioning
- ❌ Difficult model performance tracking
- ❌ Manual monitoring and maintenance

### Solution Delivered
This demo shows how Snowflake's ML platform provides:
- ✅ **Single Source of Truth**: Centralized Feature Store
- ✅ **Version Control**: Complete model lifecycle management
- ✅ **Automated Monitoring**: Performance tracking and alerting
- ✅ **Scalability**: Platform ready for production deployment
- ✅ **Cost Efficiency**: No separate ML infrastructure needed

### Key Metrics
- 📊 **10,000** activities analyzed with fraud indicators
- 🎯 **>95%** model accuracy on fraud detection
- 🚀 **2 model versions** tracked with full comparison
- ⚡ **Real-time** inference capability via stored procedures

## 🔍 What's Different in This Demo

This demo goes beyond basic ML by showcasing:
1. **Complete ML Platform**: Not just model training, but full lifecycle management
2. **Production-Ready**: Stored procedures, versioning, monitoring framework
3. **Business Context**: Real fraud detection use case with clear value proposition
4. **Best Practices**: Feature stores, model registry, monitoring - enterprise ML patterns
5. **AI Integration**: Combines traditional ML with Cortex AI for comprehensive analysis

## 📚 Additional Resources

- [Snowflake ML Documentation](https://docs.snowflake.com/en/guides-overview-ml)
- [Feature Store Guide](https://docs.snowflake.com/en/developer-guide/snowflake-ml/feature-store/overview)
- [Model Registry Guide](https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/overview)
- [Cortex AI Documentation](https://docs.snowflake.com/en/user-guide/snowflake-cortex/llm-functions)

---

**Note**: This is a demonstration project using synthetic data. For production use, implement proper data governance, security controls, and compliance measures.
