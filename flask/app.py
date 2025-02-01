from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import pandas as pd

from neo4j import GraphDatabase
import json
import networkx as nx

# *************************************************************
# Authorization variables. Change as needed
# *************************************************************
URI = "bolt://localhost:7687"
AUTH = ("neo4j", "123123123")

# *************************************************************
# Setup flask
# *************************************************************
app = Flask(__name__)
CORS(app)
api = Api(app)


app.config['CORS_HEADERS'] = 'Content-Type'
 
# Require a parser to parse our POST request.
parser = reqparse.RequestParser()
parser.add_argument("attr_a")
parser.add_argument("attr_b")
parser.add_argument("attr_filter")

  
# *************************************************************
# Working Axios request
# *************************************************************
		
class RM_small(Resource):
  # def load_data(path = "./src/data/CommV4.csv"):
  def load_data(path = "./src/data/weekV4.csv"):
    df = pd.read_csv(path)
    return df

  def load_hash():
    # Hashed id's for subject who completed study
    hashed = pd.read_csv("./src/data/Hashed.csv")
    hashed_lst = list(hashed['hashedNumber'])
    hashed_str = [str(x) for x in hashed]
    return hashed, hashed_lst, hashed_str
  
  def event_graph(df, hashed_lst):
    # add edges
    G = nx.from_pandas_edgelist(df[df['hashNum'].isin(hashed_lst)], source='startname', target='endname', edge_attr=True)
    #  attribute columns
    col_names = ['date', 'description', 'direction', 'contact', 'duration', 'event', 'order_f', 'order_l', 'order_o', 'order_a', 'bin_duration', 'working_hours', 'hour', 'day']
    # add nodes
    G.add_nodes_from((d.startname, dict(d[col_names], case=d.Subject_Id)) for n, d in df.iterrows())
    return G

  
  def load_event_graph(df, hashed_lst):
    G = RM_small.event_graph(df, hashed_lst)

    return json.dumps(nx.node_link_data(G))
  
  def load_filtered_event_graph(df, hashed_lst, filter):
    seq_attr = RM_small.load_data("./src/data/sequence_attributeV3.csv")
    seq_attr.loc[-1] = 'TBR'
    seq_attr.loc[-1,'id'] = 107  # 107 part of unfiltered arc, not shown when filtering.
    seq_attr = seq_attr.fillna('TBR') # To Be Replaced
    
    for l in filter:
      if len(l)==0:
        pass
      else:
        seq_attr = seq_attr[seq_attr[l[0]].isin(l[1])]
    selection = list(seq_attr.id)
    event_node_names = list(df[df['Subject_Id'].isin(selection)]['startname']) + list(df[df['hashNum'].isin(selection)]['endname'])

    df = df[df['Subject_Id'].isin(selection)]

    G = RM_small.event_graph(df, hashed_lst)

    # G = nx.from_pandas_edgelist(df[df['hashNum'].isin(hashed_lst)], source='startname', target='endname', edge_attr=True)
    # # add nodes
    # G.add_nodes_from((d.startname, dict(d[['date', 'description', 'direction', 'contact', 'duration', 'event', 'order_f', 'order_l', 'order_o', 'order_a', 'bin_duration', 'working_hours']], case=d.Subject_Id)) for n, d in df.iterrows())
    
    
    G = G.subgraph(event_node_names) 


    return json.dumps(nx.node_link_data(G))
  
  def load_event_graph_aggr(df, hashed_lst):
    # sample 
    # df = df.sample(10)
    # add edges
    df['Subject_Id_str'] = df['Subject_Id_str'].astype("Int64").astype("string")
    #df['hashNum_str'] = df['hashNum_str'].astype("Int64").astype("string")
    G = nx.from_pandas_edgelist(df[df['hashNum'].isin(hashed_lst)], source='Subject_Id_str', target='hashNum_str', edge_attr=True)
    # add nodes
    # G.add_nodes_from((d.startname, dict(d[['date', 'description', 'direction', 'contact', 'duration', 'event']], case=d.Subject_Id_str, source=True)) for n, d in df.iterrows())
    # G.add_nodes_from((d.endname, dict(d[['date', 'description', 'duration', 'event']], case=d.hashNum, source=False)) for n, d in df[df['hashNum'].isin(hashed_lst)].iterrows())
    return json.dumps(nx.node_link_data(G))
    
  def process_graph(graph, hashed, label):
    # dictionary for column names.
    na2name = {'NaN':0, 'NaN.1':1, 'NaN.2':2, 'NaN.3':3, 'NaN.4':4, 'NaN.5':5, 'NaN.6':6, 'NaN.7':7,
       'NaN.8':8, 'NaN.9':9, 'NaN.10':10, 'NaN.11':11, 'NaN.12':12, 'NaN.13':13, 'NaN.14':14,
       'NaN.15':15, 'NaN.16':16, 'NaN.17':17, 'NaN.18':18, 'NaN.19':19, 'NaN.20':20, 'NaN.21':21,
       'NaN.22':22, 'NaN.23':23, 'NaN.24':24, 'NaN.25':25, 'NaN.26':26, 'NaN.27':27, 'NaN.28':28,
       'NaN.29':29, 'NaN.30':30, 'NaN.31':31, 'NaN.32':32, 'NaN.33':33, 'NaN.34':34, 'NaN.35':35,
       'NaN.36':36, 'NaN.37':37, 'NaN.38':38, 'NaN.39':39, 'NaN.40':40, 'NaN.41':41, 'NaN.42':42,
       'NaN.43':43, 'NaN.44':44, 'NaN.45':45, 'NaN.46':46, 'NaN.47':47, 'NaN.48':48, 'NaN.49':49,
       'NaN.50':50, 'NaN.51':51, 'NaN.52':52, 'NaN.53':53, 'NaN.54':54, 'NaN.55':55, 'NaN.56':56,
       'NaN.57':57, 'NaN.58':58, 'NaN.59':59, 'NaN.60':60, 'NaN.61':61, 'NaN.62':62, 'NaN.63':63,
       'NaN.64':64, 'NaN.65':65, 'NaN.66':66, 'NaN.67':67, 'NaN.68':68, 'NaN.69':69, 'NaN.70':70,
       'NaN.71':71, 'NaN.72':72, 'NaN.73':73, 'NaN.74':74, 'NaN.75':75, 'NaN.76':76, 'NaN.77':77,
       'NaN.78':78, 'NaN.79':79, 'NaN.80':80, 'NaN.81':81, 'NaN.82':82, 'NaN.83':83, 'NaN.84':84,
       'NaN.85':85, 'NaN.86':86, 'NaN.87':87, 'NaN.88':88, 'NaN.89':89, 'NaN.90':90, 'NaN.91':91,
       'NaN.92':92, 'NaN.93':93}
    # replace index names
    graph.rename(hashed.hashedNumber, inplace=True)
    # replace column names
    graph = graph.fillna(0).astype(int).rename(na2name, axis=1)
    graph.rename(hashed.hashedNumber, axis=1, inplace=True)
    # create graph from df
    graph = nx.from_pandas_adjacency(graph, create_using=nx.MultiDiGraph)
    # set edge attributes
    nx.set_edge_attributes(graph, values=label, name='kind')
    #return graph
    return graph

  def load_seq_graph(hashed, b_seq_rel):

    seq_attr = RM_small.load_data("./src/data/sequence_attributeV3.csv")
    seq_attr = seq_attr.fillna('TBR') # To Be Replaced
    attr = dict(zip(seq_attr.id, seq_attr.to_dict(orient='records') ))
    attr = {s: {k: v for k, v in d.items() if v != 'TBR'} for s, d in attr.items()}
     
    if b_seq_rel == "All_Seq":
      n_friends = pd.read_csv("./src/data/network_friends.csv")
      n_lab = pd.read_csv("./src/data/network_lab.csv")
      n_outlab = pd.read_csv("./src/data/network_outlab.csv")
      
      G_friends = RM_small.process_graph(n_friends, hashed, label = 'Friendship')
      G_lab = RM_small.process_graph(n_lab, hashed, label = 'Lab')
      G_outlab = RM_small.process_graph(n_outlab, hashed, label = 'Outlab')

      G_friends.update(edges=G_lab)
      G_friends.update(edges=G_outlab)
      nx.set_node_attributes(G_friends, attr)
      return json.dumps(nx.node_link_data(G_friends))
  
    elif b_seq_rel == "Friendship":
      n_graph = pd.read_csv("./src/data/network_friends.csv")
    elif b_seq_rel == "Lab":
      n_graph = pd.read_csv("./src/data/network_lab.csv")
    elif b_seq_rel == "Outlab":
      n_graph = pd.read_csv("./src/data/network_outlab.csv")

    G = RM_small.process_graph(n_graph, hashed, label = b_seq_rel)
    nx.set_node_attributes(G, attr)
    return json.dumps(nx.node_link_data(G))
  
  def load_filtered_seq_graph(hashed, b_seq_rel, filter=[[]]):

    seq_attr = RM_small.load_data("./src/data/sequence_attributeV3.csv")
    seq_attr = seq_attr.fillna('TBR') # To Be Replaced

    for l in filter:
      if len(l)==0:
        pass
      else:
        seq_attr = seq_attr[seq_attr[l[0]].isin(l[1])]
    selection = list(seq_attr.id)
    selection.append(107)

    attr = dict(zip(seq_attr.id, seq_attr.to_dict(orient='records') ))
    attr = {s: {k: v for k, v in d.items() if v != 'TBR'} for s, d in attr.items()}
     
    if b_seq_rel == "All_Seq":
      n_friends = pd.read_csv("./src/data/network_friends.csv")
      n_lab = pd.read_csv("./src/data/network_lab.csv")
      n_outlab = pd.read_csv("./src/data/network_outlab.csv")
      
      G_friends = RM_small.process_graph(n_friends, hashed, label = 'Friendship')
      G_lab = RM_small.process_graph(n_lab, hashed, label = 'Lab')
      G_outlab = RM_small.process_graph(n_outlab, hashed, label = 'Outlab')

      G_friends.update(edges=G_lab)
      G_friends.update(edges=G_outlab)
      G_friends = G_friends.subgraph(selection)
      nx.set_node_attributes(G_friends, attr)
      return json.dumps(nx.node_link_data(G_friends))
  
    elif b_seq_rel == "Friendship":
      n_graph = pd.read_csv("./src/data/network_friends.csv")
    elif b_seq_rel == "Lab":
      n_graph = pd.read_csv("./src/data/network_lab.csv")
    elif b_seq_rel == "Outlab":
      n_graph = pd.read_csv("./src/data/network_outlab.csv")

    G = RM_small.process_graph(n_graph, hashed, label = b_seq_rel)
    G = G.subgraph(selection)
    nx.set_node_attributes(G, attr)
    return json.dumps(nx.node_link_data(G))
  
  def add_rows(df):
    "performs inplace"
    df.sort_index(inplace=True, ascending=False, ignore_index=True)
    rows = df.index
    cols = df.columns
    for row in rows:
        df[row] = 0
    for col in cols:
        # df.loc[col]=0
        df.loc[-1]=0
        df.index = df.index + 1  # shifting index
        df.sort_index(inplace=True) 
    return df

  def prepare_matrix(df):
    df = df.replace(-1, 0)
    df['contact'] = df['contact'].where(df['contact']<1, 1) # if condition is false return second statement (1)
    df['duration'] = df['duration'].replace('[]', 0).astype('float')
    df['duration'] = df['duration'].where(df['duration']<1, 1)
    df['description'] = df['description'].replace({'Voice call': 1, 'Short message': 1, 'Packet Data':1})
    df['direction'] = df['direction'].replace({'Missed': 1, 'Incoming': 1, 'Outgoing':1})
    return df
  
  def matrixify(matrix_df, attr_b):
    # matrix_df = matrix_df.sample(10)
    matrix_df = matrix_df[matrix_df['Subject_Id']==attr_b][["contact", "description", "direction", "duration"]]
    df_nodes = RM_small.add_rows(matrix_df)
    df_edges = RM_small.prepare_matrix(matrix_df)
    matrix_list = [df_nodes.to_numpy().transpose().tolist(), df_edges.to_numpy().transpose().tolist() ]
    return json.dumps(matrix_list)
  
  def matrixify_all(matrix_df):
    # matrix_df = matrix_df.sample(10)
    matrix_df = matrix_df[["contact", "description", "direction", "duration"]]
    df_nodes = RM_small.add_rows(matrix_df)
    df_edges = RM_small.prepare_matrix(matrix_df)
    matrix_list = [df_nodes.to_numpy().transpose().tolist(), df_edges.to_numpy().transpose().tolist() ]
    return json.dumps(matrix_list)

  def post(self):
    args = parser.parse_args()
    print('args', args)
    attribute_a = args["attr_a"] # at the moment equal to string 'all'  
    attribute_b = args["attr_b"] 
    attribute_filter = args["attr_filter"]
    result = 'failed to receive one or more arguments'
    
    hashed, hashed_lst, hashed_str = RM_small.load_hash()

    if (attribute_a == 'event'):
      df = RM_small.load_data()
      print(len(df))
      result = RM_small.load_event_graph(df, hashed_lst)
    elif (attribute_a in ['Seq', 'Friendship', 'Lab', "Outlab", "All_Seq"]):
      result = RM_small.load_seq_graph(hashed, attribute_a)
    elif (attribute_a == 'aggr'):
      df = RM_small.load_data()
      result = RM_small.load_event_graph_aggr(df, hashed_lst)
    elif (attribute_a == 'time'):
      df = RM_small.load_data()
      result = df.to_json(orient='records')
    elif (attribute_a == 'singles'):
      df = RM_small.load_data("./src/data/sequence_attributeV3.csv")
      df = df.drop(columns=['order_o', 'order_l', 'order_f', 'my_mac', 'mac', 'my_hashedNumber' ])
      result = df.to_json(orient='records')
    elif (attribute_a == 'chords'):
      df = RM_small.load_data("./src/data/weekV2.csv")
      if (attribute_b == 'all'):
        result = RM_small.matrixify_all(df)
      else:
        result = RM_small.matrixify(df, int(attribute_b))
    elif (attribute_a == "filter"):
      f = json.loads(attribute_filter)
      if (attribute_b) == 'event': # load event graph (unfiltered for now)
        df = RM_small.load_data()
        result = RM_small.load_filtered_event_graph(df, hashed_lst, f)
        
      else: # sequence graph
        result = RM_small.load_filtered_seq_graph(hashed, attribute_b, f)

    return {"answer": result}

  

### changes here ###
@app.route("/test")
def hello_world():
    return "<p>Hello, World!</p>"

### changes here ###  
api.add_resource(RM_small, "/RM_small")

if __name__ == "__main__":
  app.run(debug=True)
  

