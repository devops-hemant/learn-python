#!/usr/bin/python3

'''
🔹 Task 1
Read a file and:
Print only lines containing "INFO"
'''

with open("app.log", "r") as file:
    for line in file:
        if "INFO" in line:
            print(line.strip())


'''
🔹 Task 2
Create a file summary.txt:
Write total number of "ERROR" lines from app.log
'''

error_count = 0
with open("app.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            error_count += 1

with open("summary.txt", "w+") as file:
    file.write(f"Total number of Errors: {error_count}")
    
    file.seek(0)
    content=file.read()
    print(content)



'''
🔹 Task 3 (Bonus)
If error count > 5:
Write "CRITICAL" in report
'''
def err_count(logfile):
    error_count = 0
    try:
        with open(logfile, "r") as file:
            for line in file:
                if "ERROR" in line:
                    error_count += 1
        return error_count
    except FileNotFoundError:
        print("❌ file not found")
        return -1


def report(error_count, status):
    with open("summary.txt", "w") as file:
        file.write(f"Total errors: {error_count}\n")
        file.write(f"Status: {status}\n")

    with open("summary.txt", "r") as file:
        print(file.read())


logcheck = err_count("app.log")

if logcheck == -1:
    report(logcheck, "Log file missing")
elif logcheck > 5:
    report(logcheck, "Critical")
elif logcheck >= 3:
    report(logcheck, "High")
else:
    report(logcheck, "Low")