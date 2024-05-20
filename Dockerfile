FROM python:3.12.2
WORKDIR /project
COPY . /project
RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "main:app"]