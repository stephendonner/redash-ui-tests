# -*- coding: utf-8 -*-

"""Page model for the queries page."""

import typing

from pypom import Page, Region
from selenium.webdriver.common.by import By

Selector = typing.Tuple[typing.Any, str]


class QueryDetailPage(Page):

    _query_description_locator: Selector = (
        By.CSS_SELECTOR,
        ".edit-in-place p",
    )

    @property
    def description(self) -> typing.Any:
        return self.find_element(*self._query_description_locator).text


class QueryRow(Region):

    _query_link_locator: Selector = (By.CSS_SELECTOR, "td a")

    @property
    def link(self) -> typing.Any:
        return self.selenium.find_element(*self._query_link_locator)

    def click(self) -> QueryDetailPage:
        self.link.click()
        return QueryDetailPage(self.selenium)


class QueryPage(Page):

    _query_table_locator: Selector = (By.TAG_NAME, "table")
    _table_row_locator: Selector = (By.TAG_NAME, "tr")

    @property
    def queries(self) -> typing.List[QueryRow]:
        table = self.selenium.find_element(*self._query_table_locator)
        items = table.find_elements(*self._table_row_locator)
        return [self.QueryRow(self, item) for item in items]
