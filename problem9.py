class Cache:
    def get(self, key):
        print(f"Cache: Getting data for key '{key}'")


class DB:
    def fetch(self, table):
        print(f"DB: Fetching data from table '{table}'")


class API:
    def call(self):
        print("API: Calling external API")


class DataFacade:
    def __init__(self):
        self.cache = Cache()
        self.db = DB()
        self.api = API()

    def get_all_data(self):
        cache_data = self.cache.get("user")
        db_data = self.db.fetch("users")
        api_data = self.api.call()
        return {"cache": cache_data, "db": db_data, "api": api_data}

    def get_cache(self):
        return self.cache

    def get_db(self):
        return self.db

    def get_api(self):
        return self.api


facade = DataFacade()


facade.get_all_data()
facade.get_cache().get("settings")
facade.get_db().fetch("logs")
facade.get_api().call()
