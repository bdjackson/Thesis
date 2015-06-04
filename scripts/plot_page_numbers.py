import matplotlib.pyplot as plt
import pandas
import datetime
import time

## -----------------------------------------------------------------------------
# read the page numbers file into a data frame
page_number_file_name = 'PageNumbers.md'
page_number_df = pandas.DataFrame.from_csv(page_number_file_name,
                                           header=0,
                                           index_col=None)

# convert the date/time column to a date, then normalize to only the date
page_number_df['date-time'] = pandas.to_datetime(page_number_df['date-time'],
                                                 dayfirst=True,
                                                 utc=False)
# page_number_df['date'] = pandas.DatetimeIndex(
#         page_number_df['date-time']).normalize()
page_number_df['date'] = pandas.DatetimeIndex(page_number_df['date-time'])

# extract the first date in the data frame, and compute the day number
first_date = page_number_df['date'].iloc[0]
first_date = first_date.date()
page_number_df['day_num'] = (page_number_df['date'] -
                             first_date)/pandas.offsets.Day(1)

## -----------------------------------------------------------------------------
# draw the figure
ax = page_number_df.plot(x='day_num', y='pages', legend=False,
                         color='steelblue', mec='steelblue', mfc='steelblue',
                         linestyle='-', marker='o', lw=3, ms=5)
ax.fill_between(page_number_df['day_num'], 0, page_number_df['pages'],
                facecolor='steelblue', alpha=0.5)

# plot styling
ax.set_xlabel('Days since %s' % first_date)
ax.set_ylabel('Pages')
ax.set_ylim([0, 1.05*page_number_df['pages'].max()])
ax.set_xlim([-1, page_number_df['day_num'].max()+1])
plt.grid(None)

# text box with current page count
plt.text(0.02, 0.95,
         'Current page count: %d' % page_number_df['pages'].iloc[-1],
         horizontalalignment='left', verticalalignment='top',
         transform=ax.transAxes,
         bbox=dict(facecolor='gray', alpha=0.2, boxstyle='round'))

## -----------------------------------------------------------------------------
# draw labels for major milestones
def draw_annotation(label_text, date_string, offset_x, offset_y,
                    text_color='black', arrow_color='black', arrow_alpha=0.5,
                    shrinkA=0, shrinkB=5, line_width=2, arrow_style='-|>',
                    angle_a=90, angle_b=0):
    connection_style = 'angle3,angleA=%s,angleB=%s' % (angle_a, angle_b)
    arrow_props = dict(facecolor=arrow_color, alpha=arrow_alpha,
                       shrinkA=shrinkA, shrinkB=shrinkB,
                       linewidth=line_width, arrowstyle=arrow_style,
                       connectionstyle=connection_style)

    this_date=datetime.datetime.strptime(date_string,
                                         '%b %d %Y')
                                         # '%a %b %d %H:%M:%S %Z %Y')
                                         # '%a %b %d %H:%M:%S %Y')

    point_x = (this_date.date() - first_date).days + 1
    point_x += (time.mktime(this_date.timetuple()) -
                time.mktime(this_date.date().timetuple()))/(26*60*60)
    point_y = page_number_df[page_number_df['date-time'] < this_date
                            ]['pages'].iloc[-1]

    text_x = point_x + offset_x
    text_y = point_y + offset_y

    ax.annotate(label_text, color=text_color, xy=(point_x, point_y),
                xytext=(text_x, text_y), arrowprops=arrow_props)

# draw_annotation('Begin\nThesis',
#                 date_string='Mar 27 2015',
#                 offset_x=+0, offset_y=+50, angle_b=30)

draw_annotation('Started\noutline',
                date_string='Apr 01 2015',
                offset_x=-5, offset_y=+80,
                shrinkB=20, angle_a = 210, angle_b=110)

draw_annotation('Started\nB-L stop\nchapter',
                date_string='Apr 7 2015',
                offset_x=-4, offset_y=+50,
                shrinkB=5, angle_a = 225, angle_b=140)

draw_annotation('First draft\nB-L stop\nchapter',
                date_string='May 8 2015',
                offset_x=-20, offset_y=-30,
                shrinkB=15, angle_a = 90, angle_b=160)

draw_annotation('Started\nTheory\nchapter',
                date_string='May 19 2015',
                offset_x=-25, offset_y=0,
                shrinkB=15, angle_a = 20, angle_b=170)

draw_annotation('Moved to\nChicago',
                date_string='May 30 2015',
                offset_x=-25, offset_y=-10,
                shrinkB=10, angle_a = 20, angle_b=90)

## -----------------------------------------------------------------------------
# save the figure to a pdf
# plt.savefig('pages.pdf', bbox_inches='tight', format='pdf')
plt.savefig('pages.png', bbox_inches='tight', dpi=200)
