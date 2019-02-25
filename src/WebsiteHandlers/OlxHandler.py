from src.Requests.RequestHandler import RequestHandler
from src.DP.DictHandler import DictHandler
import requests


class OlxScrapper:

    @staticmethod
    def get_products(product: str, city_id: str = '', region_id: str = '', dist_id: int = 0, dist: str = ''):

        request_cookies = DictHandler({
            'dfp_segment_test_v3': '94',
            'dfp_segment_test': '76',
            'dfp_segment_test_v4': '59',
            'dfp_user_id': '55a33916-5b00-85f0-fe7f-6c095996efc0-ver2',
            'used_adblock': 'adblock_disabled',
            'laquesis': '',
            'laquesis_ff': '',
            '_ga': 'GA1.2.80702524.1549015664',
            '__gfp_64b': 'DGqAzmuFmpsuw4t7DqaQokzAelBBzZDGM9GVEDKdJvD.F7',
            'optimizelyEndUserId': 'oeu1549015665036r0.8129927509795887',
            '__gads': 'ID=8fc7441cff365397:T=1549015664:S=ALNI_MbNbejudPpwf_lmwgMyyZ71O9DzPQ',
            '_gcl_au': '1.1.1468737743.1549015666',
            'lister_lifecycle': '1549015677',
            'G_ENABLED_IDPS': 'google',
            'PHPSESSID': '63f583dac4d320303e197ba9bfe37f4d4dd63396',
            'refresh_token': 'ba5d424dba183ecb2603955b020c3d3616303137',
            'invite': '"sr=serviceletterMessage&cn=email--link&td=1549980182"',
            '__diug': 'true',
            'layerappsSeen': '1',
            '_gid': 'GA1.2.1243740843.1550262141',
            'disabledgeo': '1',
            'last_locations': '13897-0-0-Poniatowa-opolski-poniatowa_8959-0-0-Krak%C3%B3w-Ma%C5%82opolskie-krakow',
            '__utmz': '221885126.1550756149.31.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
            'newrelicInited': '0',
            'mobile_default': 'desktop',
            'ldTd': 'true',
            'from_detail': '0',
            '__utmc': '221885126',
            'pvps': '1',
            'lqstatus': '1551119679|||',
            '__utma': '221885126.80702524.1549015664.1551114401.1551118479.49',
            '__utmt': '1',
            '_gat_clientNinja': '1',
            '__utmb': '221885126.3.10.1551118479',
            'onap': '168a8874361x4ad033d0-48-16925ddae92x666c0c18-13-1551120810',
            'didomi_token': 'eyJ1c2VyX2lkIjoiMTY4YTg4NzQtN2Q4OS02ZDAzLWEwZjktZWNjODBkOGIzNTY4IiwiY3JlYXRlZCI6IjIwMTktMD'
                            'ItMDFUMTA6MDc6NDQuNjgzWiIsInVwZGF0ZWQiOiIyMDE5LTAyLTAxVDEwOjA3OjQ0LjY4M1oiLCJ2ZW5kb3JzIjp7'
                            'ImVuYWJsZWQiOltdLCJkaXNhYmxlZCI6W119LCJwdXJwb3NlcyI6eyJlbmFibGVkIjpbXSwiZGlzYWJsZWQiOltdfX'
                            '0=',
            'dfp_segment': '%5B%22t000%22%2C%22t012%22%2C%22t025%22%2C%22o948%22%2C%22o276%22%2C%22o929%22%2C%22o154%22'
                           '%2C%22o867%22%2C%22o657%22%2C%22o480%22%2C%22o003%22%2C%22o145%22%2C%22o679%22%5D',
            'fingerprint': 'MTI1NzY4MzI5MTs4OzA7MDswOzA7MDswOzA7MDswOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTswOzE7MTsxOzA'
                           '7MDswOzA7MTswOzA7MTsxOzE7MTsxOzA7MTswOzA7MTsxOzE7MDswOzA7MDswOzA7MTswOzE7MDswOzA7MDswOzA7MD'
                           'sxOzE7MDsxOzE7MTsxOzA7MTswOzE2MDE5Mjg1Mzg7MjsyOzI7MjsyOzI7MzsxMjM3Njc3NTc5OzE2NTk1ODk2NDk7M'
                           'TsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzA7MDswOzIxMzIwMzE0MjQ7NTM4MDk4Nzc4OzM1OTE4MTcy'
                           'OTg7MzMwODM4ODQxOzEwMDUzMDEyMDM7MTkyMDsxMDgwOzI0OzI0OzEyMDs2MDsxMjA7NjA7MTIwOzYwOzEyMDs2MDs'
                           'xMjA7NjA7MTIwOzYwOzEyMDs2MDsxMjA7NjA7MTIwOzYwOzEyMDs2MDswOzA7MA==',
            'ak_bmsc': '57B92B3D2FD92C9A7199E9A3972A71C2685E645642360000A020745C22BBD31A~plHbmKzzpLnoCghKt2UH0RoDPRLdOn'
                       'yvnAtH7Zi3JAOFnn8LJNx7IJ5/48T2xVxT70UNpBmUfylJ5NbCLh9DDegg0NfiNn+OdbN6bxeCupfhAQmmdJnAC59JiaU74'
                       'HaR1zVZFzaU2A0sRoKFGnOJVN2r0J7F5A+sgR0Qa77FPvoAN2hgo2SjerxfUBH9ykvOVSqOlgkwCRXl47MQ9KEwXoc1XKx5'
                       '77um0hojyd0JQqUVCPoHvdKf/oQ6TyvxVnz/tl; new_dfp_segment_user_id_34986433=%5B%22t000%22%2C%22t01'
                       '2%22%2C%22t025%22%2C%22o948%22%2C%22o276%22%2C%22o929%22%2C%22o154%22%2C%22o867%22%2C%22o657%22'
                       '%2C%22o480%22%2C%22o003%22%2C%22o145%22%2C%22o679%22%5D',
            'bm_sv': 'B89AEDB91A54973D3021D004187FEAEF~VqxBhQMxoymZQ2pz+v4dr7vgSxmusPVXKHg6FLjZ2BrjZDfWWAtD1ZMpDeSwErO1'
                     'zQ5MtXV+NzUmUm2b9Lj27a5uI61XHkPmeT5ye6bn72jloibKk4EZgvkJV4kpSxjClmgvnTj/5wHTzPFNQtt9fOOlOMl+EONtJ'
                     'ixRxs71Uts=',
        })

        request_headers = DictHandler({
            'authority': 'www.olx.pl',
            'method': 'GET',
            'path': str('/oferty/q-' + product + '/').replace(' ', '-'),
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'cookie': '; '.join(f'{k}={v}' for k, v in request_cookies.get_dict().items()),
            'referer': 'https://www.olx.pl/',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/72.0.3626.109 Safari/537.36'
        })

        data = DictHandler({
            'q': product,
            'search[city_id]': city_id,
            'search[region_id]': region_id,
            'search[district_id]': dist_id,
            'search[dist]': dist
        })

        request_url = str('https://www.olx.pl/oferty/q-' + product + '/').replace(' ', '-')

        response = RequestHandler.request(request_url, 'GET', headers=request_headers.get_dict(), cookies=request_cookies.get_dict(), data=data.get_dict())
        if type(response) != requests.models.Response or response.status_code != 200:
            print(response)
            return None