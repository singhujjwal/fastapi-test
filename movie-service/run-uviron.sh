export DATABASE_URI='postgresql://movie_user:movie_password@localhost/movie_db'
uvicorn app.main:app --reload --host 0.0.0.0 
