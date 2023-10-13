#!/usr/bin/env python3
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.exceptions import APIException
from recombee_api_client.api_requests import *
import csv
import random
private_token = "U5y6vlgvS6iRIbqE7SpwQ7KMBujtbJ56V4l4MOzCqYCY0pkk4bZLwJCtmAIRhCWs"
client = RecombeeClient('upbss-dev',private_token,region=Region.EU_WEST)

#add properties
client.send(AddItemProperty('Domain Code','string'));
client.send(AddItemProperty("Domain","string"));
client.send(AddItemProperty("Item","string"));
client.send(AddItemProperty("Description","string"));

with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            # add ids 
            # print(row[2])
            client.send(AddItem(row[2]))
            #add values 
            client.send(SetItemValues(row[2],
            {
              'Domain Code' : row[0], 
              'Domain': row[1], 
              'Description': row[3]
            }))
            line_count += 1

#add user, add user-item interactions 
for user_id in range(5):
  client.send(AddUser(user_id))
  client.send(AddPurchase(user_id, random.randint(400,3000)));


#recommend items to user 
client.send(RecommendItemsToUser(1, 4));
client.send(RecommendItemsToUser(2, 3));