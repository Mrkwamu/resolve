import logging

from fastapi import HTTPException
from playwright.async_api import (
    Browser,
)
from playwright.async_api import (
    Error as PlaywrightError,
)
from playwright.async_api import (
    TimeoutError as PlaywrightTimeoutError,
)

from resolve.browser.schema import BrowserSchema

logger = logging.getLogger(__name__)

TIMEOUT_MS = 30_000


async def fetch_page_content(data: BrowserSchema, browser: Browser):
    context = None

    try:
        context = await browser.new_context()
        page = await context.new_page()

        response = await page.goto(data.url, timeout=TIMEOUT_MS)

        if response is None or not response.ok:
            raise HTTPException(
                status_code=502,
                detail="Failed to load the requested website",
            )

        html = await page.content()

        return html

    except PlaywrightTimeoutError as exc:
        logger.warning("Navigation timed out for URL: %s", data.url)
        raise HTTPException(
            status_code=504,
            detail="Navigation timeout",
        ) from exc

    except PlaywrightError as exc:
        logger.error("Playwright error while opening URL: %s", data.url, exc_info=True)
        raise HTTPException(
            status_code=502,
            detail="failed to perform browser operation",
        ) from exc

    except HTTPException:
        raise

    except Exception as exc:
        logger.exception("Unexpected error while opening URL: %s", data.url)
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred",
        ) from exc

    finally:
        if context is not None:
            await context.close()
