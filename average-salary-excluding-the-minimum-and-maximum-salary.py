Given an array of unique integers 'salary' where salary[i] is the salary of the employee i.
Return the average salary of employees excluding the minimum and maximum salary.

#Solution:
class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        min_sal=salary[0]
        max_sal=salary[0]
        for x in salary:
            if x > max_sal:
                max_sal=x
            elif x < min_sal:
                min_sal=x
        print(max_sal)
        print(min_sal)
        final_salary=[]
        sal_sum=0
        for x in salary:
            if x!=min_sal and x!=max_sal:
                print(x)
                sal_sum+=int(x)
        
        avg=sal_sum/((len(salary))-2)
        return avg
         
