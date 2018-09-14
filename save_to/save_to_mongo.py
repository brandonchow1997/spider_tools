import pymongo


# 连接本地数据库
# 连接到MongoDB
MONGO_URL = 'localhost'
MONGO_DB = '库名'
MONGO_COLLECTION = '表名'
client = pymongo.MongoClient(MONGO_URL, port=27017)
db = client[MONGO_DB]


def save_to_mongo(data):
    # 保存到MongoDB中
    try:
        if db[MONGO_COLLECTION].insert(data):
            print('存储到 MongoDB 成功')
    except Exception:
        print('存储到 MongoDB 失败')
