from abc import ABC,abstractmethod
class customer:
    def __init__(self,customer_id,name,email,phonenumber,age,income,credit_score):
        self.customer_id=customer_id
        self.name=name
        self.email=email
        self.phonenumber=phonenumber
        self.age=age
        self.income=income
        self.credit_score=credit_score

    def check_eligibility(self):
        if self.age<21 or self.credit_score<650 or self.income<25000:
            return False
        return True  
    def display_customer(self):
        print("\nCustomer Details")
        print("-----------------")
        print("Customer ID :",self.customer_id)
        print("Name:",self.name)
        print("Email:",self.email)
        print("Phone number",self.phonenumber)
        print("Age",self.age)
        print("Incoome:",self.income)
        print("Credit score:",self.income)



zaib=customer(1,"zaib","zaib@123",999898989,22,90000,880)
zaib.display_customer()
print("Check Eligibility:",zaib.check_eligibility())



class Loan(ABC):
    def __init__(self,loan_id,customer,loan_amount,intrest_rate,tenure):
        self.loan_id=loan_id
        self.customer=customer
        self.loan_amount=loan_amount
        self.intrest_rate=intrest_rate
        self.tenure=tenure
        self.__balance=loan_amount
        self.__total_paid=0
        self.repayment_history=[]
        self.status="Applied"

    @abstractmethod
    def calculate_emi(self):
        pass
    def check_loan_eligibility(self):

        if not self.customer.check_eligibility():
            self.status="Rejected"
            return False
        return True
    def sanction_loan(self):
        if self.status=="Rejected":
            print("Loan application is rejected")
            return
#double checking is done abobe this and below this 
        if not self.check_loan_eligibility():
            print("Customer is not eligible for loan")
            return
        self.status="Sanctioned"
        print("\nLoan Sanctioned Successfully")

    def replay(self,amount):

        if self.status != "Sanctioned":
            print("Repayment is not allowed")
            print("Loan Status:",self.status)
            return

        if amount<=0:#when low balance
            print("Invalid repayment amount")
            return

        if amount>self.__balance:
            print("Repayment is grater than outstanding balance")
            return

        self.__balance -=amount
        self.__total_paid +=amount

        self.repayment_history.append(amount)

        print("\nRepayment Successfull")
        print("Amount paid:",amount)
        print("outstanding balance:",self.__balance)

        if self.__balance==0:
            self.status="Closed"
            print("Loan closed successfully")

    def get_balance(self):
        return self.__balance
    def get_loan_amount(self):
        return self.__loan_amount

    def get_total_paid(self):
        return self.__total_paid




    def display_statement(self):
        print("\n")
        print("Loan Statement")



        print("loan Id               :",self.loan_id)
        print("Customer name          :",self.customer.name)
        print("Loan Amount            :",self.__loan_amount)
        print("Intrest Rate            :",self.intrest_rate)
        print("Tenure                  :",self.tenure)
        print("TOtal Paid               :",self.__total_paid)
        print("Outstanding Balance       :",self.__balance)
        print("Loan Status               :",self.status)


        print("\n Repayment History")


        if not self.repayment_history:
            print("No repayment made")

        else:
            for i in range(len(self.repayment_history)):
                print(f"Payment {i+1}           :{self.repayment_history[i]}")

    def __str__(self):
        return(
            f"Loan Id :{self.loan_id},"
            f"Customer:{self.customer.name},"
            f"Loan Amount:{self.__loan_amount},"
            f"Outstanding:{self.__balance},"
            f"Status:{self.status}"
                                            )


zaib=customer(1,"zaib","zaib@123",999898989,22,90000,880)
zaib.display_customer()
print("Check Eligibility:",zaib.check_eligibility())