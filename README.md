# SOCH UGC

SOCH UGC is a Python library for accessing and writing data to the [User Generated Content API](https://ugc.kulturarvsdata.se/UGC-hub/) that is a part of the Swedish Open Cultural Heritage (SOCH/K-Samsök) API.

## Install SOCH UGC

```bash
pip install sochugc
```

## Usage Examples

```python
from sochugc import UGC

# the endpoint defaults to https://ugc.kulturarvsdata.se/
# the key parameter is only needed for write actions
ugc = UGC(endpoint='http://localhost:8080/', key='<API-KEY>')

# get the total number of user generated items
ugc.get_total_items_count()

# return an user generated content item by its id
ugc.get_item(679)

# Searching all items or items tied to a specific URI
# to search all items and not only ones connected to a specific URI omit the uri parameter
ugc.search_items(uri='http://kulturarvsdata.se/raa/bbr/21400000440954', offset=0, limit=100)

# deleting an item using its id
ugc.delete_item(679)

# creating a new relation, see below for possible relations
ugc.create_item_relation('http://kulturarvsdata.se/raa/kmb/16001000004075', 'isPartOf', 'http://kulturarvsdata.se/pm/photo/POST036605', 'Albin Larsson')
```

## Supported Item Relations

 - sameAs
 - isDescribedBy
 - visualizes
 - hasPart
 - isPartOf
 - isVisualizedBy
 - isContainedIn
 - author
 - authorOf
 - hasBeenUsedIn
 - isRelatedTo
 - architectOf
 - architect
 - user
 - userOf
 - child
 - mother
 - father
 - photographerOf
 - photographer
 - isMentionedBy
 - mentions
