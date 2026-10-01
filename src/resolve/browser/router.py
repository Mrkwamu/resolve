from fastapi import APIRouter, Request

from resolve.browser.browser import open_browser
from resolve.browser.schema import BrowserSchema

router = APIRouter()


def getBrowser(request: Request):
    return request.app.state.browser


@router.get("/check-browser")
async def check_browser(request: Request):
    browser = getBrowser(request)
    return {"connected": browser.is_connected()}


@router.post("/browser")
async def open_browser_route(data: BrowserSchema, request: Request):
    browser = getBrowser(request)

    return await open_browser(data, browser)
