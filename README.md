# sharefin
A microservice to handle finances as an extension for the [PLACEHOLDER] application.

## Installation
Todo

## Usage
Todo

## Deployment

This application is intended as an extension to the [PLACEHOLDER] application. To host his extension, consider the following diagram:

```mermaid
graph LR
    user("👤 User")

    subgraph swarm["Docker Swarm"]
        subgraph frontend-container["frontend-container (Docker)"]
            frontend["Frontend App"]
        end
        subgraph backend-container["backend-container (Docker)"]
            fastapi["FastAPI App"]
        end
        subgraph db-container["db-container (Docker)"]
            mariadb[("MariaDB")]
        end
    end

    subgraph ext["External Microservice Platform"]
        subgraph user-service-container["user-service-container (Docker)"]
            userservice["User Microservice"]
        end
    end

    user -->|HTTPS| frontend
    frontend -->|"REST API (HTTP/JSON)"| fastapi
    fastapi -->|"SQL (TCP 3306)"| mariadb
    fastapi -->|"REST API (HTTP/JSON)"| userservice
```

## Data Model

This application will only store expenses, which are represented by the following data model:

```mermaid
erDiagram
    EXPENSE {
        int id PK
        float amount
        datetime date
        varchar description
        int paid_by_id FK
    }
    EXPENSE_SPLIT {
        int expense_id PK, FK
        int person_id FK
    }

    EXPENSE ||--|{ EXPENSE_SPLIT : "split"
```