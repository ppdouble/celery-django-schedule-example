#celery -A search_portal worker -B -l info --concurrency=1 2>&1 > celery.log &
nohup celery -A djproj worker -B -l info --concurrency=1 2>&1 > celery.log &
