SGD_LIST = [
    {
        "id": 1,
        "name": "No Poverity"
    },
    {
        "id": 2,
        "name": "Zero Hunger"
    },
    {
        "id": 3,
        "name": "Good Health and Well-being"
    },
    {
        "id": 4,
        "name": "Quality Education"
    },
    {
        "id": 5,
        "name": "Gender Equality"
    },
    {
        "id": 6,
        "name": "Clean Water and Sanitation"
    },
    {
        "id": 7,
        "name": "Affordable and Clean Energy"
    },
    {
        "id": 8,
        "name": "Decent Work and Economic Growth"
    },
    {
        "id": 9,
        "name": "Industry, Innovation and Infrastructure"
    },
    {
        "id": 10,
        "name": "Reduced Inequality"
    },
    {
        "id": 11,
        "name": "Sustainable Cities and Communities"
    },
    {
        "id": 12,
        "name": "Responsible Consumption and Production"
    },
    {
        "id": 13,
        "name": "Climate Action"
    },
    {
        "id": 14,
        "name": "Life Below Water"
    },
    {
        "id": 15,
        "name": "Life on Land"
    },
    {
        "id": 16,
        "name": "Peace, Justice, and Strong Institutions"
    },
    {
        "id": 17,
        "name": "Partnerships for the Goal"
    }
]


IMPACT_LIST = [
    {
        "id": 1,
        "name": "Strongly Alligned"
    },
    {
        "id": 2,
        "name": "Alligned"
    },
    {
        "id": 3,
        "name": "Misalligned"
    },
    {
        "id": 4,
        "name": "Strongly Misalligned"
    }
]

PRODUCT_LIST = [
    {
        "id": 1,
        "name": "Food",
        "sgd_id": 2,
        "impact_id": 1,
        "parent_id": None
    },
    {
        "id": 2,
        "name": "Fruits",
        "sgd_id": None,
        "impact_id": None,
        "parent_id": 1
    },
    {
        "id": 3,
        "name": "Apple",
        "sgd_id": None,
        "impact_id": None,
        "parent_id": 2
    },
    {
        "id": 4,
        "name": "Pear",
        "sgd_id": None,
        "impact_id": None,
        "parent_id": 2
    },
]

COMPANY_LIST = [
    {
        "id": 1,
        "name": "Upright"
    },
    {
        "id": 2,
        "name": "Downleft"
    },
    {
        "id": 3,
        "name": "Bruce"
    },
    {
        "id": 4,
        "name": "Nguyen"
    }
]

REVENUE_LIST = [
    {
        "id": 1,
        "company_id": 1,
        "product_id": 1,
        "gmv": 1
    },
    {
        "id": 2,
        "company_id": 1,
        "product_id": 3,
        "gmv": 2
    },
    {
        "id": 3,
        "company_id": 1,
        "product_id": 4,
        "gmv": 4
    }
]