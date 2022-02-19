import pandas
from flask import Flask, render_template, request,redirect

app = Flask(__name__)

def learn():
    df= pandas.read_csv('temps.csv')
    df.head(5)

    df.head() #Вывод первых пяти строк

    trans_df = pandas.get_dummies(df, columns=['week'])
    #trans_df = pandas.get_dummies(df, columns=['city','vacation_preference', 'transport_preference']) # get_dummies преобразовывает строки в столбцы, расставляя 0 и 1

    #x = trans_df.drop('target',axis=1) # все колонки кроме target кладем в X, это будут наши входные данные,
    # на снове их бы будем делать предсказания (drop  выкидывает нужный столбец)
    #y = trans_df['target'] # это то, что мы пытаемся предсказать

    x = trans_df.drop('actual',axis=1) # все колонки кроме target кладем в X, это будут наши входные данные,
    # на снове их бы будем делать предсказания (drop  выкидывает нужный столбец)
    y = trans_df['actual'] # это то, что мы пытаемся предсказать

    # обучающая выборка (train), учебник
    # тестовая выборка (test), экщамен
    from sklearn.model_selection import train_test_split # sclearn это библиотека для машинного обучения. train_test_split - обчучение с учителем

    #x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.33) # 33% отправляем на тестовую выборку
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 42) # 33% отправляем на тестовую выборку

    x_test # в нее не вошла колонка target

    y_train # это только target колонка. Это ответы

    #from sklearn.ensemble import RandomForestClassifier # RandomForestClassifier алгоритм случайной классификации. Он для обучения
    from sklearn.ensemble import RandomForestRegressor

    #rfc = RandomForestClassifier(n_estimators=1000) # Создаем объект библиотеки. Можно указать параметры (n_estimators - количество деревьев "дерево решений")
    rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)

    rf.fit(x_train,y_train) # непосредственно обучение!!!!
    print(x.loc[100:100])
    s1 = pandas.DataFrame({'year': [1], 'month': [2], 'day': [2], 'temp_2': [2], 'temp_3': [2], 'average': [2], 'forecast_noaa': [2], 'forecast_acc': [2], 'month': [2], 'forecast_under': [2], 'friend': [2]})
    #s1 = pandas.Series([1,2,3], 2, 3, 4, 5])
    print('s1 ',s1.loc[0:0])
    print(s1)
    '''
    my_test = {0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0}
    mydf = pandas.DataFrame(my_test, columns=["year"])
    print(type(mydf), mydf)
    prediction = rf.predict(my_test)
    print(prediction)
    '''''
@app.route('/', methods=["POST", "GET"])
def sui():
    learn()

    if request.method == "POST":
        return redirect('/')

    return render_template('weatherakinator.html')




'''my_test = x.loc[100:100]
my_test.head()

prediction = rf.predict(my_test)#(x_test) # делаем предсказания
print(prediction)
print(df.loc[100:100]['actual'])

prediction=rf.predict(x_test) # делаем предсказания
print(prediction)
print(y_test)'''


app.run()

