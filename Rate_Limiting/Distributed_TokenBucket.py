import redis
import time

# Connect to Redis
r = redis.Redis(host='localhost', port=6379)

TOKEN_BUCKET_SCRIPT = """
-- KEYS[1]: user bucket key
-- ARGV[1]: capacity
-- ARGV[2]: refill_rate (tokens/sec)
-- ARGV[3]: now (timestamp)
-- ARGV[4]: cost (usually 1) (tokens_needed)
--H = hash and M = Multi
local bucket = redis.call('HMGET',KEYS[1], 'tokens', 'last_refill')
--first item in bucket('tokens')
local tokens = tonmber(bucket[1]) or ARGV[1]
--second Item in bucket('last_refill')
local last_refill =tonmber(bucket[2]) or ARGV[3]

local delta = ARGV[3] - last_refill
tokens = math.min(ARGV[1], tokens + delta * ARGV[2])

if tokens >= ARGV[4] then
    token = token - ARGV[4]
    redis.call('HMSET',KEYS[1],'tokens',tokens,'last_refill',ARGV[3])
    redis.call('EXPIRE',KEYS[1],60)
    return 1 --True or allowed
esle
    redis.call('HMSET',key[1],'tokens',tokens,'last_refill',ARGV[3])
    return 0
end 
"""

# Compile once so you can reuse
bucket_script = r.register_script(TOKEN_BUCKET_SCRIPT)

class RedisRateLimiter:
    def __init__(self, redis_client, capacity, refill_rate):
        self.r = redis_client
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.script = bucket_script

    def allow_request(self, client_id: str) -> bool:
        now = time.time()
        result = self.script(
            keys=[f"rate_limit:{client_id}"],
            args=[self.capacity, self.refill_rate, now, 1]
        )
        return result == 1