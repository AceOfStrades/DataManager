"""
Master the exchange of informations from all the sources
Manage the relation between info extracted by Dataminer.py and their storage in Database.py
Manage the agenda of executions
Clean and check up the data info from Dataminer.py
"""

def getData(self, data, source):
    return data;

def storeData(self, data, source):
    print("Data stored in database")

class executions(object):
    return list(objects.time)

def init_config(config_dir:str, config_fp:str, data_dir:str, data_fp:str, colors:dict) -> dict:
    """
    It checks if the config directory and data directory exist, if they don't, it creates them. Then it
    checks if the config file exists, if it doesn't, it creates it. Then it creates the data file. Then
    it reads the config file and returns it
    
    :param config_dir: The directory where the config file is located
    :type config_dir: str
    :param config_fp: The filepath to the config file
    :type config_fp: str
    :param data_dir: The directory where the data file is stored
    :type data_dir: str
    :param data_fp: The filepath to the data file
    :type data_fp: str
    :return: A dict of the config.json file
    """
    res, log, war, spe = colors['res'], colors['log'], colors['war'], colors['spe']

    # Log the config dir, config file, data dir, and data file
    print(f'{log}[LOG]      {res}Config directory: {spe}{config_dir}{res}')
    print(f'{log}[LOG]      {res}Config file:      {spe}{config_fp}{res}')
    print(f'{log}[LOG]      {res}Data directory:   {spe}{data_dir}{res}')
    print(f'{log}[LOG]      {res}Data file:        {spe}{data_fp}{res}')

    # Checks if config dir exists
    if os.path.exists(config_dir):
        print(f'{log}[LOG]      {res}{spe}{config_dir}{res} exists')
    # If it doesnt, creates it
    else:
        print(f'{war}[WARNING]{res}  {spe}{config_dir}{res} does not exist. Creating it')
        os.makedirs(config_dir)

    # Checks if data dir exists
    if os.path.exists(data_dir):
        print(f'{log}[LOG]    {res}  {spe}{data_dir}{res} exists')
    # If it doesnt, creates it
    else:
        print(f'{war}[WARNING]{res}  {spe}{data_dir}{res} does not exist. Creating it')
        os.makedirs(data_dir)
    
    # Checks if config file exists
    if os.path.exists(config_fp):
        print(f'{log}[LOG]    {res}  {spe}{config_fp}{res} exists')
    # If it doesnt, creates an empty config.json
    else:
        print(f'{war}[WARNING]{res}  {spe}{config_fp}{res} does not exist. Creating it')
        with open(config_fp, 'w') as f:
            json.dump({ 'reddit':{'username':''} , 'discord':{'token':''} , 'twitter':{'username':''} }, f, indent=4)
    
    # Checks if data file exists
    if os.path.exists(data_fp):
        print(f'{log}[LOG]    {res}  {spe}{data_fp}{res} exists')
    # If it doesnt, creates an empty data file
    else:
        print(f'{log}[LOG]    {res}  {spe}{data_fp}{res} does not exist. Creating it')
        with open(data_fp, 'w') as f:
            json.dump({}, f)

    # Reads config.json and returns it
    with open(config_fp) as f:
        config = json.load(f)
    
    return config