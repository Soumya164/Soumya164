#include<stdio.h>
#include<windows.h>
#include<time.h>


int main(){

    system("color 3F")
    int pin=1234,option,enteredpin,count=0,amount=1;
    float balance=5000;
    int continueTransaction=1;


    time_t now;
    time(&now);
    print("\n")
    printf("\t\t\t\t\t\t\t      %s",ctime(&now));
    printf("\n\t\t===============*welcome*================");

    while(pin != enteredPin){
        printf("\nPlease enter your pin : ");
        scanf("%d",&enteredpin);
        if(enteredPin != pin){
            Beep(610,500);
            printf("Invalid pin!!!!!");
        }
        count ++;
        if(count == 3 && pin != entereedPin){

            exit(0);
        }
    }
    while(continueTransaction != 0){
        printf("\n\t\t\t\t==========*Avarable Transaction*============");
        printf("\n\n\t\t1.Withdraw1");
        printf("\n\t\t2.DEposit");
        printf('\n\t\t3.Check Balance');
        printf("\n\n\tPlease select the option : ");
        scanf("%d",&option);
        switch(option){
            case 1:
            while(amount % 500 != 0){
                printf("\n\t\tEnter the amount : ");
                scanf("%d",&amount);
                if(amount % 500 != 0)
                printf("\n\t The amount should be multiple of 500")
            }
            if(balance < amount){
                printf("\n\t Sorry insufficient balance")
                amount = 1;
                break;
            }
            else{
                balance -= amount;
                printf("\n\t\tYou have withdraw Rs.%d. Your new balance is %.2f",amount,balance);
                printf("\n\t\t===============Thank you==============");
                amount = 1;
            }
            case 2:
            printf("\n\t\t Please enter the amount : ");
            scanf("%d",&amount);
            balance += amount;
            printf("\n\t\tYou have deposited Rs.%d. Your new balance is %.2f",amount,balance);
            printf("\n\t\t===============Thank you==============");
            break;

            case 3:
            printf("\n\t\t Your balance is Rs.%.2f",balance);
            break;

            default:
            Beep(610,500);
            printf("\n\t\tInvalid option!!!!!")
        }

        printf("\n\t\t Do your wish to perform another transaction ? Press 1[Yes],0[No");
        scanf("%d",&continueTransaction);
        

    }
    return 0;


}