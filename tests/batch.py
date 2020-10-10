def batch(lst, n=5):
    """Yield successive n-sized chunks from list lst
    
    adapted from https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    
    Input
        lst: list 
        n: selected batch size
        
    Return 
        List: Nested list that contains batches of len(lst)/n lists
    """
    
    batched_list = []

    for i in range(0, len(lst), n):
        batched_list.append(lst[i:i + n])

    return batched_list