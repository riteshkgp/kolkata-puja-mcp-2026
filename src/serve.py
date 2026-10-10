   import os
   from server import mcp

   if __name__ == "__main__":
       mcp.run(
           "streamable-http",
           host="0.0.0.0",
           port=int(os.environ.get("PORT", "10000")),
           stateless_http=True,
       )
