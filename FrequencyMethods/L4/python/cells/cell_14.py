# Исходные данные
average_orig = subset["Average"].to_numpy()
_average_orig = average_orig[::-1]

t = np.arange(0, average_orig.size)

average_day = apply_W_dynamic(t, _average_orig, W1_tf(time['day']), dt=1, y0=_average_orig[0])[::-1]
average_week = apply_W_dynamic(t, _average_orig, W1_tf(time['week']), dt=1, y0=_average_orig[0])[::-1]
average_month = apply_W_dynamic(t, _average_orig, W1_tf(time['month']), dt=1, y0=_average_orig[0])[::-1]
average_quarter = apply_W_dynamic(t, _average_orig, W1_tf(time['month']*3), dt=1, y0=_average_orig[0])[::-1]
average_year = apply_W_dynamic(t, _average_orig, W1_tf(time['year']), dt=1, y0=_average_orig[0])[::-1]


plt.plot(subset['Date'], average_orig, 'k-', linewidth=.4, alpha=.2)

plt.plot(subset['Date'], average_day, '-', linewidth=.5, alpha=.4, label='Среднее за день')
plt.plot(subset['Date'], average_week, '-', linewidth=1, alpha=.7, label='Среднее за неделю')
plt.plot(subset['Date'], average_month, '-', linewidth=1, alpha=.9, label='Среднее за месяц')
plt.plot(subset['Date'], average_quarter, '-', linewidth=1, alpha=.9, label='Среднее за квартал')
plt.plot(subset['Date'], average_year, '-', linewidth=1, alpha=.9, label='Среднее за год')

plt.legend(loc=(.05, .6))

ax = plt.gca()
# ax.xaxis.set_major_locator(mpl.dates.MonthLocator(interval=12))  # каждые 3 месяца – квартал
# ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(interval=3))             # минорные – каждый месяц
# ax.xaxis.set_major_formatter(mpl.dates.DateFormatter('%Y'))


# ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(10000))
# ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(2500))

ax.grid(which='major', linestyle='--', alpha=0.5)
ax.grid(which='minor', linestyle=':', alpha=0.3)

plt.margins(.05)
plt.tight_layout()

start_date = pd.to_datetime("2017-01-01")
end_date = pd.to_datetime("2023-02-21")
ax.set_xlim(start_date, end_date)

%mkdir -p ../fig/2
plt.savefig('../fig/2/1.png')
date_range = mpl.dates.num2date(ax.get_xlim())
print("Figure ../fig/2/1.png date range:", date_range[0].strftime('%Y-%m-%d'), "to", date_range[1].strftime('%Y-%m-%d'))
plt.savefig('../fig/2/1.png')

start_date = pd.to_datetime("2019-01-01")
end_date = pd.to_datetime("2022-01-01")

ax.set_xlim(start_date, end_date)
plt.savefig('../fig/2/2.png')
date_range = mpl.dates.num2date(ax.get_xlim())
print("Figure ../fig/2/1.png date range:", date_range[0].strftime('%Y-%m-%d'), "to", date_range[1].strftime('%Y-%m-%d'))

start_date = pd.to_datetime("2021-01-01")
end_date = pd.to_datetime("2021-07-01")

ax.set_xlim(start_date, end_date)
plt.savefig('../fig/2/3.png')
date_range = mpl.dates.num2date(ax.get_xlim())
print("Figure ../fig/2/1.png date range:", date_range[0].strftime('%Y-%m-%d'), "to", date_range[1].strftime('%Y-%m-%d'))