num1<-as.integer(readline(prompt="enter the first number:"))
num2<-as.integer(readline(prompt="enter the second number:"))
num3<-as.integer(readline(prompt="enter the third number:"))
if(num1>=num2&num1>=num3)
{
print(paste(num1,"is greatest"))
}else if(num2>=num1&num2>=num3)
{
print(paste(num2,"is greatest"))
}else
{
print(paste(num3,"is the greatest"))
}