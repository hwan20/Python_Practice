#matplotlib 모듈의 기능 보충용 seaborn
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset("titanic")
print(titanic.info())
"""
#age로 히스토그램을 그림
sns.displot(titanic['age'])
plt.show()

#sns.boxplot(titanic['age'])
sns.boxplot(y='age', data = titanic, palette='Paired')
plt.show()

#sns.countplot(x="class", data=titanic)
sns.countplot(x="class", data=titanic, hue="who") #hue는 카테고리형 변수
plt.show()
"""

#pivot_table의 결과를 size를 보여줌
t_pivot=titanic.pivot_table(index="class", columns="sex", aggfunc="size")
print(t_pivot)

#pivot_table의 결과를 시각화해서 보여줌
sns.heatmap(t_pivot, cmap=sns.light_palette(color="gray", as_cmap=True),
            annot=True, fmt="d")
plt.show()






