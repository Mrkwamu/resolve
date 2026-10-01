from playwright.async_api import Browser

from resolve.browser.schema import BrowserSchema


async def open_browser(data: BrowserSchema, browser: Browser):
    try:
        context = await browser.new_context()
        page = await context.new_page()
        response = await page.goto(data.url)

        if not response.ok:
            return

        return response.ok
    finally:
        "Testing is working"
