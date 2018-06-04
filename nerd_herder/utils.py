import logging
import os
import sys

import requests
from django.conf import settings
from django.core.cache import cache

logger = logging.getLogger(__name__)
ASSET_MANIFEST_KEY = 'ASSET_MANIFEST'
DEFAULT_LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


def init_logging(log_format=DEFAULT_LOG_FORMAT, date_format=DEFAULT_DATE_FORMAT):
    logging.basicConfig(
        format=log_format,
        datefmt=date_format,
        level=os.environ.get("METRICS_WEB_LOG_LEVEL", "INFO"),
        stream=sys.stdout,
    )


def get_asset_manifest(request):
    logger.info('Retrieving asset manifest')
    host = getattr(settings, 'ASSET_MANIFEST_HOST', request.META.get('HTTP_HOST'))
    url = f'https://{host}/asset-manifest.json'
    logger.info(f'Asset Manifest URL: {url}')
    r = requests.get(url, verify=False)
    return r.json()


def get_asset_urls(request):
    manifest = cache.get(ASSET_MANIFEST_KEY, None)

    if manifest is None:
        manifest = get_asset_manifest(request)
        cache.set(ASSET_MANIFEST_KEY, manifest, 60)

    return f'/{manifest["main.js"]}', f'/{manifest["main.css"]}'
