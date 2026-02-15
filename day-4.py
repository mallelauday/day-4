from logging import critical

size = int(input("Enter the size of the scores: "))
scores = [0] * size
register_no = "AP24110011605"
register_D = int(register_no[-1])
low_risk = []
medium_risk = []
high_risk = []
critical_risk=[]
for i in range(size):
    scores[i] = int(input("Enter score: "))
ignore=0
valid=0
for i in range(size):
    if scores[i] <0:
        ignore=ignore+1
    elif 0<=scores[i]<=30:
        low_risk=low_risk+[scores[i]]
        valid=valid+1
    elif 31<=scores[i]<=60:
        medium_risk=medium_risk+[scores[i]]
        valid=valid+1
    elif 61<=scores[i]<=100:
        high_risk=high_risk+[scores[i]]
        valid=valid+1
    elif scores[i]>100:
        critical_risk=critical_risk+[scores[i]]
        valid=valid+1
print("Register Digit(D):",register_D)
print("Low Risk:",low_risk)
print("Medium Risk:",medium_risk)
print("High Risk:",high_risk)
print("Critical Risk:",critical_risk)
print("After Personalized Filtering:")
if register_D%2==0:
    a = len(low_risk)
    low_risk = []
    print("Low Risk:", low_risk)
    print("Medium Risk:", medium_risk)
    print("High Risk:", high_risk)
    print("Critical Risk:", critical_risk)
    print("Total Valid Entries:", valid)
    print("Ignored Entries:", ignore)
    print("Removed due to Personalization:", a)
else:
    print("Low Risk:", low_risk)
    print("Medium Risk:", medium_risk)
    print("High Risk:", high_risk)
    b = len(critical_risk)
    critical_risk = []
    print("critical risk:", critical_risk)
    print("Total Valid Entries:", valid)
    print("Ignored Entries:", ignore)
    print("Removed due to Personalization:", b)

