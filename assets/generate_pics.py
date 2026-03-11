from bing_image_downloader import downloader
import os

# 1. Define your classes (The 4 Pokemon)
queries = ["Pikachu", "Bulbasaur", "Charmander", "Squirtle"]

# 2. Set the output directory
output_directory = 'dataset'

# 3. Loop through and download
for query in queries:
    print(f"--- Starting download for: {query} ---")
    
    downloader.download(
        query, 
        limit=25, 
        output_dir=output_directory, 
        adult_filter_off=True, 
        force_replace=False, 
        timeout=60,
        verbose=True
    )

print("\n[FINISH] All Pokemon images have been saved to the 'dataset' folder!")