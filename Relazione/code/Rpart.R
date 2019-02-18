library(rpart)
library(rpart.plot)

fit <- rpart(V22 ~ .,                           # Building the tree
   data=train_set_principalComponents,
   control=rpart.control(cp=0.01), 
    method="class")

t_pred <- predict(fit, test_set_principalComponents, type="class")  # Predicting on test-set
confMat <- table(test_set_principalComponents$V22,t_pred)           # Computing confusion matrix
accuracy <- sum(diag(confMat))/sum(confMat)

#plot(fit)
#text(fit, use.n=TRUE, all=TRUE)



accuracy

rpart.plot(fit, # middle graph
           type=1,
           extra=101, 
           box.palette="GnBu",
           branch.lty=3, 
           shadow.col="gray",
          nn=TRUE)
printcp(fit)
