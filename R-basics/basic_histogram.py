## Basic histogram plot ##

#Example histogram plot:

qplot(x = variable_name, data = df_name, xlim = c(0,1000))

'''
Can alter the BIN WIDTH by adding 'binwidth=20' as a parameter to qplot()
Can specify the axes tick marks by using the 'breaks' parameter, which takes a 'sequence' 
of a starting point, an end point, and a 'step' width.
'''

#e.g.
qplot(x = variable_name, data = df_name, xlim = c(0,1000), binwidth=25, breaks = seq(0, 1000, 50))
# this will have tick marks every 50 units.


# 'ggplot' offers more advanced styling than 'qplot'.

#Example ggplot plot:

ggplot(aes(x = tenure / 365), data = pf) +      # the 'aes' is the 'aesthetics' wrapper
  geom_histogram(color = 'black', fill = '#F79420') +
  scale_x_continuous(breaks = seq(1, 7, 1), limits = c(0, 7)) +
  xlab('Number of years using Facebook') +
  ylab('Number of users in sample')

  