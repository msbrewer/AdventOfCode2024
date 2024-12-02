import sys
infile = sys.argv[1] if len(sys.argv)>=2 else 'input'
data = open(infile).read().strip()

reports = data.split("\n")
safe_reports = 0
for report in reports:
    report_values1 = list(map(int, report.split()))
    relaxed_good = False
    for j in range(len(report_values1)):
        report_values = report_values1[:j] + report_values1[j+1:]
        inc_dec = (report_values==sorted(report_values) or report_values==sorted(report_values,reverse=True))
        ok = True
        for i in range(len(report_values)-1):
            diff = abs(report_values[i]-report_values[i+1])
            if not 1<=diff<=3:
                ok = False
        if inc_dec and ok:
            relaxed_good = True
    if relaxed_good:
        safe_reports += 1
print(safe_reports)

