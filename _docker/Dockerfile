FROM python:3.9

# set environment variables
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

ENV YOUR_ENV=1.3.1 \
    POETRY_VERSION=1.3.1

# update pip
RUN pip install --upgrade pip \
    && pip install "poetry==$POETRY_VERSION"

# set work directory
WORKDIR /home/tz_cg
COPY poetry.lock pyproject.toml /home/tz_cg/

RUN poetry config virtualenvs.create false
RUN poetry install $(test "$YOUR_ENV" == production && echo "--no-dev")  --no-root --no-interaction --no-ansi

COPY . /home/tz_cg