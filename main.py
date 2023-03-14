import streamlit as st
import pandas as pd
import numpy as np
import calculator as calc


st.title("Relative evaluation calculator (Bağıl değerlendirme hesap makinesi)")
my_grade = st.number_input('Your grade (real or estimate)', min_value=0.0, max_value=100.0, value=90.0, step=1.0)
m = st.number_input('Average grade of your class (real or estimate)', min_value=0.0, max_value=100.0, value=50.0, step=1.0)
s = st.number_input('Standard deviation (normally, it is near 15)', min_value=8.0, max_value=50.0, value=15.0, step=1.0)
t = st.number_input('Tolerance level (0 by default = no tolerance)', min_value=0.0, max_value=0.2, value=0.0, step=0.1)


st.metric(label="Your letter grade", value=calc.cal_letter(my_grade, m, s, t))

letters = calc.get_letters(m, s, t)

df = pd.DataFrame(np.c_[letters[0], letters[1]], index = np.round(letters[2],2), columns=['Letter','Limit'])

st.subheader("Letter limits")
st.table(df)

"""

### Important Notes 

1. Students with a grade of less than 20 or equal to 100 should be excluded from the arithmetic mean calculation. 
2. To apply this grading method, the number of students in the class must be larger than 20 and the standard deviation must be greater than 8. Otherwise, you should use the absolute (Mutlak) grading method.
3. The tolerance level is set at 0 by default, but depending on your university or professor, it could be 0.1 or 0.2. 
4. The calculations and information presented here are based on the Turkish-German University's [Undergraduate Assessment and Evaluation Directive](http://3fcampus.tau.edu.tr/uploads/cms/oidb.tau/5690_9.pdf) document (Turkish).
"""

st.write("This app was created by **Muhammed Şihebi**. Please get in touch with me via [LinkedIn](https://www.linkedin.com/in/muhammed-shihebi/).")
