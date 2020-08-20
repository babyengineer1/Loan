import request

url = 'http://localhost:5000/results'
r = request.post(url,json={'ApplicantIncome':4000, 'CoaplicantIncome':2000,
                           'LoanAmount':600, 'Loan_Amount_Term':360,'Credit_History':1,
                           'Self_Employed':1, 'Property_Area':1, 'Married':1, 'Education':0,
                           'Gender':1 })

print(r.json())
