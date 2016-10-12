setwd("~/z/projects/jobs")
drv <- dbDriver("PostgreSQL")
con <- dbConnect(drv, dbname = 'scratch', host = 'gpdb', port=5432,user='cwei',password='kuc7Wr@PEsupRu7t')

click_per_day <- dbGetQuery(con, 'SELECT click_date, COUNT(*) AS count FROM clickstream.log GROUP BY click_date ORDER BY click_date;')
#click_per_day becomes a dataframe
library(plotly)
library(gglot2)

model <- lm(count~click_date, data = click_per_day)
coef <- coef(model)
p <- ggplot(click_per_day, aes(click_date, count)) + geom_point() + geom_abline(intercept=coef[1], slope=coef[2]) + ggtitle('click per day vs time') + labs(x = 'date', y = 'click times') + scale_x_date(date_breaks = "1 month")
ggplotly(p)


click_before_expire <- dbGetQuery(con, "SELECT abs(DATE_PART('day',DateExpired::timestamp - click_date::timestamp)) as days FROM clickstream.log JOIN clickstream.expire ON GUID = job_id;")
hist(a$days, main='click distribution vs days until job expired', xlab='number of days until expire', ylab = 'clicks')

q <- ggplot(click_before_expire, aes(click_before_expire$days), col = I('red')) + geom_histogram()+ ggtitle('click distribution vs days until job expired') + labs(x = 'number of days until expire', y = 'clicks') 
ggplotly(q)

dbDisconnect(con)
dbUnloadDriver(drv)