from classes.File import FILE

def delete_toc_entry_route(id_number, request): 
    new_entries = FILE.entries
    potential_index = False
    potential_entry = False

    try:
        potential_index = int(request.form['index'])
        potential_entry = new_entries[potential_index]
    except:
        potential_entry = {'id_number': -1} # Fake an entry so we fail the if else statement below.

    index_for_removal = False
    deleted_entry = False

    if potential_entry['id_number'] == int(id_number):
        index_for_removal = potential_index
    else:
        for i in range(len(new_entries)):
            current_entry = new_entries[i]
            if current_entry['id_number'] == int(id_number):
                index_for_removal = i
                deleted_entry = current_entry
                break
        
    if str(index_for_removal) != str(False):
        new_entries.pop(index_for_removal)
        FILE.entries = new_entries
    else:
        return 'Could not find entry.', 400

    return {
        'deleted_entry': deleted_entry
    }

