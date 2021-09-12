
#%% import modules

import trading_volatility_measure as tvm

import numpy as np


#%%

def func_dict_nparray_extract(df_data,
                                str_period_sampling = '5D',
                                str_column_open_column_name = 'Open',
                                str_column_high_column_name = 'High',
                                str_column_low_column_name = 'Low',
                                str_column_close_column_name = 'Close',
                                str_rolling_sampling_period ='30D',
                                float_volatility_high_to_low_quantile = 0.80,
                                int_takeprofit_multiplier = 3):

    df_data = df_data.copy()
    dict_pdseries_volatility_parameters = tvm.func_dict_pdseries_generate_high_to_low_volatility_percentile_score( df_data = df_data,
                                                                                                str_period_number = '14D',
                                                                                                str_column_open_column_name = str_column_open_column_name,
                                                                                                str_column_high_column_name = str_column_high_column_name,
                                                                                                str_column_low_column_name = str_column_low_column_name,
                                                                                                str_column_close_column_name = str_column_close_column_name,
                                                                                                bool_plotlychart_create_chart_True_or_False = False,
                                                                                                str_percentile_of_score_sampling_rolling_or_expanding ='rolling', 
                                                                                                str_percentile_of_score_sampling_roling_frequency = str_rolling_sampling_period, 
                                                                                                bool_take_absolute_of_high_to_low_volatility_True_or_False = False)

    df_data['VolatilityRank'] = dict_pdseries_volatility_parameters['VolatilityRank']
    df_data['RollingPercentChangeHighToLow'] = dict_pdseries_volatility_parameters['RollingPercentChangeHighToLow']
    
    #%%

    df_data['StopLossRate'] = df_data['RollingPercentChangeHighToLow'].abs().rolling(str_period_sampling).apply(lambda x: np.quantile(x,float_volatility_high_to_low_quantile))
    df_data['StopLossRate'] = df_data['StopLossRate'].fillna(method = 'bfill')
    #%%
    df_data['TakeProfitRate'] = df_data['StopLossRate'] * int_takeprofit_multiplier
    df_data['TakeProfitRate'] = df_data['TakeProfitRate'].fillna(method = 'bfill')
    #%%
    
    dict_nparray_takeprofit_and_stoploss = {'StopLossRate': np.array(df_data['StopLossRate']), 
                                            'TakeProfitRate': np.array(df_data['TakeProfitRate'])
                                            }
    return dict_nparray_takeprofit_and_stoploss


if __name__  == '__main__':
    from asset_price_etl import etl_fx_histadata_001 as etl
    df_data = etl._function_extract(_str_valuedate_start = '1/1/2018',
                                    _str_valuedate_end = '12/7/2019',
                                    _str_resample_frequency = 'D')
    
    dict_nparray_takeprofit_and_stoploss  = func_dict_nparray_extract(  df_data = df_data,
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
     