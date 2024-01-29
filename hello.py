import os
from googleapiclient.discovery import build

# Set your API key (get one from the Google Cloud Console: https://console.developers.google.com/)
api_key = 'AIzaSyAd2TROT0G079wtaGFPl_ep50rjuE-cZEE'
youtube = build('youtube', 'v3', developerKey=api_key)

def get_videos_by_date(api_key, channel_id, date):
    try:
        # Call the YouTube Data API to search for videos by date
        request = youtube.search().list(
            part="id",
            channelId=channel_id,
            publishedAfter=f"{date}T00:00:00Z",
            publishedBefore=f"{date}T23:59:59Z",
            type="video",
            maxResults=50  # You can adjust this value
        )

        response = request.execute()

        # Extract video IDs
        video_ids = [item['id']['videoId'] for item in response['items']]

        print(video_ids)

        # Get video details (you can extract more information if needed)
        videos = youtube.videos().list(
            part="snippet",
            id=",".join(video_ids)
        ).execute()

        # for key, value in videos.items():
        #     print(key)

        for video in videos['items']:
            video_url = f"https://www.youtube.com/watch?v={video['id']}"
        
        return video_url

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
channel_id = 'UCq-Fj5jknLsUf-MWSy4_brA'
search_date = '2024-01-01'  # Replace with the date you're interested in
get_videos_by_date(api_key, channel_id, search_date)

