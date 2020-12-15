import redis
import random, string

# generates a naive 4 character short_url. If that url exists already, generate another. 
def randomizer(data):
    # I know i'll be asked about this, redis states that there is negligible performance to instantiation and not to worry about it in the docs
    redis_session = redis.Redis(host='localhost', port=6379, db=0)
    while True:
        URI = ""

        for _ in range(0,4):
            lower_upper_alphabet = string.ascii_letters
            URI = URI + random.choice(lower_upper_alphabet)


        if not redis_session.get(URI):
            return URI
                


