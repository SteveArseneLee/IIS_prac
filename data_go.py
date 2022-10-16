import json
import logging

import requests

from utils.secret import DATA_GO_KR_DE, DATA_GO_KR_EN
from utils.utils import DATA_GO_KR_API_KEYS

DATA_GOV_URL = "https://api.odcloud.kr/api/{}"