## Project Structure

```
review_master/
├── backend/           # Django REST Framework backend
│   ├── api/          # Django app for REST API
│   ├── price_dekho/  # Django project settings
│   ├── manage.py     # Django management script
│   ├── requirements.txt
│   └── .env          # Environment variables
├── frontend/         # Frontend application (to be added)
├── venv/            # Python virtual environment
└── .gitignore      # Root gitignore file
```

## Setup

### Backend
1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the backend directory with:
```
DJANGO_SECRET_KEY=your_secret_key
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

### Frontend
Frontend setup instructions will be added once the frontend is implemented.
