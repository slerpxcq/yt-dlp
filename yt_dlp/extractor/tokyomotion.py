from .common import InfoExtractor

from ..utils import (
    ExtractorError,
    determine_ext,
    merge_dicts,
    parse_duration,
    parse_resolution,
    str_to_int,
    url_or_none,
    urlencode_postdata,
    urljoin,
)

class TokyoMotionIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?tokyomotion\.net/user/(?P<id>[0-9]+)'
    _TESTS = [{
        'url': 'https://www.tokyomotion.net/video/4186488/%E4%BE%9D%E9%9F%B3%E3%80%80%E3%82%A2%E3%83%8A%E3%83%AB%E3%82%AC%E3%83%B3%E8%A6%8B%E3%81%9B%E3%82%AF%E3%83%AA%E3%81%97%E3%81%93%E2%91%A0',
        'only_matching': True
        # 'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
        # 'info_dict': {
            # For videos, only the 'id' and 'ext' fields are required to RUN the test:
        #    'id': '42',
        #    'ext': 'mp4',
            # Then if the test run fails, it will output the missing/incorrect fields.
            # Properties can be added as:
            # * A value, e.g.
            #     'title': 'Video title goes here',
            # * MD5 checksum; start the string with 'md5:', e.g.
            #     'description': 'md5:098f6bcd4621d373cade4e832627b4f6',
            # * A regular expression; start the string with 're:', e.g.
            #     'thumbnail': r're:^https?://.*\.jpg$',
            # * A count of elements in a list; start the string with 'count:', e.g.
            #     'tags': 'count:10',
            # * Any Python type, e.g.
            #     'view_count': int,
        }]

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        # TODO more code goes here, for example ...
        title = self._html_search_regex(r'<h1>(.+?)</h1>', webpage, 'title')

        return {
            'id': video_id,
            'title': title,
            'description': self._og_search_description(webpage),
            'uploader': self._search_regex(r'<div[^>]+id="uploader"[^>]*>([^<]+)<', webpage, 'uploader', fatal=False),
            # TODO more properties (see yt_dlp/extractor/common.py)
        }