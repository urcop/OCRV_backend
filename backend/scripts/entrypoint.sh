#!/bin/bash

cd /app/backend/

sh ./scripts/migrate.sh
sh ./scripts/collectstatic.sh

exec gunicorn -c "gunicorn_config.py" core.wsgi