from contextlib import asynccontextmanager

from fastapi import FastAPI
from playwright.async_api import async_playwright


@asynccontextmanager
async def playwright(app: FastAPI):
    async with async_playwright() as p:
        browser = await p.chromium.launch(channel="chrome")

        app.state.browser = browser

        yield

        await browser.close()
