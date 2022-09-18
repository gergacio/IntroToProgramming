from nis import match


def get_name(record_store):
    return record_store["name"]

def find_record_by_title(given_record, record_store):
    #given_record is a string....we return back whole record (dictionary)!!!
    for record in record_store["records"]:
        if record["title"] == given_record:
            return record
    
def sell_record(record_3, record_store):
    #add record_3 price tag to store money
    record_store["money"] += record_3["price"]
    #take out sold record
    record_store["records"].remove(record_3)

