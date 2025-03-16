✨ Features
✅ User Authentication & JWT - Secure login system using token-based authentication.
✅ CRUD Operations for Blogs - Create, Read, Update, and Delete blog posts.
✅ Protected Routes - Only authenticated users can perform certain actions.
✅ SQLAlchemy ORM - Efficient database interactions with relational models.
✅ Pydantic Validation - Ensures request data integrity.

🛠️ Tech Stack
FastAPI - High-performance web framework
SQLAlchemy - ORM for database management
JWT Authentication - Secure user login
Pydantic - Data validation and serialization
Uvicorn - ASGI server for running the app

🚀 Endpoints
User Authentication
🔹 POST /login - Authenticate user and receive JWT token

Blog CRUD
(Requires authentication)
🔹 POST /blog/ - Create a new blog 
🔹 GET /blog/ - Fetch all blogs
🔹 GET /blog/{id} - Get a specific blog by ID
🔹 PUT /blog/{id} - Update a blog (Authenticated users only)
🔹 DELETE /blog/{id} - Delete a blog (Authenticated users only)

Setup & Installation

**clone the repo:**
git clone https://github.com/moazakramkhan1/BlogsApi.git

**create a virtual environment:**
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

**install dependencies:**
pip install -r requirements.txt

**Run the application:**
uvicorn main:app --reload
