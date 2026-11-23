from src.api_data_assignment.api_data_retrieval_and_storage import Books
from src.api_data_assignment.data_process_and_visualization import process_and_visualize_scores
from src.api_data_assignment.csv_data_import import process_csv_import, print_users

# PS - 1
books = Books()
all_books = books.get_all_books()
books.print_books(all_books)

#PS-2
dataframe, average_scores, chart_path = process_and_visualize_scores()

print(f"Loaded {len(dataframe)} student records.")
print("Average scores:")

for subject, average in average_scores.items():
    print(f"  {subject}: {average:.2f}")

print(f"Bar chart saved at: {chart_path}")


#PS-3
inserted_count, users = process_csv_import()

print(f"Inserted {inserted_count} users.")
print_users(users)