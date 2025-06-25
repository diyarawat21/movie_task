import requests
import csv

def get_movie_titles():
    titles_input = input("Enter movie/series titles (using comma ): ")
    titles = [title.strip() for title in titles_input.split(",")]
    return titles

def fetch_movie_data(title):
    api_key = "4683d8a5"  
    url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f" Error fetching data for {title}: HTTP {response.status_code}")
        return None
    data = response.json()
    if data.get("Response") == "False":
        print(f" Title not found: {title}")
        return None
    return data  

def save_to_csv(data_list, filename):
    if not data_list:
        print(" No valid data to save.")
        return
    
    keys = data_list[0].keys()
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data_list)
    print(f" Full data saved to {filename}")

def main():
    titles = get_movie_titles()
    all_data = []
    for title in titles:
        data = fetch_movie_data(title)
        if data:
            print(f" Title: {data.get('Title')}, Year: {data.get('Year')}")
            all_data.append(data)  # Save full data
    save_to_csv(all_data, "movie_data.csv")

if __name__ == "__main__":
    main()
