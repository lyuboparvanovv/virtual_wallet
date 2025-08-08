# Virtual Wallet Web App

## 1. Authentication & Authorization
- **Register** (`/auth/register`) – checks for unique username, email, and phone.
- **Login** (`/auth/token`) – validates user, password, and admin approval status.
- **JWT tokens** – created and verified using `python-jose`.
- **Password hashing** – handled with `passlib[bcrypt]`.
- **Protected routes** – enforce checks for active users and administrators.

## 2. User Management
- View own profile (`/users/me`).
- Update own profile.
- Admin actions:
  - List all users.
  - Approve/deactivate/activate users.

## 3. Cards Management
- Create a card (16-digit number, CVV, expiry date).
- Retrieve cards by user.
- Delete a card.

## 4. Categories
- Create categories for transactions.
- View own categories.
- Edit and delete categories.

## 5. Transactions
- Create a transaction (amount, sender, receiver, category, card).
- View transaction history (with pagination).

## 6. Contacts
- Add a contact (another user).
- View contact list.
- Remove a contact.

## 7. Technical Stack
- **FastAPI** – API endpoints and data validation (Pydantic).
- **Uvicorn** – ASGI server.
- **SQLAlchemy ORM** – models and database queries.
- **PostgreSQL** – main database.
- **psycopg2-binary** – PostgreSQL driver.
- **python-dotenv** – configuration from `.env`.
- **Passlib[bcrypt]** – password hashing.
- **python-jose[cryptography]** – JWT token authentication.

---
