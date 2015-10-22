#!/usr/bin/env python
import redis, argparse, sys

def consume_and_feed(config):
    con = redis.StrictRedis(config.host, port=6379, db=0)
    command = getattr(con,config.store_command)
    key = config.redis_key
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        command(key,line)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='redisfeeder. Read lines from stdin and send them to redis.')
    parser.add_argument('host',help='redis host')
    parser.add_argument('store_command',help='redis command to store the line')
    parser.add_argument('redis_key',help='key to store the line into')
    config = parser.parse_args()
    consume_and_feed(config)
        
    
