
python -m venv venv
if [ -z "$VIRTUAL_ENV" ]; then
    source ./venv/bin/activate
fi
pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000