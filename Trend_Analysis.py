#Checking for the trend in the data

# We can check through seasonal decomposition, moving average and the linear regression modelling for checking the trend in the data
fig=plt.figure(figsize=(20,18))
layout=(3,2)
pm_ax=plt.subplot2grid(layout,(0,0),colspan=2)
mv_ax=plt.subplot2grid(layout,(1,0),colspan=2)
fig_ax=plt.subplot2grdi(layout,(2,0),colspan=2)

# Automatic decomposing through seasonal decomposition
plt.figure(num=None, figsize=(50, 20), dpi=80, facecolor='w', edgecolor='k')
series = air_pollution.pollution_today[:365]
result = seasonal_decompose(series, model='multiplicative')
result.plot()
pm_ax.plot(result.trend)
pm_ax.set_title("Automatic decomposed trend")

#Moving Average Method
mm=air_pollution.pollution_today.rolling.mean()
mv_ax.plot(mm)
mv_ax.set_title("Moving Average 12 steps")

#Fitting a linear regression  model to identify trend
X=[i for i in range(0, len(air_pollution.pollution_today))]
X=np.reshape(X, len(X),1)
y=air_pollution.pollution_today.values
model=LinearRegression()
model.fit(X,y)

trend = model.predict(X)
fit_ax.plot(trend)
fit_ax.set_title("Trend fitted by linear regression")

plt.tight_layout()

