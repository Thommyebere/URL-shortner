import database


class URL(object):
    def __init__(self, url):
        pass

    @staticmethod
    def insert_url(url):
        database.create_table()
        return database.make_record(url)

    @staticmethod
    def gets_url(original_id):
        return database.get_record(original_id)


    # @staticmethod
    # def get_ids():
    #     database.get_id()

# xp = URL.gets_url(1)
# print(xp)
