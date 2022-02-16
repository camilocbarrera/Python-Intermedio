from data_filtering_db import DATA

# all_python_devs = [ worker["name"] for worker in DATA if worker["language"] == "python"  ]
all_python_devs = list(filter(lambda worker: worker["language"].lower()=="python", DATA ))

# all_platzi_workers = [ worker["name"] for worker in DATA if worker["organization"].lower()=="platzi" ]

all_platzi_workers = list(filter(lambda worker: worker["organization"].lower() =="platzi", DATA ))
all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers ))

# adults = list( filter( lambda worker: worker["age"] > 18, DATA ) )

adults = [ w["name"] for w in DATA if w["age"]>18 ]

old_people = list(map(lambda worker: worker | {"old":worker["age"] > 70 },DATA))

old_people = [ worker | {"old":worker["age"] > 70 } for worker in DATA if worker["age"] > 70 ]


for x in old_people:
    print(x["name"]," tiene ", x["age"], " Es viejo ¿? ", x["old"])


# for w in all_platzi_workers:
#     print(w["name"], " Trabaja en: ",w["organization"])


def run():
    pass



if __name__ == '__main__':
    run()
