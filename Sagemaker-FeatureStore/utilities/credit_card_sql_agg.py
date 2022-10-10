
def transform_query(fg_name: str) -> str:
    return f'''
        SELECT cc_num,
            COUNT(*) OVER 30day_w as trans_count_30d,
            COUNT(*) OVER day_w as trans_count_1d,
            AVG(amount) OVER 30day_w as amt_avg_30d,
            AVG(amount) OVER day_w as amt_avg_1d,
            SUM(amount) OVER 30day_w as amt_sum_30d,
            SUM(amount) OVER day_w as amt_sum_1d,
            date_format(datetime, "yyyy-MM-dd'T'HH:mm:ss.SS'Z'") as event_time
        FROM {fg_name}
        WINDOW
           30day_w AS (PARTITION BY cc_num order by cast(datetime AS timestamp) 
                  RANGE INTERVAL 30 DAY PRECEDING),  
           day_w  AS (PARTITION BY cc_num order by cast(datetime AS timestamp) 
                  RANGE INTERVAL 1 DAY PRECEDING)
        '''
