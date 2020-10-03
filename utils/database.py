import utils as op

def update_one(query,stuff):
    check = op.Users.update_one(query,stuff)
    if check.matched_count==0:
        user = create_new(query["id"])
    

def create_new(id):
    data = {"id":id,"cmd_count":1,"xp":20,"bal":0,"items":[],"inv":[]}
    op.Users.insert_one(data)
    return data

def show(id):
    data = op.Users.find_one({"id":id})
    if not data:
        data = create_new(id)
    return data

def get_items(id):
    data = op.Users.find_one({"id":id},{"items"})
    print('CHECK:',data)
    return data