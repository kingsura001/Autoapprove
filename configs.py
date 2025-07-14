# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27940539"))
    API_HASH = getenv("API_HASH", "2390dfdb25011dd1dac1de83cd68946b")
    BOT_TOKEN = getenv("BOT_TOKEN", "8196124006:AAFT6cYvREZxyv81S4SRFOGA6zXzwM4Xhpw")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002549323332")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "6954573092").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Kingsura001:kingsura875744@clusterbot.rj0n2ys.mongodb.net/?retryWrites=true&w=majority&appName=Clusterbot")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
