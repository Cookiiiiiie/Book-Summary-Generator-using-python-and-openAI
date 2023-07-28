import csv
import openai

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = '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'

def generate_summary(book_name, book_content):
    prompt = f"Summarize the book '{book_name}' in brief. The book is about {book_content}."
    # Rest of the code remains the same
    response = openai.Completion.create(
        engine="text-davinci-002",  # You can use a different engine if you prefer
        prompt=prompt,
        temperature=0.7,
        max_tokens=200,
        stop=["\n"],
    )
    return response.choices[0].text.strip()

def main(input_csv_file):
    with open('c:\\BookSummaryProject\\books.csv', "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present

        for row in reader:
            book_name = row[0]
            book_content = row[1]  # Assuming the book content is in the second column
            summary = generate_summary(book_name, book_content)
            # Rest of the code remains the same


            # Save summary to a text file
            output_file = f"{book_name}_summary.txt"
            with open(output_file, "w") as summary_file:
                summary_file.write(summary)

            print(f"Summary for '{book_name}' saved in '{output_file}'.")

if __name__ == "__main__":
    input_csv_file = "books.csv"  # Replace with the name of your CSV file
    main(input_csv_file)
