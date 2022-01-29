uvicorn app.main:app --reload --host 0.0.0.0 --port 8121 &
uvicorn app.main:app --reload --host 0.0.0.0 --port 8122 &
uvicorn app.main:app --reload --host 0.0.0.0 --port 8123 &
uvicorn app.main:app --reload --host 0.0.0.0 --port 8124 &

## shutdown pkill uvicorn
