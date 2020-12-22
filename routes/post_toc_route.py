from classes.TOCEntry import TOCEntry
# from classes.File import FILE

# direction -1 for below 1 for above.
# index is the location of the entry we are inserting above or below


def post_toc_route(request):
    new_entries = FILE.entries
    new_entry = TOCEntry('NEW ENTRY', False, 0)
    new_entry['text_error'] = True
    new_entry['page_number_error'] = True

    direction = int(request.form['direction'])

    if direction == 1:  # Insert below
        index = int(request.form['index']) + 1
    else:
        index = int(request.form['index'])

    new_entries.insert(index, new_entry.data)

    FILE.entries = new_entries
    FILE.entries_error = True

    return {
        'new_entry': new_entry,
        'entries_error': True
    }
