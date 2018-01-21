## TRANSFORMING GRAPHS THROUGH SCALING ##

# Some of the long-tailed user data can be transformed to approximate a normal distribution by using a log scale.

#Can transform the summary stats table directly:
#e.g.
summary(log10(df$friend_count + 1))     # note: the '+ 1' is added to avoid a case of log 0 (gives -infinity)

#or,
summary(sqrt(df$age))   # returns square root of 'age' variable

#When using in a plot you can do it two ways.
#You can transform the values first:
#e.g.
qplot(x=log10(df$variable), data=df)    # return a histogram with the log10 of the 'variable'

#Or can apply 'scale_x_log10' to a previously defined plot:
#e.g.
plot <- qplot(x=df$variable, data=df)
log_plot <- scale_x_log10(plot)     # applies the log10() func to each value on the x-axis of 'plot'

'''
IMPORTANT: using the log10() 'wrapper' (the first example) will give the x-axis log units, 
whereas using scale_x_log10 will keep the original values units.

ALSO: Careful when using 'ylim=' or 'scale_y_continuous(c(0,100))' as these actually ommit the data points 
outside these limits, and so may affect median values etc.
A safer way to re-scale the plots is therefore to use 'coord_cartesian(ylim=c(0,100))' function.
'''