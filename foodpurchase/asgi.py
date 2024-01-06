
import os
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_asgi_middleware import FastMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodpurchase.settings')

application = get_asgi_application()
app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
app.add_middleware(FastMiddleware, dispatch=application)
