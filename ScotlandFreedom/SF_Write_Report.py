import pandas as pd


def CreateExcelReport(output, df, df_ext, df_folders):
    # Create ScotlandFreedomReport.xlsx

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    output_path = output + "ScotlandFreedomReport.xlsx"
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name="Kill List", index=False)
    df_ext.to_excel(writer, sheet_name="Analysis")
    df_folders.to_excel(writer, sheet_name="Folder Analysis", index=False)
   
    # Format the Excel output.
    worksheet = writer.sheets["Kill List"]
    worksheet.set_column('A:A', 150)
    worksheet.set_column('B:B', 50)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 20)

    worksheet = writer.sheets["Analysis"]
    worksheet.set_column('A:A', 20)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 20)

    worksheet = writer.sheets["Folder Analysis"]
    worksheet.set_column('A:A', 150)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    
    # Add a chart to Analysis sheet showing the top 10 file extensions and their sizes and counts and means.
    chart = writer.book.add_chart({'type': 'column'})
    chart.add_series({
        'name':       '=Analysis!$B$1',
        'categories': '=Analysis!$A$2:$A$11',
        'values':     '=Analysis!$B$2:$B$11',
    })
    chart.add_series({
        'name':       '=Analysis!$C$1',
        'categories': '=Analysis!$A$2:$A$11',
        'values':     '=Analysis!$C$2:$C$11',
    })
    chart.add_series({
        'name':       '=Analysis!$D$1',
        'categories': '=Analysis!$A$2:$A$11',
        'values':     '=Analysis!$D$2:$D$11',
    })
    chart.set_title({'name': 'Top 10 file extensions'})
    chart.set_x_axis({'name': 'File extension'})
    chart.set_y_axis({'name': 'Size (GB)'})
    worksheet = writer.sheets["Analysis"]
    worksheet.insert_chart('F2', chart, {'x_offset': 2, 'y_offset': 2})

    # Close the Pandas Excel writer and output the Excel file.
    writer.close()