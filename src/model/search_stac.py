from pystac_client import Client

class SearchSTAC:
    def __init__(self, stac_url, feature_geojson={}):
        self.stac_url = stac_url
        self.feature_geojson = feature_geojson
        self.client = self.connect_client()

    def connect_client(self):
        return Client.open(self.stac_url)

    def __get_collections(self):
        return self.client.get_collections()

    def __get_collection_info(self, collection):
        return self.client.get_collection(collection)

    def __get_items(self, **kwargs):
        return self.client.search(
            intersects=self.feature_geojson,
            **kwargs
        ).item_collection()

    def get_collections(self):
        return [collection.to_dict() for collection in self.__get_collections()]

    def get_collection_info(self, collection):
        return self.__get_collection_info(collection).to_dict()

    def get_items(self, **kwags):
        return [item.to_dict() for item in self.__get_items(**kwags)]
