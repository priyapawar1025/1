TP = 90
TN = 9560
FP = 210
FN = 140

total = TP+TN+FP+FN

accuracy = (TP+TN)/total
error_rate =(FP+FN)/total
precision = TP/(TP+FP)
recall = TP/(TP+FN)

print("accuracy:",accuracy)
print("error rate:",error_rate)
print("precision:",precision)
print("recall:",recall)