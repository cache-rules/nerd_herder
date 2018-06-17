import json
import logging
import os
import sys

import requests
from django.conf import settings
from django.core.cache import cache

logger = logging.getLogger(__name__)
ASSET_MANIFEST_KEY = "ASSET_MANIFEST"
DEFAULT_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def init_logging(log_format=DEFAULT_LOG_FORMAT, date_format=DEFAULT_DATE_FORMAT):
    logging.basicConfig(
        format=log_format,
        datefmt=date_format,
        level=os.environ.get("METRICS_WEB_LOG_LEVEL", "INFO"),
        stream=sys.stdout,
    )


def get_asset_manifest():
    logger.info("Retrieving asset manifest")
    host = getattr(settings, "ASSET_MANIFEST_HOST")

    if host is None:
        # This should only be in dev mode. You will need to manually copy a built css file from
        # the frontend build to nerd_herder/static/main.css
        return {"main.js": "", "main.css": "static/main.css"}

    url = f"https://{host}/asset-manifest.json"

    try:
        r = requests.get(url, verify=False)
        return r.json()
    except requests.RequestException:
        logger.error(f"Unable to retrieve asset manifest from {url}")
    except json.decoder.JSONDecodeError:
        logger.error(f"Asset manifest URL {url} did not return JSON")

    return {"main.js": "", "main.css": ""}


def get_asset_urls():
    manifest = cache.get(ASSET_MANIFEST_KEY, None)

    if manifest is None:
        manifest = get_asset_manifest()
        cache.set(ASSET_MANIFEST_KEY, manifest, 60)

    return f'/{manifest["main.js"]}', f'/{manifest["main.css"]}'
