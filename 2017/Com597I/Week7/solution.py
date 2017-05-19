# clean the congress data for further analysis

# column mappings:
#  construction: 37
# manufactoring: 38
# finance: 43
# median income: 65
# mean income: 66

file_handle = open("cd11414dp3.csv")
file_handle.readline()

output_file = open("cd1141dp3_clean.csv", "w")

output_file.write("total,constr,manuf,finance,constr_r,manuf_r,finance_r,mean_income,median_income")
output_file.write("\n")

for line in file_handle:
    line_parts = line.split(',')  # 
    
    if line_parts[1] == 'PR' or line_parts[1] == "DC":
        continue
        
    total_workforce = float(line_parts[5])
    construction = float(line_parts[36])
    manufactoring = float(line_parts[37])
    finance = float(line_parts[42])
    median_income = float(line_parts[64])
    mean_income = float(line_parts[65])
    
    construction_ratio = construction / total_workforce
    manufactoring_ratio = manufactoring / total_workforce
    finance_ratio = finance / total_workforce
    output_list = [str(total_workforce), str(construction), 
            str(manufactoring), str(finance), 
            str(construction_ratio), str(manufactoring_ratio), 
            str(finance_ratio), str(mean_income), 
            str(median_income)]

    output_file.write(",".join(output_list))
    output_file.write("\n")

