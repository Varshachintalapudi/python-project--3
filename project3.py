import openpyxl

def save_to_excel(data_list, file_name):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    for row_idx, row_data in enumerate(data_list, start=1):
        for col_idx, value in enumerate(row_data, start=1):
            sheet.cell(row=row_idx, column=col_idx, value=value)

    workbook.save(file_name)
    print(f"Data has been saved to {file_name}")

def main():
    data_list = []
    num_rows = int(input("Enter the number of rows: "))
    num_cols = int(input("Enter the number of columns: "))

    for _ in range(num_rows):
        row_data = []
        for col in range(num_cols):
            data = input(f"Enter data for row {_+1}, column {col+1}: ")
            row_data.append(data)
        data_list.append(row_data)

    if data_list:
        file_name = input("Enter the file name (without extension): ") + ".xlsx"
        save_to_excel(data_list, file_name)
    else:
        print("No data to save. Exiting...")

if __name__ == "__main__":
    main()
