# includes all helper functiosn for the project

# chunking function - split text into smaller chunks for better summarization
def chunk_text(text: str, chunk_size: int=2000, overlap: int=200) -> list:
# chunk_size - max size of each chunk, 
# overlap - number of overlapping characters between chunks - it helps maintain continuity among chunks
    chunks=[]
    start =0
    text_length = len(text)
    
    while start < text_length: # loop until the entire text is processed
        end = min(start + chunk_size, text_length) # calculate end index ensuring it doesn't exceed text length
        chunk = text[start:end] # extract the chunk from start to end
        chunks.append(chunk) # add the chunk to the list of chunks
        
        start += chunk_size - overlap 
        # move start forward by chunk_size minus overlap to create overlapping chunks
        
        if start < 0: # ensure start index is not negative
            start = 0 # reset to 0 if negative
    return chunks

# chunk-summary function - summarize each chunk and combine summaries
def chunked_summarize(text :str, summarize_func, max_chunk_size: int=2000) -> str:
    
    text_chunks = chunk_text(text, chunk_size=max_chunk_size, overlap=200)
    # split text into chunks using chunk_text function
    
    partial_summaries = [summarize_func(chunk) for chunk in text_chunks]
    # summarize each chunk using the provided summarize_func
    
    combined_summary_input = " ".join(partial_summaries)
    # combine all partial summaries into a single text
    
    final_summary = summarize_func(combined_summary_input)
    # summarize the combined summary input to get the final summary 
    
    return final_summary