import json
from apscheduler.schedulers.blocking import BlockingScheduler
import os

def read_json():
    with open('/home/ubuntu/project/json/apg_visualizer.json') as f:
      data = json.load(f)
    
    # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
    print(data)
    output={}
    res={}
    res['error']=False
    for element in data:  # iterate on each element of the list
        # element is a dict
        id = element['renderstatus']  # get the id
        print(id)
        if 'ready' in id:
            res['error']=True
            break
    if res['error']==False:
        for element in data:
            output_filename=element['output']
            email=element['email']
            output['output']=output_filename
            output['email']=email
            print(output)
            with open("test.txt", "a") as myfile:
                myfile.write(json.dumps(output)+ "\n")
        create_new_json()
def create_new_json():
    #f = open("/home/ubuntu/project/json/campaign_id", "r")
    ##print(f.readline())
    #id = f.readline()
    #print(id)
    #id=str(id)
    #print(id)
    #path="/home/ubuntu/project/json"
    #name="campaign_000000{}'.json'".format(id)
    ##print(name)
    #for root, dirs, files in os.walk(path):
    #    if name in files:
    #        a= os.path.join(root, name)
    #        #print(a)
    for i in range(1, 1001):
        file_name="campaign_000000{0}.json".format(i)
        if os.path.isfile(file_name):
            print("Success!")
            print(file_name)
            with open("/home/ubuntu/project/json/{}".format(file_name)) as f:
                with open("/home/ubuntu/project/json/apg_visualizer.json", "w") as f1:
                    for line in f:
                        f1.write(line)
                        print(line)
            os.remove("/home/ubuntu/project/json/{}".format(file_name))
            print("File {} Removed!".format(file_name))
            break
    else:
        print("Failure!")
scheduler = BlockingScheduler()
scheduler.add_job(read_json, 'interval', seconds=10)
scheduler.start()
