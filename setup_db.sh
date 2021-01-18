apt update
apt install postgresql postgresql-contrib
createuser movie_user movie_password
createdb movies
useradd movie_user
