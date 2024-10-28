library(faraway)
data(insulgas)
summary(insulgas)

plot(Gas ~ Temp, data=insulgas, col=ifelse(insulgas$Insulate=="Before", "blue", "orange"))
