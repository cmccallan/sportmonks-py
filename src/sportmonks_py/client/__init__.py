from ..utils.config import Config
from ..fixture import FixturesClient
from ..teams import TeamsClient
from ..odds import OddsClient
from ..leagues import LeaguesClient
from ..standings import StandingsClient
from ..misc import OtherClient
from ..core import CoreClient


class APIClient:
    def __init__(self, sport: str, api_token: str):
        """
        Initialize client-specific clients.

        :param sport: Sport being requested.
        :param api_token: API token for authenticating requests.
        """

        # Base URLs for sport and core
        base_urls = {
            "core": f"{Config.BASE_URL}/",
            "sport": f"{Config.BASE_URL}{sport}/",
        }

        client_classes = {
            "fixtures": FixturesClient,
            "odds": OddsClient,
            "teams": TeamsClient,
            "leagues": LeaguesClient,
            "standings": StandingsClient,
            "other": OtherClient,
            "core": CoreClient,
        }

        for attr_name, client_cls in client_classes.items():
            base_url = base_urls["core"] if attr_name == "core" else base_urls["sport"]
            setattr(self, attr_name, client_cls(base_url, api_token))