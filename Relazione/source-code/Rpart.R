library(rpart)
library(rpart.plot)

fit <- rpart(V42 ~V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, V29, V30, V31, V32, V33, V34, V35, V36, V37, V38, V39, V40, V41,
 data=fileone, method="class",control=rpart.control(minsplit=30))


# plot
rpart.plot(fit, # middle graph
           type=4,
           extra=101, 
           box.palette="GnBu",
           branch.lty=3, 
           shadow.col="gray", 
           nn=TRUE
)

#plot(fit, uniform=TRUE,
#     main="Classification Tree for Botswana Children")
#text(fit, use.n=TRUE, all=TRUE, cex=.8)