import os
import uuid

from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContextConfig


def build_chrome_browser():
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    browser_data_dir = os.path.join("browser-data", f"browser-data-{uuid.uuid4()}")

    config = BrowserConfig(
        headless=False,
        browser_binary_path=chrome_path,
        extra_browser_args=[
            "--incognito",
            f"--user-data-dir={browser_data_dir}",
        ],
        new_context_config=BrowserContextConfig(
            force_new_context=True,
        ),
    )

    return Browser(config)
