FROM python:3.9.6


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /concentrate

RUN pip install --upgrade pip

WORKDIR /concentrate

COPY --chown=concentrate:concentrate . .

RUN pip install -r requirements.txt

USER concentrate

CMD ["gunicorn", "-b", "0.0.0.0:8000", "Concentrate.wsgi.application"]
