FROM python:3.14-slim
RUN pip install --no-cache-dir -r requirements.txt gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
