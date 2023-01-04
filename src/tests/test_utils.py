from utils.trim_link import get_username_with_links


def test_get_username_with_links_g():
    check = []

    links = get_username_with_links([
        'https://twitter.com/elonmusk',
        'https://twitter.com/VitalikButerin',
        'https://twitter.com/jack',
    ])

    for link in links:
        check.append(link)

    assert len(check) == 3


def test_get_username_with_links_b():
    check = []

    links = get_username_with_links([
        'https://twitter.com/elonmusk',
        'https://twitter.com/VitalikButerin',

        'https://twitter.com/jack/test',
        'https://vk.com/msg/test',

        'https://twitter.com/jack',
        'https://twitter.com/jack/',
    ])

    for link in links:
        check.append(link)

    assert len(check) == 3
