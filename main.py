def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(query: str) -> dict:
    from urllib import parse
    res = dict(parse.parse_qsl(query, separator=';'))
    # print(res)
    return res


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('devicePixelRatio=1;ident=exists;__utma=13103r6942.2918') == \
           {'devicePixelRatio': '1', 'ident': 'exists', '__utma': '13103r6942.2918'}
    assert parse_cookie('__utmz=1942.1.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=') == \
           {'__utmz': '1942.1.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr='}
    assert parse_cookie('mp_3cb00tinct_id%224initial_referrer=%=22htt=ps%32Fwww.pion_created_at%220%%22%7D') == \
           {'mp_3cb00tinct_id"4initial_referrer': '%=22htt=ps2Fwww.pion_created_at"0%"}'}
    assert parse_cookie('t_session=BAh7DUkiD3Nl3NhZ2UGOwBGVA%3D%3D--6ce6ef4bd6bc1a469164b6740e7571c754b31cca') == \
           {'t_session': 'BAh7DUkiD3Nl3NhZ2UGOwBGVA==--6ce6ef4bd6bc1a469164b6740e7571c754b31cca'}
    assert parse_cookie('username=John;hash=4c70884bd91727c931b91616c2d2b4d8;rememberme=yes') == \
           {'username': 'John', 'hash': '4c70884bd91727c931b91616c2d2b4d8', 'rememberme': 'yes'}
    assert parse_cookie("chips=ahoy;vienna=finger") == {'chips': 'ahoy', 'vienna': 'finger'}
    assert parse_cookie('name=value;name2=value2') == {'name': 'value', 'name2': 'value2'}
    assert parse_cookie('domain=reqbin.com') == {'domain': 'reqbin.com'}
    assert parse_cookie('...=...') == {'...': '...'}
    assert parse_cookie('=') == {}
