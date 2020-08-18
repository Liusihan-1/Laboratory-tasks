import pandas as pd

df = pd.read_csv('train.csv')
print(df.head())
print(df.columns)
print(df.isnull().sum())
print(df.describe())
df['Age'] = df['Age'].fillna(df['Age'].median())
print(df.describe())
print(df['Embarked'].unique())
print(dict(df['Embarked'].value_counts()))
df['Embarked'] = df['Embarked'].fillna('S')
df.loc[df['Embarked'] == 'S','Embarked'] = 0
df.loc[df['Embarked'] == 'C','Embarked'] = 1
df.loc[df['Embarked'] == 'Q','Embarked'] = 2

print(df['Embarked'].unique())
# 使用随机森林模型
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier

# 设置标签
predictors = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']

# 通过随机森林进行预测，这里随机森林的参数只是随便设定的，具体参数需要建立一个随机森林模型
# n_estimators指树的个数，min_samples_split指内部节点再划分所需最小样本数，min_samples_leaf叶子节点最少样本数
alg_2 = RandomForestClassifier(random_state=1, n_estimators=50,   min_samples_split=4, min_samples_leaf=2)
kf = model_selection.KFold(n_splits=3, random_state=1, shuffle=True)
scores_1 = model_selection.cross_val_score(alg_2, df[predictors], df['Survived'], cv=kf)
print(scores_1.mean())
