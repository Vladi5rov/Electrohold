import openpyxl

file_path = "day_ahead_bid_scale.xlsx"
wb = openpyxl.load_workbook(file_path)
ws = wb["Numeric Example"]

# Поставяме единичната динамична формула в клетка A100
formula = (
    '=TRANSPOSE(SORT(UNIQUE(FILTER(VSTACK(-600, 4000,'
    " TOCOL(IF((A2:C97<>'')*(A2:C97>=-600)*(A2:C97<=4000), HSTACK(A2:C97-0.1,"
    " A2:C97), NA()), 2, TRUE), TOCOL(IF((D2:F97<>'')*(D2:F97>=-600)*(D2:F97<=4000),"
    " HSTACK(D2:F97, D2:F97+0.1), NA()), 2, TRUE)),"
    " (VSTACK(-600, 4000, TOCOL(IF((A2:C97<>'')*(A2:C97>=-600)*(A2:C97<=4000),"
    " HSTACK(A2:C97-0.1, A2:C97), NA()), 2, TRUE),"
    " TOCOL(IF((D2:F97<>'')*(D2:F97>=-600)*(D2:F97<=4000), HSTACK(D2:F97,"
    " D2:F97+0.1), NA()), 2, TRUE))>=-600) *"
    " (VSTACK(-600, 4000, TOCOL(IF((A2:C97<>'')*(A2:C97>=-600)*(A2:C97<=4000),"
    " HSTACK(A2:C97-0.1, A2:C97), NA()), 2, TRUE),"
    " TOCOL(IF((D2:F97<>'')*(D2:F97>=-600)*(D2:F97<=4000), HSTACK(D2:F97,"
    " D2:F97+0.1), NA()), 2, TRUE))<=4000)))))"
)

ws["A100"] = formula

wb.save("day_ahead_bid_scale_solution.xlsx")
print(
    "Файлът 'day_ahead_bid_scale_solution.xlsx' е създаден с динамични формули!"
)