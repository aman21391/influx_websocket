# Python Test Task

## Basic skills

 - Install InfluxDb 1.8.x
 
 - Setup with custom username/password

 - Check out Binance Spot API https://binance-docs.github.io/apidocs/spot/en/
 
## Python skills

### Write a service to save Exchange data to InfluxDb

 - You should not use Binance libraries -- solution should use general libraries 
 and schemas that could be used for various exchanges. 
 
 - You should get "All Book Tickers Stream" using websocket connection
 
    - Pay attention to https://binance-docs.github.io/apidocs/spot/en/#websocket-market-streams
 
 - Write all data to InluxDb that you setup previously
 
 - Separate data with "tag" 
 
 - With code design pay attention to:
 
   - Stability (uptime 0.999+)
   
   - No settings hardcoding
   
   - Logs, but not too much
   
   - Do not overcomplicate
