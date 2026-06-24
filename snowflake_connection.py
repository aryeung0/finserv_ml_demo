"""
Snowflake Connection Helper for Local Development

This module provides connection utilities for running Snowflake notebooks locally
in Cursor/VS Code while keeping notebooks compatible with Snowflake UI.

Usage in notebooks:
    Add this to the top of any notebook to enable dual compatibility:
    
    try:
        from snowflake.snowpark.context import get_active_session
        session = get_active_session()  # Works in Snowflake Notebooks
    except:
        from snowflake_connection import get_local_session
        session = get_local_session()  # Works locally in Cursor
"""

import os
from pathlib import Path
from snowflake.snowpark import Session
import json


def get_local_session():
    """
    Create a Snowflake session for local development.
    
    Reads credentials from config.json in the project root.
    Falls back to environment variables if config.json doesn't exist.
    
    Returns:
        Session: Snowflake Snowpark session
    """
    
    # Try to load from config.json first
    config_path = Path(__file__).parent / "config.json"
    
    if config_path.exists():
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        connection_params = {
            "account": config.get("account"),
            "user": config.get("user"),
            "password": config.get("password"),
            "role": config.get("role", "FINSERV_DEMO_ADMIN"),
            "warehouse": config.get("warehouse", "FINSERV_DEMO_WH"),
            "database": config.get("database", "FINSERV_FRAUD_DEMO"),
            "schema": config.get("schema", "FINSERV_MODEL_REGISTRY")
        }
        
        # If using key pair authentication
        if "private_key_path" in config:
            import cryptography.hazmat.backends
            import cryptography.hazmat.primitives.serialization
            
            with open(config["private_key_path"], "rb") as key_file:
                private_key = cryptography.hazmat.primitives.serialization.load_pem_private_key(
                    key_file.read(),
                    password=config.get("private_key_passphrase", "").encode() if config.get("private_key_passphrase") else None,
                    backend=cryptography.hazmat.backends.default_backend()
                )
            
            pkb = private_key.private_bytes(
                encoding=cryptography.hazmat.primitives.serialization.Encoding.DER,
                format=cryptography.hazmat.primitives.serialization.PrivateFormat.PKCS8,
                encryption_algorithm=cryptography.hazmat.primitives.serialization.NoEncryption()
            )
            
            connection_params["private_key"] = pkb
            del connection_params["password"]  # Don't use password with key pair
    
    else:
        # Fall back to environment variables
        connection_params = {
            "account": os.getenv("SNOWFLAKE_ACCOUNT"),
            "user": os.getenv("SNOWFLAKE_USER"),
            "password": os.getenv("SNOWFLAKE_PASSWORD"),
            "role": os.getenv("SNOWFLAKE_ROLE", "FINSERV_DEMO_ADMIN"),
            "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE", "FINSERV_DEMO_WH"),
            "database": os.getenv("SNOWFLAKE_DATABASE", "FINSERV_FRAUD_DEMO"),
            "schema": os.getenv("SNOWFLAKE_SCHEMA", "FINSERV_MODEL_REGISTRY")
        }
    
    # Validate required parameters
    if not all([connection_params.get("account"), connection_params.get("user")]):
        raise ValueError(
            "Missing required Snowflake credentials. "
            "Please create config.json or set environment variables."
        )
    
    # Create and return session
    session = Session.builder.configs(connection_params).create()
    print(f"✅ Connected to Snowflake (Local)")
    print(f"🏢 Account: {session.get_current_account()}")
    print(f"👤 User: {session.get_current_user()}")
    print(f"🏗️ Warehouse: {session.get_current_warehouse()}")
    print(f"🗃️ Database: {session.get_current_database()}")
    print(f"📁 Schema: {session.get_current_schema()}")
    
    return session


def get_session():
    """
    Get Snowflake session - works both locally and in Snowflake Notebooks.
    
    Returns:
        Session: Snowflake Snowpark session
    """
    try:
        # Try Snowflake Notebooks first
        from snowflake.snowpark.context import get_active_session
        return get_active_session()
    except:
        # Fall back to local connection
        return get_local_session()

