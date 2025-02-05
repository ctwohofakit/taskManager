from app.database import get_db #importing from init, python package

#tuple is immuable, in order, tuple os mpt compatible with Json
#we have to create a list as dictionary

def output_formatter(results): 
    out=[]
    for result in results:
        res={
            "id": result[0],
            "name": result[1],
            "summary": result[2],
            "description": result[3],
            "is_done": result[4]
        }
        out.append(res)
    return out


#columns

def scan():
    conn=get_db() #retriving dtabase connection
    cursor=conn.execute("SELECT*FROM task WHERE is_done=0", ()) #column, empty tuple
    results=cursor.fetchall()
    cursor.close()
    return output_formatter(results)#return



def select_by_id(task_id):
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task WHERE id = ?", (task_id, )) #comma, special character will be dropp, esacpe it
    results=cursor.fetchall()
    cursor.close()
    if results:
        return output_formatter(results)[0]
    return{}



def create_task(task_data):
    statement = """
        INSERT INTO task (
            name,
            summary,
            description
        )VALUES (?, ?, ?)
    """
    conn=get_db()
    task_tuple=(
        task_data.get("name"),
        task_data.get("summary"),
        task_data.get("description")
    )
    conn.execute(statement, task_tuple)
    conn.commit()
   

def update_by_id(task_data, task_id):
    statement="""
        UPDATE task
        SET
            name = ?,
            summary = ?,
            description = ?,
            is_done = ?
        WHERE id = ?
    """
    task_tuple=(
        task_data.get("name"),
        task_data.get("summary"),
        task_data.get("description"),
        task_data.get("is_done")
    )
    conn=get_db()
    conn.execute(statement, task_tuple)
    conn.commit()



def delete_by_id(task_id):
   conn=get_db()
   conn.execute("DELETE FROM task WHERE id =?", (task_id, ))
   conn.commit()