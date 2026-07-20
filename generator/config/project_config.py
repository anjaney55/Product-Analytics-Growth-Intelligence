"""
Project level configuration.
"""

PROJECT_NAME = "Product Analytics & Growth Intelligence"

PROJECT_VERSION = "1.0.0"

RANDOM_SEED = 42

ENVIRONMENT = "development"

ENVIRONMENTS = {
    "development": 100,
    "testing": 1000,
    "production": 10000
}

TOTAL_USERS = ENVIRONMENTS[ENVIRONMENT]

START_DATE = "2025-01-01"

END_DATE = "2025-12-31"