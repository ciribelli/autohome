# This Motor IA file is responsible to the real time classification of air conditioning system behavior #
import sqlite3
import os
import pandas as pd
import joblib
import time
import django
import datetime
dir_path = os.path.dirname(os.path.realpath(__file__))
os.environ['DJANGO_SETTINGS_MODULE'] = 'home.settings'
django.setup()
from controleambiente.models import Local, Ambiente, ArcondState


def load_sql(sql_path):
    con = sqlite3.connect(sql_path)
    db_env_output = pd.read_sql_query("SELECT * from controleambiente_ambiente", con) # connect to temp and humid table
    db_local = pd.read_sql_query("SELECT * from controleambiente_local", con)         # connect to locals available
    con.close()
    return db_env_output, db_local

def raise_math(local, env_conditions, win_s, win_m, win_l):
    df = env_conditions[env_conditions.local_id == local]
    df = df[-win_l:]
    # Calculation parameters for classification
    temp_series = df['temperatura']
    s_arcon = temp_series.rolling(win_s).std()[-1:] # desvio padrao
    v_arcon = temp_series.rolling(win_s).var()[-1:] # variancia
    min_arc = temp_series.rolling(win_m).min()[-1:]
    max_arc = temp_series.rolling(win_m).max()[-1:]
    a_arcon = max_arc - min_arc # amplitude
    r_arcon = temp_series.rolling(win_l).mean()[-1:] # real media
    temp_vr = temp_series[-1:]
    n_df_tPredict = pd.DataFrame({'desvio padrao': s_arcon, 'variancia': v_arcon, 'amplitude': a_arcon, 'media real': r_arcon, 'temperatura': temp_vr})
    return n_df_tPredict

dir_path = os.path.dirname(os.path.realpath(__file__))
sql_path = dir_path + "/db.sqlite3"
# Definition of time ranges:
timeRange1 = 12
timeRange2 = 20

def main(): 
    while(1):
        # Retrives locals and environments registers from db
        env_conditions, locals = load_sql(sql_path)
        # Defines the windows to screening data
        svm_model = joblib.load(dir_path + '/svm_model.pkl')
        win_s, win_m, win_l = 12, 20, 60
        result = [(i, svm_model.predict(raise_math(i, env_conditions, win_s, win_m, win_l))) for i in locals['id']]
        print (result)
        now = datetime.datetime.now() # adding time information
        print (now)
        res0 = ArcondState(local = Local.objects.get(pk=result[0][0]), onoff = result[0][1], data = now)
        res1 = ArcondState(local = Local.objects.get(pk=result[1][0]), onoff = result[1][1], data = now)
        res0.save()
        res1.save()
        time.sleep(60)
main()
