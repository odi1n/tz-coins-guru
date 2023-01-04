from typing import List


def get_username_with_links(links: List[str]):
    for link in links:
        if "https://twitter.com/" in link is False:
            continue
        line_split = link.split('/')
        if len(line_split) != 4:
            continue

        yield line_split[-1]
