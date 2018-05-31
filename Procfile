web: gunicorn GDPRHero.wsgi
worker: celery -A GDPRHero.celery_app worker
beat: celery -A GDPRHero.celery_app beat -S django
 