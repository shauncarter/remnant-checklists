import pandas as pd

def update_location(row):
    how_to_get = row["How To Get"]
    if "Losomn" in how_to_get:
        return "Losomn"
    elif "Yaesha" in how_to_get:
        return "Yaesha"
    elif "N'erud" in how_to_get or "N'Erud" in how_to_get:
        return "N'erud"
    elif "Ward" in how_to_get or "Ward 13" in how_to_get or "bought from Cass" in how_to_get:
        return "Ward 13"
    elif "Can be found in Root Earth" in how_to_get:
        return "Root Earth"
    elif "Labyrinth" in how_to_get:
        return "The Labyrinth"
    else:
        return "Unclear"

def main():
    # Replace 'your_input.csv' with the actual file path or URL of your CSV file
    input_file = 'remnant-rings.csv'
    output_file = 'remnant-rings-output.csv'

    # Load CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Apply the update_location function to create the "Location" column
    df["Location"] = df.apply(update_location, axis=1)

    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()
