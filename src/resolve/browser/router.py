from fastapi import APIRouter, Request

from resolve.browser.browser import fetch_page_content as page_content
from resolve.browser.schema import BrowserSchema

router = APIRouter()


def get_browser(request: Request):
    return request.app.state.browser


@router.get("/check-browser")
async def check_browser(request: Request):
    browser = get_browser(request)
    return {"connected": browser.is_connected()}


@router.post("/pages/content")
async def get_page_content(data: BrowserSchema, request: Request):
    browser = get_browser(request)
    return await page_content(data, browser)
