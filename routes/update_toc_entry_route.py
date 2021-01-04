# from classes.File import FILE

from utils.misc.is_number import is_number


def update_toc_entry_route(idNumber, request):
    new_entries = FILE.entries
    potential_index = False
    potential_entry = False

    try:
        potential_index = int(request.form['index'])
        potential_entry = new_entries[potential_index]
    except:
        # Fake an entry so we fail the if else statement below.
        potential_entry = {'idNumber': -1}

    index_of_updated = False
    updated_entry = False
    if potential_entry['idNumber'] == int(idNumber):
        index_of_updated = potential_index
    else:
        for i in range(len(new_entries)):
            current_entry = new_entries[i]
            if current_entry['idNumber'] == int(idNumber):
                index_of_updated = i
                updated_entry = current_entry
                break

    if str(index_of_updated) != str(False):
        key = request.form['key']
        value = request.form['value']

        if key == 'entry':
            new_entries[index_of_updated][key] = value.strip()
        else:  # key is page_number_in_pdf
            page_number_difference = FILE.difference_in_page_numbers
            new_entries[index_of_updated][key] = value.strip()
            new_entries[index_of_update]['page_number_for_me'] = int(
                value) + page_number_difference

        new_entries[index_of_updated] = set_entry_errors(
            key, new_entries[index_of_updated])

        updated_entry = new_entries[index_of_updated]
        FILE.entries = new_entries
    else:
        return 'Could not find entry.', 400

    return {
        'updated_entry': updated_entry
    }


def set_entry_errors(key, new_entry):
    if key == 'entry':
        entry_text = new_entry['entry']
        entry_text_as_num = is_number(new_entry['entry'])
        if len(entry_text) == 0 or is_number == True:
            new_entry['text_error'] = True
        else:
            new_entry['text_error'] = False
    else:  # key == page_num_for_me
        print(key)
        print(new_entry)
        hey = 'hey'
    return new_entry
