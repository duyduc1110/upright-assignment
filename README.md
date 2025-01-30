# Assignment from The Upright Project for Bruce
Date: 2025-01-30 15:00

## Quick Start

### Run the Docker Compose file:
```bash
docker compose -f compose.dev.yml up --build
```

### Database Connection
Default PostgreSQL connection details:

* Host: `localhost`
* Port: `5432`
* Database: `dev`
* Username: `admin`
* Password: `123456`

### API Documentation
Access the interactive API documentation at:
```
http://localhost:18000/docs
```

1. `GET /revenues/1`

Shows detailed revenue transactions for Upright (company_id=1), including:
- Revenue ID
- Product name & ID  
- SGD ID & Impact ID (inherited from parent products if not directly set)
- GMV value

2. `GET /reports/1`

Shows aggregated GMV by SGD and Impact types for Upright (company_id=1):
- Groups revenues by SDG types
- Shows total GMV for each SDG-Impact combination
- Includes SGD and Impact names
- Helps analyze company's contribution to different SDGs

## Sample Data
The application automatically initializes the database with sample data from `dictionaries.py`:

1. SGDs: 17 Sustainable Development Goals types

2. Products hierarchy: Food (root) => Fruits => [Apple, Pear]

3. Companies:
* Upright
* Downleft
* Bruce
* Nguyen

4. Revenues: Three sample revenue records logged with:
* Company ID
* Product ID
* GMV (Gross Merchandise Value)
The sample data demonstrates the product hierarchy and relationships between companies, products and revenues.

```
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
```