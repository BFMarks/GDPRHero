web: gunicorn GDPRHero.wsgi --debug --log-level debug
worker: celery -A GDPRHero worker
beat: celery -A GDPRHero beat -S django
 