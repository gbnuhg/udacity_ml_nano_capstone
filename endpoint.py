import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://3a51d690-8529-43c6-bdfd-4ae7ec2d19c1.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'bidYWKcZvZq3r3piukoLRnsXW2h0sILk'

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            'age' : 75,
            'anaemia' :0,
            'creatinine_phosphokinase' :582,
            'diabetes' :0,
            'ejection_fraction' :20,
            'high_blood_pressure' :1,
            'platelets' :265000,
            'serum_creatinine' :1.9,
            'serum_sodium' :130,
            'sex' :1,
            'smoking' :0,
            'time' :4
          },
          {
            'age' :55,
            'anaemia' :0,
            'creatinine_phosphokinase' :7861,
            'diabetes' :0,
            'ejection_fraction' :38,
            'high_blood_pressure' :0,
            'platelets' :263385.03,
            'serum_creatinine' :1.1,
            'serum_sodium' :136,
            'sex' :1,
            'smoking' :0,
            'time' :6
          }
        ]
      }

# data = {"data":
#         [
#           {
#             "age": 17,
#             "campaign": 1,
#             "cons.conf.idx": -46.2,
#             "cons.price.idx": 92.893,
#             "contact": "cellular",
#             "day_of_week": "mon",
#             "default": "no",
#             "duration": 971,
#             "education": "university.degree",
#             "emp.var.rate": -1.8,
#             "euribor3m": 1.299,
#             "housing": "yes",
#             "job": "blue-collar",
#             "loan": "yes",
#             "marital": "married",
#             "month": "may",
#             "nr.employed": 5099.1,
#             "pdays": 999,
#             "poutcome": "failure",
#             "previous": 1
#           },
#           {
#             "age": 87,
#             "campaign": 1,
#             "cons.conf.idx": -46.2,
#             "cons.price.idx": 92.893,
#             "contact": "cellular",
#             "day_of_week": "mon",
#             "default": "no",
#             "duration": 471,
#             "education": "university.degree",
#             "emp.var.rate": -1.8,
#             "euribor3m": 1.299,
#             "housing": "yes",
#             "job": "blue-collar",
#             "loan": "yes",
#             "marital": "married",
#             "month": "may",
#             "nr.employed": 5099.1,
#             "pdays": 999,
#             "poutcome": "failure",
#             "previous": 1
#           },
#       ]
#     }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


