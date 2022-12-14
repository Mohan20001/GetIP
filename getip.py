import os
from pyngrok import ngrok, conf

conf.get_default().auth_token = "299FED0QV81gQREsrXHLmdey2S2_5saXiXSDzhSgxp6AcWPgf"
url = ngrok.connect(5000, "http")
print(" [+] "+ str(url))
os.system("node server.js")