# 딕셔너리 모양 문자열 칼럼 데이터프레임으로 만들기  

def get_columns(columns_list: list):
    """" 딕셔너리 모양으로 들어간 문자열 칼럼을 데이터 프레임으로 변환해주는 함수  
    Args:
        columns_list(list): df(pd.DataFrame)에서 변환이 필요한 칼럼명 리스트 

    Returns:
        pd.DataFrame: 각 딕셔너리 key와 values가 분리된 데이터프레임

    """""
    json_columns = ['device', 'geoNetwork', 'totals', 'trafficSource']

    for col in json_columns:
        chagne_df = pd.DataFrame(json.loads(row) for row in list(df[col]))
        chagne_df.columns = [f'{col}.{subcol}' for subcol in chagne_df.columns]
        df2 = df.drop(col, axis=1)
        df2 = pd.concat([df2, chagne_df], axis = 1)
    return df2
    
# df2 = df2.drop([col], axis=1)

get_columns(json_columns)
