class Lists:

    def __init__(self):
        """ Convenient methods to modify, process and create lists 
        """


    def list_flatten(nested_list):
        """Flattens nested list"""
        return [element for sublist in nested_list for element in sublist]

    def list_remove_duplicates(l):
        """Removes duplicates from list elements whilst preserving element order
        adapted from 
        https://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-whilst-preserving-order
        
        Input
            list with string elements
        
        Return 
            Sorted list without duplicates
        
        """
        seen = set()
        seen_add = seen.add
        return [x for x in l if not (x in seen or seen_add(x))]

    def list_batch(lst, n=5):
        """Yield successive n-sized chunks from list lst
        
        adapted from https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
        
        Input
            lst: list 
            n: selected batch size
            
        Return 
            List: lst divided into batches of len(lst)/n lists
        """
        
        for i in range(0, len(lst), n):
            yield lst[i:i + n]
