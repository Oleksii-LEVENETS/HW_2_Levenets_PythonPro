def parse(query: str) -> dict:
    from urllib import parse
    split_result = parse.urlsplit(query)
    res = dict(parse.parse_qsl(split_result.query))
    # print(res)
    return res


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse("http://www.example.org") == {}
    assert parse("http://www.example.org/default.html") == {}
    assert parse("http://www.example.org/default.html?ct=32") == {'ct': '32'}
    assert parse("http://www.example.org/default.html?ct=32&") == {'ct': '32'}
    assert parse("http://www.example.org/default.html?ct=32&op") == {'ct': '32'}
    assert parse("http://www.example.org/default.html?ct=32&op=") == {'ct': '32'}
    assert parse("http://www.example.org/default.html?ct=32&op=92") == {'ct': '32', 'op': '92'}
    assert parse("http://www.example.org/default.html?ct=32&op=92&") == {'ct': '32', 'op': '92'}
    assert parse("http://www.example.org/default.html?ct=32&op=92&item=98") == {'ct': '32', 'op': '92', 'item': '98'}
    assert parse("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1672161351&rver=7.3.6962.0&"
                 "wp=MBI_SSL_SHARED&&lc=1033&id=250206&cbcxt=sky") == \
           {'wa': 'wsignin1.0', 'rpsnv': '13', 'ct': '1672161351', 'rver': '7.3.6962.0',
            'wp': 'MBI_SSL_SHARED', 'lc': '1033', 'id': '250206', 'cbcxt': 'sky'}


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
