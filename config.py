from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", "18202635"))
    API_HASH = getenv("API_HASH", "237d1160ac8cd4767cf5b217dda3a5f6")
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    STRING_SESSION = getenv("STRING_SESSION", None)
    SPAMWATCH_API = "JuiT02xWPb_wBJ64F2jErY8RsD2Dif0iYI4QTQzjPdw86q~HlTGkwUh8BhV6~5QD"
    TOKEN = getenv("TOKEN", None)
    OWNER_ID = int(getenv("OWNER_ID", "5477247654"))  # sᴛᴀʀᴛ @Exon_Robot ᴛʏᴘᴇ /id
    OWNER_USERNAME = getenv("OWNER_USERNAME", "Noah_Afk")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "Xd_Bot_Support")
    LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001217847667"))
    MONGO_URI = getenv("MONGO_DB_URI" , "mongodb+srv://sano07:sano07@cluster0.jxywgnn.mongodb.net/?retryWrites=true&w=majority")
    REDIS_URL = "redis://default:0nLBaxJed1LJaNgn9xhL1oyTL49u4B1T@redis-14243.c85.us-east-1-2.ec2.cloud.redislabs.com:14243/matrixx-free-db"
    DATABASE_URL = getenv("DATABASE_URL" , "postgres://ctoixwyr:CThCpbMv1lkdUuN90qeGdZ4VxdjpgTty@snuffleupagus.db.elephantsql.com/ctoixwyr")

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
