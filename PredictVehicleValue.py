# Simple Vehicle Value Prediction based on Make year

import cx_Oracle
import pandas as pd

con = cx_Oracle.connect('VCI_DATA_ANALYTICS','VCI_DATA_ANALYTICSpre',cx_Oracle.makedsn('ddmprod.usvci001.vci.na.vwg',1527,'DIM_PREPROD'))

curconn = con.cursor()
curconn.execute("""select veh.vehicle_dim_id, veh.vehicle_id_nbr, veh.MAKE_NM,veh.MODEL_NM,  veh.MODEL_YEAR_NBR,  veh.BLCK_BOOK_RTL_CLN_AMT, veh.MSRP_AMT
from dw_mart.vehicle_dim veh
where veh.close_dt_id = 99991231 
and veh.BLCK_BOOK_RTL_CLN_AMT is not null
and veh.BLCK_BOOK_RTL_CLN_AMT not in (0,-1)
and veh.MSRP_AMT is not null
and veh.MSRP_AMT not in (0,-1)
and veh.MAKE_NM = 'Audi'
and veh.MODEL_NM = 'A3'""")


for result in curconn:
    print(result)	

curconn.close()
con.close()