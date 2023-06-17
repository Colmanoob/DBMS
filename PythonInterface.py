from pydrill.client import PyDrill

def ChangeSourceInQuery(Inputted_SQL_query):
    try:
        StartingIndex, EndingIndex = Inputted_SQL_query.index("FROM"), -1
        BlanksSpace, IndexAfterFrom, IndexOfDot = 0, -1, -1
        for i in range(StartingIndex, len(Inputted_SQL_query)):
            if Inputted_SQL_query[i]==' ':
                if BlanksSpace==0:
                    IndexAfterFrom = i+1
                BlanksSpace += 1
            if Inputted_SQL_query[i]=='.':
                IndexOfDot = i
            if BlanksSpace==2:
                EndingIndex = i
                break
            elif BlanksSpace==1 and i==len(Inputted_SQL_query)-1:
                EndingIndex = i
                break
        QueryToMySQL, QueryToMongo = "", ""
        Database, Collection_Table = Inputted_SQL_query[IndexAfterFrom:IndexOfDot], Inputted_SQL_query[IndexOfDot+1:EndingIndex+1]
        for i in range(StartingIndex):
            QueryToMySQL += Inputted_SQL_query[i]
            QueryToMongo += Inputted_SQL_query[i]
        QueryToMySQL += "FROM mysql." + Database + "." + Collection_Table
        QueryToMongo += "FROM mongo." + Database + "." + Collection_Table
        if BlanksSpace==2:
            for i in range(EndingIndex, len(Inputted_SQL_query)):
                QueryToMySQL += Inputted_SQL_query[i]
                QueryToMongo += Inputted_SQL_query[i]

        return QueryToMySQL, QueryToMongo

    except ValueError:
        print('SQL syntax error!(No sources)')
        return Inputted_SQL_query

def QueryToMySQL_MongoDB(Inputted_SQL_query):
    drill = PyDrill(host='localhost', port=8047)
    QueryToMySQL, QueryToMongo = ChangeSourceInQuery(Inputted_SQL_query)
    print('QueryToMySQL: ', QueryToMySQL)
    print('QueryToMongo: ', QueryToMongo)
    MySQL_Result = drill.query(QueryToMySQL)
    Mongo_Result = drill.query(QueryToMongo)

    return MySQL_Result, Mongo_Result