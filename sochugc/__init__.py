import re

from typing import Dict, List, Union

import requests
from ksamsok import KSamsok

class UGC:
    def __init__(self, key: str, endpoint: str = 'http://ugc.kulturarvsdata.se/') -> None:
        self.endpoint = endpoint + 'UGC-hub/'
        self.key = key

        self.headers = {
            'User-Agent': 'SOCH-UGC.py'
        }

        self.soch = KSamsok()

        self.relation_types = list([
            'sameAs',
            'isDescribedBy',
            'visualizes',
            'hasPart',
            'isPartOf',
            'isVisualizedBy',
            'isContainedIn',
            'author',
            'authorOf',
            'hasBeenUsedIn',
            'isRelatedTo',
            'architectOf',
            'architect',
            'user',
            'userOf',
            'child',
            'mother',
            'father',
            'photographerOf',
            'photographer',
            'isMentionedBy',
            'mentions'
        ])

        # so that the user get endpoint/key errors early
        self.get_total_items_count()

    def get_total_items_count(self) -> str:
        url = '{}api?x-api={}&method=retrieve&scope=count&objectUri=all&format=json'.format(self.endpoint, self.key)
        data = self.make_get_request(url)

        return data['response']['relations']['numberOfRelations']

    def get_item(self, item_id: Union[int, str]) -> Union[Dict, bool]:
        url = '{}api?x-api={}&method=retrieve&objectUri=all&contentId={}&scope=single&format=json'.format(self.endpoint, self.key, item_id)
        data = self.make_get_request(url)

        if data['response']['relations'][0]['id'] is 0:
            return False

        return data['response']['relations'][0]

    def search_items(self, uri: str = 'all', offset: int = 0, limit: int = 50) -> List:
        url = '{}api?x-api={}&method=retrieve&scope=all&objectUri={}&selectFrom={}&maxCount={}&format=json'.format(self.endpoint, self.key, uri, offset, limit)
        data = self.make_get_request(url)

        return data['response']['relations']

    def delete_item(self, item_id: Union[int, str]) -> bool:
        url = '{}api?x-api={}&method=delete&objectId={}&format=json'.format(self.endpoint, self.key, item_id)
        data = self.make_get_request(url)

        if data['response']['result'] == 'SUCCESS':
            return True
        return False

    def create_item_relation(self, kulturarvsdata_uri: str, relation: str, target: str, user: str) -> bool:
        kulturarvsdata_uri = self.soch.formatUri(kulturarvsdata_uri, 'rawurl')
        if not kulturarvsdata_uri:
            raise ValueError('{} is not an valid Kulturarvsdata URI.'.format(kulturarvsdata_uri))

        if relation not in self.relation_types:
            raise ValueError('{} is not a valid relation type.'.format(relation))

        if not self.valid_relation_target(target):
            raise ValueError('{} is not a valid target.'.format(target))

        url = '{}api?x-api={}&method=insert&scope=relationAll&objectUri={}&user={}&relationType={}&relatedTo={}&format=json'.format(self.endpoint, self.key, kulturarvsdata_uri, user, relation, target)
        data = self.make_get_request(url)

        if data['response']['result'] == 'SUCCESS':
            return True
        return False

    def valid_relation_target(self, target: str) -> bool:
        if target.startswith('http://kulturarvsdata.se/'):
            if not self.soch.formatUri(target, 'rawurl'):
                return False
            return True

        if target.startswith('https://commons.wikimedia.org/wiki/File:'):
            return True

        if target.startswith('https://commons.wikimedia.org/wiki/Category:'):
            return True

        if target.startswith('http://www.wikidata.org/entity/Q'):
            return True

        if target.startswith('http://data.europeana.eu/item/'):
            return True

        if re.match(r'^https:\/\/libris\.kb\.se\/.{14,17}$', target):
            return True

        if re.match(r'^https:\/\/\w{2}\.wikipedia\.org\/wiki\/.+', target):
            return True

        return False

    def make_get_request(self, url: str) -> Dict:
        r = requests.get(url, headers = self.headers)

        # note UGC always returns 200 codes for now.
        if r.status_code is not 200:
            raise ValueError('Could not access endpoint.')

        data = r.json()
        if 'error' in data['response']:
            raise ValueError('Bad API key.')

        return data
