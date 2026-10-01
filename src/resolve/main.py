from fastapi import FastAPI

from resolve.browser.playwright import playwright
from resolve.browser.router import router

app = FastAPI(lifespan=playwright)

app.include_router(router)
