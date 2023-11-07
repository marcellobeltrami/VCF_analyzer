import vcf

# 打开VCF文件
vcf_reader = vcf.Reader(open('trios.vcf', 'r'))
# 解析变异信息

# 初始化字典用于存储变异信息
variant_summary = {'location': [], 'type': [], 'function': []}

# 遍历 VCF 文件中的每个变异
for record in vcf_reader:
    variant_summary['location'].append(f"{record.CHROM}:{record.POS}")
    variant_summary['type'].append(record.var_type)
    variant_summary['function'].append(record.INFO.get('Func', 'N/A'))

# 打印变异信息总结
for i in range(len(variant_summary['location'])):
    print(f"Location: {variant_summary['location'][i]}, Type: {variant_summary['type'][i]}, Function: {variant_summary['function'][i]}")

# 打开文件以写入报告
with open('variant_report.txt', 'w') as f:
    for i in range(len(variant_summary['location'])):
        location = variant_summary['location'][i]
        var_type = variant_summary['type'][i]
        function = variant_summary['function'][i]

        # 将每个变异信息写入文件
        f.write(f"Location: {location}, Type: {var_type}, Function: {function}\n")

