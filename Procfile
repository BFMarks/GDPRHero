web: gunicorn GDPRHero.wsgi 
worker: celery -A GDPRHero worker
beat: celery -A GDPRHero beat -S django
 