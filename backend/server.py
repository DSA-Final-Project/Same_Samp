from flask import Flask, jsonify, request 
from flask_cors import CORS
from Vertex import Vertex
from GraphBuild import GraphBuild
from os import listdir
import csv
import json
import copy

#this part is horribly designed please don't judge D: 

a_new_day_graph = GraphBuild()
amen_graph = GraphBuild()
ashley_graph = GraphBuild()
bring_the_noise_graph = GraphBuild()
changed_the_beat_graph = GraphBuild()
funk_drummer_graph = GraphBuild()
funk_pres_graph = GraphBuild()
here_we_go_graph = GraphBuild()
hot_pants_graph = GraphBuild()
impeach_the_president_graph = GraphBuild()
kool_is_back_graph = GraphBuild()
la_di_da_graph = GraphBuild()
long_red_graph = GraphBuild()
sing_simple_graph = GraphBuild()
synthetic_graph = GraphBuild()
take_me_mardi_gra_graph = GraphBuild()
the_champ_graph = GraphBuild()
think_about_it_graph = GraphBuild()
ufo_graph = GraphBuild()


with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/a_new_day_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         a_new_day_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/amen_brother_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         amen_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/ashley_roachclip_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         ashley_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/bring_the_noise_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         bring_the_noise_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/changed_the_beat_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         changed_the_beat_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/funk_drummer_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         funk_drummer_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/funky_president_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         funk_pres_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/here_we_go_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         here_we_go_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/hot_pants_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         hot_pants_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/impeach_the_president_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         impeach_the_president_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/kool_is_back_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         kool_is_back_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/la_di_da_di_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         la_di_da_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/long_red_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         long_red_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/sing_a_simple_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         sing_simple_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/synthetic_substitution_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         synthetic_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/take_me_mardi_gra_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         take_me_mardi_gra_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/the_champ_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         the_champ_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/think_about_it_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         think_about_it_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()
with open('C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/CSVs/ufo_spotified.csv', 'r', newline='', encoding='utf-8') as infile:

      reader = csv.reader(infile, quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, skipinitialspace=True)
      
      for row in reader:
         market = []
         for country in csv.reader(row[10], delimiter=','):
            market.append(country)

         ufo_graph.insertVertex(row[1],row[2],row[4],row[5],int(row[6]),int(row[7]),int(row[8]),row[9], market, int(row[11]),int(row[12]),int(row[13]),float(row[14]) )

      infile.close()



def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]


csv_files = find_csv_filenames("C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/SpotifyDataCollector/spotified_csvs")

app = Flask(__name__)
CORS(app)

@app.route("/members")
def members():
  return {"members" : ["member1", "Member2", "Member3"]}


@app.route('/vertex', methods=['POST'])
def post_vertex():
   
   global data 
   global sample
   data = request.get_json()
   

  
   # getting sample name and grabbing associated csv file
   sample =  data['userData'][0]
   

   # creating graph from csv data
  #  inserting userVertex into graph

   return jsonify({"message": "Vertex received and stored."}), 200

  #  inserting userVertex into graph

@app.route('/algorithm', methods=['GET'])
def get_algorithm():
    global graphCopy
    
    def switch(song):
        if song == 'Amen, Brother - The Winstons':
            graphCopy = amen_graph
        elif song == 'Think (About It) - Lyn Collins':
            graphCopy = think_about_it_graph
        elif song == 'Change the Beat (Female Version) - Beside':
            graphCopy = changed_the_beat_graph
        elif song == 'Funky Drummer - James Brown':
            graphCopy = funk_drummer_graph
        elif song == 'La Di Da Di - Doug E. Fresh and Slick Rick':
            graphCopy = la_di_da_graph
        elif song == 'Funky President (People It\'s Bad) - James Brown':
            graphCopy = funk_pres_graph
        elif song == 'Bring the Noise - Public Enemy':
            graphCopy = bring_the_noise_graph
        elif song == 'Synthetic Substitution - Melvin Bliss':
            graphCopy = synthetic_graph
        elif song == 'Here We Go (Live at Funhouse) - Run-DMC':
            graphCopy = here_we_go_graph
        elif song == 'Hot Pants (Bonus Beats) - Bobby Byrd':
            graphCopy = hot_pants_graph
        elif song == 'Long Red - Mountain' :
            graphCopy = long_red_graph
        elif song == 'Impeach the President - The Honey Dripper':
            graphCopy = impeach_the_president_graph
        elif song == 'The Champ - The Mohawks':
            graphCopy = the_champ_graph
        elif song == 'Apache - Incredible Bongo Band':
            graphCopy
        elif song == 'Kool is Back - Funk, Inc':
            graphCopy = kool_is_back_graph
        elif song == 'UFO - ESG':
            graphCopy = ufo_graph
        elif song == 'It\'s a New Day - Skull Snaps':
            graphCopy = a_new_day_graph
        elif song == 'Ashley\'s Roadclip - The Soul Searchers':
            graphCopy = ashley_graph 
        elif song == 'Sing a Simple Song - Sly & the Family Stone':
            graphCopy = sing_simple_graph
        elif song == 'Take Me to the Mardi Gras - Bob James':
            graphCopy  = take_me_mardi_gra_graph

    switch(sample)
    
  # running selected algorithm
    graphCopy.insertVertex("userVertex", "userName", data['userData'][3],  data['userData'][1],  int(data['userData'][2]), 50,  int(data['userData'][5]), data['userData'][6], "US",50000, (50000 * 0.002), 2023 - int(data['userData'][2], (50000 * 0.002))  )
    graphCopy.formulateGraph()

    adjlist = graphCopy.getAdjList()      
    storage = graphCopy.getStorage()

    graph = {
       "songs": []
    }

    for key, value in adjlist.items():
        tempSong = {}
        tempSong["name"] = storage[key].getName()
        tempSong["neighbors"] = []
        for name, weight in adjlist[key]:
          tempSong["neighbors"].append({"name": name,"weight": weight})
        graph["songs"].append(tempSong)
        

    algo =  data['userData'][4]
    if algo== "Dijkstra":
      S, dv, pv = graphCopy.dijkstra("i got your back")
      algoDict = {}

      for val in S:
        counter = 0
        while counter < 15:
          algoDict[val] = (int(dv[val]), pv[val])
          counter += 1

      mainJSON = {
       "graph": graph,
       "algo": algoDict
      }
      json_main_obj = json.dumps(mainJSON)   
    elif algo == "Breadth First Search":
       traversal = graphCopy.BFS("i got your back", 15)
       mainJSON = {
       "graph": graph,
       "algo": traversal
      }
       json_main_obj = json.dumps(mainJSON) 

       

  # creating main JSON and inserting Graph JSON

   #running algo on graph and inserting algo JSON into main JSON package

   # delete global instance of current graph so that it is not stored

   #return main JSON

    # with open("C:/Users/eunoia/Desktop/Coding_Projects/COP3530/SameSampMaster/Same-Samp/backend/testjson/sample.json", "w") as outfile:
    #       outfile.write(json_main_obj)

    return json_main_obj, 200


## two types of requests. One for dijkstras and the other for BFS

# for any new post request first build a new vertex. Then grab the associated csv file
# and build new graph with csv and newly created vertex from user inputs. Build main JSON and build graph JSON representation.
# after making graph, run selected algorithm and package result with main JSON.
# send main JSON to client 



if __name__ == "__main__" :
  app.run(debug=True)
