#confusion matrix values
TP = 1
FP = 1
TN = 8
FN =90

total = TP+FP+TN+FN

accuracy = (TP+TN)/total
error_rate =(FP+FN)/total
precision = TP/(TP+FP)
recall = TP/(TP+FN)

print("accuracy:",accuracy)
print("error rate:",error_rate)
print("precision:",precision)
print("recall:",recall)