# d = {'kind': 'youtube#searchListResponse', 'etag': '7KjspfNthrtrfYP_AKwS-Jt5ycI', 
#      'regionCode': 'IN', 'pageInfo': {'totalResults': 2, 'resultsPerPage': 2}, 
#      'items': [{'kind': 'youtube#searchResult', 'etag': 'OlxKlQ1mws6lLY_6WAeUA_7CMDA', 
#                 'id': {'kind': 'youtube#video', 'videoId': 'tmcIXxHAvn8'}},
#                   {'kind': 'youtube#searchResult', 'etag': 'WdY2WJq1nhYOx5mCEO_fJQzzohQ', 
#                    'id': {'kind': 'youtube#video', 'videoId': 'L5nyPNlkixo'}}]}
date_video = {'2023-05-22': ['Db2xSI-PSEc', 'H3q0mCpUhvA', '9w56giTNzY0'], '2023-05-23': ['D8oCXA3BVyU'], '2023-05-24': ['ZUJo0Qky-mg', 'bBE88-7ZyPw'], '2023-05-25': ['1SiK7WtjvRc', 'iVP_eIjTDkY', 'hA91wG0ZZGs', '2J4wxvro3oo', 'M-Nz1o3yrek', 'w4jFJCLWQGg', '2xJlerdkTyU', 'A_cp1oKIVxA'], '2023-05-26': ['YS4_4KdNEQI', '7KKVb0_IdD4', 'cChAHb1BAcU', 'GMPdEeA3vX4', '6tH1ed9DQyI', 'RVPd9-Q77bc'], '2023-05-27': ['Sk0DsJuJ_y8', 'wVqgbpseUiA', 'Afp7rqZDt04'], '2023-05-28': ['eoIkvoO_yMA', 'MCoEIsg873U', 'WNnA2h2Qprc', 'Wi-nZoQHHgI', 'RRi9K2m2xSA', 'ZRVphzCBtD0', 'HuXsWcCVFsE', 'Ra8ky5pCGAc', 'uCZ2CK7KTMk', '2ccuss7eMA4', 'WpCCBXOGotc', 'TMGtP-0dULs', '7G0yDyRnTWM'], '2023-05-29': ['GXWfue9VhTY', 'NEcbe7q9dzg'], '2023-05-30': ['6IW-iZ3tV94', 'B8bpOdiOT48', '7SQKLp63epM', 'ALYQsFRpSEM', 'LlxpaJ2Ls1M', 'P13NDbzXCos', 'U-t9pICp_-8', 'hv8Fgw3WeHo', 'Tv1TrcAXJ9Y', 'KmDsCrW4378', 'DefDuDO1gr0', 'V2XXXB4jdAE', 'NwsJpbfz7FA', '_Rw4gra4B78', 'I3R8iztxmSg', 'aelace0lGT4', 'yNd344pBykU'], '2023-05-31': ['GeYp0IZozYQ', 'OoMBHDZCpFA', 'd_d2AoozUy4', '1nffLJldOAY', 'VhLHRnk3AyM'], '2023-06-01': ['YfOLdtbHluo', 'xKobMKy1rzs', 'k6JGVIigQ54'], '2023-06-02': ['0PMBOGf5Z5w', 'jQvE-7SF9hU', 'f1xAtf6OEio', 'ESlQPmsEPeg', 'jLOB-REmGBk'], '2023-06-03': ['_N64z22_PR8', 'u_HxDGOv_gM', 'ZE6dQqUfttg'], '2023-06-04': ['FBq61EXYk58', 'npwn6KVMtFI', 'mCE_1Vo8hG8'], '2023-06-05': ['hyCbiyQ4JqQ', '0lSxjDYdvpQ'], '2023-06-06': ['ljEDVxiCw6s', 'WCOtd14m3ZY', 'X7lRGozX8KQ', 'LmcgdcKtc0o', 'OQa-zu4ix1A', '9xz_bjWV5tU', 'yGyCiv1YKKk'], '2023-06-07': ['Tl4bQBfOtbg', '8lZbiF_rC2I', 'QWaMHy1LdwI', 'EQmM2IDfUZ0', '05hrTUrPBaY'], '2023-06-08': ['WRHnBD8qs94', 'Qi2A2GFlyVY', 'uldNZixQszI', 'lXNT7mFH1OE', 'HaHmWRl856c', 'mkxKZVM84WM', '70G8pW8dCJI', 'd__a6dLrbtU'], '2023-06-09': ['R_gK9F9Z77E', '5I3K2DtH9x8', 'go8MhN8mtEw', 'Q8YZHfSDCco'], '2023-06-10': ['MPLWw4-q93U', 'j3Nd6QMbpaE', 'GK2XMcS61yo', '1Hj51WjvBwU', 'PPrbMPpKWp0'], '2023-06-11': ['EywX_uxreYA', 'lYdAkDqvrpU', 'QMYbxTNMqz0'], '2023-06-12': ['vC6bSavM_Eo', 'k-4zfXxjdK0', 'A_iy3g2preo', '4GacaSFJwG4', 'AyB6iEbDkxQ'], '2023-06-13': ['CPHFu4oUpo0', '8uqnjvm0Or0', 'BXMjHubMGxM', 'vjOUtLFlwxY', 'mY8o8c5MsyY'], '2023-06-14': ['ZJcGY32MtVs', 'j41etIHcGQc'], '2023-06-15': ['tjPMcJ6Daqk', 'lzYGlGrRqx0', 'A0dieDI4kSs', '90mMgzGpCTY'], '2023-06-16': ['xUkroAWdTnM', 'SOMNwWo5HPg', 'TjPgRGhgW40', 'nalWoUUz6LA', 'WFnH6T6s690'], '2023-06-17': ['w7NLhcZPEB4', 'EzdlGgn7frQ', 'ZR5P4KhY8SU', 'YvOsB_oHJHA', 'gO7WnC6TYKA'], '2023-06-18': ['3XTPCM13eiE', 'HJNRdmFb8Qs', 'uT7ESWWGFsI', 'bvUNXch3rdI', 'lX66pufC5bk', '7T0MomojCqc', 'BExN5Tcp03I', 'TGL2IasS7lM', 'VMr-ijRXwXk', 'zPENipKf7yE', 'v7Kk8cc-3rs'], '2023-06-19': ['BSK29-Hagsg', '-3m26BQc1BM', 'Bec-jWygewM', 'BTouG4McDBE', 'zFdmht7V280', 'j9rUb0EXeH8', 'eQWCGUMlXJQ', 'HGhQpjTJCQ4', '_vFdgHmFTKk', 'XcgkjnU5rwM', 'Iw0_74vXEOA', 'qB7L3NbVQWA'], '2023-06-20': ['ngjUEDEY18E', 'mp6kOVyWcUA', 'GjOVfX01yJA', 'axFWhzrnzvs', 'ui-nZpN0H1k', 'a7Lsc1wA-io'], '2023-06-21': ['AxA2xYbMCVo', 'ZHjjXZYN7Yg', 'VH2HXkHF1o0', 'So3fbMjvtEA'], '2023-06-22': ['2UkE1Xb_oAs', 'yGl8MgpBJtk', 'ItR_bh5fRus'], '2023-06-23': ['lxsJP_I33b4', 'R-_4TJsgpPs', 'f0xNLG83juA', 'n23wMcXa95M'], '2023-06-24': ['8QtNfpohymg'], '2023-06-25': ['ifQQbfnO1jY', 'iqGi4o7v9h8', 'VJ-o8y8JqCQ', 'o7wfiQQdLaY'], '2023-06-26': ['xaciGzadGTo', 'Yiw354fkSOs', 'Pm_JL0FzURI', 'je17EI7oMys'], '2023-06-27': ['VhWnOFHoDMQ', 'jXscoTpsOMM', 'Nj4J7PDmoxE', 'ozbCQHXhpGA', 'E4sIKrdMUlA'], '2023-06-28': ['MYUnwR5Ait0', 'pQPkwWuQq2g', '-PirxyNxO_M', 'oMHxtQtRdS8', 'yeLPbMbgwc0', 'zbdBfcM-v70', 'sSA9EQLHW60', 'qv5R2Ce9m6c', '3vxBE_LfWGw', 'M25oWGZF-IU', 'GpYojTWPpPM', 'VJ2QX8N8Hyo'], '2023-06-29': ['_in9SMrUkD0', 'ydrzUjGHi9I', 'DmsarGOD-o4', '9Iq8UCp1jYU', 'PZu35g-z_Lg'], '2023-06-30': ['9o3NjnwCh-8', 'pgkoQA7lbe8', 'xfxHibiU4xc', 'AzZDh6gWGps'], '2023-07-01': ['R_XiBKkSAxY', '77l9ol70P6U', '6JehgiVUB5U', 'roRSpk9mNEg', '7tCmU3jUwlE', 'yXCjj2jcm9g'], '2023-07-02': ['hmZwuwbOjQo', '9kwEtY01O-4', 'sU_vrQ_plPs', '1kn2Sdd12bE'], '2023-07-03': ['c7s4rsmnKHA', '0wUNGBPEvF4', 'K5fwbm-JT-A'], '2023-07-04': ['dRftQa5ctKc', 'Kx6WY-rxQQM', 'uvGdMu8Xilg', '22VumHyAwVo', 'IL3hoPmNfus', '2v0TwVp4XfM'], '2023-07-05': ['qV1TbRqDWfU', 'Q6xrawvWA1M', '6z6eXrFcfcg', 'Fd81aiHnFOQ', 'MTLfgMjupKA', '8tXmfDmui4c', 'jophtol6P-A', 'nlNI_1ErmGA'], '2023-07-06': ['UWceWcNym7k', 'jTgubN6NbJw', 'jrOZ9RU7zXw'], '2023-07-07': ['m0HEWP5o7DI', 'swhjLMyWZDQ', '4T-QaZiKxPQ', 'dvcgpTlVerM', '74JCnCZva90', 'Ca625m1vz-g'], '2023-07-08': ['Lghkbiwrauc', 'JIcsSYkJ5gQ'], '2023-07-09': ['qYwQC_Nkj3Q', '-sUDGEcqNJM', 'GYHY1a2wz6Q', 'SO74tGYb5og', 'TeaMjaCKEis', 'v8Pc2XOpTCs', 'snQdDbsTm0o', 'RZDEnyl4HJY'], '2023-07-10': ['jyZsX8OyrmQ', '6JtZjy04BU4', 'oA2ciy-wh80', 'SmS2QRjuSLc', 'xm6FnsNHBsQ', 'AGPCLpPkGIA', '774PKgf_Uz4', 'vjcyf0myfeQ', 'SS_F-b5FDog', 'norGD-p4R3o'], '2023-07-11': ['UmciPIE_Ows', 'UsyfG5tLAC0', '_W-AKcLeLRw', 'c2_iQsyoulc', '9KNVLTYar0g', '6v41EcgDWMw', 'vTdZtpWKw-Y', 'S6wAXRF8_do', 'BA66itXmfxQ'], '2023-07-12': ['OfmGYgLMbjs', 'HDi-5Ox9kgE', 'TQqXRtVXcnA', '9fAzyTza7W8', 'Zbl1S06yixA', '7xR8O90DBf0', 'PL9414Zf5_U', 'QuAPfzCD6Zo', 'oqSQQjxSuSI', 'B4dmO1fwHGM', 'ywzvlcQhn2I', 'A81NPegkjwU'], '2023-07-13': ['aDBKcFpRknk', 'EyYof1cQoKA', 'ZAE1JwBoVoA', 'C1f89eaxGWM', 'R4EbMyHXMUs', '2OG2milZZ6I', 'truRtNvsBlw', 'EFqOKTGE-IU', '1glWWQP5ENs', 'dR9BS1E_PXw', 'wfr1a_XWvyA', 'wl7O0zwR42o'], '2023-07-14': ['3_iYqDuYYSc', 'iKbsZJ3Qn9g', 'UAuvmx3cPos', 'BRYLg732Ajk', 'IfDaIG3rsOg', 'RdVK0_LljRo', 'Mfsn9xZ9pP0'], '2023-07-15': ['IMCqhBxMuks', 'pEI8mUNAUQk', 'FpOzrIP9NtA', 'XsGJGIgEXKA', 'Ws5IlKQ-CC8', 'rRsoL2OFU2M', 'wltVLr_P8LY', 'iDF8c3Na0xc', 'AXMtX6L3bVo', 'qKqp2kaQpvY'], '2023-07-16': ['tnxGPvZcOWk', 'QQfSBGRosvk', 'E6s0XVrfpKk', 'd18QdQhpxu8', 'A09O3AtLvu8', 's6-t2ckprGw', 'Mp88CJtNPwQ', 'OiJtPstjZrg', 'xwSRrPCOMZk'], '2023-07-17': ['QaKpeRxaZxM', 'vXv8FZuvJ08', 'kgibSvXqQuI', 'BYbq0TQO24o', 'xPxNXWvDmaU', '753-gCWtYcM', 'Qy_nZNsfrIs', 'kqKe6sZYg6I', 'HAR4U53oo7s', 'rJaUNuhRu7g', 'H0VUX01HG6w', 'nA65wBvSIGI', 'pSw1kc9kWeM', 'pR9ShV1TXks', 'uCrBL-8qgFo', 'sf5soB47vUk'], '2023-07-18': ['1sP8ZpeM0Ak', 'vMT4ogwVV_o', 'CKAbdB6k4hk', 'og-umnezR-U', 'ieUizW7b0ko', 'L0pmGr3e2NI', 'MjaqbdDwOr4'], '2023-07-19': ['Gcmk7C21Jlw', 'OJuUNZBJ50c', '0XeFIQz1yB4', 's0hkdwqBzOo', 'w_c4pLFkIUA'], '2023-07-20': ['PyHd2Ev9h10', 'ayCVOiWafis'], '2023-07-21': ['aXojslK7w4I', '91JLKbSrOXw', 'O9IOitkCFHI', '7WXRZNScpeQ'], '2023-07-22': ['iqhkp6339r4', '-OAvyoQryfg', 'cBYLONr-e_Q', 'wH2w6ZmQOgA'], '2023-07-23': ['hUscd_dkDcs', 'WzuIcK4IxA0', 'Xw-DrzO0dts', 'VQ4javkA4MQ', 'R_mkSrAqZcU', 't_zPMR4sVsc'], '2023-07-24': ['uSb0M_UQE1o', 'k3wukPrf37I', 'KbjwyBaz6Fs', 'rB5QPIP5H6k'], '2023-07-25': ['-i3Ilas24X4', 'oE40KlLhQQg', 'IXa3sId1iF4', 'OD1LhUu4bRI'], '2023-07-26': ['RBOyjrXLQSU', 'DYNXlv0A3sE', 'Cybo2U_d0Xs', 'prpJfiEmrmg', 'Dm0Y_x6bOaQ', 'FkgnpnzeKx0', '2SuNLFYD41A', 'cVHN-GFVtH0', '8gbrGt4hbjc'], '2023-07-27': [], '2023-07-28': ['7uBJEPh-mYk', 'EpdsVO9pt9g', '4-30eu39wRM'], '2023-07-29': ['46QxVICzPB8', 'YsCeMprm2O0', 'fKfqHDdWKKU', 'BwhM9RMDL_4', 'Z2HJfQCtLQ0', 'eG40RRp0Zas', 'VT5i6p1w0B0', 'T0d8uvpXq9I'], '2023-07-30': ['bIAgVjk7wkA', 'DiV0sSjM12A', 'F6ql3Aw53js', 'f_W_l4hmodA'], '2023-07-31': ['AQEc4BwX6dk', 'UiUBPysceNY', '5rOqzd3KC5o'], '2023-08-01': ['_Hs5RhHZ9ms', '2xg_luaPSnQ', 'IUffiaUue-U', 'qs-Kvkds1ks', 'PEI3tn_0Smg'], '2023-08-02': ['nCMpesZUIWA', 'tVNQNFwIa6I', 'Nc2p7FZBnDU', 'zNfc-q_BF-8', 'WQEiXWuDrhs', '6QpLsw4ki00'], '2023-08-03': ['AponoBIY3BU', 'VHlYqwNM7k8', '3hVZ7tBOn08', 'xOHejhEwMDY'], '2023-08-04': ['I-_LHvTeVy4', 'PaTUh_adayw', '3ihp0OpjD04'], '2023-08-05': ['0ZfJUjtEeG8', '5X6CNliwiAM', 'OdzSxyowu7s', 'CiwlhIiZtxc', 'xrsqaB3kwp0', '0GS_pfG-yaE'], '2023-08-06': ['nuaxkTOSPX8', 'bSnegiL8mF8', 'rIKSCTMIoss', 'z0vOhkzefCE'], '2023-08-07': ['mZ-9dul2wak', 'CO0YM4m5-hc', 'BkqrQQF-0_8', '7aWRK7i1aH8', 'GgMNrnJ5tcI', 'NIKwvL4b0uE', 'b2HqYOYTCgE', 'tXqApqaK_8Y'], '2023-08-08': ['kfSSwxS9aOs', 'C-Bp3_4VjMQ', 'nhb4lCCKKjk', 'k2kXTRaLQbs', 'qXEqLWgg9UY', 'MKrJVADW7T4']}