from typing import List

from pydantic import BaseModel


class LinkProfile(BaseModel):
    links: List[str] = ["https://twitter.com/tyler"]
