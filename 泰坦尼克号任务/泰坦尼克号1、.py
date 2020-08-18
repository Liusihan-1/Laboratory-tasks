import pandas as pd
from IPython.display import display
# 查看数据
train=pd.read_csv('train.csv')
test=pd.read_csv('test.csv')
display(train)        # 查看训练集
display(test)         # 查看测试集
# 利用for循环来查看缺失率
for column in train.columns:
    print("name:{0} miss rate:{1:.2f} ".format(column,1-train[column].count()/len(train)))
for column in test.columns:
    print("name:{0} miss rate:{1:.2f} ".format(column,1-test[column].count()/len(train)))
# 删除PassengerId, Name, Ticket, Cabin的特征
# 这些都与最终预测结果无关
train,test= train.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin']),test.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])
# 用训练集Age的平均值来填补空缺的Age
train['Embarked'] = train['Embarked'].fillna('S')
test['Embarked'] = test['Embarked'].fillna('S')
train['Age'] = train['Age'].fillna(int(train['Age'].mean()))
test['Age'] = test['Age'].fillna(int(test['Age'].mean()))
test['Fare'] = test['Fare'].fillna(float(test['Fare'].dropna().mode()[0]))
# 机器学习算法一般来说解决不了对字符的分类
# 所以我们就要把"Sex、Embarked"这两列的数据进行处理，把它们改为数值型
# 所以我们对它们进行编号
# loc是通过行标签索引行数据，iloc是通过行号获取行数据， ix是结合前两种的混合索引
train.loc[train["Sex"]=="male","Sex"] = 0;
train.loc[train["Sex"]=="female","Sex"] = 1;
train.loc[train["Embarked"]=="S","Embarked"] = 0;
train.loc[train["Embarked"]=="C","Embarked"] = 1;
train.loc[train["Embarked"]=="Q","Embarked"] = 2;
test.loc[test["Sex"]=="male","Sex"] = 0;
test.loc[test["Sex"]=="female","Sex"] = 1;
test.loc[test["Embarked"]=="S","Embarked"] = 0;
test.loc[test["Embarked"]=="C","Embarked"] = 1;
test.loc[test["Embarked"]=="Q","Embarked"] = 2;
# 加载数据集,并提取X_train,y_train,X_test,y_test
result=pd.read_csv('gender_submission.csv')
X_train,y_train=train.drop(columns=['Survived']),train['Survived']
X_test,y_test=test,result.drop(columns=['PassengerId'])
# 放入k-NN模型
print("使用k-NN模型： ")
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_predict = knn.predict(X_test)
print(y_predict)
print('train score: {:.2f}'.format(knn.score(X_train, y_train)))
print('test score: {:.2f}'.format(knn.score(X_test, y_test)))
# 使用决策树分类器模型
print("使用决策树分类器模型: ")
from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
Predict = dtc.predict(X_test)
print(Predict)
print('train  score: {:.2f}'.format(dtc.score(X_train, y_train)))
print('test  score: {:.2f}'.format(dtc.score(X_test, y_test)))
