# Arquivo de configuração do Gunicorn

import os

# Define o numero de Workers para o Gunicorn
workers = int(os.environ.get("GUNICORN_PROCESSES", "4"))

# Define o numero maximo de Threads.
threads = int(os.environ.get("GUNICORN_THREADS", "2"))
