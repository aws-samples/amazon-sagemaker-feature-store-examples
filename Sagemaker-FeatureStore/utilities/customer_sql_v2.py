
def transform_query(fg_name: str) -> str:
    return f'''
        SELECT *, 
            IF (Id > 3, 0, 1) as Persona, 
            (zipcode * 2) + RAND() as NewFeature1 
        FROM {fg_name} 
        '''
