
loglevel = "info"
errorlog = "-"  # stderr
accesslog = "-"  # stdout
worker_tmp_dir = "/dev/shm"
graceful_timeout = 120
worker_class = "egg:meinheld#gunicorn_worker"
bind = "127.0.0.1:5050"
timeout = 120
keepalive = 5
threads = 3