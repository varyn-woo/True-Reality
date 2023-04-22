# Author: Luc Davis

# TODO options:
# -Store each list of tags seperately, as a dictionary of lists?
# ^ this can yield O(1) retrieval time
# -Keep storage of most popular tags first (like huffman encoding)
# ^ this can yield O(log(n)) retrieval time
# -Fast intersection of two lists algorithm for search tag_list?

def search_by_tag(string: tag, list: lst):
    ans = []
    for i in lst:
        if tag in i:
            ans.append(i)
    return ans

def search_by_tag_list(liast: tag_list, list: lst):
    ans = []
    for i in lst:
        store = True
        for j in tag_list:
            if j not in i:
                store = False
                break
        if store == True:
            ans.append(i)
    return ans