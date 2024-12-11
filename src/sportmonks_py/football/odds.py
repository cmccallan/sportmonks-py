from typing import Dict, Any, Iterator, Optional

from sportmonks_py.base_client import BaseClient
from sportmonks_py.core.common_types import Includes, Selects, Filters


class OddsClient(BaseClient):
    """
    A client for accessing odds-related data from the SportMonks API.
    """

    def __init__(self, api_token: str, base_url: str) -> None:
        """
        Initialize the OddsClient with an API token and base URL.

        :param api_token: API token for authenticating requests.
        :param base_url: Base URL for the API.
        """
        super().__init__(api_token=api_token, base_url=base_url)

    def get_all_prematch_odds(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Retrieve all available pre-match odds.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over pre-match odds data.
        """
        return self._get(
            "odds/pre-match",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_fixture_prematch_odds(
        self,
        fixture_id: int,
        bookmaker_id: Optional[int] = None,
        market_id: Optional[int] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Retrieve pre-match odds for a specific fixture. Optionally filter by bookmaker or market.

        :param fixture_id: ID of the fixture.
        :param bookmaker_id: (Optional) ID of the bookmaker.
        :param market_id: (Optional) ID of the market.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over pre-match odds data.
        """
        if bookmaker_id:
            return self._get(
                f"odds/pre-match/fixtures/{fixture_id}/bookmakers/{bookmaker_id}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        if market_id:
            return self._get(
                f"odds/pre-match/fixtures/{fixture_id}/markets/{market_id}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        return self._get(
            f"odds/pre-match/fixtures/{fixture_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_latest_prematch_odds(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Retrieve pre-match odds for fixtures updated within the last 10 seconds.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over updated pre-match odds data.
        """
        return self._get(
            "odds/pre-match/latest",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_all_inplay_odds(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Retrieve all available in-play odds.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over in-play odds data.
        """
        return self._get(
            "odds/inplay",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_fixture_inplay_odds(
        self,
        fixture_id: int,
        bookmaker_id: Optional[int] = None,
        market_id: Optional[int] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Retrieve in-play odds for a specific fixture. Optionally filter by bookmaker or market.

        :param fixture_id: ID of the fixture.
        :param bookmaker_id: (Optional) ID of the bookmaker.
        :param market_id: (Optional) ID of the market.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over in-play odds data.
        """
        if bookmaker_id:
            return self._get(
                f"odds/inplay/fixtures/{fixture_id}/bookmakers/{bookmaker_id}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        if market_id:
            return self._get(
                f"odds/inplay/fixtures/{fixture_id}/markets/{market_id}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        return self._get(
            f"odds/inplay/fixtures/{fixture_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_latest_inplay_odds(
        self,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Retrieve in-play odds for fixtures updated within the last 10 seconds.

        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over updated in-play odds data.
        """
        return self._get(
            "odds/inplay/latest",
            params={"include": includes, "select": selects, "filter": filters},
        )

    def get_premium_fixture_prematch_odds(
        self,
        fixture_id: int,
        bookmaker_id: Optional[int] = None,
        market_id: Optional[int] = None,
        includes: Optional[Includes] = None,
        selects: Optional[Selects] = None,
        filters: Optional[Filters] = None,
    ) -> Iterator[Dict[str, Any]]:
        """
        Retrieve pre-match odds for a specific fixture from the Premium feed.
        Optionally filter by bookmaker or market.

        For more information about the Premium feed, visit:
        https://docs.sportmonks.com/football/endpoints-and-entities/endpoints/premium-odds-feed

        :param fixture_id: ID of the fixture.
        :param bookmaker_id: (Optional) ID of the bookmaker.
        :param market_id: (Optional) ID of the market.
        :param includes: Objects to include in the response.
        :param selects: Fields to include or exclude in the response.
        :param filters: Filters to apply to the results.
        :return: Iterator over Premium pre-match odds data.
        """
        if bookmaker_id:
            return self._get(
                f"odds/premium/pre-match/fixtures/{fixture_id}/bookmakers/{bookmaker_id}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        if market_id:
            return self._get(
                f"odds/premium/pre-match/fixtures/{fixture_id}/markets/{market_id}",
                params={"include": includes, "select": selects, "filter": filters},
            )
        return self._get(
            f"odds/premium/pre-match/fixtures/{fixture_id}",
            params={"include": includes, "select": selects, "filter": filters},
        )
