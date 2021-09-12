# trading_stoploss_and_takeprofit

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

trading_stoploss_and_takeprofit is a python program that calculate stop loss and take profit


## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

First, you need to create a conda virtual environment together with python version 3.9.5 and at the same time install the dependencies in the requirements.txt file.

### Windows CMD Terminal
```
conda create --name TypeYourVirtualEnvironmentHere python=3.9.5 --file requirements.txt

```
Next, activate the virtual environment that you just created now. In the windows terminal, type the following commands.

### Windows CMD Terminal
```
conda activate TypeYourVirtualEnvironmentHere

```
### Installing

Next, after you have created a conda virtual environment with python version 3.9.5 together with the dependencies in the requirements.txt, you need to pip install sqlconnection (the "Module"). In the windows terminal, type the following codes below.

### Windows CMD Terminal
```
pip install version pip install git+https://github.com/Iankfc/trading_stoploss_and_takeprofit.git@master
```

To use the module in a pythone terminal, import the module just like other python modules such as pandas or numpy.

### Python Terminal
```
import trading_stoploss_and_takeprofit as st 
from asset_price_etl import etl_fx_histadata_001 as etl

df_data = etl._function_extract(_str_valuedate_start = '1/1/2018',
                                _str_valuedate_end = '12/7/2019',
                                _str_resample_frequency = 'D')

dict_nparray_takeprofit_and_stoploss  = st.func_dict_nparray_extract(  df_data = df_data,
                                                                        str_period_sampling = '5D',
                                                                        str_column_open_column_name = 'Open',
                                                                        str_column_high_column_name = 'High',
                                                                        str_column_low_column_name = 'Low',
                                                                        str_column_close_column_name = 'Close',
                                                                        str_rolling_sampling_period ='30D',
                                                                        float_volatility_high_to_low_quantile = 0.80,
                                                                        int_takeprofit_multiplier = 3)

df_data['StopLossRate'] = dict_nparray_takeprofit_and_stoploss['StopLossRate']
df_data['TakeProfitRate'] = dict_nparray_takeprofit_and_stoploss['TakeProfitRate']

```


## Usage <a name = "usage"></a>

The module can be use to for extract transform and load (ETL) flow of data science.
