# Installation

```
pip install -r requirements.txt
```

# Run


Celery Worker

```
celery worker -A proj:worker --loglevel=info
```

Celery producer

```
python -m proj task1
python -m proj task2
```


Flower Dashboard

```
flower -A proj --port=5555
```
