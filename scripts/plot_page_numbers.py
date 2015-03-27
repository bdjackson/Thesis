# import matplotlib as mp
import matplotlib.pyplot as plt
import pandas

# read the page numbers file into a data frame
page_number_file_name = 'PageNumbers.md'
page_number_df = pandas.DataFrame.from_csv(page_number_file_name,
                                           header=0,
                                           index_col=None)

# convert the date/time column to a date, then normalize to only the date
page_number_df['date-time'] = pandas.to_datetime(page_number_df['date-time'],
                                                 dayfirst=True)
page_number_df['date'] = pandas.DatetimeIndex(
        page_number_df['date-time']).normalize()
page_number_df = page_number_df.drop('date-time', 1)

# extract the first date in the data frame, and compute the day number
first_date = page_number_df['date'].iloc[0]
page_number_df['day_num'] = (page_number_df['date'] -
                             first_date)/pandas.offsets.Day(1)

# draw and save the figure
ax = page_number_df.plot(x='day_num', y='pages', legend=False,
                         color='steelblue', mec='steelblue', mfc='steelblue',
                         linestyle='-', marker='o', lw=3, ms=5)
ax.set_xlabel('Days since %s' % first_date.date())
ax.set_ylabel('Pages')
ax.set_ylim([0, 1.05*page_number_df['pages'].max()])
plt.grid(None)
plt.savefig('pages.pdf', bbox_inches='tight', format='pdf')
