FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# make sure needed packages are up to date
RUN pip install --upgrade pip setuptools wheel

# Setup project structure and dependencies
WORKDIR /app
COPY src/backend/ .
RUN pip install -r requirements-dev.txt

# install setup.py and run as package. If debug flag is active switch to debug entry point
RUN pip install .
CMD ["sh", "-c", "if [ \"$DEBUG\" = '1' ]; then sharefin-backend-debug; else sharefin-backend; fi"]
