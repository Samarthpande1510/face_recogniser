from bing_image_downloader import downloader
import os


queries = ["chess_board"]


output_directory = 'assets'


for query in queries:
    print(f"--- Starting download for: {query} ---")
    
    downloader.download(
        query, 
        limit=2, 
        output_dir=output_directory, 
        adult_filter_off=True, 
        force_replace=False, 
        timeout=60,
        verbose=True
    )

print("\n Chess pics are here!")