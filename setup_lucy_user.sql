-- Switch back to SECURITYADMIN to create the user
USE ROLE SECURITYADMIN;

-- Create the user. Replace the values with your coworker's information.
CREATE OR REPLACE USER lucy
    LOGIN_NAME = 'lucy'
    PASSWORD = 'REDACTED'
    EMAIL = 'lucy.martin@snowflake.com'
    MUST_CHANGE_PASSWORD = TRUE;

-- Assign the admin role to the new user
GRANT ROLE STRAVA_ADMIN TO USER lucy;

-- (Optional but Recommended) Set the user's default role and warehouse
ALTER USER lucy SET
    DEFAULT_ROLE = STRAVA_ADMIN
    DEFAULT_WAREHOUSE = 'COMPUTE_WH';

SHOW DATABASES HISTORY;
UNDROP DATABASE STRAVA_SAMPLE;

ALTER DATABASE STRAVA_SAMPLE RENAME TO STRAVA_SAMPLE_new;